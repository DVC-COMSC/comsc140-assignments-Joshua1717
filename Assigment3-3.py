
import sys

email = input("Please enter a email adress: ")
length=len(email)
index_at=email.find('@')
index_dot= email.find('.')

if not ( email[0].isalpha() ):
	print ('The first lettter should be a letter of the alphabet')
	sys.exit(0)
if ( length <= 5 or length >= 30):
	print ('The length should be less than 5 and more than 30')
	sys.exit(0)
if not (index_at != -1):
    print("The adress should include the @ symbol.")
    sys.exit(0)
if not ( "." in email):
    print("The adress should include a period.")
    sys.exit(0)
if not (index_dot > index_at):
     print("The adress should include a period after the @ symbol.")
     sys.exit(0)

else: print(email, "is a vaild email adress.")

