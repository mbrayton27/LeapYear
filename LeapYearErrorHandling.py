#Run this code by typing "python matthew_brayton_hw1.py" on the engineering server command line. It is just a normal python file
check = False;
while not check:
    try:
        number = int(input("What year do you want to check?"))
        check = True;
        break;
    except ValueError:
        print("Please enter an integer")
        continue


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
