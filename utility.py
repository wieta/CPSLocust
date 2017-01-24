
import simplejson as sjson

def toJson(object):
	return sjson.dumps(object, indent = True, ensure_ascii=False, encoding="utf-8")

def printJson(object):
	print(toJson(object))

def doWhile(func, loop=False):
	func()
	while loop:
		func(
)
def responseFail(response = {}, time=''):
	if response.status_code == 0:
		return [response.status_code, 'Timeout ' + str(time)]
	return [response.status_code, toJson(response.text)]