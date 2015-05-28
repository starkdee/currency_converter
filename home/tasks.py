from celery import task


@task()
def test():
    print 'task works'
