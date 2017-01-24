from faker.providers import BaseProvider
import itertools

class CustomerProvider(BaseProvider):
	
    def default_customer(self):

        return self.customer(['FirstName', 'LastName', 'PhoneNumber'])

    def customer(self, fields=None):

        if fields is None:
            fields = []

        d = {
            'FirstName' : self.generator.first_name(),
			'LastName' : self.generator.last_name(),
			'PhoneNumber': str(self.generator.numerify('4860#######')),
			'Email': self.generator.email(),
			'Street':self.generator.street_name(),
			'HouseNumber': str(self.generator.building_number()),
			'ApartmentNumber': str(self.generator.building_number()),
			'PostalCode': self.generator.postcode(),
			'City': self.generator.city(),
			'PersonalDataProcessingConsent': True,
			'EmailCommunicationConsent': self.generator.boolean(),
			'SmsCommunicationConsent': True,
			'AlcoholMarketingConsent': True,
			'PreferredLanguage': "pl-PL",
			'DateOfBirth': self.generator.date("%Y-%m-%d"),
			'Gender': 'Male',
			'Password': '12345678'
			#'PreferredStore': str(self.generator.random_number(4))
        }

        if len(fields) > 0:
            d = dict((k, v) for (k, v) in d.items() if k in fields)

        return d
