# Celery Example

This is a simple example for celery, a queue management framework. This simple walk through is intended for local runing on mac

Official [tutorial](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html) 

### Installation

* Celery in python
```shell script
python -m pip install celery
python -m pip install redis
python -m pip install flower
```
* Broker : install and start Redis
```shell script
# for mac
brew install redis
brew services restart redis
```
* or we can jsut use docker
```shell script
# docker
docker run -d -p 6379:6379 redis
```
### Coding a celery worker
The example coding will be named [task.py](tasks.py)

### Running Worker
* Run the following at the terminal, in the directory you arranged the ```task.py```, you can run 2 worker processes at a time
```shell script
celery -A tasks worker --loglevel=info
```
* Web UI: flower, run the following and you can visit the webpage at ```http://localhost:5555```
```shell script
celery flower --broker=redis://localhost
```

### Examples 
Try out some [dummy test](testings.ipynb)，it's a notebook file located in current directory