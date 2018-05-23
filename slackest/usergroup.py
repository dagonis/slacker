from .api import BaseAPI

class UserGroupsUsers(BaseAPI):
    def list(self, usergroup, include_disabled=None):
        if isinstance(include_disabled, bool):
            include_disabled = int(include_disabled)

        return self.get('usergroups.users.list', params={
            'usergroup': usergroup,
            'include_disabled': include_disabled,
        })

    def update(self, usergroup, users, include_count=None):
        if isinstance(users, (tuple, list)):
            users = ','.join(users)

        if isinstance(include_count, bool):
            include_count = int(include_count)

        return self.post('usergroups.users.update', data={
            'usergroup': usergroup,
            'users': users,
            'include_count': include_count,
        })


class UserGroups(BaseAPI):
    def __init__(self, *args, **kwargs):
        super(UserGroups, self).__init__(*args, **kwargs)
        self._users = UserGroupsUsers(*args, **kwargs)

    @property
    def users(self):
        return self._users

    def list(self, include_disabled=None, include_count=None, include_users=None):
        if isinstance(include_disabled, bool):
            include_disabled = int(include_disabled)

        if isinstance(include_count, bool):
            include_count = int(include_count)

        if isinstance(include_users, bool):
            include_users = int(include_users)

        return self.get('usergroups.list', params={
            'include_disabled': include_disabled,
            'include_count': include_count,
            'include_users': include_users,
        })

    def create(self, name, handle=None, description=None, channels=None,
               include_count=None):
        if isinstance(channels, (tuple, list)):
            channels = ','.join(channels)

        if isinstance(include_count, bool):
            include_count = int(include_count)

        return self.post('usergroups.create', data={
            'name': name,
            'handle': handle,
            'description': description,
            'channels': channels,
            'include_count': include_count,
        })

    def update(self, usergroup, name=None, handle=None, description=None,
               channels=None, include_count=None):
        if isinstance(channels, (tuple, list)):
            channels = ','.join(channels)

        if isinstance(include_count, bool):
            include_count = int(include_count)

        return self.post('usergroups.update', data={
            'usergroup': usergroup,
            'name': name,
            'handle': handle,
            'description': description,
            'channels': channels,
            'include_count': include_count,
        })

    def disable(self, usergroup, include_count=None):
        if isinstance(include_count, bool):
            include_count = int(include_count)

        return self.post('usergroups.disable', data={
            'usergroup': usergroup,
            'include_count': include_count,
        })

    def enable(self, usergroup, include_count=None):
        if isinstance(include_count, bool):
            include_count = int(include_count)

        return self.post('usergroups.enable', data={
            'usergroup': usergroup,
            'include_count': include_count,
        })

class IDPGroups(BaseAPI):
    def list(self, include_users=False):
        return self.get('idpgroups.list',
                        params={'include_users': int(include_users)})