import logging
import os
import csv
import helper as h
import pandas as pd
import stats


def read_csv(path: str) -> pd.DataFrame:
    """
    Convert CSV file to Pandas DataFrame

    See format of `data/demo.csv`
    """
    entry_year, district, discipline, birth_year, study_place = [], [], [], [], []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        header = next(reader)
        for row in reader:
            if data_is_complete(row, header):
                entry_year.append(h.to_year(row[1]))
                district.append(row[9])
                discipline.append(h.rename_course_to_discipline(row[16]))
                birth_year.append(h.to_year(row[17]))
                study_place.append(h.rename_study_place(row[18]))

    h.sanity_check_column_lengths(len(entry_year), len(district), len(discipline), len(birth_year), len(study_place))

    d = {"birth_year": birth_year, "entry_year": entry_year,
         "district": district, "study_place": study_place, "discipline": discipline}
    return pd.DataFrame(data=d)


def data_is_complete(row: [], header) -> bool:
    indices = [1, 9, 16, 17, 18]
    for i in indices:
        if len(row[i]) <= 0:
            logging.warning(f"Skipping data point:\n\t- {row[5]} ({row[6]}) {row[7]}\n\t- {header[i]}")
            return False
    if row[16] == "-":  # course not specified
        logging.warning(f"Skipping data point:\n\t- {row[5]} ({row[6]}) {row[7]}\n\t- {header[16]}: {row[16]}")
        return False
    return True


if __name__ == '__main__':
    dir_name, file_name = os.path.split(os.path.realpath(__file__))
    df = read_csv(f"{dir_name}/data/demo.csv")
    # df = read_csv(f"{dir_name}/data/members.csv")
    stats.scatter_place(df, "entry_year")
    stats.scatter_place(df, "entry_year", "Berlin")
    stats.scatter_place(df, "entry_year", "Karlsruhe")
