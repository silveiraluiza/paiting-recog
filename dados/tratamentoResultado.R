library(readr)
library(tidyverse)
setwd("C:/Users/carva/Documents/")

results <- read_csv("./paiting-recog/Nova pasta/test_results.csv")

auth_predict <- results$AUTHOR_PREDICTED
auth_real <-  results$AUTHOR_EXPECTED

acertos <- 0
for(i in 1:500){
  if( auth_predict[i] == auth_real[i]){
    acertos = acertos + 1
  }
}
percent_aut <- acertos/500
percent_aut

tech_predict <- results$TECHNIQUE_PREDICTED
tech_real <-  results$TECHNIQUE_EXPECTED

acertos <- 0
for(i in 1:500){
  if( tech_predict[i] == tech_real[i]){
    acertos = acertos + 1
  }
}
percent_tec <- acertos/500
percent_tec



sch_predict <- results$SCHOOL_PREDICTED
sch_real <-  results$SCHOOL_EXPECTED

acertos <- 0
for(i in 1:500){
  if( sch_predict[i] == sch_real[i]){
    acertos = acertos + 1
  }
}
percent_sc <- acertos/500
percent_sc

acert <- results$MATCHES
acertos <- 0
for(i in 1:500){
  acertos = acertos + acert[i]
  }
}
perc_total <- acertos/1500

percentual <- c(100*percent_sc, 100*percent_aut, 100*percent_tec, round(100*perc_total,2))
tipo <- c("Escola", "Artista", "Técnica", "Total")

acertos <- as.data.frame(cbind(tipo, percentual))

p <- ggplot(data=acertos, aes(x=tipo, y=percentual)) +
  geom_bar(stat="identity", fill = "#436396") +  theme(axis.title.x = element_blank(),axis.title.y=element_blank(),
                                     axis.ticks.y=element_blank())
p + coord_flip()
