print('Welcome to the love calculator')
name1 = input("What is your name? ") 
name2 = input("What is their name? ") 
#will take names and compare them to 'true love'
#names combined and counts number of letter matches to 'true'
#names combined and counts number of letter matches to 'love'

combine_names = name1 + name2
lower_names = combine_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

true_name = t +  r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

love_name = l + o + v + e
#add together as string, but place in integer to compare to a number

love_score = int(str(true_name) + str(love_name))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, better luck next time")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are compatible")
else: 
  print(f"Not sure, but your love score is {love_score}")
  
  



