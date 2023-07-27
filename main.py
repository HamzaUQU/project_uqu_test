username = "admin"
password = "123"



def login():

  entered = input("enter ur user name ") #enter pass word
  if entered != username:   #the if statment
    print("no acount with this name") #wrong user
    return login()
  else:
    passworddef()

def passworddef():
  enteredpass = input("enter ur password ")
  if enteredpass != password:
    print("wrong password")
    return passworddef()
  else:
    print("correct")

login()
