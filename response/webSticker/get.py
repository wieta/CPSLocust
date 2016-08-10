# -*- coding: utf-8 -*-
class Get():

	def customerNotModified():
		r = {
			'HttpCode' : '304',
			'MessageCode': 'CustomerNotModified',
			'Message' : 'Dane klienta nie zostały zmodyfikowane'
		}
		return r

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

	def customerNotFoundByCardAndPhoneNumber():
		r = {
			'HttpCode' : '404',
			'MessageCode': 'CustomerNotFoundByCardAndPhoneNumber',
			'Message' : 'Klient o zadanym numerze karty i telefonu nie istnieje'
		}
		return r
