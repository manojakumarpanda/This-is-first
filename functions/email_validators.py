#To validate email in the format of foo./_/+/123@some.com 
#0->invalid,1->valid
def validate_email(email):
	try:
		if (re.search("[!#$%^&*()?=,<>/]",email)):
			return 0
		else:
			regex='[A-Z0-9a-z._+-]+[@][a-z]+[.]+[a-z]{2,3}'
			match=re.match(regex,email)
			# match=re.findall(regex,email)
			return 1 if match else 0
	except Exception as e:
		pass