# -*- coding: utf-8 -*-


# Groups to query.
FB_GROUPS = [
	('Psytrance Poznań', '144388485683974')
]


# Get facebook User Access Token from file.
try:
	with open("access_token.txt", "r") as at_file:
		ACCESS_TOKEN = at_file.read()

except IOError:
	print("No access_token.txt file found.")
	print("Please put your User Access Token in access_token.txt file.")
	exit(2)
