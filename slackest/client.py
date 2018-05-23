from .im import IM, MPIM
from .api import API, Auth, IncomingWebhook, RTM
from .chat import Chat
from .channel import Channels
from .file import Files
from .group import Groups
from .reminder import Reminders
from .search import Search
from .team import Team
from .user import Users
from .usergroup import IDPGroups, UserGroups
from .utils import Apps, Bots, DND, Emoji, OAuth, Pins, Presence, Reactions, Stars

DEFAULT_TIMEOUT = 10
DEFAULT_RETRIES = 0
# seconds to wait after a 429 error if Slack's API doesn't provide one
DEFAULT_WAIT = 20

class Slackest(object):
    oauth = OAuth(timeout=DEFAULT_TIMEOUT)

    def __init__(self, token, incoming_webhook_url=None,
                 timeout=DEFAULT_TIMEOUT, http_proxy=None, https_proxy=None,
                 session=None, rate_limit_retries=DEFAULT_RETRIES):

        proxies = self.__create_proxies(http_proxy, https_proxy)
        api_args = {
            'token': token,
            'timeout': timeout,
            'proxies': proxies,
            'session': session,
            'rate_limit_retries': rate_limit_retries,
        }
        self.im = IM(**api_args)
        self.api = API(**api_args)
        self.dnd = DND(**api_args)
        self.rtm = RTM(**api_args)
        self.apps = Apps(**api_args)
        self.auth = Auth(**api_args)
        self.bots = Bots(**api_args)
        self.chat = Chat(**api_args)
        self.team = Team(**api_args)
        self.pins = Pins(**api_args)
        self.mpim = MPIM(**api_args)
        self.users = Users(**api_args)
        self.files = Files(**api_args)
        self.stars = Stars(**api_args)
        self.emoji = Emoji(**api_args)
        self.search = Search(**api_args)
        self.groups = Groups(**api_args)
        self.channels = Channels(**api_args)
        self.presence = Presence(**api_args)
        self.reminders = Reminders(**api_args)
        self.reactions = Reactions(**api_args)
        self.idpgroups = IDPGroups(**api_args)
        self.usergroups = UserGroups(**api_args)
        self.incomingwebhook = IncomingWebhook(url=incoming_webhook_url,
                                               timeout=timeout, proxies=proxies)

    def __create_proxies(self, http_proxy=None, https_proxy=None):
        proxies = dict()
        if http_proxy:
            proxies['http'] = http_proxy
        if https_proxy:
            proxies['https'] = https_proxy
        return proxies
