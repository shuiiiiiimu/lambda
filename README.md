# AWS lambda sandbox

* Zappa, Serverless Python Web Services for aws lambda.
* scrapy, a fast high-level web crawling & scraping framework for Python.
* Flask, A web microframework.

**run**

```bash
(env) ➜  lambda git:(master) ✗ virtualenv -p `which python` env
(env) ➜  lambda git:(master) ✗ source env/bin/activate
(env) ➜  lambda git:(master) ✗ pip install -r requirements.txt
```

## Zappa

### deploy

`dev` is defined in your zappa_settings.json.

```bash
(env) ➜  zappa deploy dev
```

### release

```bash
(env) ➜  zappa update dev
```

### zappa tail log

```bash
(env) ➜  zappa tail
```

### package

```bash
(env) ➜  zappa package dev
```

## Flask


### /

```bash
➜  ~ curl http://127.0.0.1:5000/
{
  "message": "hello lambda!"
}
```

### /fetch

```bash
➜  ~ curl http://127.0.0.1:5000/fetch
{
  "current": 2017073,
  "deadline": "2017-03-21 19:56",
  "deadts": 1490097360.0,
  "name": "a163"
}
```

## Scrapy

### fetch draw number

```bash
(env) ➜  scrapy crawl a163
```


## warming

### tmp file

Lambda function will not have local file write permissions everywhere on the machine. Try writing to the /tmp directory.
