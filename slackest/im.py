from .api import BaseAPI

class IM(BaseAPI):
    def list(self):
        return self.get('im.list')

    def history(self, channel, latest=None, oldest=None, count=None,
                inclusive=None, unreads=False):
        return self.get('im.history',
                        params={
                            'channel': channel,
                            'latest': latest,
                            'oldest': oldest,
                            'count': count,
                            'inclusive': inclusive,
                            'unreads' : int(unreads)
                        })

    def replies(self, channel, thread_ts):
        return self.get('im.replies',
                        params={'channel': channel, 'thread_ts': thread_ts})

    def mark(self, channel, ts):
        return self.post('im.mark', data={'channel': channel, 'ts': ts})

    def open(self, user):
        return self.post('im.open', data={'user': user})

    def close(self, channel):
        return self.post('im.close', data={'channel': channel})


class MPIM(BaseAPI):
    def open(self, users):
        if isinstance(users, (tuple, list)):
            users = ','.join(users)

        return self.post('mpim.open', data={'users': users})

    def close(self, channel):
        return self.post('mpim.close', data={'channel': channel})

    def mark(self, channel, ts):
        return self.post('mpim.mark', data={'channel': channel, 'ts': ts})

    def list(self):
        return self.get('mpim.list')

    def history(self, channel, latest=None, oldest=None, inclusive=False,
                count=None, unreads=False):
        return self.get('mpim.history',
                        params={
                            'channel': channel,
                            'latest': latest,
                            'oldest': oldest,
                            'inclusive': int(inclusive),
                            'count': count,
                            'unreads': int(unreads)
                        })

    def replies(self, channel, thread_ts):
        return self.get('mpim.replies',
                        params={'channel': channel, 'thread_ts': thread_ts})