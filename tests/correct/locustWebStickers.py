from tests.common.customRequests import Requests as requests
import json
from faker.providers import BaseProvider
from providers.cpsProviders import Providers as cps

class LocustWebStickers():
	fakeData = cps.all() 

	def login(self):
		cardNumber = LocustWebStickers.fakeData.cardNumberAuthorization()
		cardPin = LocustWebStickers.fakeData.cardPasswordAuthorization(cardNumber)
		url = '/loyalty/v1/login'
		data = {
    "Login": "4832846501887",
    "Password": "@q6Cruh)"
}#{
    			#"Login": cardNumber,
    			#"Password": cardPin
			   #}		
		with requests.Post(self, url, data) as response:
			res = response.json()
			if response.status_code == 200:
				response.success()
				return res['SessionId']
			else:
				#print (data)
				response.failure("Response fail with data")	
			

	def logout(self, sessionId):
		url = '/loyalty/v1/logout'
		data = {}
		with requests.Post(self, url, data, sessionId) as response:
			if response.status_code == 204:
				response.success()
			else:
				response.failure("Got wrong response exected 204")

	def getCustomer(self, sessionId):
		url = '/loyalty/v1/customers/current'
		with requests.Get(self, url, sessionId) as response:
			if response.status_code == 200:
				print ("Pobrano dane uzytkownika: " + response.json())
				response.success()
			else:
				response.failure("Got wrong response exected 200")


	
	def changeClientData(self, sessionId):
		url = '/loyalty/v1/customers/current'
		data = {"FirstName": LocustWebStickers.fakeData.customer('FirstName')}
		with requests.Path(self, url, data, sessionId) as response:
			if response.status_code == 200:
				response.success()
			else:
				print (response.json())
				response.failure("Got wrong response exected 200")


			
	def getClientName(self, sessionId):
		url = '/loyalty/v1/customers/{cardNumber+phoneNumber}/first-name'
		with requests.Get(self, url, sessionId) as response:
			response.success()

	
	def addSingleToMasterCard(self, sessionId):
		url = '/loyalty/v1/customers/current/master-card/{MasterCardNumber}'
		data = {}
		with requests.Post(self, url, data, sessionId) as response:
			response.success()

	
	def removeSingleFromMaster(self, sessionId):
		url = '/loyalty/v1/customers/current/master-card/'
		with requests.Delete(self, url, sessionId) as response:
			response.success()

	
	def setClientMessageRead(self, sessionId):
		url = '/loyalty/v1/customers/current/unread-messages/USERID'
		with requests.Delete(self, url, sessionId) as response:
			response.success()

	
	def changePassword(self, sessionId):
		cardNumber = LocustWebStickers.fakeData.cardNumberAuthorization()
		cardPassword = LocustWebStickers.fakeData.cardPasswordAuthorization(cardNumber)
		cardOldPassword = LocustWebStickers.fakeData.cardPinAuthorization(cardNumber)
		url = '/loyalty/v1/customers/current/password'
		data = { "OldPassword": cardOldPassword, "NewPassword" : cardPassword }
		print (data)
		with requests.Post(self, url, data, sessionId) as response:
			if response.status_code == 204:
				print ("zmieniono hasło, dla sesji " + "" + sessionId)
				response.success()
			else:
				res = response.json()
				print (data)
				response.failure("Got wrong response")