# Name:        Sam Zhong
# Class:       CSC 110 - Fall 2022
# Assignment:  Programming Project Design
# Due Date:    November 11, 2022

# Program Title:  TV Show Data

# Project Description:
# --------------------
# This program will tell the user the specific stats they would want to know about the all the TV Shows in the Dataset.
# The user will choose a number between 1 and 7 and the program will give the user data depending on
# what the user has entered.
# --------------------

# Pseudocode
# --------------------
# The main function will contain all these options for the user to chose from, and when the user chooses one of them,
# the main function will run a function defined earlier that does a corresponding task. The program will only end
# when the user enters the input 7, else it will keep repeating and ask the user to enter a new value.
# 1 -- Find all shows with a certain rating
# 2 -- Find the show with the highest score released in a specified range of years
# 3 -- Search for  show by title
# 4 -- Find the average score for films with a specific rating
# 5 -- Find all shows with a score higher than the score for a given show
# 6 -- Sort all lists by year and write results to a new file
# 7 -- Quit
# --------------------

# Function design
# --------------------

# This function will test if the file name entered exists
def getFile():
    return fname


# This function will get the data and store all the data in 4 separate lists
def getData():
    return titleList, ratingList, yearList, scoreList


# 1
# ---------------------
# This function will test if the rating entered by the user is a valid rating
def testRating():
    return rating


# This function will find all shows with a certain rating
def getRating(titleList, ratingList):
    return goodRatingIndex


# This function will print the TV shows that meets the criteria
def printResultRating(goodRatingIndex, titleList, ratingList, yearList, scoreList):
    return


# ---------------------

# 2
# ---------------------
# This function will get year 1 and test if in range
def getYear1():
    return year1


# This function will get year 2 and test if in range
def getYear2():
    return year2


# This function will test is year 2 is after year 1
def testYear(year1, year2):
    return year1, year2


# This function will find the TV show with the highest rating
def getHighest(scoreList, yearList):
    return highestIndex


# This function will print the TV show that has the highest rating in the range the user entered
def printResultHighest(highestIndex, titleList, ratingList, yearList, scoreList):
    return


# ----------------------

# 3
# ----------------------
# This function check if the title entered by the user is valid, not case-sensitive
def getTVShow():
    return TVShow


# This function will give the position of the TV show entered by the user
def getTVShowIndex(TVShow, titleList):
    return TVShowIndex


# This function will print out the datas for the TV show entered by the user
def printResultTVShowData(TVShowIndex, titleList, ratingList, yearList, scoreList):
    return


# ----------------------

# 4
# ----------------------
# A function to test if the rating entered is valid is needed which is already defined above

# This function will find the average score of the rating input by the user
def averageScore(rating, ratingList):
    return averageScore


# ----------------------

# 5
# ----------------------
# A function to test if the TV show name entered is valid is needed which is already defined above

# A function to get the index of the TV show entered will be needed which is defined above

# This function will get the index of all the TV show with a score higher than the one entered by the user
def getHigherRatedShowsIndex(TVShowIndex, titleList, scoreList):
    return higherRatedShowsIndex


# This function will print all the TV shows
def printResultHigherRatedShows(higherRatedShowsIndex, titleList, ratingList, yearList, scoreList)
    return


# ----------------------

# 6
# ----------------------
# This function will sort the years
def sortYears(yearList):
    return sortedYearIndex


# This function will print the outputs in a separate file
def printSortedYear(sortedYearIndex, titleList, ratingList, yearList, scoreList):
    return


# ----------------------

# 7
# ----------------------
# This function will check if the number entered by the user is between 1 and 7
def testNum():
    return Num


# ----------------------

# This function is the main function, and it will call all the functions from above
def main():
    return
