from mysite.celery import app


@app.task()
def create_random_user_accounts(total):
    for i in range(total):
        print('I am app1_test task!')


@app.task()
def create_random_user_accounts_2(total):
    for i in range(total):
        print('I am app1_test task!2')
