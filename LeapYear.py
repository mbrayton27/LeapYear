#Run this code by typing "python matthew_brayton_hw1.py" on the engineering server command line. It is just a normal python file
number = int(input("Enter an integer number: "))

if(number%4) == 0:
    if(number%100) == 0:
        if (number%400) == 0:
            print("That year is leap year")
        else:
            print("That year is NOT a leap year")
    else:
        print("That year is a leap year")
else :
    print("That year is NOT a leap year")
