# Name:        Sam Zhong
# Class:       CSC 110 - Fall 2022
# Assignment:  Programming Project Design
# Due Date:    December 13, 2022

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
        fname = input("Enter the name of the data file: ")
        try:
            infile = open(fname, 'r')
            goodFile = True
        except FileNotFoundError:
            print('Invalid file name - try again')

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

    # Defines rating as a variable
    rating = ''

    # Set good Rating to False
    goodRating = False

    # A while loop that keeps running goodRating is False, and it tests if the rating that the user entered is a valid
    # rating, and when the user enters a valid rating, goodRating will e set to True and the while loop will stop
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

    # Returns rating
    return rating


# This function will find all shows with a certain rating
def getRating(ratingList):

    # Defines rating
    rating = testRating()

    # Initializes an empty list
    goodRatingIndex = []

    # A for loop that adds the index of all the tv shows with the same rating that the user entered
    for i in range(len(ratingList)):
        if ratingList[i] == rating:
            goodRatingIndex.append(i)

    # Returns the rating the user entered and the Index of tv shows with the corresponding ratings
    return goodRatingIndex, rating


# This function will print the TV shows that meets the criteria
def printResultRating(goodRatingIndex, titleList, ratingList, yearList, scoreList):

    # Prints the output in the specific format
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

    # Defines the variable year1
    year1 = ''

    # Sets goodYear to False
    goodYear = False

    # A while loop that keeps running until goodYear doesn't equal to False, goodYear will be set to True when the user
    # enters a number, and the number is in range
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

    # Returns year1
    return year1


# This function will get year 2 and test if in range and test if year 2 is bigger than year 1
def getYear2():

    # Defines year2 as a variable
    year2 = ''

    # Gets year 1 from the function getYear1()
    year1 = getYear1()

    # Sets goodYear to False
    goodYear = False

    # A while loop keeps running until goodYear doesn't equal to False, it will test if year2 is an integer, it will
    # also test if it is in range, and it will test if year2 is bigger than year1, if it's not, it will ask for year1
    # again, and will keep running until year2 is bigger than year1
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

    # Returns year1 and year2
    return year1, year2


# This function will create a list with the years in range
def findYearsInRange(yearList):

    # Defines year1 and year2 with the function getYear2()
    year1, year2 = getYear2()

    # Defines an empty list to store the index of tv shows that came out between year1 and year2
    yearsInRangeIndex = []

    # A for loop that stores the index of all the tv shows that is between year1 and year2
    for i in range(len(yearList)):
        if year1 <= yearList[i] <= year2:
            yearsInRangeIndex.append(i)

    # Returns the index of all the TV shows that is between year1 and year2
    return yearsInRangeIndex


# This function will find the TV show with the highest rating
def getHighest(scoreList, yearsInRangeIndex):

    # Initializes the highest rated tv show as the first element in the list
    highestIndex = scoreList[yearsInRangeIndex[0]]

    # A for loop that finds the highest rating tv show in the range the user entered
    for i in yearsInRangeIndex:
        if scoreList[i] > scoreList[highestIndex]:
            highestIndex = i

    # Returns the index of the highest rated tv show in the range the user entered
    return highestIndex


# This function will print the TV show that has the highest rating in the range the user entered
def printResultHighest(highestIndex, titleList, ratingList, yearList, scoreList):

    # Prints the info of the highest rated tb show in the range the user entered
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

    # Sets TVShow to the users input
    TVShow = input('Enter show title: ')

    # Returns the tv show entered by user
    return TVShow


# This function will give the position of the TV show entered by the user
def getTVShowIndex(TVShow, titleList):

    # The for loop makes tv show not case-sensitive, and finds the index of the tv show entered by the user
    for i in range(len(titleList)):
        if titleList[i].lower() == TVShow.lower():
            TVShowIndex = i

            # returns the index of the tv show the user entered
            return TVShowIndex


# This function will print out the datas for the TV show entered by the user
def printResultTVShowData(TVShowIndex, titleList, ratingList, yearList, scoreList):

    # A conditional statement that prints No shows meet your criteria if no tv shows matches the users input
    if TVShowIndex is None:
        print('\nNo shows meet your criteria')

    # Prints the info of the tv show enter by the user in the required format
    else:
        print('The TV shows that meet your criteria are:\n')
        print('TITLE                                   RATING    YEAR  SCORE')
        print(titleList[TVShowIndex].ljust(40), ratingList[TVShowIndex].ljust(8), str(yearList[TVShowIndex]).ljust(5),
              str(scoreList[TVShowIndex]).ljust(4))
    return


# ----------------------

# 4
# ----------------------
# A function to test if the rating entered is valid is needed which has already been defined above


# This function will find the average score of the rating input by the user
def averageScore(goodRatingIndex, scoreList):

    # Defines the variable Sum and set it equal to zero
    Sum = 0

    # A for loop that adds all the scores of the rating entered by the user
    for i in range(len(goodRatingIndex)):
        Sum += scoreList[goodRatingIndex[i]]

    # sets average to the total score divided by the amount of tv shows with that specific rating
    average = Sum / len(goodRatingIndex)

    # Returns the average rating
    return average


def printAverageScore(average, rating):

    # Prints the average rating
    print('The average score for shows with a ', rating, ' rating is ', round(average, 2))
    return


# ----------------------

# 5
# ----------------------

# A function to test if the TV show name entered is valid is needed
def testTVShow(titleList):

    # Sets goodShow to False
    goodShow = False

    # Defines TVShow as a variable
    TVShow = ''

    # A while loop that will run until goodShow doesn't equal to False, the while loop will test if the tv show entered
    # by the user is in the dataset, and it will also test if the input is a valid string, goodShow will be set to True
    # when all requirements meet
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

    # Returns the tv show entered by the user
    return TVShow


# A function to get the index of the TV show entered will be needed which is defined above


# This function will get the index of all the TV show with a score higher than the one entered by the user
def getHigherRatedShowsIndex(TVShowIndex, scoreList):

    # Initializes a list that will store all the tv shows that has a higher score than the one that the user entered
    higherRatedShowsIndex = []

    # A for loop that gets the index of all the tv shows with a score higher than the one that the user entered
    for i in range(len(scoreList)):
        if scoreList[i] > scoreList[TVShowIndex]:
            higherRatedShowsIndex.append(i)

    # Returns the list of indexes of the shows with a score higher than the one that the user entered
    return higherRatedShowsIndex


# This function will print all the TV shows
def printResultHigherRatedShows(higherRatedShowsIndex, titleList, ratingList, yearList, scoreList):

    # A conditional statement that prints No shows meet your criteria if no tv shows has a higher score than the one the
    # user entered
    if len(higherRatedShowsIndex) == 0:
        print('\nNo shows meet your criteria')

    # Prints the tv shows that has a higher score than the tv show the user entered
    else:
        print('The TV shows that meet your criteria are:\n')
        print('TITLE                                   RATING    YEAR  SCORE')
        for i in range(len(higherRatedShowsIndex)):
            print(titleList[higherRatedShowsIndex[i]].ljust(40), ratingList[higherRatedShowsIndex[i]].ljust(8),
                  str(yearList[higherRatedShowsIndex[i]]).ljust(5), str(scoreList[higherRatedShowsIndex[i]]).ljust(4))
    return


# ----------------------

# 6
# ----------------------
# Bubble sort function
# A bubble sort will find the largest number and move it to the top throughout the list, and it is more effective when
# there are a lot of data to sort
def bubbleSort(theList):
    for n in range(0, len(theList)):
        temp = 0
        for i in range(1, len(theList)):
            temp = theList[i]
            # comparison
            if theList[i] < theList[i - 1]:
                # swap
                theList[i] = theList[i - 1]
                theList[i - 1] = temp
    return theList


# This function will sort the years
def sortYears(yearList):

    # Copied the yearList to sorted, so I could still use the original yearList
    new_yearList = list.copy(yearList)

    # Uses the BubbleSort function to sort the yearList and stores it in a variable called sorted_yearList
    sorted_yearList = bubbleSort(new_yearList)

    # Defines a list to store the sorted indexes
    indexList = []

    # A for loop that gets the index of the dataset sorted according to the order by year published
    for i in range(len(sorted_yearList)):
        for j in range(len(yearList)):
            if sorted_yearList[i] == yearList[j]:
                if j not in indexList:
                    indexList.append(j)

    # Returns the sorted indexList
    return indexList


# This function will print the outputs in a separate file
def printSortedYear(indexList, titleList, ratingList, yearList, scoreList):

    # Prints the info for the sorted data in another file called year-sorted-shows.csv
    print("\nData sorted by years written to file year-sorted-shows.csv")
    outfile = open('year-sorted-shows.csv', 'w')
    outfile.write('Title,Rating,Year,Score')
    for i in range(len(indexList)):
        outfile.write('\n' + titleList[indexList[i]] + ',' + str(ratingList[indexList[i]]) + ',' +
                      str(yearList[indexList[i]]) + ',' + str(scoreList[indexList[i]]))
    return


# ----------------------

# 7
# ----------------------
# This function will check if the number entered by the user is between 1 and 7
def testNum():
    goodNum = False
    Num = ''
    while goodNum is False:
        Num = input('Choice ==> ')
        try:
            Num = int(Num)
            while Num > 7 or Num < 1:
                print('Invalid entry - try again')
                Num = int(input('Choice ==> '))
            goodNum = True
        except ValueError:
            print('Invalid entry - try again')
    return Num


# ----------------------

# This function is the main function, and it will call all the functions from above
def main():

    # Stores all 4 difference data in 4 different variables
    titleList, ratingList, yearList, scoreList = getData()

    # Gives the user a table of content
    print('Please choose one of the following options:'
          '\n1 -- Find all shows with a certain rating'
          '\n2 -- Find the show with the highest score released in a specified range of years'
          '\n3 -- Search for a show by title'
          '\n4 -- Find the average score for films with a specific rating'
          '\n5 -- Find all shows with a score higher than the score for a given show'
          '\n6 -- Sort all lists by year and write results to a new file'
          '\n7 -- Quit')

    # Sets done to False
    done = False

    # A while loop that keeps running until done doesn't equal to False, it asks the user to type a number and tells the
    # user the info, and keeps asking them until they enter the number 7, when 7 is entered by the user,
    # the program will stop.
    while done is False:
        Choice = testNum()
        if Choice == 1:
            goodRatingIndex, rating = getRating(ratingList)
            printResultRating(goodRatingIndex, titleList, ratingList, yearList, scoreList)
            print('Please choose one of the following options:'
                  '\n1 -- Find all shows with a certain rating'
                  '\n2 -- Find the show with the highest score released in a specified range of years'
                  '\n3 -- Search for a show by title'
                  '\n4 -- Find the average score for films with a specific rating'
                  '\n5 -- Find all shows with a score higher than the score for a given show'
                  '\n6 -- Sort all lists by year and write results to a new file'
                  '\n7 -- Quit')
        elif Choice == 2:
            print('Enter year range to search (oldest year first)')
            yearsInRangeIndex = findYearsInRange(yearList)
            highestIndex = getHighest(scoreList, yearsInRangeIndex)
            printResultHighest(highestIndex, titleList, ratingList, yearList, scoreList)
            print('Please choose one of the following options:'
                  '\n1 -- Find all shows with a certain rating'
                  '\n2 -- Find the show with the highest score released in a specified range of years'
                  '\n3 -- Search for a show by title'
                  '\n4 -- Find the average score for films with a specific rating'
                  '\n5 -- Find all shows with a score higher than the score for a given show'
                  '\n6 -- Sort all lists by year and write results to a new file'
                  '\n7 -- Quit')
        elif Choice == 3:
            TVShow = getTVShow()
            TVShowIndex = getTVShowIndex(TVShow, titleList)
            printResultTVShowData(TVShowIndex, titleList, ratingList, yearList, scoreList)
            print('Please choose one of the following options:'
                  '\n1 -- Find all shows with a certain rating'
                  '\n2 -- Find the show with the highest score released in a specified range of years'
                  '\n3 -- Search for a show by title'
                  '\n4 -- Find the average score for films with a specific rating'
                  '\n5 -- Find all shows with a score higher than the score for a given show'
                  '\n6 -- Sort all lists by year and write results to a new file'
                  '\n7 -- Quit')
        elif Choice == 4:
            goodRatingIndex, rating = getRating(ratingList)
            average = averageScore(goodRatingIndex, scoreList)
            printAverageScore(average, rating)
            print('Please choose one of the following options:'
                  '\n1 -- Find all shows with a certain rating'
                  '\n2 -- Find the show with the highest score released in a specified range of years'
                  '\n3 -- Search for a show by title'
                  '\n4 -- Find the average score for films with a specific rating'
                  '\n5 -- Find all shows with a score higher than the score for a given show'
                  '\n6 -- Sort all lists by year and write results to a new file'
                  '\n7 -- Quit')
        elif Choice == 5:
            TVShow = testTVShow(titleList)
            TVShowIndex = getTVShowIndex(TVShow, titleList)
            higherRatedShowsIndex = getHigherRatedShowsIndex(TVShowIndex, scoreList)
            printResultHigherRatedShows(higherRatedShowsIndex, titleList, ratingList, yearList, scoreList)
            print('Please choose one of the following options:'
                  '\n1 -- Find all shows with a certain rating'
                  '\n2 -- Find the show with the highest score released in a specified range of years'
                  '\n3 -- Search for a show by title'
                  '\n4 -- Find the average score for films with a specific rating'
                  '\n5 -- Find all shows with a score higher than the score for a given show'
                  '\n6 -- Sort all lists by year and write results to a new file'
                  '\n7 -- Quit')
        elif Choice == 6:
            indexList = sortYears(yearList)
            printSortedYear(indexList, titleList, ratingList, yearList, scoreList)
            print('Please choose one of the following options:'
                  '\n1 -- Find all shows with a certain rating'
                  '\n2 -- Find the show with the highest score released in a specified range of years'
                  '\n3 -- Search for a show by title'
                  '\n4 -- Find the average score for films with a specific rating'
                  '\n5 -- Find all shows with a score higher than the score for a given show'
                  '\n6 -- Sort all lists by year and write results to a new file'
                  '\n7 -- Quit')
        else:
            print('\nGood-bye')
            done = True
    return
