library(readr)
pka379DataBestSettings <- read_csv("pka379DataBestSettings.csv")
pka379DataSwapPoints <- read_csv("pka379DataSwapPoints.csv")
pka379DataInsertingPoints <- read_csv("pka379DataInsertingPoints.csv")
pka379DataReverseSubpath <- read_csv("pka379DataReverseSubpath.csv")
xql662DataBestSettings <- read_csv("xql662DataBestSettings.csv")
xql662DataSwapPoints <- read_csv("xql662DataSwapPoints.csv")
xql662DataInsertingPoints <- read_csv("xql662DataInsertingPoints.csv")
xql662DataReverseSubpath <- read_csv("xql662DataReverseSubpath.csv")

plottingFunction<-function(nameOfTheFile) {
  plot(get(paste(nameOfTheFile,"DataReverseSubpath", sep=""))$X1,
       get(paste(nameOfTheFile,"DataReverseSubpath", sep=""))$Distance, 
       xaxt='n', main=paste("Simulated Annealing performance (between temperatures 100 and 0.2 on", 
       nameOfTheFile, "file from Waterloo University website)"), ylab="Calculated distance", 
       xlab="Temperature", type="l", col="orange", lty=1:2, lwd=3)
  axis(1, at=c(0, 114, 227, 308), labels=c(98, 10, 1, 0.2));
  lines(get(paste(nameOfTheFile,"DataSwapPoints", sep=""))$X1,
        get(paste(nameOfTheFile,"DataSwapPoints", sep=""))$Distance, 
        type="l", col="blue", cex=0.8, lwd=3)
  lines(get(paste(nameOfTheFile,"DataInsertingPoints", sep=""))$X1,
        get(paste(nameOfTheFile,"DataInsertingPoints", sep=""))$Distance, 
        type="l", col="green", cex=0.8, lwd=3)
  lines(get(paste(nameOfTheFile,"DataBestSettings", sep=""))$X1,
        get(paste(nameOfTheFile,"DataBestSettings", sep=""))$Distance, 
        type="l", col="red", cex=0.8, lwd=3)
  legend("topright", legend=c("Combined three methods", "Only Swap Points enabled", "Only Inserting Points enabled", "Only Reverse Subpath enabled"),
         col=c("red", "blue", "green", "orange"), lwd=3)
}

plottingFunction("pka379")
plottingFunction("xql662")
