from tests.common.customRequests import Requests as requests
import json
from providers.cpsProviders import Providers as cps
import utility as u 
from faker import Factory

class LocustAlcs():
	fakeData = cps.all()
	

	def registerClient(self):
		data = LocustAlcs.fakeData.client()
		cardNumber = data.get('LoyaltyCard').get('CardNumber')
		url = '/alcs/loyalty/v1/loyalty-cards/' + str(cardNumber)
		with requests.Post(self, url, data) as response:
			if response.status_code == 200:
				response.success()
				return response.json()
			else:
				response.failure(u.responseFail(response))

	def activateClient(self):
		cardNumber = LocustAlcs.fakeData.client('CardNumber').get('CardNumber')
		phoneNumber = LocustAlcs.fakeData.customer('PhoneNumber').get('PhoneNumber')
		url = '/alcs/loyalty/v1/loyalty-cards/' + str(cardNumber) + '/activate'
		data = phonenumber
		with requests.Put(self, url, data) as response:
			if response.status_code == 204:
				response.success()
			else:
				response.failure(u.responseFail(response))

	def changeClientPhoneNumber(self):
		cardNumber = LocustAlcs.fakeData.client('CardNumber').get('CardNumber')
		phoneNumber = LocustAlcs.fakeData.customer('PhoneNumber').get('PhoneNumber')
		url = '/alcs/loyalty/v1/loyalty-cards/' + str(cardNumber)
		data = phonenumber
		with requests.Put(self, url, data) as response:
			if response.status_code == 204:
				response.success()
			else:
				response.failure(u.responseFail(response))

	def lockClient(self):
		cardNumber = LocustAlcs.fakeData.client('CardNumber').get('CardNumber')
		url = '/alcs/loyalty/v1/loyalty-cards/'+ str(cardNumber) + '/lock'
		with requests.Put(self, url, data) as response:
			if response.status_code == 204:
				response.success()
			else:
				response.failure(u.responseFail(response))
