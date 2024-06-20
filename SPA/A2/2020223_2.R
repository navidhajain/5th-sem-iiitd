rm(list=ls())
# set.seed(12345)

xbin<-c()
pos <- 5
path<-c(5)
status<-0
while (status == 0){
  x <- rbinom(1, 1, 0.8)
  xbin<-c(xbin, x)
  if (x == 1) 
    pos <- pos + 1
  if (x == 0) 
    pos <- pos - 1
  path <- c(path, pos)
  if (pos == 10) 
    status <- 1
  if (pos == 0) 
    status <- 1
}

print(xbin)

plot(path, xlab="Time",ylab="Dollars", ylim=c(0,10), col="red", pch=19)
