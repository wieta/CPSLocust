from locust import HttpLocust

class Requests(HttpLocust):

	def Post(self, url, data={}):
		return self.client.post(url, data=data, headers={'Content-type': 'application/json'}, catch_response=True)

	def Get(self, url):
		return self.client.get(url, headers={'Content-type': 'application/json'}, catch_response=True)
