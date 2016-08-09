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
	@task(1)
	def test1(self):
		alcsRequests.registerClient(self)
		#time.sleep(20)
		#sessionId = webStickers.login(self)['SessionId']
		#changePasswordRequired = webStickers.login(self)['IsPasswordChangeRequired']
		#if changePasswordRequired:
		#	webStickers.changePassword(self, sessionId)
		#ifMatch = webStickers.getCustomer(self, sessionId)['ETag']
		#webStickers.getCustomer(self, sessionId)

		#webStickers.changeClientData(self, ifMatch)
		#alcsRequests.activateClient(self)
		#webStickers.getClientName(self, sessionId)
		#webStickers.logout(self, sessionId)



class WebsiteUser(HttpLocust):
	task_set = UserBehavior
	min_wait=5000
	max_wait=9000