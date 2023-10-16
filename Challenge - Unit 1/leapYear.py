#note: To help bring the calendar back into alignment, we skip Leap Day if it falls on the start of a century, unless that century is divisible by 400. The rule is that if the year is divisible by 100 and not divisible by 400, leap year is skipped

def leapYear():
    year = int(input("Enter the year:"))
    if(year%4==0):
        if(year%100==0)and(year%400!=0):
            print("This is a skipped leap year")
        else:
            print("This is a leap year")
    else:
        print("This is not a leap year")

print("LEAP YEAR")
leapYear();
while(True):
    choice=input("Enter  y to check another one...")
    if(choice=='y' or choice=='Y'):
        leapYear()
    else:
        break;
print("sayonera");



