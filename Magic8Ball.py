#Magic8Ball.py
#Name: Edip Uman
#Date:02/01/2026
#Assignment: Lab 2 Magic8Ball.py

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  responses = ["Magic 8 Ball needs help","Not Good","You will understand",
  "Bannanas",  "Lucky",  "Acrobatic", "Tell me more"]
  #Prompt the user for their question.
  userquestion = input("How am I feeling today")
  #Answer question randomly with one of the options from your earlier list.
  print(random.choice(responses))

if __name__ == '__main__':
  main()
