import json

def toJson(object):
	return json.dumps(object, indent = True, ensure_ascii=False, encoding="utf-8")

def printJson(object):
	print(toJson(object))

def doWhile(func, loop=False):
	func()
	while loop:
		func()

def responseFail(response):
	return [response.status_code, response.json()]