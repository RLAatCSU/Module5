#Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
#The program should first ask for the number of years. The outer loop will iterate once for each year. The inner
#loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the
#inches of rainfall for that month. After all iterations, the program should display the number of months,
#the total inches of rainfall, and the average rainfall per month for the entire period.

numberEntered = False                                                  #declare Boolean used for while condition

#while loop verifies a number was entered
while numberEntered == False:
    rainDataYears = str(input('Enter a positive whole number for the number of years of rainfall data that '
                              'was collected:\n'))                     #Ask the user to input the years
    numberEntered = rainDataYears.isnumeric() and rainDataYears != '0' #Verify entry is a number, exit loop if True
    if numberEntered == False:
        print('You did not enter a positive whole '
              'number, please enter a positive whole number.')        #Inform user they did not enter a number

rainDataYearsInt = int(rainDataYears)                                 #convert numeric entry to an integer
numberOfMonths = rainDataYearsInt * 12                                #determine total number of months
totalRain = 0.0                                                       #declare totalRain as a float
numberEntered = False                                                 #reset Boolean used for while condition
years = 0                                                             #declare years as an integer
months = 0                                                            #declare months as an integer
monthTuple = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December')  #declare monthTuple

#Outer loop iterates for total number of years, inner loop iterates for the 12 months
while years < rainDataYearsInt:
    while months < 12:
        numberEntered = False                                               #reset Boolean used for while condition
        # while loop verifies a number was entered
        while numberEntered == False:
            rainForMonth = input(str('Enter amount of rain in inches for ' +
                monthTuple[months] + ' in year ' + '{:d}'.format(years + 1)
                    + ':\n'))                                        #Ask the user to input the rain for the month
            check2 = rainForMonth.replace(".", "").strip()     #Remove decimal points for numeric check
            numberEntered = check2.isnumeric()                             # Verify entry is a number, exit loop if True
            if numberEntered == False:
                print('You did not enter a positive number, please enter a number.') #Inform user not a + number
        rainForMonthReal = float(rainForMonth)                               #convert numeric entry to a float
        totalRain += rainForMonthReal                                        #accumulate total rain
        months += 1                                                          #increment number of months
        numberEntered = False                                                #reset Boolean used for while condition
    years += 1                                                               #increment number of years
    months = 0                                                               #clear number of months

monthlyAverageRain = totalRain / numberOfMonths                              #determine monthly average rain

print('The total number of months was: ' + '{:d}'.format(numberOfMonths))
print('The total amount of rain in inches was: ' + '{:.2f}'.format(totalRain))
print('The average amount of rain in inches per month was: ' + '{:.2f}'.format(monthlyAverageRain))