def main():
    # prob1()
    prob2()






#Create a function that has a loop
# Prompt for numbers until the user enters q to quit
# If the user doesn't enter q, ask them to input another number
# When the user enters q to quit, print the SUM of all numbers entered

# def prob1():
#
#     userNum = int(input("Enter a number"))
#     sumofall = []
#
#
#     while(userNum != 0):
#         userNum = int(input("Enter another number"))
#         sumofall.append(userNum)
#
#
#     print(sum(sumofall))
#
#





def prob2():


    userNum1 = int(input("Enter a number"))
    userNum2 = int(input("Enter another number"))
    thisVar = do_the_math(userNum1, userNum2)

    print(f"The SUM result is: {thisVar['sum']}\nThe DIFFERENCE result is: {thisVar['diff']}\nThe QUOTIENT result is: {thisVar['quot']}\nThe PRODUCT result is: {thisVar['prod']}")


def do_the_math(x, y):

    numDiction= {"diff": x-y, "sum": x + y, "quot": x/y, "prod": x*y}



    return numDiction






if __name__ == '__main__':
    main()