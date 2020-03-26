import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

folder = "../report/"
all_dati = pd.read_csv("../dati-regioni/dpc-covid19-ita-regioni.csv")

regione = ["Lombardia"]
for nome_regione in regione:

    dati = all_dati[all_dati["denominazione_regione"] == nome_regione]

    dati["delta_prev_day"] = dati["totale_casi"] - dati["totale_casi"].shift(1)

    dati["delta_delta_prev_day"] = dati["delta_prev_day"] - dati[
        "delta_prev_day"
    ].shift(1)

    html = (
        dati[["data", "totale_casi", "delta_prev_day", "delta_delta_prev_day",]]
        .to_html()
        .replace("<tr>", '<tr align="center">')
        .replace("<th>", '<th align="center">')
    )
    text_file = open(f"{folder}/{nome_regione}.html", "w")
    text_file.write(html)
    text_file.close()
    plt.close()
