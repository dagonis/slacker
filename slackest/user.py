from .api import BaseAPI
from .utils import get_item_id_by_name

class UsersProfile(BaseAPI):
    def get(self, user=None, include_labels=False):
        return super(UsersProfile, self).get(
            'users.profile.get',
            params={'user': user, 'include_labels': int(include_labels)}
        )

    def set(self, user=None, profile=None, name=None, value=None):
        return self.post('users.profile.set',
                         data={
                             'user': user,
                             'profile': profile,
                             'name': name,
                             'value': value
                         })


class UsersAdmin(BaseAPI):
    def invite(self, email, channels=None, first_name=None,
               last_name=None, resend=True):
        return self.post('users.admin.invite',
                         params={
                             'email': email,
                             'channels': channels,
                             'first_name': first_name,
                             'last_name': last_name,
                             'resend': resend
                         })


class Users(BaseAPI):
    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)
        self._profile = UsersProfile(*args, **kwargs)
        self._admin = UsersAdmin(*args, **kwargs)

    @property
    def profile(self):
        return self._profile

    @property
    def admin(self):
        return self._admin

    def info(self, user):
        return self.get('users.info', params={'user': user})

    def user_list(self, presence=False):
        return self.get('users.list', params={'presence': int(presence)})

    def identity(self):
        return self.get('users.identity')

    def set_active(self):
        return self.post('users.setActive')

    def get_presence(self, user):
        return self.get('users.getPresence', params={'user': user})

    def set_presence(self, presence):
        return self.post('users.setPresence', data={'presence': presence})

    def get_user_id(self, user_name):
        members = self.user_list().body['members']
        return get_item_id_by_name(members, user_name)