library(readr)
pka379DataBestSettings <- read_csv("pka379DataBestSettings.csv")
pka379DataSwapPoints <- read_csv("pka379DataSwapPoints.csv")
pka379DataInsertingPoints <- read_csv("pka379DataInsertingPoints.csv")
pka379DataReverseSubpath <- read_csv("pka379DataReverseSubpath.csv")
xql662DataBestSettings <- read_csv("xql662DataBestSettings.csv")
xql662DataSwapPoints <- read_csv("xql662DataSwapPoints.csv")
xql662DataInsertingPoints <- read_csv("xql662DataInsertingPoints.csv")
xql662DataReverseSubpath <- read_csv("xql662DataReverseSubpath.csv")

pka379Data250iter <- read_csv("pka379Data250iter.csv")
pka379Data500iter <- read_csv("pka379Data500iter.csv")
pka379Data750iter <- read_csv("pka379Data750iter.csv")
pka379Data1000iter <- read_csv("pka379Data1000iter.csv")
pka379Data1250iter <- read_csv("pka379Data1250iter.csv")
pka379Data1500iter <- read_csv("pka379Data1500iter.csv")

pka379DataPoint941CoolingRate <- read_csv("pka379Data.941CoolingRate.csv")
pka379DataPoint96CoolingRate <- read_csv("pka379Data.96CoolingRate.csv")
pka379DataPoint98CoolingRate <- read_csv("pka379Data.98CoolingRate.csv")
pka379DataPoint99CoolingRate <- read_csv("pka379Data.99CoolingRate.csv")
pka379DataPoint995CoolingRate <- read_csv("pka379Data.995CoolingRate.csv")

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
upperBound <- c()
lowerBound <- c()

plottingIterFunction<-function(nameOfTheFile) {
  upperBound <- c()
  lowerBound <- c()
  colors <- c("blue", "green", "red", "yellow", "grey")
  for (i in 250:1500){
    if (i %% 250 != 0){
      next
    }
    upperBound <- c(upperBound, head(get(paste(nameOfTheFile,"Data", i, "iter", sep=""))$Distance, n=1))
    lowerBound <- c(lowerBound, tail(get(paste(nameOfTheFile,"Data", i, "iter", sep=""))$Distance, n=1))
  }
  plot(get(paste(nameOfTheFile,"Data250iter", sep=""))$X1,
       get(paste(nameOfTheFile,"Data250iter", sep=""))$Distance, 
       xaxt='n', main=paste("Simulated Annealing performance (dependent on the amount of iterations on",
                            nameOfTheFile, "file)"), ylim = c(min(lowerBound), max(upperBound)),
                            ylab="Calculated distance", 
                            xlab="Temperature", type="l", col="orange", lty=1:2, lwd=3)
  axis(1, at=c(0, 114, 227, 308), labels=c(98, 10, 1, 0.2));
  legendLabels <- c("250 iterations")
  for (i in 500:1500){
    if (i %% 250 != 0){
      next
    }
    lines(get(paste(nameOfTheFile,"Data", i, "iter", sep=""))$X1,
          get(paste(nameOfTheFile,"Data", i, "iter", sep=""))$Distance, 
          type="l", col=colors[(i-250)/250], cex=0.8, lwd=3)
    legendLabels <- c(legendLabels, paste(i, "iterations"))
  }
  legend("topright", legend=legendLabels, col=c("orange", colors), lwd=3)
}

cleaningUpFiles <- function() {
  pka379DataPoint99CoolingRateEdited <- pka379DataPoint99CoolingRate[seq(1, nrow(pka379DataPoint99CoolingRate), 2),]
  pka379DataPoint99CoolingRateEdited$X1 <- 0:309
  pka379DataPoint99CoolingRateEdited <- head(pka379DataPoint99CoolingRateEdited, -2) 
  
  pka379DataPoint995CoolingRateEdited <- pka379DataPoint995CoolingRate[seq(1, nrow(pka379DataPoint995CoolingRate), 4),]
  pka379DataPoint995CoolingRateEdited$X1 <- 0:309
  pka379DataPoint995CoolingRateEdited <- head(pka379DataPoint995CoolingRateEdited, -2) 
  
  pka379DataPoint96CoolingRateEdited <- pka379DataPoint96CoolingRate[rep(seq_len(nrow(pka379DataPoint96CoolingRate)), each=2),]
  temp <- data.frame(pka379DataPoint96CoolingRateEdited$X1[306], pka379DataPoint96CoolingRateEdited$Temperature[306], pka379DataPoint96CoolingRateEdited$Distance[306])
  colnames(temp) <- c("X1", "Temperature", "Distance")
  pka379DataPoint96CoolingRateEdited <- rbind(pka379DataPoint96CoolingRateEdited, temp)
  pka379DataPoint96CoolingRateEdited <- rbind(pka379DataPoint96CoolingRateEdited, temp)
  pka379DataPoint96CoolingRateEdited$X1 <- 0:307
  
  pka379DataPoint941CoolingRateEdited <- pka379DataPoint941CoolingRate[rep(seq_len(nrow(pka379DataPoint941CoolingRate)), each=3),]
  pka379DataPoint941CoolingRateEdited <- head(pka379DataPoint941CoolingRateEdited, -1) 
  pka379DataPoint941CoolingRateEdited$X1 <- 0:307
}


plottingCoolingFunction<-function(nameOfTheFile) {
  upperBound <- c(head(get(paste(nameOfTheFile,"DataPoint941CoolingRateEdited", sep=""))$Distance),
                  head(get(paste(nameOfTheFile,"DataPoint96CoolingRateEdited", sep=""))$Distance),
                  head(get(paste(nameOfTheFile,"DataPoint98CoolingRate", sep=""))$Distance),
                  head(get(paste(nameOfTheFile,"DataPoint99CoolingRateEdited", sep=""))$Distance),
                  head(get(paste(nameOfTheFile,"DataPoint995CoolingRateEdited", sep=""))$Distance))
  lowerBound <- c(tail(get(paste(nameOfTheFile,"DataPoint941CoolingRateEdited", sep=""))$Distance),
                  tail(get(paste(nameOfTheFile,"DataPoint96CoolingRateEdited", sep=""))$Distance),
                  tail(get(paste(nameOfTheFile,"DataPoint98CoolingRate", sep=""))$Distance),
                  tail(get(paste(nameOfTheFile,"DataPoint99CoolingRateEdited", sep=""))$Distance),
                  tail(get(paste(nameOfTheFile,"DataPoint995CoolingRateEdited", sep=""))$Distance))
  colors <- c("blue", "green", "orange", "red", "yellow")
  plot(get(paste(nameOfTheFile,"DataPoint98CoolingRate", sep=""))$X1,
       get(paste(nameOfTheFile,"DataPoint98CoolingRate", sep=""))$Distance, 
       xaxt='n', main=paste("Simulated Annealing performance (dependent on the amount of the cooling rate on",
                            nameOfTheFile, "file)"), ylim = c(min(lowerBound), max(upperBound)),
       ylab="Calculated distance", 
       xlab="Temperature", type="l", col=colors[3], lty=1:2, lwd=3)
  axis(1, at=c(0, 114, 227, 308), labels=c(100, 10, 1, 0.2));
  
  legendLabels <- c(".941 Cooling Rate", ".96 Cooling Rate", ".98 Cooling Rate", ".99 Cooling Rate", ".995 Cooling Rate")
  lines(get(paste(nameOfTheFile, "DataPoint941CoolingRateEdited", sep=""))$X1,
        get(paste(nameOfTheFile, "DataPoint941CoolingRateEdited", sep=""))$Distance, 
        type="l", col=colors[1], cex=0.8, lwd=3)
  lines(get(paste(nameOfTheFile, "DataPoint96CoolingRateEdited", sep=""))$X1,
        get(paste(nameOfTheFile, "DataPoint96CoolingRateEdited", sep=""))$Distance, 
        type="l", col=colors[2], cex=0.8, lwd=3)
  lines(get(paste(nameOfTheFile, "DataPoint99CoolingRateEdited", sep=""))$X1,
        get(paste(nameOfTheFile, "DataPoint99CoolingRateEdited", sep=""))$Distance, 
        type="l", col=colors[4], cex=0.8, lwd=3)
  lines(get(paste(nameOfTheFile, "DataPoint995CoolingRateEdited", sep=""))$X1,
        get(paste(nameOfTheFile, "DataPoint995CoolingRateEdited", sep=""))$Distance, 
        type="l", col=colors[5], cex=0.8, lwd=3)
  legend("topright", legend=legendLabels, col=c(colors), lwd=3)
}

plottingFunction("pka379")
plottingFunction("xql662")
plottingIterFunction("pka379")
cleaningUpFiles()
plottingCoolingFunction("pka379")
