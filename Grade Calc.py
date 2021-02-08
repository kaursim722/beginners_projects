def calculate():

  hw = float(input("Enter HW average: "))
  quiz = float(input("Enter quiz average: "))
  special_1 = float(input("Enter Special Quiz 1: "))
  special_2 = float(input("Enter Special Quiz 2: "))

  grade = ((hw * 0.25) + (quiz * 0.25) + (special_1 * 0.25) + (special_2 * 0.25))
  print('\n',"Grade percentage:", grade)

  if grade <= 69:
    print("Letter Grade: F")
  elif grade <= 79 and grade >= 70:
    print("Letter Grade: C")
  elif grade <= 89 and grade >= 80:
    print("Letter Grade: B")
  else:
    print("Letter Grade: A")

calculate()
