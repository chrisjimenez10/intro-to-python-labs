#Global Variables
earnings = 0
investment = 0
day = 0

def startGame():
    global earnings, day
    earnings = 0
    day = 0

    print(F"Hello Landscaper! You can only use your teeth right now, but work to earn enough money to purchase equipment")
    while True:

        answer = input(F"Options: 1.Use teeth ($1) - 2.Rusty Scissors ($5) 3.Lawnmower ($50) 4.Fancy-Lawnmower ($100) 5.Lanscaping Team ($250) or 0.(Exit): ")

        while answer.isdigit() != True or len(answer) != 1:
            if len(answer) == 0:
                print("Invalid input. You entered nothing, please type single digit")
            elif len(answer) > 1:
                print("Invalid input. Multiple digits inserted, please type single digit")
            elif not answer.isdigit():
                print("Invalid input. You did not type a number, please type single digit")
            answer = input("Please type the number option: ")

        if int(answer) == 1:
            earnings += 1
            day += 1
            print(F"It is day: {day} and your total earnings are: ${earnings}")
        if int(answer) == 2:
            if earnings < 5:
                print(F"You do not have enough funds - Rusty Scissors cost ${5} - You need ${5 - earnings} more")
            else:
                earnings += 5
                day += 1
                print(F"It is day {day} and your total earnings are: ${earnings}")   
        if int(answer) == 3:
            if earnings < 25:
                print(F"You do not have enough funds - Lawnmower costs $25 - You need ${25 - earnings} more") 
            else:
                earnings += 50
                day += 1
                print(F"It is day {day} and your total earnings are: ${earnings}")  
        if int(answer) == 4:
            if earnings < 250:
                print(F"You do not have enough funds - Fancy Lawnmower costs $250 - You need ${250 - earnings} more") 
            else:
                earnings += 100
                day += 1
                print(F"It is day {day} and your total earnings are: ${earnings}")  
        if int(answer) == 5:
            if earnings < 500:
                print(F"You do not have enough funds - Landscaping Team costs $500 - You need ${500 - earnings} more") 
            else:
                earnings += 250
                day += 1
                print(F"It is day {day} and your total earnings are: ${earnings}")  

        if int(answer) == 0:
            print(F"You earned a total of ${earnings} in {day} days - Exiting...")
            break

        # Win condition
        if earnings > 1000:
            print(F" Congratulations you won! You have amassed over $1000 with a total of ${earnings}")
            break

startGame()

