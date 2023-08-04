#Email Slicer is just a simple tool that will take an email address
# as input and slice it to produce the username and the domain associated with it.
# The email must be divided into two strings by using ‘@’ as the separator.

emailadd = input("email address? ").split('@')

username,domain=emailadd

print("Your username is ",username,"& domain is", domain)