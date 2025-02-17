# *****************************************************************************
# Author:       	AJ Alstadt
# Assignment:       Assignment 2
# Date:         	2/16/2025
# Description:  	Video game rating program. This program will allow you
# to enter video games you've played and assign them a rating from 1-10. Then
# it will average the scores and tell you the minimum and maximum ratings.
# Input:        	Video games, Ratings from 1-10
# Output:       	List of all games, average score, minimum & max scores.
# Sources:      	D2L Unit 6 content
#
# Notes:            Created in Pycharm, version control with Git
# *****************************************************************************


def main():
    # Welcome message
    print("\nWelcome to the VGRS (Video Game Rating System).\n\n"
          "The VGRS will allow you to rate the video games you’ve played, "
          "and then display the \nlist of games and their corresponding ratings,"
          " as well as some statistics.")

    # Declaring variables, parallel lists
    titles = []
    scores = []
    totals = 0.00
    more = "y"

    while more.lower() == "y":

        title = input("\nPlease enter the name of a game: ")

        # Error Handling
        if title == "":
            print("You didn't enter a title.")
            continue

        # Ask for a score
        while True:
                score_input = input("\nPlease rate the game from 1.00-10.00: ")
                #convert score to float
                score = float(score_input)


                # Error handling
                if 1.00 <= score <= 10.00:
                    break
                else:
                    print("The rating must be between 1.00 and 10.00. Please try again.")

        # Store valid input in lists
        titles.append(title)
        scores.append(score)

        more = input("Would you like to enter another title? (Y/N): ")





    # Adds the scores together to get the average later
    for i in range(len(scores)):
        totals += scores[i]

    average = totals / len(scores)

    #Update highest and lowest scores
    highest = max(scores)
    lowest = min(scores)

    #Attach highest and lowest rated games to their scores
    highestindex = scores.index(highest)
    lowestindex = scores.index(lowest)
    highestgame = titles[highestindex]
    lowestgame = titles[lowestindex]



    print("\nHere is the summary of your ratings:")
    print(f"Games: {titles}")
    print(f"Scores: {scores}")
    print(f"Average Rating: {average:.2f}")
    print(f"Highest Rated Game: {highestgame} ({highest:.2f})")
    print(f"Lowest Rated Game: {lowestgame} ({lowest:.2f})")

    input("\nPress enter to exit")



main()
