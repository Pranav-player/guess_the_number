number = int(input("Enter a number: "))
actual_number = 1000
attempt = 0

while True:
  if number < actual_number:
    print("Too low")
    number = int(input("Enter a number "))
    attempt += 1
  elif number > actual_number:
    print("Too high")
    number = int(input("Enter a number "))
    attempt += 1
  elif number == actual_number:
    print("CORRECT!")
    attempt += 1
    break
  else:
    exit()
    
print("It took you", attempt, "attempts to get the correct answer")