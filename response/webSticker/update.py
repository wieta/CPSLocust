class Update():

	def noAuthorization():
		r = {
			'HttpCode' : '403',
			'MessageCode': 'NoAuthorization',
			'Message' : 'Brak uprawnień'
		}
		return r
		
	def sessionExpired():
		r = {
			'HttpCode' : '403',
			'MessageCode': 'SessionExpired',
			'Message' : ''
		}
		return r

	def notSupportedProperties():
		r = {
			'HttpCode' : '400',
			'MessageCode': 'NotSupportedProperties',
			'Message' : 'Podane pola nie odpowiadają specyfikacji'
		}
		return r

	def customerModifiedByAnotherUserOrProcess():
		r = {
			'HttpCode' : '412',
			'MessageCode': 'CustomerModifiedByAnotherUserOrProcess',
			'Message' : 'Podane pola nie odpowiadają specyfikacji'
		}
		return r

	def validationInvalid(property, value):
		r = {'ValidationErrorCodes': [{'Property':property, 'Error':'Invalid', 'Value':value}]}
		return r

	def validationMissing(property):
		r = {'ValidationErrorCodes': [{'Property':property, 'Error':'Missing'}]}
		return r

	def validationInvalidReadOnlyProperty (property, value):
		r = {'ValidationErrorCodes': [{'Property':'CustomerProperties.' + property, 'Error':'InvalidReadOnlyProperty', 'Value':value}]}
		return r

	def validationOverridingReadOnlyProperty (property, value):
		r = {'ValidationErrorCodes': [{'Property':'CustomerProperties.' + property, 'Error':'OverridingReadOnlyProperty', 'Value':value}]}
		return r
