# Data Analysis with pandas

import os

import pandas as pd
df = pd.read_csv("C:\\Users\\Prasad.keluskar\\Downloads\\nyc_weather.csv")
print(df)


#df['EST'] df['Temperature'] == rain


#df.fillna(0, inplace = True)
#df ['WindspeedMPH'].mean()

df.head()

df.head(-5)

print(df[20:26])
