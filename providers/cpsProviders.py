from faker import Factory
from providers.customerProvider import CustomerProvider
from providers.clientRegisterProvider import ClientRegisterProvider
from providers.clientCardNumberPinProvider import ClientCardNumberPin

class Providers():

	def all():
		f = Factory.create('pl_PL')
		f.add_provider(CustomerProvider)
		f.add_provider(ClientRegisterProvider)
		f.add_provider(ClientCardNumberPin)
		return f