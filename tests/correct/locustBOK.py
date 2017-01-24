from tests.common.customRequests import Requests as requests
import json
from providers.cpsProviders import Providers as cps
import utility as u 
from faker import Factory
from random import randint

class LocustBOK():
	fakeData = cps.all() 
	def changePassword(self, cardNumber):
		password = randint(0, 1000000)
		#cardPin = LocustWebStickers.fakeData.cardPinAuthorization(cardNumber)
		url = '/bok/loyalty/v1/loyalty-cards/' + cardNumber + '/customer/password'
		data ={
  				"Password": str(password)
			  }
		with requests.Post(self, url, data) as response:
			if response.status_code == 204:
				response.success()
				return response.json()
			else:
				response.failure(u.responseFail(response))
				return {"SessionId": -1}