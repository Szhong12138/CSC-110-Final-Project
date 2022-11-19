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
    # Defines infile as a variable
    infile = ''

    # Sets goodDile to False
    goodFile = False

    # A while loop to check if the file input by the user exists, and asks the user to input a file name
    # until finding one that exists
    while not goodFile:
        fname = input("Please enter the name of the data file: ")
        try:
            infile = open(fname, 'r')
            goodFile = True
        except FileNotFoundError:
            print('Invalid file name, try again ...')

    # Returns the name of the file
    return infile


# This function will get the data and store all the data in 4 separate lists
def getData():

    # Sets infile to the file defined in the function openFile()
    infile = getFile()

    # Sets 4 empty strings to store the 4 different types of data in each list
    titleList = []
    ratingList = []
    yearList = []
    scoreList = []

    # Reads one line and sets the pointer to line 2 because line 1 isn't needed because it is the title and no the data
    infile.readline()

    # Sets line to the second line for the while loop to read
    line = infile.readline()

    # A while loop that reads each line in the dataset until it gets to a blank line
    while line != '':
        # Strips all the blank lines in line and ets in to line
        line = line.strip()

        # Splits the data when a comma appears and store each category in a variable
        title, rating, year, score = line.split(',')

        # Adds each data from ech line to their corresponding lists
        yearList += [int(year)]
        titleList += [str(title)]
        ratingList += [str(rating)]
        scoreList += [int(score)]

        # Reads the next line
        line = infile.readline()

    # Closes the file
    infile.close()

    # Returns the data all stored in there corresponding list
    return titleList, ratingList, yearList, scoreList


# 1
# ---------------------
# This function will test if the rating entered by the user is a valid rating
def testRating():
    rating = ''

    goodRating = False

    while not goodRating:
        rating = str(input('Enter rating: '))
        try:
            if rating in ['TV-MA', 'TV-Y7-FV', 'TV-Y7', 'TV-G', 'TV-PG', 'TV-Y', 'TV-14']:
                rating = str(rating)
                goodRating = True
            else:
                rating = int(rating)
        except ValueError:
            print('Invalid entry - try again')

    return rating


# This function will find all shows with a certain rating
def getRating(ratingList):
    rating = testRating()
    goodRatingIndex = []
    for i in range(len(ratingList)):
        if ratingList[i] == rating:
            goodRatingIndex.append(i)
    return goodRatingIndex


# This function will print the TV shows that meets the criteria
def printResultRating(goodRatingIndex, titleList, ratingList, yearList, scoreList):
    print('The TV shows that meet your criteria are:\n')
    print('TITLE                                   RATING    YEAR  SCORE')
    for i in goodRatingIndex:
        print(titleList[i].ljust(40), ratingList[i].ljust(8), str(yearList[i]).ljust(5), str(scoreList[i]).ljust(4))
    return


# ---------------------

# 2
# ---------------------
# This function will get year 1 and test if in range
def getYear1():
    year1 = ''
    goodYear = False
    print('Enter year range to search (oldest year first)')
    while not goodYear:
        year1 = input('Year1: ')
        try:
            year1 = int(year1)
            if 2018 > year1 > 1989:
                goodYear = True
            else:
                print('Invalid year - try again')
        except ValueError:
            print('Invalid entry - try again')

    return year1


# This function will get year 2 and test if in range and test if year 2 is bigger than year 1
def getYear2():
    year2 = ''
    year1 = getYear1()
    goodYear = False
    while not goodYear:
        year2 = input('Year2: ')
        try:
            year2 = int(year2)
            if year1 > year2 > 1989:
                print('Second year should be after first year - try again')
                year1 = getYear1()
            elif 2018 > year2 > 1989:
                goodYear = True
            else:
                print('Invalid year - try again')
        except ValueError:
            print('Invalid entry - try again')
    return year1, year2


# This function will create a list with the years in range
def findYearsInRange(yearList):
    year1, year2 = getYear2()
    yearsInRangeIndex = []
    for i in range(len(yearList)):
        if year1 <= yearList[i] <= year2:
            yearsInRangeIndex.append(i)
    return yearsInRangeIndex


# This function will find the TV show with the highest rating
def getHighest(scoreList, yearsInRangeIndex):
    highestIndex = scoreList[yearsInRangeIndex[0]]
    for i in yearsInRangeIndex:
        if scoreList[i] > scoreList[highestIndex]:
            highestIndex = i
    return highestIndex


# This function will print the TV show that has the highest rating in the range the user entered
def printResultHighest(highestIndex, titleList, ratingList, yearList, scoreList):
    print('The TV shows that meet your criteria are:\n')
    print('TITLE                                   RATING    YEAR  SCORE')
    print(titleList[highestIndex].ljust(40), ratingList[highestIndex].ljust(8), str(yearList[highestIndex]).ljust(5),
          str(scoreList[highestIndex]).ljust(4))
    return


# ----------------------

# 3
# ----------------------
# This function will get the name of the tv show
def getTVShow():
    TVShow = input('Enter show title: ')
    return TVShow


# This function will give the position of the TV show entered by the user
def getTVShowIndex(TVShow, titleList):
    for i in range(len(titleList)):
        if titleList[i].lower() == TVShow.lower():
            TVShowIndex = i
            return TVShowIndex


# This function will print out the datas for the TV show entered by the user
def printResultTVShowData(TVShowIndex, titleList, ratingList, yearList, scoreList):
    if TVShowIndex is None:
        print('\nNo shows meet your criteria')
    else:
        print('The TV shows that meet your criteria are:\n')
        print('TITLE                                   RATING    YEAR  SCORE')
        print(titleList[TVShowIndex].ljust(40), ratingList[TVShowIndex].ljust(8), str(yearList[TVShowIndex]).ljust(5),
              str(scoreList[TVShowIndex]).ljust(4))
    return


# ----------------------

# 4
# ----------------------
# A function to test if the rating entered is valid is needed
def getRating2(ratingList):
    rating = testRating()
    goodRatingIndex = []
    for i in range(len(ratingList)):
        if ratingList[i] == rating:
            goodRatingIndex.append(i)
    return goodRatingIndex, rating


# This function will find the average score of the rating input by the user
def averageScore(goodRatingIndex, scoreList):
    Sum = 0
    for i in range(len(goodRatingIndex)):
        Sum += scoreList[goodRatingIndex[i]]
    average = Sum/len(goodRatingIndex)
    return average


def printAverageScore(average, rating):
    print('The average score for shows with a ', rating, ' is ', round(average, 2))
    return


# ----------------------

# 5
# ----------------------

# A function to test if the TV show name entered is valid is needed
def testTVShow(titleList):
    goodShow = False
    TVShow = ''
    while goodShow is False:
        TVShow = input('Enter title: ')
        try:
            if TVShow in titleList:
                TVShow = TVShow
            else:
                TVShow = int(TVShow)
            goodShow = True
        except ValueError:
            print('Invalid entry - try again')
    return TVShow


# A function to get the index of the TV show entered will be needed which is defined above
def getTVShowIndex2(TVShow, titleList):
    for i in range(len(titleList)):
        if titleList[i].lower() == TVShow.lower():
            TVShowIndex = i
            return TVShowIndex


# This function will get the index of all the TV show with a score higher than the one entered by the user
def getHigherRatedShowsIndex(TVShowIndex, scoreList):
    higherRatedShowsIndex = []
    for i in range(len(scoreList)):
        if scoreList[i] > scoreList[TVShowIndex]:
            higherRatedShowsIndex.append(i)
    return higherRatedShowsIndex


# This function will print all the TV shows
def printResultHigherRatedShows(higherRatedShowsIndex, titleList, ratingList, yearList, scoreList):
    print('The TV shows that meet your criteria are:\n')
    print('TITLE                                   RATING    YEAR  SCORE')
    for i in range(len(higherRatedShowsIndex)):
        print(titleList[i].ljust(40), ratingList[i].ljust(8), str(yearList[i]).ljust(5), str(scoreList[i]).ljust(4))
    return


# ----------------------
'''
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
'''


titleList, ratingList, yearList, scoreList = getData()
testTVShow(titleList)

