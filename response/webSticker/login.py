class Login():
		
	def invalidCredentials():
		r = {
			'HttpCode' : '403',
			'MessageCode': 'InvalidCredentials',
			'Message' : 'Będny numer karty lub pin'
		}
		return r
		
	def accountTemporarilyLockedFor5Minutes():
		r = {
			'HttpCode' : '403',
			'MessageCode': 'AccountTemporarilyLockedFor5Minutes',
			'Message' : ''
		}
		return r
		
	def accountLocked():
		r = {
			'HttpCode' : '403',
			'MessageCode': 'AccountLocked',
			'Message' : ''
		}
		return r
