from locust import HttpLocust, TaskSet, task
from providers.cpsProviders import Providers as cps
import utility
import json
import pinpad_message as pinpad
from tests.common.customRequests import Requests as requests
from tests.correct.locustWebStickers import LocustWebStickers as webStickers
from tests.correct.locustAlcs import LocustAlcs as alcsRequests
from tests.correct.locustBOK import LocustBOK as bokRequests
import time
from random import randint
#import response.webSticker.responses as webResp

class UserBehavior(TaskSet):
	#c = open('card', 'r+')
	#cards = c.read().splitlines()
	#c.close()
	#h =  open('hmac', 'r+')
	#hmacs = h.read().splitlines()
	#h.close()
	counterStart = 999001035000
	counter = 999001035000
	#cardNumber = counter * 10
	@task
	def test1(self):
		#rand = randint(7950000000000,7950000999999)
		#for i in range(1000):
		#bokRequests.changePassword(self, str(rand))
		#cardNumber = alcsRequests.registerClient(self)[0]
#		sessionId = bokRequests.changePassword(self, '7157834569333')
		UserBehavior.counter += 1
		cardNumber = UserBehavior.counter * 10
		if UserBehavior.counter - UserBehavior.counterStart >= 9999:
			UserBehavior.counter = UserBehavior.counterStart
		#print(cardNumber)
		
		phoneNumber, activationToken , CustomerGuid = webStickers.registerClient(self)
		formattedPhoneNumber = '-'.join((phoneNumber[2:5],phoneNumber[5:8],phoneNumber[8:]))
		webStickers.activateCustomer(self, str(activationToken), "1234")
		try:
			LoyaltyCardIssueId = webStickers.ALCSRegisterCustomer(self, "9990004716100","123456","99","312")
			LoyaltyCardIssueId1, PosActionId = webStickers.ALCSRegisterCustomerStepTwo(self, "9990004716100", LoyaltyCardIssueId)
			posacId1 = webStickers.ALCSRegisterCustomerReset(self, "9990004716100", LoyaltyCardIssueId1, PosActionId)
			posacId2 = webStickers.ALCSRegisterCustomerMessage(self, "9990004716100", LoyaltyCardIssueId1, posacId1)
			posacId3 = webStickers.ALCSRegisterCustomerConfirmPhoneNumber(self, "9990004716100", LoyaltyCardIssueId1, posacId2, pinpad(formattedPhoneNumber))
			posacId4 = webStickers.ALCSRegisterCustomerMessage(self, "9990004716100", LoyaltyCardIssueId1, posacId3)
			posacId5 = webStickers.ALCSRegisterCustomerConfirmPhoneNumber(self, "9990004716100", LoyaltyCardIssueId1, posacId4, pinpad("0000"))
			webStickers.ALCSCommitRegisterCustomer(self, "9990004716100", LoyaltyCardIssueId1)
		except Exception as e:
			print("Error: %s" % str(e))
		
		#print (pinpad.createMessage(formattedPhoneNumber) + " " + formattedPhoneNumber + " " + activationToken +" " + CustomerGuid)
		
		
		sessionId = webStickers.login(self, cardNumber)["SessionId"]
		if (str(sessionId) != str(-1)):
			#print(sessionId)
			#webStickers.changePassword(self, sessionId, cardNumber)
		#	time.sleep(1)
			ifMatch, phoneNumberGet = webStickers.getCustomer(self, sessionId)
			phoneNumberPatch, newIfMatch = webStickers.changeClientData(self, sessionId, ifMatch)
			webStickers.changePassword(self, sessionId)
			webStickers.logout(self, sessionId)
			
			#patchTime = time.strftime("[%d/%b/%Y:%H:%M:%S +0200]", time.localtime())
			#f = open(str(UserBehavior.counterStart) + ".log", "a+")
			#f.write(patchTime + " CardNumber: " + str(cardNumber) + " Old: " + str(phoneNumberGet) + " New: " + str(phoneNumberPatch) + "\n")
			#f.close()
			#webStickers.logout(self, sessionId)
		#else:
			#print(cardNumber, sessionId)
			#time.sleep(2)
		
		#ifMatch = webStickers.getCustomer(self, sessionId)
		#print (ifMatch)
		#webStickers.changePassword(self, sessionId, cardNumber)
		

		#webStickers.changeClientData(self, ifMatch)
		#alcsRequests.activateClient(self)
		#webStickers.getClientName(self, sessionId)
		#webStickers.logout(self, sessionId)



class WebsiteUser(HttpLocust):
	task_set = UserBehavior

	min_wait=1000
	max_wait=5000

