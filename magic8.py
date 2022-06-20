import random

name = "Lorice"
question = 'Will I be born on August 17th?'
answer = ""
random_number = random.randint(1, 11)

print(name + ' ' + 'asks' + ' ' + question)

print("Magic 8-Ball's answer:")

# This will show the number that correlates to the answer below. Removing this line will make it so only the answer text is printed. 
print(random_number)

if random_number == 1:
  print('Yes - definitely.')
elif random_number == 2:
  print('It is decidedly so.')
elif random_number == 3:
  print('Without a doubt.')
elif random_number == 4:
  print('Reply hazy, try again.')
elif random_number == 5:
  print('Ask again later.')
elif random_number == 6:
  print('Better not tell you now.')
elif random_number == 7:
  print('My sources say no.')
elif random_number == 8:
  print('Outlook not so good.')
elif random_number == 9:
  print('Very doubtful.')
elif random_number == 10:
  print("Not a chance.")
elif random_number == 11:
  print("Anything can happen!")
else:
   answer = 'Error'
