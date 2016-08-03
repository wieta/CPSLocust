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
			'PhoneNumber': self.generator.phone_number(),
			'Email': self.generator.email(),
			'Street':self.generator.street_name(),
			'HouseNumber': self.generator.building_number(),
			'ApartmentNumber': self.generator.building_number(),
			'PostalCode': self.generator.postcode(),
			'City': self.generator.city(),
			'Status': 'Active',
			'PersonalDataProcessingConsent': self.generator.boolean(),
			'EmailCommunicationConsent': self.generator.boolean(),
			'SmsCommunicationConsent': self.generator.boolean(),
			'PreferredLanguage': self.generator.locale(),
			'PreferredStore': self.generator.random_number(4)
        }

        d = dict(d, **self.generator.simple_profile())

        if len(fields) > 0:
            d = dict((k, v) for (k, v) in d.items() if k in fields)

        return d