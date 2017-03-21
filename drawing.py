# -*- coding: utf-8 -*-
import subprocess
import json
import uuid
from flask import Flask, jsonify


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
	return 'DONE!'


if __name__ == '__main__':
	app.run()
