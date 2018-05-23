from .api import BaseAPI
from .exception import *

def get_item_id_by_name(list_dict, key_name):
    for d in list_dict:
        if d['name'] == key_name:
            return d['id']

class Emoji(BaseAPI):
    def list(self):
        return self.get('emoji.list')


class Presence(BaseAPI):
    AWAY = 'away'
    ACTIVE = 'active'
    TYPES = (AWAY, ACTIVE)

    def set(self, presence):
        assert presence in Presence.TYPES, 'Invalid presence type'
        return self.post('presence.set', data={'presence': presence})




class Reactions(BaseAPI):
    def add(self, name, file_=None, file_comment=None, channel=None,
            timestamp=None):
        # One of file, file_comment, or the combination of channel and timestamp
        # must be specified
        assert (file_ or file_comment) or (channel and timestamp)

        return self.post('reactions.add',
                         data={
                             'name': name,
                             'file': file_,
                             'file_comment': file_comment,
                             'channel': channel,
                             'timestamp': timestamp,
                         })

    def get(self, file_=None, file_comment=None, channel=None, timestamp=None,
            full=None):
        return super(Reactions, self).get('reactions.get',
                                          params={
                                              'file': file_,
                                              'file_comment': file_comment,
                                              'channel': channel,
                                              'timestamp': timestamp,
                                              'full': full,
                                          })

    def list(self, user=None, full=None, count=None, page=None):
        return super(Reactions, self).get('reactions.list',
                                          params={
                                              'user': user,
                                              'full': full,
                                              'count': count,
                                              'page': page,
                                          })

    def remove(self, name, file_=None, file_comment=None, channel=None,
               timestamp=None):
        # One of file, file_comment, or the combination of channel and timestamp
        # must be specified
        assert (file_ or file_comment) or (channel and timestamp)

        return self.post('reactions.remove',
                         data={
                             'name': name,
                             'file': file_,
                             'file_comment': file_comment,
                             'channel': channel,
                             'timestamp': timestamp,
                         })


class Pins(BaseAPI):
    def add(self, channel, file_=None, file_comment=None, timestamp=None):
        # One of file, file_comment, or timestamp must also be specified
        assert file_ or file_comment or timestamp

        return self.post('pins.add',
                         data={
                             'channel': channel,
                             'file': file_,
                             'file_comment': file_comment,
                             'timestamp': timestamp,
                         })

    def remove(self, channel, file_=None, file_comment=None, timestamp=None):
        # One of file, file_comment, or timestamp must also be specified
        assert file_ or file_comment or timestamp

        return self.post('pins.remove',
                         data={
                             'channel': channel,
                             'file': file_,
                             'file_comment': file_comment,
                             'timestamp': timestamp,
                         })

    def list(self, channel):
        return self.get('pins.list', params={'channel': channel})

class DND(BaseAPI):
    def team_info(self, users=None):
        if isinstance(users, (tuple, list)):
            users = ','.join(users)

        return self.get('dnd.teamInfo', params={'users': users})

    def set_snooze(self, num_minutes):
        return self.post('dnd.setSnooze', data={'num_minutes': num_minutes})

    def info(self, user=None):
        return self.get('dnd.info', params={'user': user})

    def end_dnd(self):
        return self.post('dnd.endDnd')

    def end_snooze(self):
        return self.post('dnd.endSnooze')


class Bots(BaseAPI):
    def info(self, bot=None):
        return self.get('bots.info', params={'bot': bot})




class OAuth(BaseAPI):
    def access(self, client_id, client_secret, code, redirect_uri=None):
        return self.post('oauth.access',
                         data={
                             'client_id': client_id,
                             'client_secret': client_secret,
                             'code': code,
                             'redirect_uri': redirect_uri
                         })

    def token(self, client_id, client_secret, code, redirect_uri=None,
              single_channel=None):
        return self.post('oauth.token',
                         data={
                             'client_id': client_id,
                             'client_secret': client_secret,
                             'code': code,
                             'redirect_uri': redirect_uri,
                             'single_channel': single_channel,
                         })


class AppsPermissions(BaseAPI):
    def info(self):
        return self.get('apps.permissions.info')

    def request(self, scopes, trigger_id):
        return self.post('apps.permissions.request',
                         data={
                             scopes: ','.join(scopes),
                             trigger_id: trigger_id,
                         })


class Apps(BaseAPI):
    def __init__(self, *args, **kwargs):
        super(Apps, self).__init__(*args, **kwargs)
        self._permissions = AppsPermissions(*args, **kwargs)

    @property
    def permissions(self):
        return self._permissions


class Stars(BaseAPI):
    def add(self, file_=None, file_comment=None, channel=None, timestamp=None):
        assert file_ or file_comment or channel

        return self.post('stars.add',
                         data={
                             'file': file_,
                             'file_comment': file_comment,
                             'channel': channel,
                             'timestamp': timestamp
                         })

    def list(self, user=None, count=None, page=None):
        return self.get('stars.list',
                        params={'user': user, 'count': count, 'page': page})

    def remove(self, file_=None, file_comment=None, channel=None, timestamp=None):
        assert file_ or file_comment or channel

        return self.post('stars.remove',
                         data={
                             'file': file_,
                             'file_comment': file_comment,
                             'channel': channel,
                             'timestamp': timestamp
                         })
