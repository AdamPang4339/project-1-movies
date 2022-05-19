"""
CSAPX-04 Project 1: Movie

File: read_data.py
Author: Adam Pang
Date: 9/18/21 - 9/29/21

Description: Module file created to assist with reading datasets and files.
    - readInfo(): Function
"""
# Import relevant modules and files for reading data
import movie_info   # Movie and Rating object classes
from timeit import default_timer as timer   # Timing running time
import output_formatting    # Used for formatting input into instantiating
                            # Movies and Ratings

def readInfo(fileName: str, type: str, moviesDict: dict = None) -> dict:
    """
    Reads information from a given fileName depending on the type and whether
        or not a movies Dictionary is required.

    :param fileName: String containing the name and location of the file that
                    needs to be read
    :param type: String containing the type of data that needs to be read.
                    Accepts "movie" or "rating"
    :param moviesDict: Dictionary with complete Movie information for creating
                    the matching Rating dataset
    :return: dict: Dictionary with read information from fileName
    """
    # Instantiate table to be returned at the end
    infoTable = {}
    start = timer()

    # Open the given file
    with open(fileName, encoding = 'utf-8') as f:
        # Read each line
        for line in f:
            # Split each line to retrieve a list of inputs per line
            infoList = line.split("\t")

            # Ignore lines with tconst as the tconst input variable (Header line)
            if infoList[0] == "tconst":
                continue

            # Ignore all movies with isAdult as 1
            if type == "movie" and infoList[4] == "1":
                continue

            # While creating the rating dictionary, if the tconst in the rating
            # file does not exist in the completed movies dictionary, ignore it
            if type == "rating" and not infoList[0] in moviesDict:
                continue

            # Since the last if statement checked for non-existent tconsts, now
            # assume tconst exists in both rating file and movie dictionary, and
            # ignore any rating that corresponds to a movie with isAdult as 1
            if type == "rating" and moviesDict[infoList[0]].isAdult == "1":
                continue

            # Create a movie object for all valid movie information
            if type == "movie":
                instance = movie_info.Movie(infoList[0], infoList[1],
                                            infoList[2], infoList[3],
                                            infoList[4], infoList[5],
                                            infoList[6], infoList[7],
                                            infoList[8].rstrip())

                # Changing invalid inputs for movies
                instance.runTimeMinutes = output_formatting.replaceInvalids(
                    instance.runTimeMinutes)
                instance.startYear = output_formatting.replaceInvalids(
                    instance.startYear)
                instance.endYear = output_formatting.replaceInvalids(
                    instance.endYear)
                instance.genres = output_formatting.replaceInvalidsNone(
                    instance.genres)
                if instance.genres is not None:
                    instance.genres = \
                        output_formatting.formatGenres(instance.genres)
            # If running rating version of function, create a rating object
            elif type == "rating":
                instance = movie_info.Rating(infoList[0], infoList[1],
                                             infoList[2].rstrip())

                # Changing invalid inputs for ratings
                instance.numVotes = \
                    output_formatting.replaceInvalids(instance.numVotes)
                instance.average = \
                    output_formatting.replaceInvalids(instance.average)

            # Add the created instance to the dictionary
            infoTable[instance.identifier] = instance

    # Timer information
    elapsed = timer() - start
    print("reading", fileName, "into dict...")
    print("elapsed time (s):", elapsed, "\n")

    # Returns completed dictionary with relevant information
    return infoTable


# Ensuring that the file is never run on its own
if __name__ == '__main__':
    pass
