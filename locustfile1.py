from locust import HttpLocust, TaskSet, task
from providers.cpsProviders import Providers as cps
import utility
import json
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
	counterStart = 999001045000
	counter = 999001045000
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
		sessionId = webStickers.login(self, cardNumber)["SessionId"]
		if (str(sessionId) != str(-1)):
			#print(sessionId)
			webStickers.changePassword(self, sessionId, cardNumber)
		#	time.sleep(1)
			ifMatch, phoneNumberGet = webStickers.getCustomer(self, sessionId)
			phoneNumberPatch = webStickers.changeClientData(self, sessionId, ifMatch)
			patchTime = time.strftime("[%d/%b/%Y:%H:%M:%S +0200]", time.localtime())
			f = open(str(UserBehavior.counterStart) + ".log", "a+")
			f.write(patchTime + " CardNumber: " + str(cardNumber) + " Old: " + str(phoneNumberGet) + " New: " + str(phoneNumberPatch) + "\n")
			f.close()
			webStickers.logout(self, sessionId)
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

