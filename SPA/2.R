####Question 2########
rm(list=ls())
set.seed(12345)

#####part(a)#####
par(mfrow=c(1,1))
plot(density(rpois(n=100, lambda=10*100)),
     xlab="X",
     ylab=" f(x)",
     main=paste("Density of number of arrivals for lambda=10"))

#####part(b)#####
par(mfrow=c(1,1))
plot(density(rpois(n=100, lambda=20*100)),
     xlab="X",
     ylab=" f(x)",
     main=paste("Density of number of arrivals for lambda=20"))

#####part (c)#####

##density##
par(mfrow=c(1,1))
plot(density(rpois(n=100, lambda=15*100)),
     xlab="X",
     ylab=" f(x)",
     main=paste("Density of number of arrivals for lambda=15"))


#plot(rexp(100, 15))
plot(ecdf(rexp(n=100, rate=15)),
     main=paste("ECDF of First inter-arrival time"),
     xlab= "X",
     ylab="P(X<=x)")






