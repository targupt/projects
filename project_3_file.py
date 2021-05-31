import random
random_number = random.randint(1,10)
print(random_number)
print("guess a number between 1- 100 as compt has made a number")
num = input()
print("Number was ", random_number,"if it is correct write y and wrong the n")
yn = input()
if num == random_number:
    print("good")
