number = 0
while true:
 try:
    number = int(input("Enter a number (0 to exit)/n"))
    if number == 0:
        break
    else:
    total += number
  except ValueError:
    print ("invalid, please enter only numbers")

print(f" the total is: {total}")   