from .api import BaseAPI

class TeamProfile(BaseAPI):
    def get(self, visibility=None):
        return super(TeamProfile, self).get(
            'team.profile.get',
            params={'visibility': visibility}
        )


class Team(BaseAPI):
    def __init__(self, *args, **kwargs):
        super(Team, self).__init__(*args, **kwargs)
        self._profile = TeamProfile(*args, **kwargs)

    @property
    def profile(self):
        return self._profile

    def info(self):
        return self.get('team.info')

    def access_logs(self, count=None, page=None):
        return self.get('team.accessLogs',
                        params={'count': count, 'page': page})

    def integration_logs(self, service_id=None, app_id=None, user=None,
                         change_type=None, count=None, page=None):
        return self.get('team.integrationLogs',
                        params={
                            'service_id': service_id,
                            'app_id': app_id,
                            'user': user,
                            'change_type': change_type,
                            'count': count,
                            'page': page,
                        })

    def billable_info(self, user=None):
        return self.get('team.billableInfo', params={'user': user})
