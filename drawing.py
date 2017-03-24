# -*- coding: utf-8 -*-
import json
import uuid
from flask import Flask, jsonify
from scrapy.crawler import CrawlerProcess
from draw.spiders.a163 import A163Spider
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from celery import Celery
from celery.schedules import crontab


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['celery_broker_url'])
    celery.conf.update(app.config)
    celery.conf.timezone = 'Asia/Hong_Kong'
    celery.conf.imports = 'drawing'
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


app = Flask(__name__)
app.config.update(
    celery_broker_url='redis://localhost:6379/5'
)
celery = make_celery(app)


@celery.task
def add_together(a, b):
    return a + b


@celery.task()
def hello():
    print('-------------------hello ==============')


celery.conf.beat_schedule = {
    'hello-every-3-minute': {
        'task': 'drawing.hello',
        'schedule': crontab(minute='*/3'),
    },
}


@app.route('/')
def index():
    return jsonify({'message': 'hello lambda!'})


@app.route('/add')
def add():
    add_together.delay(23, 42)
    return jsonify({'message': 'hello celery!'})


@app.route('/fetch')
def fetch():
    # tmp_file = '/tmp/{}-fetch-output.json'.format(uuid.uuid4())
    # subprocess.check_output(['scrapy', 'crawl', 'a163', "-o", tmp_file])
    # with open(tmp_file) as items_file:
    # 	return jsonify(json.load(items_file)[0])

    # os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'draw.settings')
    # process = CrawlerProcess(get_project_settings())
    # process.crawl(A163Spider)
    # process.start(stop_after_crawl=True)

    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl("a163")
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    return 'DONE!'


if __name__ == '__main__':
    app.run()
