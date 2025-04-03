attempts = 0
correct_answer = "Tokyo"

while attempts < 5:
    answer = input("What is the capital city of Japan? ")

    if answer == correct_answer:
        print("Correct! Well done.")
        break

    attempts += 1
    print(f"Wrong answer. You have {5 - attempts} attempts left.")

if attempts == 5:
    print("Sorry, you've used all attempts. The correct answer is Tokyo.")