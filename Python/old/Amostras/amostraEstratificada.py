import pandas as pd
from sklearn.model_selection import train_test_split

#base de dados Iris
iris = pd.read_csv('.\Python\src\iris.csv')
# print(iris)

contagem = iris['class'].value_counts()
# print(contagem)

x, _, y, _ = train_test_split(iris.iloc[:,0:4], iris.iloc[:, 4], test_size = 0.5, stratify = iris.iloc[:, 4])
# print(x,y)

contagemY = y.value_counts()
# print(contagemY)

#base de dados Infert
infert = pd.read_csv('.\Python\src\infert.csv')
print(infert)

qt = infert['education'].value_counts()
print(qt)
total = 0
for quantidade in qt:
    total += quantidade

# Gerando uma amostra de 1oo elementos para"education", primeiro é necessario realizar uma proporcionalização => (número de elementos do estrato / amostra total) * tamanho desejado da amostra
amostras6 = (qt[0]/total) *100
amostras12 = (qt[1]/total) *100
amostras0 = (qt[2]/total) *100
fator = (248-100)/248
    
x1, _, y1, _ = train_test_split(infert.iloc[:,2:9], infert.iloc[:, 1], test_size = fator, stratify = infert.iloc[:, 1])
print(x1, y1)

valory1 = y1.value_counts()
print(valory1)