from locust import HttpLocust

class Requests(HttpLocust):

	def Get(self, url,  sessionId = None):
		if sessionId is None:
			return self.client.get(url, headers={'Content-type': 'application/json'}, catch_response=True)
		else:
			return self.client.get(url, headers={'Content-type': 'application/json', 'Authorization': str(sessionId)}, catch_response=True)
	
	def Post(self, url, data={}, sessionId = None):
		if sessionId is None:
			return self.client.post(url, json=data, headers={'Content-type': 'application/json'}, catch_response=True)
		else:
			return self.client.post(url, json=data, headers={'Content-type': 'application/json', 'Authorization': str(sessionId)}, catch_response=True)
	
	def Put(self, url, data={}, sessionId = None):
		if sessionId is None:
			return self.client.put(url, json=data, headers={'Content-type': 'application/json'}, catch_response=True)
		else:
			return self.client.put(url, headers={'Content-type': 'application/json', 'Authorization': str(sessionId)}, catch_response=True)	
	
	def Path(self, url, data={}, sessionId = None):
		if sessionId is None:
			return self.client.patch(url, json=data, headers={'Content-type': 'application/json'}, catch_response=True)
		else:
			return self.client.patch(url, json=data, headers={'Content-type': 'application/json', 'Authorization': str(sessionId)}, catch_response=True)
	
	def Delete(self, url, sessionId = None):
		if sessionId is None:
			return self.client.delete(url, headers={'Content-type': 'application/json'}, catch_response=True)
		else:
			return self.client.delete(url, headers={'Content-type': 'application/json', 'Authorization': str(sessionId)}, catch_response=True)
