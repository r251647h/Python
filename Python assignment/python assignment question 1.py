# Question 1: Age Validator
while True:
    try:
        Age=int(input("What is your Age ?:"))
        print("You are",Age,"year old")
        break
    except ValueError:
        print("Invalid input please enter age again")