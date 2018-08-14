"""
Zach Miller
10/7/2013
assignment 5-1
"""

def main():
    hoursWorked=float(input('Please enter the amount of hours worked (from 1 to 36): '))
    while (hoursWorked<1 or hoursWorked>36):
        print('ERROR: The hours worked cannot be less than 1 or greater than 36')
        hoursWorked=float(input('Please enter the amount of hours worked (from 1 to 36): '))
    hourlyRate=float(input('Please enter your hourly pay rate:'))
    while(hourlyRate<=0):
        print('ERROR: The hourly rate must be greater than 0')
        hourlyRate=float(input('Please enter your hourly pay rate:'))
    calcPay(hoursWorked,hourlyRate)

def calcPay(hours,payRate):
    grossPay=(hours*payRate)
    print('Your gross pay for',hours,'hours at',payRate,'is',format(grossPay,'.2f'),'dollars')

main()
