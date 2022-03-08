import logging
import course_discipline


def to_year(date: str) -> int:
    """
    Returns the year from string
    :param date: in format dd.mm.yyyy
    :return: year as number
    """
    if len(date) > 0:
        return int(date[-4:])
    return -1


def rename_study_place(place: str) -> str:
    """
    Rename study places that to either "Berlin" or "Karlsruhe"
    """
    if "Berlin" in place:
        return "Berlin"
    elif "Karlsruhe" in place:
        return "Karlsruhe"
    else:
        logging.error(f"Invalid place: \"{place}\"")
        return ""


def rename_course_to_discipline(course: str) -> str:
    """
    Map study course to discipline according to https://de.wikipedia.org/wiki/Einzelwissenschaft

    See `course_discipline.py`
    """
    discipline = course_discipline.get_map().get(course)
    if discipline is None:
        logging.error(f"Invalid course: \"{course}\"")
    return discipline


def sanity_check_column_lengths(entry_year: int, district: int, discipline: int,
                                birth_year: int, study_place: int) -> bool:
    """
    Verify that all columns have the same cardinality
    """
    legit = (entry_year == district and district == discipline and
             discipline == birth_year and birth_year == study_place)
    if not legit:
        raise ValueError("Lengths of columns do not match")
    logging.info(f"Found {entry_year} entries.")
    return legit
