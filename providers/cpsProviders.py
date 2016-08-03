from faker import Factory
from providers.customerProvider import CustomerProvider
from providers.clientRegisterProvider import ClientRegisterProvider

class Providers():

	def all():
		f = Factory.create('pl_PL')
		f.add_provider(CustomerProvider)
		f.add_provider(ClientRegisterProvider)
		return f