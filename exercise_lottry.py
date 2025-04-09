user_numbers = set()

while len(user_numbers) < 7:
   try:
 num = int(input(f"Enter a unique numbers ({len(user_numbers)+1}/7): "))
 if num in user_numbers:
  print("error: number already entered. please enter a different number.")
 else:
  user_number.add(num)
 except valueerror:
print(2invalid input input.please enter a valid number.)
print("the 7 unique number you entered are:/n")
 
