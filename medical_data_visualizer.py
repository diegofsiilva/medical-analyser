import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

df['overweight'] = ((df['weight']/df['height'] /100)**2 ).apply(lambda x: 1 if x>25 else 0)

df['cholesterol'] = df['cholesterol'].apply(lambda x:0 if x==1 else 1)
df["gluc"] = (df["gluc"].apply(lambda x: 0 if x == 1 else 1))

def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    df_cat["total"]=1
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).count()
    # o as_index vai retornar os objetos como um grupo labels    
    fig = sns.catplot(x="variable", y="total", data=df_cat, hue="value",kind="bar",col="cardio").fig
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
