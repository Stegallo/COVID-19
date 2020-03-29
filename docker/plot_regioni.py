from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from utils import color_negative_red, highlight_max

folder = "../report/"
cm = sns.light_palette("green", as_cmap=True)

all_dati = pd.read_csv("../dati-regioni/dpc-covid19-ita-regioni.csv")
all_dati = all_dati[["data", "denominazione_regione", "totale_casi"]]
lista_regioni = set(all_dati["denominazione_regione"])

for nome_regione in lista_regioni:

    dati = all_dati[all_dati["denominazione_regione"] == nome_regione]

    dati["delta_prev_day"] = dati["totale_casi"] - dati["totale_casi"].shift(1)
    dati["delta_delta_prev_day"] = dati["delta_prev_day"] - dati[
        "delta_prev_day"
    ].shift(1)

    html = (
        dati.style.format(
            "{:0}",
            subset=["totale_casi", "delta_prev_day", "delta_delta_prev_day"],
            na_rep="-",
        )
        .format(
            {
                "data": lambda t: datetime.strptime(t, "%Y-%m-%dT%H:%M:%S").strftime(
                    "%Y-%m-%d"
                )
            }
        )
        .applymap(color_negative_red, subset=["delta_prev_day", "delta_delta_prev_day"])
        .bar(
            subset=["totale_casi", "delta_delta_prev_day"],
            align="mid",
            color="lightblue",
        )
        .apply(highlight_max, subset=["delta_prev_day"])
        .background_gradient(subset=["delta_prev_day"], cmap=cm)
        .set_properties(**{"font-size": "12pt", "font-family": "Calibri"})
        .hide_index()
        .render()
    )
    text_file = open(f"{folder}/{nome_regione}.html", "w")
    text_file.write(html)
    text_file.close()
    plt.close()
