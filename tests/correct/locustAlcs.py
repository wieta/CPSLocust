from tests.common.customRequests import Requests as requests
import json
from providers.cpsProviders import Providers as cps
import utility as u 
from faker import Factory

class LocustAlcs():
	fakeData = cps.all()
	

	def registerClient(self, cardNumber, hmac):
		data = LocustAlcs.fakeData.client()
		data['LoyaltyCard']['CardPinHMac']=hmac
		data['LoyaltyCard']['CardNumber']=cardNumber
		print(data)
		#cardNumber = data.get('LoyaltyCard').get('CardNumber')
		url = '/alcs/loyalty/v1/loyalty-cards/' + str(cardNumber)
		print(url)
		with requests.Put(self, url, data) as response:
			print(response)
			if response.status_code == 200:
				print('ok')
				response.success()
			else:
				response.failure(u.responseFail(response))
			return [cardNumber, response.json()]

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
