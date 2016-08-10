from locust import HttpLocust, TaskSet, task
from providers.cpsProviders import Providers as cps
import utility
import json
from tests.common.customRequests import Requests as requests
from tests.correct.locustWebStickers import LocustWebStickers as webStickers
from tests.correct.locustAlcs import LocustAlcs as alcsRequests
import time
#import response.webSticker.responses as webResp

class UserBehavior(TaskSet):
	@task
	def test1(self):
		cardNumber = alcsRequests.registerClient(self)[0]
		#sessionId = webStickers.login(self, cardNumber)['SessionId']
	
		sessionId = webStickers.loginPass(self, cardNumber)['SessionId']	
		ifMatch = webStickers.getCustomer(self, sessionId)
		print (ifMatch)
		webStickers.changePassword(self, sessionId, cardNumber)
		

		#webStickers.changeClientData(self, ifMatch)
		#alcsRequests.activateClient(self)
		#webStickers.getClientName(self, sessionId)
		#webStickers.logout(self, sessionId)



class WebsiteUser(HttpLocust):
	task_set = UserBehavior
	min_wait=5000
	max_wait=9000