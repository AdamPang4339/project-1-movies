def formatGenres(genres: str) -> str:
    return genres.replace(",", ", ")


def replaceInvalids(replaced) -> str:
    if (replaced == "\\N"):
        replaced = "0"

    return replaced


def replaceInvalidsNone(replaced) -> str:
    if (replaced == "\\N"):
        replaced = None

    return replaced


if __name__ == "__main__":
    pass
