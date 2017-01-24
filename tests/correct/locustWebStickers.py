from tests.common.customRequests import Requests as requests
import json
from providers.cpsProviders import Providers as cps
import utility as u 
from faker import Factory
import datetime as d
from xml.etree.ElementTree import XML


class LocustWebStickers():
	fakeData = cps.all() 
	
	def registerClient(self):
		data = LocustWebStickers.fakeData.customer()
		print(data)
		url = '/loyalty/v1/customers'
		with requests.Post(self, url, data) as response:
			if response.status_code == 200:
				response.success()
				return [data["PhoneNumber"], response.json()["ActivationToken"], response.json()["CustomerGuid"]]
			else:
				response.failure(u.responseFail(response))
	
	def login(self, cardNumber):
		#cardPin = LocustWebStickers.fakeData.cardPinAuthorization(cardNumber)
		url = '/loyalty/v1/login'
		data ={
				"Login": cardNumber,
  				"Password": "12345678"#cardPin
			  }
		start = d.datetime.now()
		with requests.Post(self, url, data) as response:
			end = d.datetime.now()
			if response.status_code == 200 or response.status_code == 403:
				response.success()
				if response.status_code == 403:
					#response = response.json()
					return {"SessionId" : -1}
				return response.json()
			else:
				time = ''
				if response.status_code == 499:
					time = (end - start).total_seconds()
					if time > 10 :
						time = 10
				response.failure(u.responseFail(response, time))
				return {'SessionId': -1}

	def loginPass(self, cardNumber):
		cardPass = LocustWebStickers.fakeData.cardPasswordAuthorization(cardNumber)
		url = '/loyalty/v1/login'
		data ={
				"Login": cardNumber,
  				"Password": cardPass
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
				return [int(response.headers.get('ETag')), response.json()["PhoneNumber"]]
			else:
				response.failure(u.responseFail(response))
				return -1
	
	def changeClientData(self, sessionId, ifMatch):
		url = '/loyalty/v1/customers/current'
		data = LocustWebStickers.fakeData.customer()
		with requests.Patch(self, url, data, sessionId, ifMatch) as response:
			if response.status_code == 200:
				response.success()
				return [data["PhoneNumber"], int(response.headers.get('ETag'))]
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
		cardPassword = 12345679#LocustWebStickers.fakeData.cardPasswordAuthorization(cardNumber)
		cardOldPassword = 12345678#LocustWebStickers.fakeData.cardPinAuthorization(cardNumber)
		url = '/loyalty/v1/customers/current/password'
		data = { "OldPassword": cardOldPassword, "NewPassword" : cardPassword }
		with requests.Post(self, url, data, sessionId) as response:
			if response.status_code == 204:
				response.success()
			else:
				response.failure(u.responseFail(response))
				
	def activateCustomer(self, token, smscode):
		url = '/loyalty/v1/customers/activate'
		data = {"ActivationToken": token, "SmsCode": str(smscode)}
		with requests.Post(self, url, data) as response:
			if response.status_code == 204:
				response.success()
			else:
				response.failure(u.responseFail(response))
				
	def ALCSRegisterCustomer(self, cardNumber, siteid, posNumber, creationData):
		url = 'http://kblade7:60200/forcom/loyalty/alcs/pos/v2/loyalty-cards/' + cardNumber + '/issue'
		data = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                    <LoyaltyCardIssueRequest>
                    <CardNumber>"""+ cardNumber + """</CardNumber>
                    <Identity>
                       <SiteId>""" + siteid + """</SiteId>
                       <PosNumber>"""+ posNumber + """</PosNumber>
                       <PosId></PosId>
                       <PosOperatorNumber>99</PosOperatorNumber>
                       <PosOperatorId></PosOperatorId>
                    </Identity>
                    <Language>
    	               <CashierLanguage>pl</CashierLanguage>
                       <ClientLanguage>pl</ClientLanguage>
                    </Language>
	                <BusinessDay>2017-01-09T00:00:00.000</BusinessDay>
                    </LoyaltyCardIssueRequest>"""
		with requests.PostALCS(self, url, data) as response:
			if response.status_code == 201:
				response.success()
				return XML(response.content).find("LoyaltyCardIssueId").text
			else:
				response.failure()
	
	def ALCSRegisterCustomerStepTwo(self, cardNumber, cardIssueId):
		url = 'http://kblade7:60200/forcom/loyalty/alcs/pos/v2/loyalty-cards/' + cardNumber + '/issue/' + cardIssueId + '/execute'
		with requests.PutALCS(self. url) as response:
			if response.status_code == 200:
				response.success()
				return [XML(response.content).find("LoyaltyCardIssueId").text, XML(response.content).find("PosAction/Id").text]
			else:
				response.failure()
	
	def ALCSRegisterCustomerConfirmPhoneNumber(self, cardNumber, cardIssueId, posActionId, phoneNumber):
		url = 'http://kblade7:60200/forcom/loyalty/alcs/pos/v2/loyalty-cards/' + cardNumber + '/issue/' + cardIssueId + '/posAction/' + posActionId
		data = """<PosActionResponse>
	 				   <PosActionId>""" + posActionId + """</PosActionId>
						<Result>Ok</Result>
						<Data>"""+ phoneNumber + """</Data>
						<DataEntryMode>Manual</DataEntryMode>
						</PosActionResponse>"""
		with requests.PutALCS(self, url, data) as response:
			if response.status_code == 200:
				response.success()			
				return [XML(response.content).find("PosAction/Id").text]
			else:
				response.failure()

	def ALCSRegisterCustomerReset(self, cardNumber, cardIssueId, posActionId):
		url = 'http://kblade7:60200/forcom/loyalty/alcs/pos/v2/loyalty-cards/' + cardNumber + '/issue/' + cardIssueId + '/posAction/' + posActionId
		data = """<PosActionResponse>
	 				   <PosActionId>""" + posActionId + """</PosActionId>
						<Result>Ok</Result>
						<Data>AlMxQR8xHzAwMDAwMB8wMDAwHBwcMzg5MDAyMTgcMDc2HDADGg==</Data>
						<DataEntryMode>Manual</DataEntryMode>
						</PosActionResponse>"""
		with requests.PutALCS(self, url, data) as response:
			if response.status_code == 200:
				response.success()			
				return [XML(response.content).find("PosAction/Id").text]
			else:
				response.failure()

	def ALCSRegisterCustomerMessage(self, cardNumber, cardIssueId, posActionId):
		url = 'http://kblade7:60200/forcom/loyalty/alcs/pos/v2/loyalty-cards/' + cardNumber + '/issue/' + cardIssueId + '/posAction/' + posActionId
		data = """<PosActionResponse>
	 				   <PosActionId>""" + posActionId + """</PosActionId>
						<Result>Ok</Result>
						<Data></Data>
						<DataEntryMode>Manual</DataEntryMode>
						</PosActionResponse>"""
		with requests.PutALCS(self, url, data) as response:
			if response.status_code == 200:
				response.success()			
				return [XML(response.content).find("PosAction/Id").text]
			else:
				response.failure()
				
	def ALCSCommitRegisterCustomer(self, cardNumber, cardIssueId):
		url = 'http://kblade7:60200/forcom/loyalty/alcs/pos/v2/loyalty-cards/' + cardNumber + '/issue/' + cardIssueId + '/commit'
		with requests.PutALCS(self, url) as response:
			if response.status_code == 200:
				 response.success()
			else:
				response.failure()
	