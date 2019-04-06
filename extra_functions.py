from tkinter import *
import json
import hashlib
import os
import re
#import Database as database


#print( "valid_login =", database.valid_login( username="reuben", password="matlala" ))
#database.create_user(username="reuben", password="matlala", email="reuben.mahloele@gmail.com", phone="1234567890")
data={}
data['people']=[]
def print_signUp_details( username, email, phone, pass1,pass2 ):
	print("usename =", username)
	print("email =", email)
	print("phone =", phone)
	print("pass1 =", pass1)
	print("pass2 =", pass2)

def details_check(username, email, phone, pass1,pass2):

	return_message = ''
	if username == "":
		# Don't forget to check if a username exists or not
		return "Username Field is required!"
	elif email == "":
		return "Email Filed is required!"
	elif phone == "":
		return "Phone Field is required!"
	elif pass1 == "":
		return "Password field is required!"
	elif pass2 == "":
		return "Confirm Password field is required!"
	elif pass1 != pass2:
		return "Password mismatch!"
	else:
		#Push the information to a database
		#for now will be using a json file to store the data
		data['people'].append({
			'username': username,
			'email': email,
			'phone': phone,
			'pass': pass2
		})
		with open('data.txt','w') as outfile:
			json.dump(data,outfile)
		return_message ="Account created!"
	return return_message

def login_check(username,password):
	return_message =''
	a = False
	if username=="" or password=="":
		return_message="Please fill in your details."
		return return_message

	else:
		with open('data.txt') as json_file:
			data_read = json.load(json_file)
			for p in data['people']:
				if p['username']==username and p['pass']== password:
					a=True

		if a:
			return_message = " You have successfully logged in"
			return return_message
		else:
			return_message  = "Invalid username or password"
			return return_message
