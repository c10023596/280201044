pword = str(input("Okay throw me a password. "))
frick_counter = 1
while True:
  verify = str(input("Now type that again. "))
  if verify == pword:
    print("Wow gee you sure know your passwords.")
    break
  if frick_counter >= 3:
    print("How dare you to forget the password you typed 10 seconds ago!")
    break
  elif frick_counter<=3:
    print("Oopsies, try again.")
    frick_counter += 1