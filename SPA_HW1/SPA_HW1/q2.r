rm(list = ls())
set.seed(12345)
par(mfrow=c(2,2))

#Q2
#a)
plot(density(rpois(n=100, lambda=20*50)))


#b)
plot(ecdf(rpois(n=100, lambda=20*50)))
plot(ecdf(rpois(n=100, lambda=20*100)))

