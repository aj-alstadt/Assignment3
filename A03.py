#*****************************************************************************
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
#*****************************************************************************


def main():
    print("\nWelcome to the VGRS (Video Game Rating System).\n\n"
          "The VGRS will allow you to rate the video games you’ve played, "
          "and then display the \nlist of games and their corresponding ratings,"
          " as well as some statistics.")

    #Declaring variables
    titles = []
    scores = []
    totals = 0.00

    #Adds the scores together to get the average later
    for i in range(len(scores)):
        totals += scores[i]

    average = totals / len(scores)

    while more == "y":

        title = input("\nPlease enter the name of a game, or type 'done' to finish: ")
        score =











main()