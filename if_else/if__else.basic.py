# if = do some code only if some codition is true
#   else do something else

age = int(input("Enter your age: "))
if age >= 20 :
    print('You are now signed up!')
elif age < 0:
    print("you haven't been yet!")
else:
    print("you must be 20+ to sign up!")

print('-----------------------------------------')


name = input("Enter your name: ")

if name == "" :
    print ("you didn't type in your name!")
else:
    print(f"Hello {name}")
