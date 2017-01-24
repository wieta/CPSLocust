import redis
import uuid as u

#r.hgetall('card:7950000008000')
#r.delete('card:' + str(7950000000000 + i))
#r.hmset('card:795000000000', {'field1':'Hello', 'field2':'World'})

r = redis.StrictRedis(host='lblade4', port=6379, db=0, decode_responses=True)

#cards = r.keys()

def deletePass():
	pins = r.keys('hmac:Password:*')
	for i in pins:
		x = r.hgetall(i)
		for j in x:
			if int(j) >= 7950000000000 and int(j) <=7950000999999:
				r.delete(i)
				print(j)

def deleteCustomers():				
	customers = r.keys('customer:*')
	for i in customers:
		x = r.hgetall(i)
		for j in x:
			if 'Card.795' in str(j):
				r.delete(i)
				print(j)
				
def deleteCards():				
	cards = r.keys('card:*')
	for i in cards:
		if 'card:795' in str(i):
			r.delete(i)
			print(i)

def generateGuid():
	line = str(u.uuid4())
	line = line.replace('-', '')
	return line

	
def add():
	guid=generateGuid()	
	num = '7950000000000'
	cardKey = 'card:' + num
	cardVal = {'Status': 'Active', 'Wallet.Stickers2016.Stat.Issued': '0.000', 'Wallet.Stickers2016.Balance': '0.000', 'Wallet.Stickers2016.Stat.TransferredOut': '0.000', 'Wallet.Stickers2016.Stat.Collected': '0.000', 'Wallets.Initialized': '1', 'Guid': 'd4750455bed947869cf0db7ab7cce53f', 'Wallet.Stickers2016.Stat.Lost': '0.000', 'Wallet.Stickers2016.Stat.TransferredIn': '0.000', 'Wallet.Stickers2016.Version': '2'}
	cardVal['Guid'] = guid
	customerKey = 'customer:' + guid
	customerVal = {'Version': '3', 'Email': 'ada@abc.com', 'PostalCode': '00-111', 'PreferredStore': '4532', 'City': 'X', 'Street': 'xyz', 'PreferredLanguage': 'pl-PL', 'FirstName': 'Adam999', 'PersonalDataProcessingConsent': '1', 'ApartmentNumber': '1', 'EmailCommunicationConsent': '1', 'LastName': 'ABC', 'HouseNumber': '6', 'Status': 'Active', 'SmsCommunicationConsent': '0'}
	customerVal['Card.' + num] = 'Active'
	hmacKey = 'hmac:Password:+ewTfSPRI83xo7FIibxcqE2i3zjO/xImLEsUaCXUhtY='
	hmacVal = {num: guid}
		
	keys = [cardKey, customerKey, hmacKey]
	values = [cardVal, customerVal, hmacVal]
	for i in range(len(keys)):
		r.hmset(keys[i], values[i])
		

#add()
deleteCustomers()
deletePass()
deleteCards()