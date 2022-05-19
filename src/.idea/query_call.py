"""
CSAPX-04 Project 1: Movies

File: query_call.py
Author: Adam Pang
Date: 9/18/21 - 9/29/21

Description: Master module containing all relevant queries needed for organizing
 information for Movie objects and Rating objects.
    - List of queries:
        - lookup(): LOOKUP query, searches for specific movie instance
        - contains(): CONTAINS query, searches for all instances with
                        specific key words
        - year_and_genre(): YEAR_AND_GENRE query, searches for all instances
                            that fall within a specific year and match the
                            requested genres
        - runtime(): RUNTIME query, searches for all instances that fall within
                        a range of runtimes
        - most_votes(): MOST_VOTES query, searches for instances with the most
                        votes for ratings
        - top(): TOP query, searches for the top movies given specifications
"""
# Import timer and relevant modules for running queries
from timeit import default_timer as timer
import operator

def sortList(unsortedList: list, attr: str, reverse = False) -> None:
    """
    Sorting function meant to sort lists of objects such as Movies or Ratings
    :param unsortedList: Unsorted list of objects
    :param attr: Attribute being sorted that falls under instances within the
                    unsortedList.
    :param reverse: Boolean value for whether or not to sort
                    ascending/descending.
    :return: None
    """
    # Return the unsortedList, sorted through the sort() function
    unsortedList.sort(key = operator.attrgetter(attr), reverse = reverse)


def lookup(movieDict: dict, ratingDict: dict, tconst: str) -> None:
    """
    LOOKUP query that outputs a Movie instance's information given
    its identifier.
    :param movieDict: Movie dictionary containing all movies in dataset
    :param ratingDict: Rating dictionary containing all matching ratings for
                        movies found in movieDict.
    :param tconst: String identifier for movie being searched
    :return: None
    """
    # Begin timer
    start = timer()

    print("processing: LOOKUP", tconst)

    # If the identifier has a movie instance and a rating instance, output it's
    # information from the corresponding dictionaries
    if (tconst in movieDict) and (tconst in ratingDict):
        # Create helper variables for the specific instances
        movie = movieDict[tconst]
        rating = ratingDict[tconst]

        # Output information from both instances
        print("\tMOVIE: Identifier:", tconst + ", Title:", movie.primTitle
              + ", Type:", movie.titleType + ", Year:", movie.startYear
              + ", Runtime:", movie.runTimeMinutes
              + ", Genres:", movie.genres)
        print("\tRATING: Identifier:", tconst + ", Rating:", rating.average
              + ", Votes:", rating.numVotes)
    else:
        # No movie and/or rating was found
        print("\tMovie not found!")
        print("\tRating not found!")

    # Output total runtime for the query process
    elapsed = timer() - start
    print("elapsed time (s):", elapsed, "\n")


def contains(movieTable: dict, titleType: str, keywords: str) -> None:
    """
    CONTAINS query that returns information regarding movies that contain a
    specific string of words, word for word.

    :param movieTable: Full dictionary of all movies being searched.
    :param titleType: String of the specific type of instances that will
                        be searched. (Ex: movie, tvshow, episode, etc.)
    :param keywords: Specific words that will be searched for in all instances
                        of movieTable.
    :return: None
    """
    # Found boolean value checks if any movie was found
    found = False
    # Begin timer
    start = timer()

    print("processing: CONTAINS", titleType, keywords)

    # Iterate through all movie Instances
    for val in movieTable:
        movie = movieTable[val]

        # Check each instance and verify requirements
        if keywords in movie.primTitle and movie.titleType == titleType:
            # If valid movie was found, output it's information
            found = True

            print("\tIdentifier:", movie.identifier + ", Title:",
                  movie.primTitle + ", Type:", movie.titleType + ", Year:",
                  movie.startYear + ", Runtime:", movie.runTimeMinutes +
                  ", Genres:", movie.genres)

    # If no movie was found, output accordingly
    if not found:
        print("\tNo match found!")

    # Output total run time of query process
    elapsed = timer() - start
    print("elapsed time (s):", elapsed, "\n")


def year_and_genre(movieDict: dict, titleType: str, startYear: int, genre: str) -> None:
    """
    YEAR_AND_GENRE query that returns information on all instances that fall
    within a specific year and specified genres.

    :param movieDict: Dictionary containing all movies being checked
    :param titleType: String of the specific type of instances that will
                        be searched. (Ex: movie, tvshow, episode, etc.)
    :param startYear: String of the integer of the specific year being searched.
    :param genre: String of genre that is required to be checked for.
    :return: None
    """
    # Begin timer
    start = timer()
    # Initiate boolean for when nothing is found
    found = False
    # List for storing and sorting for output
    foundList = []

    print("processing: YEAR_AND_GENRE", titleType, startYear, genre)
    # Iterate through all movie instances
    for val in movieDict:
        movie = movieDict[val]

        # Ignore all movies that have no genres
        if movie.genres is None:
            continue
        # If the movie meets the requirements, add the movie to the foundList.
        if (titleType == movie.titleType) and (startYear == int(movie.startYear)) \
                and (genre in movie.genres):
            found = True
            foundList.append(movie)

    # No movie was found, output accordingly
    if not found:
        print("\tNo match found!")
    else:
        # Movie was found, sort and output all information on the instances
        sortList(foundList, "primTitle")

        for i in foundList:
            print("\tIdentifier:", i.identifier + ", Title:",
                  i.primTitle + ", Type:", i.titleType + ", Year:",
                  str(i.startYear) + ", Runtime:", str(i.runTimeMinutes) +
                  ", Genres:", i.genres)

    # Output total run time of query process
    elapsed = timer() - start
    print("elapsed time (s):", elapsed, "\n")


def runtime(movieDict: dict, titleType: str, minTime: int, maxTime: int) -> None:
    """
    RUNTIME query that returns all movies that match a specific range of runtime
    given in minutes.

    :param movieDict: Dictionary of all movies that are being checked.
    :param titleType: String of the specific type of instances that will
                        be searched. (Ex: movie, tvshow, episode, etc.)
    :param minTime: Lower bound of the range of minutes being checked for.
    :param maxTime: Upper bound of the range of minutes being checked for.
    :return: None
    """
    # Begin timer
    start = timer()
    # Initiate variables for storing information for future output
    found = False
    foundList = []

    print("processing: RUNTIME", titleType, minTime, maxTime)

    # Iterate through entire movie Dictionary
    for val in movieDict:
        movie = movieDict[val]

        # If requirements are satisfied, add to foundList
        if (movie.titleType == titleType) and \
                (minTime <= int(movie.runTimeMinutes)) and \
                (int(movie.runTimeMinutes) <= maxTime):
            found = True
            foundList.append(movie)

    # If nothing was found, output accordingly
    if not found:
        print("\tNo match found!")
    else:
        # Movies that are in the foundList are sorted, and then outputted
        sortList(foundList, "primTitle")
        sortList(foundList, "runTimeMinutes", True)

        for i in foundList:
            print("\tIdentifier:", i.identifier + ", Title:",
                  i.primTitle + ", Type:", i.titleType + ", Year:",
                  str(i.startYear) + ", Runtime:", str(i.runTimeMinutes) +
                  ", Genres:", i.genres)

    # Output run time of query process
    elapsed = timer() - start
    print("elapsed time (s):", elapsed, "\n")


def most_votes(movieDict: dict, ratingDict: dict, titleType: str, num: int) -> None:
    """
    MOST_VOTES query that returns a specific number of movie instances that
    satisfy a specific titleType and have the highest amount of votes.

    :param movieDict: Dictionary of all movies being checked for.
    :param ratingDict: Dictionary with all ratings of the movies being checked for.
    :param titleType: String of the specific type of instances that will
                        be searched. (Ex: movie, tvshow, episode, etc.)
    :param num: Number of movies being outputted with the most votes.
    :return: None
    """
    # Begin timer
    start = timer()
    # Initiate variables needed for storing information for future output
    found = False
    ratingList = []

    print("processing: MOST_VOTES", titleType, num)

    # Iterate through all movies
    for val in movieDict:
        movie = movieDict[val]

        # Ignore movie if not given a rating or not in specified titleType
        if (movie.titleType == titleType) and (val in ratingDict):
            found = True
            rating = ratingDict[val]
            # Make sure all numVotes are integers to prepare for sorting
            rating.numVotes = int(rating.numVotes)
            # Append any and all valid ratings
            ratingList.append(rating)

    # Sort all ratings by highest to lowest number of votes
    sortList(ratingList, "numVotes", True)

    # If no ratings were appended or found, output accordingly
    if not found:
        print("\tNo match found!")
    else:
        # Ratings were found
        i = 0
        while i < num and i < len(ratingList):
            # Output the maximum number of ratings in a descending order
            # from most votes to least votes.
            count = i + 1
            tconst = ratingList[i].identifier
            movie = movieDict[tconst]

            print("\t" + str(count) + ". VOTES:", str(ratingList[i].numVotes) +
                  ", MOVIE: Identifier:", movie.identifier + ", Title:",
                  movie.primTitle + ", Type:", movie.titleType + ", Year:",
                  str(movie.startYear) + ", Runtime:", str(movie.runTimeMinutes) +
                  ", Genres:", movie.genres)

            # Increment to the next possible rating in the rating list
            i += 1

    # Output run time of query process
    elapsed = timer() - start
    print("elapsed time (s):", elapsed, "\n")


def top(movieDict: dict, ratingDict: dict, titleType: str, num: int,
        startYear: int, endYear: int) -> None:
    """
    TOP query that displays information of a number of movies that fall within
    a specific titleType and in a specific year.

    :param movieDict: Dictionary of movies being checked for.
    :param ratingDict: Dictionary of ratings corresponding to the movies being checked for.
    :param titleType: String of the specific type of instances that will
                        be searched. (Ex: movie, tvshow, episode, etc.)
    :param num: Number of movies per year that should be displayed at max.
    :param startYear: Integer of the start year of the movie instances being accepted.
    :param endYear: Integer of the end year of the movie instances being accepted.
    :return: None
    """
    # Begin timer
    start = timer()
    # Declare lists needed to organize and sort information
    validList = []
    movieList = []

    print("processing: TOP", titleType, num, startYear, endYear)

    # Given all ratings, trace through each rating to check requirements
    for tconst in ratingDict:
        # Create corresponding rating and movie instances for all tconsts
        rating = ratingDict[tconst]
        movie = movieDict[tconst]

        # Ignore all movies that have no startYear or average
        if (movie.startYear == "0") or (rating.average == "0"):
            continue
        # Check all requirements for each movie
        if (int(rating.numVotes) >= 1000) and (
                int(movie.startYear) <= endYear) and \
                (int(movie.startYear) >= startYear) and (
                movie.titleType == titleType):
            # Append valid movies into movieList
            found = True
            movieList.append(movie)

    # Sort movieList by alphabetical
    sortList(movieList, "primTitle")
    # Update validList to store the corresponding valid movies' ratings
    for movie in movieList:
        validList.append(ratingDict[movie.identifier])
    # Clear movieList to prepare to update with sorted votes and
    # averages from ratings list
    movieList = []
    sortList(validList, "numVotes", True)
    sortList(validList, "average", True)
    # With the finished sorting rating list (validList), update the
    # currently empty movieList to store the proper movie instance order
    for rating in validList:
        movieList.append(movieDict[rating.identifier])

    # Sort both lists one final time for the sortedyears to prepare for
    # output
    sortList(movieList, "startYear")
    validList = []
    for movie in movieList:
        validList.append(ratingDict[movie.identifier])

    # Both movieList and validList are now sorted by Year, Average,
    # numVotes, and then lastly alphabetically by primTitle
    if len(movieList) >= 0:
        # Iterate through all the possible years
        for year in range(startYear, endYear + 1, 1):
            count = 1
            # Output each year
            print("\tYEAR:", year)

            # Iterate through the movieList for all passed movie instances
            for i in range(len(movieList)):
                movie = movieList[i]
                rating = validList[i]

                # Output the maximum number of movies that fall within this
                # specific year iteration (parent for year loop)
                if (count <= num) and (int(movie.startYear) == year):
                    print("\t\t" + str(count) + ". RATING:", str(rating.average)
                          + ", VOTES:", str(rating.numVotes) +
                          ", MOVIE: Identifier:", movie.identifier + ", Title:"
                          , movie.primTitle + ", Type:", movie.titleType +
                          ", Year:", str(movie.startYear) + ", Runtime:",
                          str(movie.runTimeMinutes) + ", Genres:", movie.genres)

                    count += 1

            # If count was never incremented for a specific year,
            # nothing was found.
            if count == 1:
                print("\t\tNo match found!")

    # Output run time for query process
    elapsed = timer() - start
    print("elapsed time (s):", elapsed, "\n")


if __name__ == '__main__':
    pass
