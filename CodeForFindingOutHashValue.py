import hashlib

m = hashlib.md5()
m.update("hello how are you".encode('utf-8'))
word_hash = m.hexdigest()
print(word_hash)
