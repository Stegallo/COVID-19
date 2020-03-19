import pandas as pd
import matplotlib.pyplot as plt

dati = pd.read_csv("../dati-regioni/dpc-covid19-ita-regioni.csv")

lombardia = dati[dati["denominazione_regione"]=="Lombardia"]
print(lombardia)

plt.bar(lombardia["data"], lombardia["totale_casi"])
plt.savefig('data.png')
plt.show()
plt.close()
