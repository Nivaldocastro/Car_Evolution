import pandas as pd

caminho = "/datasets/car+evaluation/car.data"
cols = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
df = pd.read_csv(caminho, names=cols)
print(df.head())
print("\n")
print(df.info())
print("\n")
print(df.describe())

# valores ausentes ou duplicados
print("\n Valores ausentes:", df.isnull().sum().sum())
print(" Linhas duplicadas:", df.duplicated().sum())

# Distribuição das variáveis categóricas
print("\n Distribuição das variáveis categóricas:")
for c in df.columns:
    print(f"{c}: {df[c].nunique()} categorias -> {df[c].unique()}")

# Codificação das variáveis categóricas utilizando fatoração
df['buying'] = df['buying'].replace({'vhigh': 4, 'high': 3, 'med': 2, 'low': 1})
df['maint'] = df['maint'].replace({'vhigh': 4, 'high': 3, 'med': 2, 'low': 1})
df['doors'] = df['doors'].replace({'2': 2, '3': 3, '4': 4, '5more': 5})
df['persons'] = df['persons'].replace({'2': 2, '4': 4, 'more': 5})
df['lug_boot'] = df['lug_boot'].replace({'small': 1, 'med': 2, 'big': 3})
df['safety'] = df['safety'].replace({'low': 1, 'med': 2, 'high': 3})
df['class'] = df['class'].replace({'unacc': 1, 'acc': 2, 'good': 3, 'vgood': 4})

print(df.dtypes)
print(df.head())
print(" Shape final:", df.shape)

df.to_csv("carr_dataset_ajustado.csv", index=False)