import pandas as pd
import csv

df = pd.read_csv("main.csv")

del df ["pl_orbeccenerr1"]
del df ["pl_orbeccenerr2"]

df.to_csv("new.csv")
