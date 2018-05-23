from .api import BaseAPI

class FilesComments(BaseAPI):
    def add(self, file_, comment):
        return self.post('files.comments.add',
                         data={'file': file_, 'comment': comment})

    def delete(self, file_, id):
        return self.post('files.comments.delete',
                         data={'file': file_, 'id': id})

    def edit(self, file_, id, comment):
        return self.post('files.comments.edit',
                         data={'file': file_, 'id': id, 'comment': comment})


class Files(BaseAPI):
    def __init__(self, *args, **kwargs):
        super(Files, self).__init__(*args, **kwargs)
        self._comments = FilesComments(*args, **kwargs)

    @property
    def comments(self):
        return self._comments

    def list(self, user=None, ts_from=None, ts_to=None, types=None,
             count=None, page=None, channel=None):
        return self.get('files.list',
                        params={
                            'user': user,
                            'ts_from': ts_from,
                            'ts_to': ts_to,
                            'types': types,
                            'count': count,
                            'page': page,
                            'channel': channel
                        })

    def info(self, file_, count=None, page=None):
        return self.get('files.info',
                        params={'file': file_, 'count': count, 'page': page})

    def upload(self, file_=None, content=None, filetype=None, filename=None,
               title=None, initial_comment=None, channels=None):
        if isinstance(channels, (tuple, list)):
            channels = ','.join(channels)

        data = {
            'content': content,
            'filetype': filetype,
            'filename': filename,
            'title': title,
            'initial_comment': initial_comment,
            'channels': channels
        }

        if file_:
            with open(file_, 'rb') as f:
                return self.post('files.upload', data=data, files={'file': f})
        else:
            return self.post('files.upload', data=data)

    def delete(self, file_):
        return self.post('files.delete', data={'file': file_})

    def revoke_public_url(self, file_):
        return self.post('files.revokePublicURL', data={'file': file_})

    def shared_public_url(self, file_):
        return self.post('files.sharedPublicURL', data={'file': file_})