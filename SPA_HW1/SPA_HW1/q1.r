rm(list = ls())
set.seed(12345)
par(mfrow=c(2,2))
bern1.data = rbinom(100,10,0.7)
bern2.data = rbinom(100,50,0.7)
bern3.data = rbinom(100,100,0.7)
bern4.data = rbinom(100,500,0.7)

#b)

plot(density(bern1.data))
plot(density(bern2.data))
plot(density(bern3.data))
plot(density(bern4.data))


#c)
plot(ecdf(bern1.data))
plot(ecdf(bern2.data))
plot(ecdf(bern3.data))
plot(ecdf(bern4.data))

#D)
bern5.data = rbinom(n=100, size=100, p=0.1)
plot(density(bern5.data))

#e)
rgeo.data = rgeom(n=100, p=0.7)
plot(ecdf(rgeo.data))


