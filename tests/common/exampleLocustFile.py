from locust import HttpLocust, TaskSet, task
from providers.cpsProviders import Providers as cps
import utility
import json
from tests.common.customRequests import Requests as requests

import response.webSticker.responses as webResp

class UserBehavior(TaskSet):
	@task(1)
	def test1(self):
		url = '/loyalty/v1/logout'
		with requests.Post(self, url) as response:
			response.success()

	@task(1)
	def test2(self):
		url = '/loyalty/v1/login'
		data = utility.toJson({"CardNumber": "9012312312312", "CardPin": "3309"})
		with requests.Post(self, url, data) as response:
			response.success()


class WebsiteUser(HttpLocust):
	task_set = UserBehavior
	min_wait=5000
	max_wait=9000