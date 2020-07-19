import hashlib

enc_word = word.encode('utf-8')
encrypted = hashlib.md5(enc_word.strip()).hexdigest()

