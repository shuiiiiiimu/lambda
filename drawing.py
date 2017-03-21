# -*- coding: utf-8 -*-
import json
import uuid
from flask import Flask, jsonify
from scrapy.crawler import CrawlerProcess
from draw.spiders.a163 import A163Spider


app = Flask(__name__)


@app.route('/')
def index():
	return jsonify({'message': 'hello lambda!'})


@app.route('/fetch')
def fetch():
	# tmp_file = '/tmp/{}-fetch-output.json'.format(uuid.uuid4())
	# subprocess.check_output(['scrapy', 'crawl', 'a163', "-o", tmp_file])
	# with open(tmp_file) as items_file:
	# 	return jsonify(json.load(items_file)[0])
	settings = {
		'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5',
	}
	process = CrawlerProcess(settings)
	process.crawl(A163Spider)
	process.start(stop_after_crawl=True)
	return 'DONE!'


if __name__ == '__main__':
	app.run()
