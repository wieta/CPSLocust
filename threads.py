import _thread
import http.client
import json
import redis

#c = open('card', 'r+')
#cards = c.read().split()
#h = open('hmac')
r = redis.StrictRedis(host='lblade4', port=6379, db=0, decode_responses=True)

def add(cardNumber, hmac):
	headers = {'Content-type': 'application/json'}
	body = {"Identity":
			{"PosId": "09fae9a5d4ea40e79dd7c1096c361478", "PosNumber": "14", "PosOperatorId": "b614f1dbda36454b970b4e1d409f1478", "PosOperatorNumber": 14, "SiteId": "1478"},
		"ResponseLanguage":
			{"ClientLanguage": "pl_PL", "CashierLanguage": "pl_PL"},
		"LoyaltyCard":
			{"CardNumber": "99419283746389", "PhoneNumber": "", "Gender": "U", "CardPinHMac": "3f729ea140a769400985ade930f695452cf622fd0dd3ca69218319333ca2386c",
			"Wallets": [
				{"Id": "Strickers2016", "Balance": 0, "Stat":
					{"Lost": 0, "TransferredOut": 0, "TransferredIn": 0, "Issued": 0},
					"Version": "2",
				}],
			}
		}
	body['LoyaltyCard']['CardNumber'] = str(cardNumber)
	body['LoyaltyCard']['CardPinHMac'] = str(hmac)
	body = json.dumps(body)
	print(body)
	conn = http.client.HTTPConnection("10.60.99.99", 7443)
	conn.request("PUT", "/alcs/loyalty/v1/loyalty-cards/" + str(cardNumber), body, headers)
	response = conn.getresponse()
	for i in response:
		print(i)
	conn.close()

	password = {'Password': '1235'}
	password = json.dumps(password)
	print(password)
	conn = http.client.HTTPConnection("10.60.99.99", 4532)
	conn.request("POST", "/bok/loyalty/v1/loyalty-cards/" + str(cardNumber) + "/customer/password", password, headers)
	z = r.hgetall('card:' + str(cardNumber))
	print(z)
	z['Status'] = 'Active'
	z['Wallets.Initialized'] = 1
	print(z)
	r.hmset('card:' + str(cardNumber), z)
	print(r.hgetall('card:' + str(cardNumber)))

#try:
#	for i in range(0, 1):
#		_thread.start_new_thread( myPrint, (i, ) )

#except:
#   print("Error: unable to start thread")
   
#while 1:
#	pass

add(7950000000000, '+ewTfSPRI83xo7FIibxcqE2i3zjO/xImLEsUaCXUhtY=')
