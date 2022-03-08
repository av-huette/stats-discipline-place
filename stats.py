import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from discipline import Discipline


def page_size_landscape(scale: float):
    din_a4 = (11.7, 8.3)  # inches
    return tuple(scale * i for i in din_a4)


'''
# Scatter is better
def bar(df: pd.DataFrame, year_type: str) -> None:
    grouped = df.groupby([year_type])
    # count disciplines
    years = list(grouped.groups.keys())
    discipline_count = {
        Discipline.Geisteswissenschaften: [],
        Discipline.Humanwissenschaften: [],
        Discipline.Ingenieurwissenschaften: [],
        Discipline.Naturwissenschaften: [],
        Discipline.Agrarwissenschaften: [],
        Discipline.Philosophie: [],
        Discipline.Rechtswissenschaften: [],
        Discipline.Sozialwissenschaften: [],
        Discipline.Strukturwissenschaften: [],
        Discipline.Theologie: [],
        Discipline.Wirtschaftswissenschaften: [],
    }

    birth_year_discipline_count = pd.DataFrame(0, index=years, columns=discipline_count.keys())
    for year in years:
        group = grouped.get_group(year)
        group_discipline_count = group["discipline"].value_counts()
        for key in group_discipline_count.keys():
            count = group_discipline_count.get(key)
            if count is None:
                birth_year_discipline_count[key][year] = 0
            else:
                birth_year_discipline_count[key][year] = count

    # remove empty disciplines
    for disc in birth_year_discipline_count.keys():
        if birth_year_discipline_count[disc].sum() == 0:
            birth_year_discipline_count = birth_year_discipline_count.drop(disc, axis=1)

    fig, ax = plt.subplots()
    fig = plt.gcf()
    fig.set_dpi(100)
    fig.set_size_inches(page_size_landscape())

    bottom = np.zeros(len(years))
    colors = plt.cm.hsv(np.linspace(0, 1, len(birth_year_discipline_count.keys()) + 1))
    i = 0
    for disc in list(birth_year_discipline_count.keys()):
        values = birth_year_discipline_count[disc].values
        ax.bar(grouped.groups.keys(), values, label=disc, bottom=bottom, color=colors[i])
        bottom += values
        i += 1

    ax.grid(which='major', axis='x', linestyle='--')
    ax.grid(which='major', axis='y', linestyle='--')
    if year_type == "birth_year":
        ax.set_title("Studiengänge nach Geburtsjahr")
        ax.set_xlabel('Geburtsjahr')
    else:
        ax.set_title("Studiengänge nach Eintrittsjahr")
        ax.set_xlabel('Eintrittsjahr')
    ax.set_ylabel('Anzahl Studierende')

    ax.set_xlim(xmin=(years[0] - 1))
    ax.set_xlim(xmax=(years[len(years) - 1] + 1))

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.6, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.subplots_adjust(left=0.05, right=box.width - 0.01, top=0.95, bottom=0.08)

    plt.show()

    print(birth_year_discipline_count.sum())
    print(birth_year_discipline_count.sum().sum())
'''

'''
def scatter(df: pd.DataFrame, year_type: str) -> None:
    grouped = df.groupby([year_type])
    # count disciplines
    years = list(grouped.groups.keys())
    discipline_count = {
        Discipline.Geisteswissenschaften: [],
        Discipline.Humanwissenschaften: [],
        Discipline.Ingenieurwissenschaften: [],
        Discipline.Naturwissenschaften: [],
        Discipline.Agrarwissenschaften: [],
        Discipline.Philosophie: [],
        Discipline.Rechtswissenschaften: [],
        Discipline.Sozialwissenschaften: [],
        Discipline.Strukturwissenschaften: [],
        Discipline.Theologie: [],
        Discipline.Wirtschaftswissenschaften: [],
    }

    birth_year_discipline_count = pd.DataFrame(np.NAN, index=years, columns=discipline_count.keys())
    for year in years:
        group = grouped.get_group(year)
        group_discipline_count = group["discipline"].value_counts()
        for key in group_discipline_count.keys():
            count = group_discipline_count.get(key)
            if count is None:
                birth_year_discipline_count[key][year] = 0
            else:
                birth_year_discipline_count[key][year] = count

    # remove empty disciplines
    for disc in birth_year_discipline_count.keys():
        if birth_year_discipline_count[disc].sum() == 0:
            birth_year_discipline_count = birth_year_discipline_count.drop(disc, axis=1)

    fig, ax = plt.subplots()
    fig = plt.gcf()
    fig.set_dpi(100)
    fig.set_size_inches((11.7, 5.2))

    # possible colormaps: hsv, tab20b, cubehelix
    colors = plt.cm.hsv(np.linspace(0, 1, len(birth_year_discipline_count.keys()) + 1))
    markers = ["o", "v", "^", "1", "2", "3", "s", "+", "x", "d"]
    i = 0
    for disc in list(birth_year_discipline_count.keys()):
        ax.scatter(grouped.groups.keys(), birth_year_discipline_count[disc].values, label=disc, color=colors[i],
                   marker=markers[i])
        i += 1

    ax.grid(which='major', axis='x', linestyle='--')
    ax.grid(which='major', axis='y', linestyle='--')
    if year_type == "birth_year":
        ax.set_title("Studiengänge nach Geburtsjahr")
        ax.set_xlabel('Geburtsjahr')
    else:
        ax.set_title("Studiengänge nach Eintrittsjahr")
        ax.set_xlabel('Eintrittsjahr')
    ax.set_ylabel('Anzahl Studierende')

    ax.set_xlim(xmin=(years[0] - 1))
    ax.set_xlim(xmax=(years[len(years) - 1] + 1))

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.6, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.subplots_adjust(left=0.05, right=box.width + 0.01, top=0.95, bottom=0.08)

    plt.show()
'''


def scatter_place(df: pd.DataFrame, year_type: str, study_place="") -> None:
    """
    :param df: result of read_csv()
    :param year_type: either "birth_year" or "entry_year"
    :param study_place: optional. Otherwise either "Berlin" or "Karlsruhe".
    :return:
    """
    # filter study place
    if len(study_place) > 0:
        df = df[df["study_place"] == study_place]

    grouped = df.groupby([year_type])
    # count disciplines
    years = list(grouped.groups.keys())

    # only use disciplines from map that are really needed
    discipline_count = {
        Discipline.Geisteswissenschaften: [],
        # Discipline.Humanwissenschaften: [],
        Discipline.Ingenieurwissenschaften: [],
        Discipline.Naturwissenschaften: [],
        Discipline.Agrarwissenschaften: [],
        # Discipline.Philosophie: [],
        Discipline.Rechtswissenschaften: [],
        Discipline.Sozialwissenschaften: [],
        Discipline.Strukturwissenschaften: [],
        # Discipline.Theologie: [],
        Discipline.Wirtschaftswissenschaften: [],
    }

    # populate DataFrame
    birth_year_discipline_count = pd.DataFrame(np.NAN, index=years, columns=discipline_count.keys())
    for year in years:
        group = grouped.get_group(year)
        group_discipline_count = group["discipline"].value_counts()
        for key in group_discipline_count.keys():
            count = group_discipline_count.get(key)
            if count is None:
                birth_year_discipline_count[key][year] = 0
            else:
                birth_year_discipline_count[key][year] = count

    ##################################################
    # Plotting
    ##################################################

    fig, ax = plt.subplots()
    fig = plt.gcf()
    fig.set_dpi(300)
    # fig.set_size_inches(page_size_landscape(0.9))
    fig.set_size_inches((11.7, 5.2))

    colors = plt.cm.hsv(np.linspace(0, 1, len(birth_year_discipline_count.keys()) + 1))
    markers = ["o", "v", "^", "1", "2", "3", "s", "+", "x", "d", "*", "_", "p", "P"]
    i = 0
    for disc in list(birth_year_discipline_count.keys()):
        values = birth_year_discipline_count[disc].values
        label = f"{disc} ({int(np.nansum(values))})"
        ax.scatter(grouped.groups.keys(), values, label=label, color=colors[i], marker=markers[i])
        i += 1
    ax.plot([], [], ' ', label=f"Insgesamt: {int(birth_year_discipline_count.sum().sum())}")

    ax.grid(which='major', axis='x', linestyle='--')
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.grid(which='major', axis='y', linestyle='--')
    if year_type == "birth_year":
        if len(study_place) > 0:
            ax.set_title(f"Studiengänge nach Geburtsjahr in {study_place}")
        else:
            ax.set_title("Studiengänge nach Geburtsjahr")
        ax.set_xlabel('Geburtsjahr')
    else:
        if len(study_place) > 0:
            ax.set_title(f"Studiengänge nach Eintrittsjahr in {study_place}")
        else:
            ax.set_title("Studiengänge nach Eintrittsjahr")
        ax.set_xlabel('Eintrittsjahr')
    ax.set_ylabel('Anzahl Studierende')

    ax.set_xlim(xmin=(years[0] - 1))
    ax.set_xlim(xmax=(years[len(years) - 1] + 1))

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.6, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    data_text = ""
    plt.gcf().text(0.91, 0.75, data_text, fontsize=10)
    plt.subplots_adjust(left=0.05, right=box.width - 0.02, top=0.95, bottom=0.08)

    plt.show()
