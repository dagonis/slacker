import json
import time

import requests

from .exception import *

API_BASE_URL = 'https://slack.com/api/{api}'
DEFAULT_TIMEOUT = 10
DEFAULT_RETRIES = 0
# seconds to wait after a 429 error if Slack's API doesn't provide one
DEFAULT_WAIT = 20

class Response(object):
    def __init__(self, body):
        self.raw = body
        self.body = json.loads(body)
        self.successful = self.body['ok']
        self.error = self.body.get('error')

    def __str__(self):
        return json.dumps(self.body)


class BaseAPI(object):
    def __init__(self, token=None, timeout=DEFAULT_TIMEOUT, proxies=None,
                 session=None, rate_limit_retries=DEFAULT_RETRIES):
        self.token = token
        self.timeout = timeout
        self.proxies = proxies
        self.session = session
        self.rate_limit_retries = rate_limit_retries

    def _request(self, method, api, **kwargs):
        if self.token:
            kwargs.setdefault('params', {})['token'] = self.token

        # while we have rate limit retries left, fetch the resource and back
        # off as Slack's HTTP response suggests
        for _ in range(self.rate_limit_retries):
            response = method(API_BASE_URL.format(api=api),
                              timeout=self.timeout,
                              proxies=self.proxies,
                              **kwargs)

            if response.status_code == requests.codes.ok:
                break

            # handle HTTP 429 as documented at
            # https://api.slack.com/docs/rate-limits
            elif response.status_code == requests.codes.too_many: # HTTP 429
                time.sleep(int(response.headers.get('retry-after', DEFAULT_WAIT)))
                continue

            else:
                response.raise_for_status()

        else:
            # with no retries left, make one final attempt to fetch the resource,
            # but do not handle too_many status differently
            response = method(API_BASE_URL.format(api=api),
                              timeout=self.timeout,
                              proxies=self.proxies,
                              **kwargs)
            response.raise_for_status()

        response = Response(response.text)
        if not response.successful:
            raise Error(response.error)

        return response

    def _session_get(self, url, params=None, **kwargs):
        kwargs.setdefault('allow_redirects', True)
        return self.session.request(
            method='get', url=url, params=params, **kwargs
        )

    def _session_post(self, url, data=None, **kwargs):
        return self.session.request(
            method='post', url=url, data=data, **kwargs
        )

    def get(self, api, **kwargs):
        return self._request(
            self._session_get if self.session else requests.get,
            api, **kwargs
        )

    def post(self, api, **kwargs):
        return self._request(
            self._session_post if self.session else requests.post,
            api, **kwargs
        )


class API(BaseAPI):
    def test(self, error=None, **kwargs):
        if error:
            kwargs['error'] = error

        return self.get('api.test', params=kwargs)


class Auth(BaseAPI):
    def test(self):
        return self.get('auth.test')

    def revoke(self, test=True):
        return self.post('auth.revoke', data={'test': int(test)})

class IncomingWebhook(object):
    def __init__(self, url=None, timeout=DEFAULT_TIMEOUT, proxies=None):
        self.url = url
        self.timeout = timeout
        self.proxies = proxies

    def post(self, data):
        """
        Posts message with payload formatted in accordance with
        this documentation https://api.slack.com/incoming-webhooks
        """
        if not self.url:
            raise Error('URL for incoming webhook is undefined')

        return requests.post(self.url, data=json.dumps(data),
                             timeout=self.timeout, proxies=self.proxies)

class RTM(BaseAPI):
    def start(self, simple_latest=False, no_unreads=False, mpim_aware=False):
        return self.get('rtm.start',
                        params={
                            'simple_latest': int(simple_latest),
                            'no_unreads': int(no_unreads),
                            'mpim_aware': int(mpim_aware),
                        })

    def connect(self):
        return self.get('rtm.connect')
