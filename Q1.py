print("welcome")
name = input("name")
if name.isalpha() and name!= "":
   age = input("age")
   if age.isdigit() and not age.isspace():

      address = input("address")
      if address!= "":
         print("Hello Mr/Ms name",{name},"age",{age},"located in address",{address},"\n thanks for being in our community,      \t\t Enjoy")
      else:
          print ("wrong value")
   else:
      print("wrong value")
else:
   print("not real name or empty")