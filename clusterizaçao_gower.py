import pandas as pd
import gower
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.metrics import silhouette_score

# Carregar dataset
df = pd.read_csv("carr_dataset_ajustado.csv")

print(df.dtypes)


# Remover variável alvo
X = df.drop(columns=['class'])

X = X.astype(float)

# Calcula a matriz de distancia de gower
gower_dist = gower.gower_matrix(X)

Z = linkage(gower_dist, method='average')

plt.figure(figsize=(12,6))
dendrogram(Z, truncate_mode='lastp', p=30)
plt.title("Dendograma com Distância de Gower")
plt.xlabel("Clusters")
plt.ylabel("Distância")
plt.show()

for k in range(2, 7):
    clusters = fcluster(Z, t=k, criterion='maxclust')
    score = silhouette_score(gower_dist, clusters, metric='precomputed')
    print(f"k={k}, silhouette={score}")

clusters = fcluster(Z, t=3, criterion='maxclust')
df['cluster'] = clusters
mapa_class = {
    1: 'unacc',
    2: 'acc',
    3: 'good',
    4: 'vgood'
}

df['class'] = df['class'].map(mapa_class)

tabela = pd.crosstab(df['cluster'], df['class'])
print(tabela)

tabela_percent = pd.crosstab(
    df['cluster'],
    df['class'],
    normalize='index'
) * 100

print(tabela_percent)