import pandas as pd
df=pd.read_csv("D:/train-passing.csv")
import matplotlib.pyplot as plt
df.plot(x="Time", y=[ "X (100g)", "Y (100g)",  "Z (100g)"])
plt.show()