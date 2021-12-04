library("TeachingSampling")

# Usando TeachingSampling
amostra = S.SY(150,10) # Gera um número de forma aleatória de 10 em 10
amostra

amostrasiris = iris[amostra,]
amostrasiris