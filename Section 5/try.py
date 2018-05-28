import sys

anyList = ['X', 0, 10]

for entry in anyList:
    try:
        print("Entry is ",entry)
        R = 1/int(entry)
        break
        
    except:
        print("OOPs!", sys.exc_info()[0], "Occured.")
        print("Next Entry.")
        print()
        
print("Reciprocal of", entry, "is", R)