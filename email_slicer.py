
# get user email adress
email = input("What is your email adress? : ").strip()

#slice pout user name

user = email[:email.index("@")]

#slice out the domain

domain = email[email.index("@") + 1 :]

#format message

output = "your username is {} and your domain name is {}".format(user,domain)


# display the output message

print(output)
