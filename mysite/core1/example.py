from celery import shared_task


@shared_task()
def ada():
    print('ffffffff')
