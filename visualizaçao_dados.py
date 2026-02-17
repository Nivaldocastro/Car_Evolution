import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("carr_dataset_ajustado.csv")
print(df.head())

# Boxplot das variáveis em relação a variável alvo (class)
sns.boxplot(x='class', y='buying', data=df)
plt.title('Distribuição de buying por Classe')
plt.show()

sns.boxplot(x='class', y='doors', data=df)
plt.title('Distribuição de doors por Classe')
plt.show()

sns.boxplot(x='class', y='safety', data=df)
plt.title('Distribuição de doors por Classe')
plt.show()

# Configuração de estilo
sns.set(style="whitegrid", palette="pastel")

# Matriz de correlação
corr = df.corr(method='pearson')

# Plot do heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Mapa de Calor - Correlação entre Variáveis (Pearson)")
plt.show()
