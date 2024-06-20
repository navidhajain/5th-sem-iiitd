rm(list=ls())
set.seed(12345)

#part a
mc<-function(){
  path<-c(1)
  pos<-1
  for(i in 1:50){
    if(pos==1){
      x1=rbinom(1, 1, 0.7)
      if(x1==1){
        path<-c(path, 2)
        pos<-2
      
      }else{
        path<-c(path, 1)
        pos<-1
        
      }
    }else{
      x2=rbinom(1, 1, 0.5)
      if(x2==1){
        path<-c(path, 2)
        pos<-2
        
      }else{
        path<-c(path, 1)
        pos<-1
        
      }
    }
  }
  return(path)
}

p1<-mc()
plot(p1, col="red", pch=19, type="b", xlab="Time",ylab="State")
p2<-mc()
plot(p2, col="blue", pch=15, type="b", xlab="Time",ylab="State")
p3<-mc()
plot(p3, col="green", pch=17, type="b", xlab="Time",ylab="State")
p4<-mc()
plot(p4, col="brown", pch=18, type="b", xlab="Time",ylab="State")
p5<-mc()
plot(p5, col="black", pch=0, type="b", xlab="Time",ylab="State")

#part b
pmat<-matrix(c(0.3, 0.5, 0.7, 0.5), nrow = 2, ncol = 2)
p10<-matrix(c(0.3, 0.5, 0.7, 0.5), nrow = 2, ncol = 2)
p20<-matrix(c(0.3, 0.5, 0.7, 0.5), nrow = 2, ncol = 2)
p50<-matrix(c(0.3, 0.5, 0.7, 0.5), nrow = 2, ncol = 2)
print(pmat)

for(i in 1:10){
  p10<-pmat%*%p10
}

for(i in 1:20){
  p20<-pmat%*%p20
}

for(i in 1:50){
  p50<-pmat%*%p50
}

print(p10)
print(p20)
print(p50)


