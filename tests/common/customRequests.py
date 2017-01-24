from locust import HttpLocust

class Requests(HttpLocust):

	def Get(self, url,  sessionId = None):
		if sessionId is None:
			return self.client.get(url, headers={'Content-type': 'application/json'}, catch_response=True, timeout=30)
		else:
			return self.client.get(url, headers={'Content-type': 'application/json', 'Authorization': str(sessionId)}, catch_response=True, timeout=30)
	
	def Post(self, url, data={}, sessionId = None, ifMatch = None):
		if (sessionId is None and ifMatch is None):
			return self.client.post(url, json=data, headers={'Content-type': 'application/json'}, catch_response=True, timeout=30)
		else:
			return self.client.post(url, json=data, headers={'Content-type': 'application/json', 'Authorization': str(sessionId), 'If-Match': str(ifMatch)} , catch_response=True, timeout=30)
	
	def Put(self, url, data={}, sessionId = None, ifMatch = None):
		if (sessionId is None and ifMatch is None):
			return self.client.put(url, json=data, headers={'Content-type': 'application/json'}, catch_response=True, timeout=30)
		else:
			return self.client.put(url, headers={'Content-type': 'application/json', 'Authorization': str(sessionId), 'If-Match': str(ifMatch)}, catch_response=True, timeout=30)	
	
	def Patch(self, url, data={}, sessionId = None, ifMatch = None):
		if (sessionId is None and ifMatch is None):
			return self.client.patch(url, json=data, headers={'Content-type': 'application/json'}, catch_response=True, timeout=30)
		else:
			return self.client.patch(url, json=data, headers={'Content-type': 'application/json', 'Authorization': str(sessionId), 'If-Match': str(ifMatch)}, catch_response=True, timeout=30)
	
	def Delete(self, url, sessionId = None):
		if sessionId is None:
			return self.client.delete(url, headers={'Content-type': 'application/json'}, catch_response=True, timeout=30)
		else:
			return self.client.delete(url, headers={'Content-type': 'application/json', 'Authorization': str(sessionId)}, catch_response=True, timeout=30)
	
	def PostALCS(self, url, data):
		return self.client.post(url, name="ALCSCustomerRegister", data=data, headers={'Content-type': 'application/xml'}, catch_response=True, timeout=30)
        
	def PutALCS(self, url, data):
		return self.client.put(url, name="ALCSCustomerRegister", data = data, headers={'Content-type': 'application/xml'}, catch_response=True, timeout=30)
		