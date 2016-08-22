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
	@task
	def test1(self):
		c = open('card', 'r+')
		cards = c.read().splitlines()
		c.close()
		h =  open('hmac', 'r+')
		hmacs = h.read().splitlines()
		h.close()
		rand = randint(0,1000)
		for i in range(1000):
			alcsRequests.registerClient(self, cards[i + (rand*1000)], hmacs[i + (rand*1000)])
		#cardNumber = alcsRequests.registerClient(self)[0]
#		sessionId = bokRequests.changePassword(self, '7157834569333')
	
		#sessionId = webStickers.loginPass(self, cardNumber)['SessionId']	
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
	max_wait=1000

