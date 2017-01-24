body = {"Identity":
			{"PosId": "09fae9a5d4ea40e79dd7c1096c361478", "PosNumber": "14", "PosOperatorId": "b614f1dbda36454b970b4e1d409f1478", "PosOperatorNumber": 14, "SiteId": "1478"},
		"ResponseLanguage":
			{"ClientLanguage": "pl_PL", "CashierLanguage": "pl_PL"},
		"LoyaltyCard":
			{"CardNumber": "99419283746389", "PhoneNumber": None, "Gender": "U", "CardPinHMac": "3f729ea140a769400985ade930f695452cf622fd0dd3ca69218319333ca2386c",
			"Wallets": [
				{"Id": "Strickers2016", "Balance": 0, "Stat":
					{"Lost": 0, "TransferredOut": 0, "TransferredIn": 0, "Issued": 0},
					"Version": "2",
				}],
			}
		}
		
body['LoyaltyCard']['CardNumber'] = '5'
print(body)