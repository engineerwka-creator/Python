import random
import datetime
import math

print("Losowa liczba:", random.randint(1, 100))
print("Dzisiejsza data:", datetime.date.today())
print("Pierwiastek z 81 to:", math.sqrt(81))
print ('Liczba PI to:', math.pi)

import requests
response = requests.get("https://api.github.com")
print(response.status_code)

import os
print(os.listdir())  # lista plików w folderze

from datetime import datetime
print(datetime.now())

import json
dane = {"imię": "Kasia", "wiek": 21}
tekst = json.dumps(dane)
print(tekst)

# import numpy as np
# tablica = np.array([1, 2, 3, 4])
# print(np.mean(tablica))  # średnia: 2.5
#
# import pandas as pd
# df = pd.DataFrame({"Imię": ["Jan", "Ola"], "Wiek": [23, 25]})
# print(df)
#
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [2, 4, 6])
# plt.title("Przykładowy wykres")
# plt.show()

# from sklearn.linear_model import LinearRegression
# model = LinearRegression()

# import torch
# x = torch.tensor([1.0, 2.0, 3.0])
# print(x * 2)