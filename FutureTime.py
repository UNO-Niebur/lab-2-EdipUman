#FutureTime.py
#Name:Edip Uman
#Date:02/01/2026
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  #Ask user for minutes
  addHours = int(input("Enter hours: "))
  addMinutes = int(input("Enter minutes: "))
  #Calculate the time after the user-supplied time has passed.
  TotalMinutes = currentHour * 60 + currentMinute
  addedMinutes = addHours * 60 + addMinutes
  FutureTotalMinutes = (TotalMinutes + addedMinutes) % (24 * 60)
  FutureHour = FutureTotalMinutes // 60
  FutureMinute = FutureTotalMinutes % 60
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(str(FutureHour) + ":" + str(FutureMinute))

if __name__ == '__main__':
  main()
