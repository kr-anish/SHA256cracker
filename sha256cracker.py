from pwn import *
import sys

if len(sys.argv) != 2:
	print( "Invalid Arguments!!!!!")
	print( ">> {} <sha256sum>".format(sys.argv[0]))
	exit()


sha256_hash = sys.argv[1]
password_file = "rockyou.txt"
attempts = 0

with log.progress("Cracking SHA256 : {}!\n".format(sha256_hash)) as p:
	with open(password_file, "r" , encoding='latin-1') as password_list:
		for password in password_list:
			password = password.strip("\n").encode('latin-1')
			password_hash = sha256sumhex(password)
			p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
			if password_hash == sha256_hash:
				p.success("Password found after {} attempts!!! {} is the hash to >>>>> {}".format(attempts, password_hash, password.decode('latin-1')))
				exit()
			attempts += 1
		p.failure("Password hash not found in file")

