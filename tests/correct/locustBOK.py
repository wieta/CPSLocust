from tests.common.customRequests import Requests as requests
import json
from providers.cpsProviders import Providers as cps
import utility as u 
from faker import Factory

class LocustBOK():
	fakeData = cps.all() 
	def login(self, cardNumber):
		cardPin = LocustWebStickers.fakeData.cardPinAuthorization(cardNumber)
		url = '/bok/loyalty/v1/loyalty-cards/' + cardNumber + '/customer/password'
		data ={
  				"Password": "1235"
			  }
		with requests.Post(self, url, data) as response:
			if response.status_code == 200:
				response.success()
				return response.json()
			else:
				response.failure(u.responseFail(response))
				return {"SessionId": -1}