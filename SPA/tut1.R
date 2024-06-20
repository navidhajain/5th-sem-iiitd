rm(list=ls())
set.seed(12345)
p<-0.8
t<-100
bernoulli.data<-sample(0:1, t, replace = T, prob = c((1-p), p))
plot(bernoulli.data)
#-------------

alt.bernoulli.data<-rbinom(n=t, size = )