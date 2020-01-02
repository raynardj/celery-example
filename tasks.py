from celery import Celery
from time import sleep
import os

app = Celery('tasks',backend = 'redis://localhost', broker='redis://localhost')

@app.task
def add(x, y):
    sleep(10)
    return x + y

@app.task
def print_pid(input_id):
    return {input_id:os.getpid()}