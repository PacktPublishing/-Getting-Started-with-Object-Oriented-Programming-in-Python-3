class Error(Exception):
	"""Base Class of other exceptions"""
pass

class ValueTooSmallError(Error):
	"""Raised when the input value is too small"""
pass

class ValueTooLargeError(Error):
	"""Raised when the input value is too large"""
pass

#out main program
#user guesses a number until he/she is right

#you need to guess this number
number = 10

while True:
    try:
        i_num = int(input("Enter a number :"))
        
        if i_num < number:
            raise ValueTooSmallError
        
        elif i_num > number:
            raise ValueTooLargeError
            
        break
        
    except ValueTooSmallError:
        print("This value is too small, try again!!")
        print()
        
    except ValueTooLargeError:
        print("This value is too large, try again!!")
        print()

print("Congratulation! You guessed it correctly.")
        