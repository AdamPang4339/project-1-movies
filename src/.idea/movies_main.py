"""
CSAPX-04 Project 1: Movies

File: movies_main.py
Author: Adam Pang
GitHub: AdamPang4339
Date: 9/18/21 - 9/29/21

Description: Driver file that takes in inputs to run queries on a specified
dataset.
    - Queries can be found in imported query_call.py file
    - Datasets are read in read_data.py file

Command Line: When run with any argument other than "small", the large datasets
determined in the data folder will be used. Otherwise, the small datasets in
the data folder will be used.
            - $ python3 movies_main.py small
            - $ python3 movies_main.py
"""
# Import relevant user-defined modules or python modules for queries
import sys
import read_data
import query_call

def main():
    """
    Main driver function that begins calling relevant functions to output
    queries.
    :return: None
    """
    # Initialize small dataset
    dataset = "small"

    # Determine the large/small dataset from cmdline
    if len(sys.argv) < 2:
        dataset = "large"

    # Apply and declare the corresponding files based on dataset
    if dataset == "small":
        moviesInfoFile = "data/small.basics.tsv"
        ratingsInfoFile = "data/small.ratings.tsv"
    else:
        moviesInfoFile = "data/title.basics.tsv"
        ratingsInfoFile = "data/title.ratings.tsv"

    # Declare default movie and rating dictionaries
    movieTable = read_data.readInfo(moviesInfoFile, "movie")
    ratingTable = read_data.readInfo(ratingsInfoFile, "rating", movieTable)

    # Print out relevant counters
    print("Total movies: " + str(len(movieTable)))
    print("Total ratings: " + str(len(ratingTable)) + " \n")

    # Read input file and rewrite movieTable/ratingTable if needed
    for line in sys.stdin:
        inputList = line.split(" ")
        queryType = inputList[0]

        # Search the first input for the query type and call the relevant
        # function from query_call.py
        if queryType == "LOOKUP":
            query_call.lookup(movieTable, ratingTable, inputList[1].rstrip())
        elif queryType == "CONTAINS":
            count = 3
            words = inputList[2]

            # Retrieve the proper input for the CONTAINS query given multiple
            # values separated by spaces (Avoiding data loss)
            while count < len(inputList):
                words += " " + inputList[count]

                count += 1

            # Call CONTAINS query
            query_call.contains(movieTable, inputList[1], words.strip())
        elif queryType == "YEAR_AND_GENRE":
            query_call.year_and_genre(movieTable, inputList[1],
                                          int(inputList[2]), inputList[3].strip())
        elif queryType == "RUNTIME":
            query_call.runtime(movieTable, inputList[1], int(inputList[2]),
                            int(inputList[3]))
        elif queryType == "MOST_VOTES":
            query_call.most_votes(movieTable, ratingTable, inputList[1],
                                  int(inputList[2]))
        elif queryType == "TOP":
            query_call.top(movieTable, ratingTable, inputList[1], int(inputList[2]),
                    int(inputList[3]), int(inputList[4]))


# Ensuring this file is not run when imported
if __name__ == "__main__":
    main()