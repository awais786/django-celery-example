from mysite.celery import app
from celery import Task


class FetchProfilePhoto(Task):
    def run(self, profile_photo_id, **kwargs):
        # Do something
        pass


app.register_task(FetchProfilePhoto())

