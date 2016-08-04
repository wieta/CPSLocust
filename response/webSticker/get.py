class Get():

	def customerNotModified():
		r = {
			'HttpCode' : '304',
			'MessageCode': 'CustomerNotModified',
			'Message' : 'Dane klienta nie zostały zmodyfikowane'
		}
		return r