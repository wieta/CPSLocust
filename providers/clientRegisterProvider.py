from faker.providers import BaseProvider
import simplejson as json

class ClientRegisterProvider(BaseProvider):
	
	def client(self, fields=None):
		cardNumber = self.generator.cardNumberAuthorization()
		d = {
		"Identity":
		{
		"PosId": self.generator.uuid4(),
		"PosNumber": self.generator.random_number(2),
		"PosOperatorId": self.generator.uuid4(),
		"PosOperatorNumber": self.generator.random_number(2),
		"SiteId": self.generator.random_number(4)
		},
		"ResponseLanguage":
		{		
		"ClientLanguage": self.generator.locale(),
		"CashierLanguage": self.generator.locale()
		},
		"LoyaltyCard":
		{
		"CardNumber": cardNumber,
		"PhoneNumber": self.generator.phone_number(),
		"Gender": self.generator.random_element(["F", "M", "U"]),
		"CardPinHMac": self.generator.cardPinHmacAuthorization(cardNumber),
		"Wallets":[],
		}
		}
		
		return d
