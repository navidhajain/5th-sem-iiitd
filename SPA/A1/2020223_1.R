### Ques 1 #####
rm(list=ls())
set.seed(12345)
p<-0.4
t<-100 #### suppose finite time is 100

bernoulli.data<-sample(0:1,t,replace=T,prob=c((1-p),p))
plot(bernoulli.data, xlab= "Time", ylab= "Success(1) or Failure(0)")

### as we generate 100 data points and with prob 0.4 we should have ones
### or successes. The sum of data should be close to 40.
### The sum(bernoulli.data) gives 45, so the simulation is correct.

########first inter arrival time########

t<-100
p<-0.4
geom.data<-rgeom(t,p)
plot(geom.data)
cdf.geom<-1-((1-p)^(sort(geom.data)+1))
plot(cdf.geom,type="n",xlab= "First Interarrival Time X1", ylab="P(X1<=x)", ylim=c(0,1),); lines(cdf.geom)

#####N(k) for p=0.4 and p=0.9##########

p1<-0.4
p2<-0.9
k=100 #let k be 100
binomial.data<-matrix(nrow=k,ncol=2)
binomial.data[1:k,1]<-rbinom(n=100,size=100,p=p1)
binomial.data[1:k,2]<-rbinom(n=100,size=100,p=p2)
colormat<-c("black","blue")
par(mfrow=c(1, 2))
plot(c(1:k),binomial.data[,1],
    xlab="Time",ylab="Number of Earthquakes",
     col=colormat[1])
abline(h=mean(binomial.data[,1]))
plot(c(1:k),binomial.data[,2],
     xlab="Time",ylab="Number of Earthquakes",
     col=colormat[2])
abline(h=mean(binomial.data[,2]))
par(mfrow=c(1, 1))

plot(density(binomial.data[,1]),ylim=c(0,0.2),xlim=c(0,100),
     main="Density curve of number of earthquakes for the 2 
     values of p", xlab="Number of successes(n)", ylab="P(number of successes=n)")

points(density(binomial.data[,2]),col="blue")

par(mfrow=c(1, 2))
plot(ecdf(binomial.data[,1]),xlab="Trials",ylab="Cummulated Probability",
     col=colormat[1],
     main=paste("CDF of number of earthquakes for p=0.4"))
plot(ecdf(binomial.data[,2]),xlab="Trials",ylab="Cummulated Probability",
     col=colormat[2],
     main=paste("CDF of number of earthquakes for p=0.9"))



