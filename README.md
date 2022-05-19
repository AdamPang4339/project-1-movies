# project-1-movies
Runs queries on specified movie data set from the IMDB movie database.

## Project Files
- **movies_main**: Driver file that takes in inputs to run queries on a specified dataset. Queries can be found in imported query_call.py file, and datasets are read in read_data.py file.
- movie_info: Dataclass file that contains the Movie and Rating dataclasses.
- read_data: Module file created to assist with reading datasets and files.
- query_call: Master module containing all relevant queries needed for organizing information for Movie objects and Rating objects. 
- output_formatting: Formats for outputting data with specifications

## Command Line Usage
`$ python 3 movies_main.py small`

Command line usage initially meant to include 0 command line arguments option, but was removed due to file size errors when importing into GitHub. Errors will appear if command line argument "small" is not provided.
