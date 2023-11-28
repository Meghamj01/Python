known_users = ["Alice","Bob","Clarie","Dan","Emma","Fred","Georgie","Harry"]

print(len(known_users))
               
while True:
    print("hi my name is Travis:")
    name = input("whats your name ?:").strip().capitalize()
    if name in known_users:
        print("Hello {}!  ".format(name))
        remove = input("would you like to remove your name from the system (y/n)?:").lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print(" no problem, i dont want to leave anyway!")
        
            
    else:
         print("hmm i dont think i have met you yet {}".format(name))
         add_me = input("would you like to add your name in the system (y/n)?:").strip().lower()
         if add_me == "y":
             
             known_users.append(name)
         elif add_me == "n":
             print("no worries, see you around!")
         
    
