import operator, base64
from functools import reduce
#python 3.x version !

def computeLrc(self):
    return reduce(operator.xor, [ord(c) for c in str(self)])

def stringToBase64(self):
    return base64.b64encode(self.encode('utf-8'))
	
def base64ToString(self):
    return base64.b64decode(self.encode('utf-8'))

def createMessage(message, code=None):
    if code:
        RESPONSE_CODE = code
    else:
        RESPONSE_CODE = '0000'
    STX = '\x02'
    TYPE_MESSAGE = 'I5A'
    VERSION = '1'
    US = '\x1F'
    MESSAGE_TAG = '000000'
    FS = '\x1C'
    ETX = '\x03'
    lrc_checksum = computeLrc(TYPE_MESSAGE + US + VERSION + US + MESSAGE_TAG + US + RESPONSE_CODE + FS + message + ETX)
    return stringToBase64(STX + TYPE_MESSAGE + US + VERSION + US + MESSAGE_TAG + US + RESPONSE_CODE + FS + message + ETX + str(chr(lrc_checksum))).decode('utf-8')

	
#result = stringToBase64("dsdasdasdsd" + str(computeLrc("sdasdasdsd")))
#print ("Encoded string: " + result)
#print  ("Decoded string: " + base64ToString(result))
#print (createMessage('0000'))
