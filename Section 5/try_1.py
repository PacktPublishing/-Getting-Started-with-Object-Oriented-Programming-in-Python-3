try:
    n1, n2 = eval(input("Input 2 Numbers, Separated by comma: "))
    ans = n1/n2
    print("Answer :", ans)
                  
except ZeroDivisionError:
    print("Division by Zero is Error!")

except SyntaxError:
    print("Comma is missing. Enter Numbers separated by comma. Eg: 5,6 ")
    
except:
    print("Wrong Input")
    
else:
    print("No Exception")
    
finally:
    print("This will execute no matter what")
	