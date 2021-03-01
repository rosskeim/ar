import pandas as pd
import numpy as np

print("Which ARS: ")
selected_ARS = int(input())

data = pd.read_excel("sample_ar.xlsx")

data['<=30'] = data['<=30'].str.replace('$', '')
data['31-60'] = data['31-60'].str.replace('$', '')
data['61-90'] = data['61-90'].str.replace('$', '')
data['91-120'] = data['91-120'].str.replace('$', '')
data['120+'] = data['120+'].str.replace('$', '')

data['<=30'] = data['<=30'].astype('float')
data['31-60'] = data['31-60'].astype('float')
data['61-90'] = data['61-90'].astype('float')
data['91-120'] = data['91-120'].astype('float')
data['120+'] = data['120+'].astype('float')

data.insert(8, "Total", data['<=30'] + data['31-60'] + data['61-90'] + data['91-120'] + data['120+'])
data.insert(8, "Over 60", data['61-90'] + data['91-120'] + data['120+'])

summary = data.groupby('ARS')[['Over 60', 'Total']].sum()

print(f"Current Over 60 for {selected_ARS}: ${summary.loc[selected_ARS]['Over 60']}")

summary.to_excel("summary.xlsx")
