import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("carr_dataset_ajustado.csv")
print(df.head())


# Medidas de tendência central e dispersão
print(" Medidas de Tendência Central e Dispersão \n")

print(df.describe())

for col in df.columns:
    media = df[col].mean()
    mediana = df[col].median()
    moda = df[col].mode()[0]
    variancia = df[col].var()
    desvio = df[col].std()
    amplitude = df[col].max() - df[col].min()

    print(f"{col}:")
    print(f"  Média: {media:.2f}")
    print(f"  Mediana: {mediana}")
    print(f"  Moda: {moda}")
    print(f"  Variância: {variancia:.2f}")
    print(f"  Desvio-padrão: {desvio:.2f}")
    print(f"  Amplitude: {amplitude}")
    print()


# Matriz de Correlação
print(" Matriz de Correlação Completa \n")

corr = df.corr(numeric_only=True)
print(corr)  # Mostra a tabela completa no console


# Heatmap da matriz de correlação
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", center=0)
plt.title("Matriz de Correlação (Pearson) entre todas as variáveis")
plt.show()