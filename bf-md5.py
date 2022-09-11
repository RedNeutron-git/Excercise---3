from __future__ import print_function
import hashlib,md5,sys,thread,time
from time import sleep

def latihan():
	count=1
	a = raw_input("md5 hash: ")
	wordlist = raw_input("wordlist: ")
	try:
		wordlist=open(wordlist,'r')
	except:
		print('Not Found!')
		quit()
	for password in wordlist:
		md5file = md5.new(password.strip()).hexdigest()		
		if a == md5file:
			print ("You got it: %s" % password.strip())
			break
if __name__ == "__main__":
	latihan()
