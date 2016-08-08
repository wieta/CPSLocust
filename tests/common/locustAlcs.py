from locust import HttpLocust, TaskSet, task
from providers.cpsProviders import Providers as cps
import utility
import json
from tests.common.customRequests import Requests as requests

import response.webSticker.responses as webResp

class UserBehavior(TaskSet):
	@task(1)
	def registerClient(self):
		url = '/alcs/loyalty/v1/loyalty-cards/cardNumber'
		data = #faker customer 
		with requests.Put(self, url, data) as response:
			response.success()

	@task(1)
	def activateClient(self):
		url = '/alcs/loyalty/v1/loyalty-cards/cardNumber/activate'
		data = #fake phonenumber
		with requests.Post(self, url, data) as response:
			response.success()

	@tast(1)
	def changeClientPhoneNumber(self):
		url = '/alcs/loyalty/v1/loyalty-cards/cardNumber'
		data = #fake phonenumber
		with requests.Path(self, url, data) as response:
			response.success()

	@test(1)
	def lockClient(self):
		url = '/alcs/loyalty/v1/loyalty-cards/cardNumber/lock'
		data = {}
		with requests.Post(self, url, data) as response:
			response.success()

class WebsiteUser(HttpLocust):
	task_set = UserBehavior
	min_wait=5000
max_wait=9000