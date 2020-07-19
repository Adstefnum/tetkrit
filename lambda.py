import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast


def lambda_handler(event):
	pass

def rsa(word_or_hash, mode):

	random_generator = Random.new().read
	key = RSA.generate(2048, random_generator) #generate pub and priv key
	publickey = key.publickey() # pub key export for exchange

	if mode == encrypt:
		encrypted = publickey.encrypt(word_or_hash, 32)
		return encrypted

	else:
		decrypted = key.decrypt(ast.literal_eval(str(word_or_hash)))
		return decrypted

def tripleDes(word_or_hash, mode):

	if mode == encrypt:
		encrypted = 
		return encrypted

	else:
		decrypted = 
		return decrypted

def tripleDes(word_or_hash, mode):

	if mode == encrypt:
		encrypted = 
		return encrypted

	else:
		decrypted = 
		return decrypted

def tripleDes(word_or_hash, mode):

	if mode == encrypt:
		encrypted = 
		return encrypted

	else:
		decrypted = 
		return decrypted

def tripleDes(word_or_hash, mode):

	if mode == encrypt:
		encrypted = 
		return encrypted

	else:
		decrypted = 
		return decrypted






