import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

folder = "../report/"
dati = pd.read_csv("../dati-regioni/dpc-covid19-ita-regioni.csv")

# for nome_regione in set(dati["denominazione_regione"]):
#     print(f"{nome_regione=}")
#     regione = dati[dati["denominazione_regione"] == nome_regione]
#
dati["delta_prev_day"] = dati["totale_casi"] - (
    dati.sort_values(by=["data"], ascending=True)
).groupby(["denominazione_regione"])["totale_casi"].shift(1)

# sns.lineplot(
#     x="data", y="delta_prev_day", hue="denominazione_regione", data=regione
# )

# # plt.savefig(f"{folder}/{nome_regione}.png")
plt.style.use("seaborn-darkgrid")

sns.lineplot(
    x="data", y="delta_prev_day", hue="denominazione_regione", data=dati,
)

plt.savefig(f"{folder}/generale.png")
plt.show()
plt.close()

# html = regione[["data", "totale_casi", "delta_prev_day"]].to_html()
# text_file = open(f"{folder}/{nome_regione}.html", "w")
# text_file.write(html)
# text_file.close()
# plt.close()
