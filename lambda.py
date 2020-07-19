import Crypto
from Crypto.Cipher import *
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from struct import pack


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
	key = 'Sixteen byte key'
	iv = Random.new().read(DES3.block_size) #DES3.block_size==8

	if mode == encrypt:
		cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
		encrypted = cipher_encrypt.encrypt(word_or_hash)
		return encrypted

	else:
		cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) 
		decrypted = cipher_decrypt.decrypt(encrypted_text)
		return decrypted

def aes(word_or_hash, mode):
	key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
	iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])

	if mode == encrypt:
		aes = AES.new(key, AES.MODE_CBC, iv)
		encrypted = aes.encrypt(data)
		return encrypted

	else:
		aes = AES.new(key, AES.MODE_CBC, iv)
		decrypted = adec.decrypt(encd)
		return decrypted

'''def blowFish(word_or_hash, mode):

	bs = Blowfish.block_size
 	key = b'An arbitrarily long key'
 	iv = Random.new().read(bs)
 	cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
 	plen = bs - divmod(len(word_or_hash),bs)[1]
 	padding = [plen]*plen
 	padding = pack('b'*plen, *padding)

	if mode == encrypt:
		encrypted = iv + cipher.encrypt(word_or_hash + padding)
		return encrypted

	else:
		iv = word_or_hash[:bs]
		word_or_hash = word_or_hash[bs:]
		decrypted = cipher.decrypt(word_or_hash)
		last_byte = decrypted[-1]
		decrypted = decrypted[:- (last_byte if type(last_byte) is int else last_byte)]
		return repr(decrypted)'''


def blowFish(word_or_hash, mode):
	key = b"bbgjbdrguhdghsebgiufvffdcjvfkjfcfghfkdcjfkdjfkhdgvkhjdgfhdcgjfkhdhjfkdgfkdgjfkhdfkdgjdhjjdchjhdjjhdjhjjhfdjjdjddgdjgdgxgdcvjgdvvgdchxdcvhgdjcghdccxdjvdgvgdxcvdhgjxvhdgjcghcdhcdcdchdchfchf"
	cipher = Blowfish.new(key)

	if mode == encrypt:
		encrypted = cipher.encrypt(word_or_hash)
		return encrypted

	else:
		decrypted = cipher.decrypt(word_or_hash)
		return decrypted






