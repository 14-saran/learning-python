#exception

try:
    numberator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numberator / denominator
    
except ZeroDivisionError:
    print("you can't divide by zero! idiot")
except ValueError:
    print("Enter only numbers plz")
except Exception:
    print("something went wrong:( ")
else:
    print(result)
finally:
    print("This will always execute")
