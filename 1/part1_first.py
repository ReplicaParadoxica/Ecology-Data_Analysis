import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("H:/Desktop/geologi/1/Data_interview.csv", na_values=['NA'])
data = data.dropna()
data.boxplot(column=['x1', 'x2', 'x3'], showfliers=False)
plt.xlabel("Stacija")
plt.ylabel("Parametri")
plt.show()
