class Logout():
	
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