from mysite.celery import app
from celery import shared_task


@app.task()
def create_random_user_accounts__1(total):
    for i in range(total):
        print('I am app2_test task!')


@app.task()
def create_random_user_accounts_2__1(total):
    for i in range(total):
        print('I am app2_test task!2')


@shared_task
def add(x, y):
    return x + y