##Function Prime Number
def startPrimeNumber():
    print("Prime numbers are numbers greater than 1 and can only be divided by itself and 1.")
    num = input("Enter a valid integer\n:")
    try:
        if int(num) > 1:
            num = int(num) ## converted to int so that all kinds of integer values can work. Initial test 17678980' did not work without this line
            for i in range(2, 9): ##iterate i starting from 2, 
                if(num % i) == 0:
                    print (num, "is not a prime number")
                    user_input = input("Press Y to try again or Press N to go to main menu or Press Q to quit\n:").lower()
                    if user_input == "y":
                       startPrimeNumber() 
                    elif user_input == "n":
                        startProgram()
                    elif user_input == "q":
                        print ("Test ended")
                    else:
                        print ("invalid input")
                        startProgram()
                else:
                    print (num, " is a prime number")
                    user_input = input("Press Y to try again or Press N to go to main menu or Press Q to quit\n:").lower()
                    if user_input == "y":
                       startPrimeNumber() 
                    elif user_input == "n":
                        startProgram()
                    elif user_input == "q":
                        print ("Test ended")
                    else:
                        print ("invalid input")
                        startProgram()
        else:
            print ("Value cannot be less than or equal to 0. Kindly refer to the prime number definition above. Thank you")
            user_input = input("Press Y to try again or Press N to go to main menu or Press Q to quit\n:").lower()
            if user_input == "y":
               startPrimeNumber() 
            elif user_input == "n":
                startProgram()
            elif user_input == "q":
                print ("Test ended")
            else:
                print ("invalid input")
                startProgram()
    except ValueError:
        print ("Value must be an integer.")
        user_input = input("Press Y to try again or Press N to go to main menu or Press Q to quit\n:").lower()
        if user_input == "y":
           startPrimeNumber() 
        elif user_input == "n":
            startProgram()
        elif user_input == "q":
            print ("Test ended. Thank you")
        else:
            print ("invalid input")         
            startProgram()
            
##function get maximum value
def startMaxValue ():
    numbers = []
    for j in range (1, 4):
        try:
            user_input = int(input("Enter value" + str(j) + ":"))#convert j to string as python can't concatenate int:j and str
        except ValueError:
            print ("Invalid input for value" + str(j) + ". Value must be an integer.")
            user_input = input("Press Y to try again or Press N to go to main menu or Press Q to quit\n:").lower()
            if user_input == "y":
               startMaxValue() 
            elif user_input == "n":
                startProgram()
            elif user_input == "q":
                print ("Test ended. Thank you")
            else:
                print ("invalid input")
                startProgram()
        else:
            numbers.append(user_input)
    print ("Max value in your list of input is:" + str(max(numbers)))


###Check Number of uppercase and lowercase characters
def startNumChar ():
    uppercase = 0
    lowercase = 0
    user_input = input("Enter your a sentence: ")
    try:
        if str(user_input):
            for i in user_input:
                if(i.islower()):
                    lowercase=lowercase+1
                elif(i.isupper()):
                    uppercase=uppercase+1
    except ValueError:
        print ("Invalid input for value" + str(j) + ". Value must be a string.")
        user_input = input("Press Y to try again or Press N to go to main menu or Press Q to quit\n:").lower()
        if user_input == "y":
           startMaxValue() 
        elif user_input == "n":
            startProgram()
        elif user_input == "q":
            print ("Test ended. Thank you")
        else:
            print ("invalid input")
            startProgram()
            
    print("The number of lowercase characters in " +user_input+ " is "+str(lowercase)+"\n")
    print("The number of uppercase characters in " +user_input+ " is "+str(uppercase)+"\n")

    

####Start Program
def startProgram():
    start_input = input("Enter 1 to test for prime number\nEnter 2 to find max value of 3 input\nEnter 3 to check number of Uppercase and lowercase characters.\n:")
    try:
        if int(start_input) == 1:
            startPrimeNumber()
        elif int(start_input) == 2:
            startMaxValue ()
        elif int(start_input) == 3:
            startNumChar ()
        else:
            print ("invalid input")
    except ValueError:
        print ("Input must be 1,2 or 3.")
        user_input = input("Want to try again?\nPress Y to try again or Press N to quit\n:").lower()
        if user_input == "y":
           startProgram() 
        elif user_input == "n":
            print ("Test ended")
        else:
            print ("invalid input")  
            quit()

    


startProgram()
