import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv')
gasolina_df.head()

with sns.axes_style('whitegrid'):
    grafico = sns.lineplot(data=gasolina_df,x="dia",y="venda")
grafico.set(title='Preços Médio Venda da Gasolina',xlabel='dias')
plt.savefig('grafico.png')