class AddSlave():
	
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

	def customerNotFoundByMasterCardNumber():
		r = {
			'HttpCode' : '404',
			'MessageCode': 'CustomerNotFoundByMasterCardNumber',
			'Message' : 'Klient o zadanym numerze karty nie istnieje'
		}
		return r

	def slaveCustomerCannotBecomeMaster():
		r = {
			'HttpCode' : '422',
			'MessageCode': 'slaveCustomerCannotBecomeMaster',
			'Message' : 'Karta o zadanym numerze karty jest kartą Slave'
		}
		return r

	def slaveCountLimitExceeded():
		r = {
			'HttpCode' : '422',
			'MessageCode': 'SlaveCountLimitExceeded',
			'Message' : ''
		}
		return r
