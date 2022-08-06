def is_leap(year):
    """Finds out if the year is a leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True #print("Leap year.")
            else:
                return False #print("Not leap year.")
        else:
            return True #print("Leap year.")
    else:
        return False #print("Not leap year.")

def days_in_month(ye,mo):
    """Represents the amount of days in the given month"""
    if mo > 12 or mo < 1:
        return "Not valid month!"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(ye) == True:
        month_days[1] = 29
    return f"There are {month_days[mo-1]} days in this month"

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

days = days_in_month(year, month)
print(days)