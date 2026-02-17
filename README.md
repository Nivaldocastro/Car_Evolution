# Projeto de Análise Estrutural do Car Evaluation Dataset

Este trabalho apresenta uma análise exploratória e estrutural do Car Evaluation Dataset, com foco na aplicação de técnicas de clusterização não supervisionada. O objetivo principal foi identificar agrupamentos naturais nos dados a partir de atributos categóricos, utilizando a distância de Gower para tratar adequadamente esse tipo de variável. Foram realizados pré-processamento, análise estatística, visualização dos dados e clusterização hierárquica. Os resultados demonstram que existem padrões significativos nos atributos avaliados, possibilitando a identificação de agrupamentos coerentes com as classes originais, em especial para a categoria “unacc”.


---

## 📁 Estrutura do Projeto
```
├── preprocessamento.py          # Pré-processamento
├── analise_estatistica.py       # análise estatistica
├── visualizaçao_dados.py        # Visualização e análise dos dados
├── clusterizaçao_gower.py       # Clusterização hierárquica 
├── Carr_dataset_ajustado.csv    # Dataset ajustado
├── imagens_Car_Evaliation       # Imagens de resultados
│   ├── boxplot_.png               # Boxplot buying
│   ├── boxplot_2.png              # Boxplot doors
│   ├── boxplot_3.png              # Boxplot safety
│   ├── matriz_correlacao.png      # Matriz de correlação
│   └── dendograma.png             # Dendograma
└── README.md
```

---

## 📂 Dataset

Fonte: UCI Machine Learning Repository  
Link: https://archive.ics.uci.edu/dataset/19/car+evaluation  
Nome: Car Evaluation Dataset  

O dataset contém avaliações de automóveis com base nos seguintes atributos categóricos:

- buying (preço de compra)
- maint (custo de manutenção)
- doors (número de portas)
- persons (capacidade de pessoas)
- lug_boot (tamanho do porta-malas)
- safety (nível de segurança)
- class (classificação final do veículo)

A variável alvo **class** possui quatro categorias:

- unacc (unacceptable)
- acc (acceptable)
- good
- vgood (very good)

O dataset é totalmente categórico, tornando necessária a utilização de uma métrica apropriada para esse tipo de dado.

---

## 🛠 Bibliotecas Utilizadas

### Pandas
Utilizada para manipulação e análise de dados tabulares.

```python
import pandas as pd
```

### NumPy
Utilizada para operações numéricas e manipulação de arrays.

```python
import numpy as np
```

### Matplotlib
Utilizada para visualizações gráficas.

```python
import matplotlib.pyplot as plt
```

### SciPy
Utilizada para clusterização hierárquica e construção do dendrograma.

```python
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
```

### Gower
Utilizada para cálculo da matriz de distância para dados categóricos.

```python
import gower
```

### Scikit-learn
Utilizada para métricas de avaliação de clusterização.

```python
from sklearn.metrics import silhouette_score
```

---

## 🔎 Pré-processamento

**Arquivo: preprocessamento.py**

Para esta etapa, foi feito primeiramente a importação do dataset bruto usando a biblioteca pandas, com o objetivo de conhecer o dataset e fazer ajustes para poder fazer a análise estatistica, visualização de dados e clusterização.
Observações importantes sobre o dataset:
* Os nomes das colunas estavam ausentes, sendo preciso colocar manualmente tendo como referencia informações dentro da fonte obtida.
* Sua estrutura é 100% categórica, ou seja, cata coluna possui rotulos como por exemplo: alto, medio ou baixo; ruim, moderado, bom ou muito bom, etc
* Variaveis possuem uma natureza ordinal, ou seja, a codificação deve preservar a ordem lógica dessas categorias.

Contudo, após verificar valores nulos, dimenções do dataset, tipos das variaveis, o problema principal se resume em codificar os dados categóricos.

Para isso, é utilizado o `replace`, uma função simples que o objetivo é substituir as categóricas por numeros inteiros de forma manual que garante a ordem semântica das variáveis ordinais.

Essa estratégia foi escolhida porque:

* Preserva a ordem natural das categorias.
* Evita distorções que poderiam ocorrer com codificação arbitrária.
* Mantém coerência semântica entre os níveis.

Concluindo, os dados pré-processados foram armazenados em um arquivo `Carr_dataset_ajustado.csv `.

## 📊 Análise Estatística

**Arquivo: analise_estatistica.py**

Esta etapa do projeto teve como objetivo realizar uma análise estatística descritiva do Car Evaluation, após o pré-processamento e a codificação das variáveis categóricas em valores numéricos ordinais.
A análise buscou:
* Compreender o comportamento das variáveis após o pré-processamento
* Avaliar medidas de tendência central 

**Medidas de Tendência Central e Disperção**
Foram calculadas média, mediana, moda, variância, desvio-padrão e amplitude para cada variável.
```
    Buying e Maint
Métrica	          Valor
Média	            2.50
Mediana           2.5
Moda             	1
Variância	        1.25
Desvio-padrão	    1.12
Amplitude	        3
```



Essas variáveis apresentam distribuição perfeitamente simétrica, com média centralizada no intervalo possível (1 a 4).

A variância de 1.25 e o desvio-padrão de 1.12 indicam boa dispersão ao longo das categorias.

Isso confirma que o dataset possui estrutura equilibrada nas variáveis explicativas, já que foi construído combinando sistematicamente todas as possibilidades de atributos.

```
         Doors
Métrica	          Valor
Média	            3.50
Mediana	          3.5
Moda	            2
Variância	        1.25
Desvio-padrão    	1.12
Amplitude	        3
```
A média elevada (3.5) é consequência da escala adotada (2, 3, 4, 5).

Apesar disso, a dispersão permanece uniforme, semelhante às variáveis buying e maint.

```
       Persons
Métrica	          Valor
Média	            3.67
Mediana	          4.0
Moda             	2
Variância	        1.56
Desvio-padrão	    1.25
Amplitude	        3
```
A variável persons apresentou a maior variância (1.56) e o maior desvio-padrão entre todas as variáveis explicativas.

Isso indica maior dispersão dos dados e potencialmente maior influência na diferenciação entre observações durante a clusterização.

```
    Lug_boot e Safety
Métrica         	Valor
Média	            2.00
Mediana	          2.0
Variância	        0.67
Desvio-padrão	    0.82
Amplitude       	2
```
Essas variáveis possuem apenas três níveis possíveis (1 a 3), o que naturalmente reduz sua variabilidade.

Apesar da menor dispersão, a variável safety é conhecida por exercer forte influência na classificação final dos veículos.

```
  Class (Variável Alvo)
Métrica	          Valor
Média	            1.41
Mediana	          1.0
Moda            	1
Variância	        0.55
Desvio-padrão   	0.74
Amplitude	        3
```
A variável class apresentou média próxima de 1, mediana igual a 1 e moda igual a 1, indicando forte concentração na categoria "unacc".

Isso demonstra que o dataset é estruturalmente desbalanceado, com predominância de veículos classificados como inaceitáveis.

O desvio-padrão reduzido confirma essa concentração nas classes mais baixas.

A análise estatística revelou três aspectos fundamentais:
* Equilíbrio estrutural nas variáveis explicativas.
As variáveis buying, maint, doors e persons apresentam distribuição relativamente uniforme.
* Desbalanceamento da variável alvo.
A classe "unacc" predomina significativamente no conjunto de dados.
* Influência potencial da variável safety.
Mesmo com menor variância, apresenta maior relação com a variável class.

Além disso, a variável persons apresentou maior variabilidade, podendo contribuir significativamente para a diferenciação entre grupos na etapa de clusterização.

---

## 📈 Visualização dos Dados

**Arquivo: visualizacao_dados.py**

Nesta etapa foi feito uma visualização dos dados através de uma matriz de correlação e boxplots com o objetivo de entender as correlações presentes entre as variáveis.

![Matriz de correlação ](matriz_correlacao.png)

Ao analisar a Matriz de correlação, percebe-se visualmente que:
* A Variável alvo `class` é a unica visualmente correlacionada
* As variáveis buying, maint, doors, persons, lug_boot e safety possuem uma correlação extremamente pequena, ou seja, seu valores são muito próximos de 0.
```
                buying         maint  ...        safety     class
buying    1.000000e+00 -2.072211e-15  ... -1.554300e-15 -0.282750
maint    -2.072211e-15  1.000000e+00  ... -2.588623e-16 -0.232422
doors     4.242286e-15  7.975102e-16  ...  9.909683e-17  0.066057
persons   7.983938e-16  1.883561e-16  ...  1.362772e-17  0.373459
lug_boot -1.525866e-16 -1.216188e-16  ...  7.131641e-18  0.157932
safety   -1.554300e-15 -2.588623e-16  ...  1.000000e+00  0.439337
class    -2.827504e-01 -2.324215e-01  ...  4.393373e-01  1.000000

```
De forma mais precisa, conseguimos análisar que essas variáveis são realmente possuem uma correlação quase 0 entre elas. 

**Sobre a variável alvo**
Ao analisar as correlações com a variável alvo, percebe-se que a variável safety possue uma maior correlação enquanto o buying possue uma maior morrelação (negativa).


![Boxplot buying x class ](/imagens_Car_Evaliation/boxplot_.png)

Ao analisarmos o boxplot do buying x class, Percebe-se que 
* A classe 1 possue uma maior variáncia enquanto sua medianá fica em `3`.
* Na classe 2 percebe-se uma mencentração por valores mais medianos.
* Na classe 3 e 4 percebe-se que seus valores variam entre `1 a 2`.
Portando, concluimos visualmente que quanto maior o preço do carro, menor vai ser sua avaliação

![Boxplot doors x class ](boxplot_2.png)

Ao analisarmos o boxplot do doors x class, Percebe-se que não tem muita diferença entre o número de portar para que o carro seja avaliado como aceitavel ou não.

![Boxplot safety x class ](boxplot_3.png)

Ao analisarmos o boxplot do doors x class, Percebe-se 
* A classe 1 possue uma concentração maior de safety entre 1 a 2
* A classe 2 e 3 possue uma variáncia mais concentrada entre 2 e 3
* A classe 4 possue seus valores de safety em 3
Portanto, conclue-se que há uma correlação positiva, ou seja, quanto maior a segurança do carro maior será a avaliação.


---

## 🤖 Clusterização Hierárquica

**Arquivo: clusterizacao.py**

---

## 🧠 Conclusão



