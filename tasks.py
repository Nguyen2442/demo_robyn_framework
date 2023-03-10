from app import celery



@celery.task
def run_hello():
    import time
    for i in range(1, 1000):
        time.sleep(2)
        print("Hello", i)
    return


run_hello()