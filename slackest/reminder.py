from .api import BaseAPI

class Reminders(BaseAPI):
    def add(self, text, time, user=None):
        return self.post('reminders.add', data={
            'text': text,
            'time': time,
            'user': user,
        })

    def complete(self, reminder):
        return self.post('reminders.complete', data={'reminder': reminder})

    def delete(self, reminder):
        return self.post('reminders.delete', data={'reminder': reminder})

    def info(self, reminder):
        return self.get('reminders.info', params={'reminder': reminder})

    def list(self):
        return self.get('reminders.list')