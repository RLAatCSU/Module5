#The CSU Global Bookstore has a book club that awards points to its students based on the number of books
#purchased each month. The points are awarded as follows:
#
#If a customer purchases 0 books, they earn 0 points.
#If a customer purchases 2 books, they earn 5 points.
#If a customer purchases 4 books, they earn 15 points.
#If a customer purchases 6 books, they earn 30 points.
#If a customer purchases 8 or more books, they earn 60 points.
#
#Write a program that asks the user to enter the number of books that they have purchased this month and
#then display the number of points awarded.

numberEntered = False                                                  #declare Boolean used for while condition

#while loop verifies a number was entered
while numberEntered == False:
    booksPurchased = str(input('Enter a non-negative whole number for the number of books purchased '
                              'this month:\n'))                       #Ask the user to input the number of books
    numberEntered = booksPurchased.isnumeric()                        #Verify entry is a number, exit loop if True
    if numberEntered == False:
        print('You did not enter a non-negative whole '
              'number, please enter a number.')                       #Inform user they did not enter a number

booksPurchasedInt = int(booksPurchased)                               #convert numeric entry to an integer

if 0 <= booksPurchasedInt < 2:
    print('0 points earned this month')
elif 2 <= booksPurchasedInt < 4:
    print('5 points earned this month')
elif 4 <= booksPurchasedInt < 6:
    print('15 points earned this month')
elif 6 <= booksPurchasedInt < 8:
    print('30 points earned this month')
else:
    print('60 points earned this month')