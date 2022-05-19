"""
CSAPX-04 Project 1: Movie

File: movie_info.py
Author: Adam Pang
Date: 9/18/21 - 9/29/21

Description: Dataclass file that contains the Movie and Rating dataclasses.
    - Class: Movie - Contains 9 fields that correspond to information given
                    by the input files found in the data folder.
    - Class: Rating - Contains 3 fields that correspond to information given
                    by the input files found in the data folder.
"""
# Import dataclass from dataclasses to instantiate classes
from dataclasses import dataclass

@dataclass
class Movie:
    """
    Movie class for Movie objects to be used for organizing data. Accepts 9 fields:
        - identifier: tconst value for identification
        - titleType: type of instance (movie, tvshow, etc.)
        - primTitle: primary title of instance
        - origTitle: original title of instance
        - isAdult: 1 or 0 value indicating if instance is meant for adults
        - startYear: integer value indicating the beginning year of instance
        - endYear: integer value indicating the end year of instance
        - runTimeMinutes: integer value indicating minutes ran for instance
        - genres: string of genres that pertain to instance
    """
    identifier: str
    titleType: str
    primTitle: str
    origTitle: str
    isAdult: str
    startYear: str
    endYear: str
    runTimeMinutes: str
    genres: str


@dataclass
class Rating:
    """
    Rating class for Rating objects to be used for organizing data. Accepts 3 fields:
        - identifier: tconst value for identification
        - average: float value for the average of rating
        - numVotes: integer value of total votes made for an instance
    """
    identifier: str
    average: str
    numVotes: str


if __name__ == '__main__':
    pass