# try block: Contains code that might cause an error.
# Python attempts to execute this block first.

try:
    x=int(input("Enter Number: "))
    ans=10/x


# except block: Executes only if an error occurs in try.

except ZeroDivisionError:               # Handles division by zero error.
    print(f"Divide by 0 is not allowed")

except ValueError:                      # Handles case when input is not a valid integer.
    print(f"String is not allowed")
    
    
# else block: Executes only when no exception occurs in try.
else:
    print(f"Ans is = {ans}")


# finally block: Always executes whether an exception occurs or not.
finally:
    print("End of the Program")