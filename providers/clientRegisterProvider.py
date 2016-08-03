from faker.providers import BaseProvider
import simplejson as json

class ClientRegisterProvider(BaseProvider):
	
	def client(self, fields=None):
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
		"CardNumber": self.generator.ean13(),
		"PhoneNumber": self.generator.phone_number(),
		"Gender": self.generator.random_element(["F", "M", "U"]),
		"CardPinHMac": "3f729ea140a769400985ade930f695452cf622fd0dd3ca69218319333ca2386c",
		"Wallets":[],
		}
		}
		
		return d
