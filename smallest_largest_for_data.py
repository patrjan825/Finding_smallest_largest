largest = None
smallest = None
for x in [1, 20, 50, 3, 5, 'done']:
    if x == "done" :
        break
    try :
        x = int(x)
    except:
        print('Invalid input')
        continue
    if largest is None :
        largest = x
    elif x > largest :
        largest = x
    if smallest is None :
        smallest = x
    elif x < smallest :
        x = smallest
print("Maximum is ", largest)
print("Minimum is ", smallest)
