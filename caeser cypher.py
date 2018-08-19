#ceaser cypher
SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE=len(SYMBOLS)

def getKey():
	while True:
		print('enter the key(1 to %s)',%MAX_KEY_SIZE)
		if key>=1 && key<=MAX_KEY_SIZE:
			return key
			
def getMode():
	whle True:
		print('Do you want to encrypt or decrypt?')
		Mode=input().lower()
		if Mode in ['encrypt','e','decrypt','d']:
			return Mode
		else:
			print('enter either encrypt, e, decrypt or d')

def getMessage():
	print('enter your message')
	message=input()
	return message

def getTranslatedMessage(Mode,Key,message):
	translated=''
	if Mode[0]='d':
		key=-key
	for symbol in message:
		symbolIndex=SYMBOLS.find(symbol)
		if symbolIndex==-1:
			translated+=symbol
		else:
			symbolIndex+=key
			if symbolIndex>=MAX_KEY_SIZE:
				symbolIndex-=MAX_KEY_SIZE
			elif symbolIndex<=0:
				symbolIndex+=MAX_KEY_SIZE
			translated+=SYMBOLS[symbolIndex]
	return translated
Mode=getMode()
Message=getMessage()
key=getKey()
print('your translated text is:')
print(getTranslatedMessage(Mode,Key,Message))
