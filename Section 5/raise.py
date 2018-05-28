try:
    raise NameError("Hello World")

except NameError:
    print("Exception Pop!!!")
    raise