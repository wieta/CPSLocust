from faker import Factory
from providers.customerProvider import CustomerProvider

class Providers():

	def all():
		f = Factory.create('pl_PL')
		f.add_provider(CustomerProvider)
		return f