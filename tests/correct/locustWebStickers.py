from tests.common.customRequests import Requests as requests
import json
from providers.cpsProviders import Providers as cps
import utility as u 
from faker import Factory

class LocustWebStickers():
	fakeData = cps.all() 
	def login(self):
		cardNumber = LocustWebStickers.fakeData.cardNumberAuthorization()
		cardPin = LocustWebStickers.fakeData.cardPinAuthorization(cardNumber)
		url = '/loyalty/v1/login'
		data ={
				"Login": cardNumber,
  				"Password": cardPin
			  }
		with requests.Post(self, url, data) as response:
			if response.status_code == 200:
				response.success()
				return response.json()
			else:
				response.failure(u.responseFail(response))

	def logout(self, sessionId):
		url = '/loyalty/v1/logout'
		with requests.Post(self, url, sessionId=sessionId) as response:
			if response.status_code == 204:
				response.success()
			else:
				response.failure(u.responseFail(response))

	def getCustomer(self, sessionId):
		url = '/loyalty/v1/customers/current'
		with requests.Get(self, url, sessionId) as response:
			if response.status_code == 200:
				response.success()
				return (response.headers.get('ETag'))
			else:
				response.failure(u.responseFail(response))
	
	def changeClientData(self, sessionId, ifMatch):
		url = '/loyalty/v1/customers/current'
		data = LocustWebStickers.fakeData.customer('FirstName')
		with requests.Patch(self, url, data, sessionId, ifMatch) as response:
			if response.status_code == 200:
				response.success()
			else:
				response.failure(u.responseFail(response))
			
	def getClientName(self, sessionId):
		cardNumber = LocustWebStickers.fakeData.cardNumberAuthorization()
		phoneNumber = LocustWebStickers.fakeData.customer('PhoneNumber').get('PhoneNumber')
		url = '/loyalty/v1/customers/'+ str(cardNumber) + '+' + str(phoneNumber) +'/first-name'
		with requests.Get(self, url) as response:
			if response.status_code == 200:
				response.success()
			else:
				response.failure(u.responseFail(response))

	def addSingleToMasterCard(self, sessionId):
		cardNumber = LocustWebStickers.fakeData.cardNumberAuthorization()
		url = '/loyalty/v1/customers/current/master-card/' + str(cardNumber)
		with requests.Post(self, url, sessionId = sessionId) as response:
			if response.status_code == 204:
				response.success()
			else:
				response.failure(u.responseFail(response))

	def removeSingleFromMaster(self, sessionId):
		url = '/loyalty/v1/customers/current/master-card/'
		with requests.Delete(self, url, sessionId) as response:
			if response.status_code == 204:
				response.success()
			else:
				response.failure(u.responseFail(response))

	def setClientMessageRead(self, sessionId):
		url = '/loyalty/v1/customers/current/unread-messages/USERID'	#TODO USERID - customerID po rejestracji
		with requests.Delete(self, url, sessionId) as response:
			if response.status_code == 204:
				response.success()
			else:
				response.failure(u.responseFail(response))

	def changePassword(self, sessionId):
		cardNumber = LocustWebStickers.fakeData.cardNumberAuthorization()
		cardPassword = LocustWebStickers.fakeData.cardPasswordAuthorization(cardNumber)
		cardOldPassword = LocustWebStickers.fakeData.cardPinAuthorization(cardNumber)
		url = '/loyalty/v1/customers/current/password'
		data = { "OldPassword": cardOldPassword, "NewPassword" : cardPassword }
		with requests.Post(self, url, data, sessionId) as response:
			if response.status_code == 204:
				response.success()
			else:
				response.failure(u.responseFail(response))
				