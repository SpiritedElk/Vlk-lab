#ps:Change the password down here ↓
password = "greetings"
while True:
  a = input("Password:")
  if a == password:
    print("welcome")
    break
  else:
    print("try again!")
print("authorization finished")
