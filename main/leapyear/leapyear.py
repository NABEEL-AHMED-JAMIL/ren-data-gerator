def check_leap(leap_year):
 # Checking if the given year is leap year
  if (leap_year % 400 == 0) or (leap_year % 100 != 0) and (leap_year % 4 == 0):
    print("Yes! This Year is a leap Year");
  else: # Else it is not a leap year
    print ("This Year is not a leap Year")


if __name__ == '__main__':
    # Taking an input year from user
    year = int(input("Enter the number here: "))
    # Printing result
    check_leap(year)