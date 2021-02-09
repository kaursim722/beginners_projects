import random

def guess_num():
  num = random.randint(0,10)
  print(num)
  user_input = input("Guess a number between 0 and 10: ")
  while True:
    if int(user_input) != int(num):
      if int(user_input) < int(num):
        user_input = input("guess a larger number: ")
      elif int(user_input) > int(num):
        user_input = input("guess a smaller number: ")
    else:
      print("Good job!")
      break

guess_num()