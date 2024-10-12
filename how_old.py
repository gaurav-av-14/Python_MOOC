# Write your solution here
from datetime import datetime, timedelta
def main():
    day = input("Day: ")
    mon = input("Month: ")
    yr = input("Year: ")
    day,mon,yr = int(day),int(mon),int(yr)
    bday = datetime(yr,mon,day)
    eve = datetime(1999,12,31)
    age_on_eve = eve - bday
    if eve.year < bday.year:
        print("You weren't born yet on the eve of the new millennium.")
        return
    print(f"You were {age_on_eve.days} days old on the eve of the new millennium.")

main()