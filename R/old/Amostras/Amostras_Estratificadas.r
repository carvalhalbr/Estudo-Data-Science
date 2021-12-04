library("sampling")

summary(iris)

amostrasiris2 = strata(iris,c("Species"),size = c(25, 25, 25), method = "srswor")

summary(amostrasiris2)

infert

# Gerando uma amostra de 1oo elementos para"education", primeiro é necessario realizar uma proporcionalização => (número de elementos do estrato / amostra total) * tamanho desejado da amostra
amostra5 = round((12/248) * 100)
amostra11 = round((120/248) * 100)
amostra12 = round((116/248) * 100)

amostrasinfert = strata(infert,c("education"),size = c(amostra5, amostra11, amostra12), method = "srswor")


summary(amostrasinfert)

