n<-10;
nosim<-1000
xbar<-apply(matrix(sample(1:6,n*nosim, replace = TRUE),nosim), 1, mean);
barplot(table(xbar), col = "lightblue");
var(xbar)