import pandas as pd
import matplotlib.pyplot as plt

dati = pd.read_csv("../dati-regioni/dpc-covid19-ita-regioni.csv")

for nome_regione in set(dati["denominazione_regione"]):
    print(f"{nome_regione=}")
    regione = dati[dati["denominazione_regione"] == nome_regione]

    plt.bar(regione["data"], regione["totale_casi"])
    plt.savefig(f"{nome_regione}.png")
    plt.show()
    plt.close()
