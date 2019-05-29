library(readr)
pka379ant3 <- read_csv("results_ants-3_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
pka379ant5 <- read_csv("results_ants-5_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
pka379ant7 <- read_csv("results_ants-7_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
pka379ant9 <- read_csv("results_ants-9_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
pka379ant11 <- read_csv("results_ants-11_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                        col_names = FALSE)
pka379ant13 <- read_csv("results_ants-13_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                        col_names = FALSE)
pka379ant15 <- read_csv("results_ants-15_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                        col_names = FALSE)

xql662ant3 <- read_csv("xql662_results_ants-3_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
xql662ant5 <- read_csv("xql662_results_ants-5_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
xql662ant7 <- read_csv("xql662_results_ants-7_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
xql662ant9 <- read_csv("xql662_results_ants-9_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
xql662ant11 <- read_csv("xql662_results_ants-11_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                        col_names = FALSE)
xql662ant13 <- read_csv("xql662_results_ants-13_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                        col_names = FALSE)
xql662ant15 <- read_csv("xql662_results_ants-15_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                        col_names = FALSE)

pka379beta2 <- read_csv("results_ants-4_iters-50_alpha-0.5_beta-2.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
pka379beta7 <- read_csv("results_ants-4_iters-50_alpha-0.5_beta-7.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
pka379beta12 <- read_csv("results_ants-4_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
pka379beta17 <- read_csv("results_ants-4_iters-50_alpha-0.5_beta-17.0_q0-0.3_rho-0.6.csv", 
                       col_names = FALSE)
pka379beta22 <- read_csv("results_ants-4_iters-50_alpha-0.5_beta-22.0_q0-0.3_rho-0.6.csv", 
                        col_names = FALSE)

pka379alpha1 <- read_csv("results_ants-4_iters-50_alpha-0.1_beta-12.0_q0-0.3_rho-0.6.csv", 
                        col_names = FALSE)
pka379alpha3 <- read_csv("results_ants-4_iters-50_alpha-0.3_beta-12.0_q0-0.3_rho-0.6.csv", 
                        col_names = FALSE)
pka379alpha5 <- read_csv("results_ants-4_iters-50_alpha-0.5_beta-12.0_q0-0.3_rho-0.6.csv", 
                         col_names = FALSE)
pka379alpha7 <- read_csv("results_ants-4_iters-50_alpha-0.7_beta-12.0_q0-0.3_rho-0.6.csv", 
                         col_names = FALSE)
pka379alpha9 <- read_csv("results_ants-4_iters-50_alpha-0.9_beta-12.0_q0-0.3_rho-0.6.csv", 
                         col_names = FALSE)

pka379custom1 <- read_csv("results_ants-4_iters-50_alpha-0.5_beta-12.0_q0-0.1_rho-0.99.csv", 
                         col_names = FALSE)
pka379custom2 <- read_csv("results_ants-4_iters-50_alpha-0.3_beta-12.0_q0-0.3_rho-0.6.csv", 
                         col_names = FALSE)
pka379custom3 <- read_csv("results_ants-4_iters-50_alpha-0.5_beta-12.0_q0-0.5_rho-0.5.csv", 
                         col_names = FALSE)
pka379custom4 <- read_csv("results_ants-4_iters-50_alpha-0.5_beta-12.0_q0-0.6_rho-0.3.csv", 
                         col_names = FALSE)
pka379custom5 <- read_csv("results_ants-4_iters-50_alpha-0.5_beta-12.0_q0-0.99_rho-0.1.csv", 
                         col_names = FALSE)


colors <- c("blue", "green", "red", "yellow", "grey", "magenta3")

plottingFunction<-function(nameOfTheFile) {
  upperBound <- c()
  lowerBound <- c()
  for (i in 3:15){
    if (!i %% 2){
      next
    }
    upperBound <- c(upperBound, head(get(paste(nameOfTheFile,"ant", i, sep=""))$X3, n=1))
    lowerBound <- c(lowerBound, tail(get(paste(nameOfTheFile,"ant", i, sep=""))$X3, n=1))
  }
  
  plot(get(paste(nameOfTheFile,"ant3", sep=""))$X1,
       get(paste(nameOfTheFile,"ant3", sep=""))$X3, 
       ylim = c(min(lowerBound), max(upperBound)),
       main=paste("Ant Colony Algorithm performance (calculated in the first 50 iterations on", 
       nameOfTheFile, "file from Waterloo University website)"), ylab="Calculated distance", 
       xlab="Iterations per ant", type="l", col="orange", lty=1:2, lwd=3)
  
  legendLabels <- c("Ant Colony algorithm with 3 ants")
  for (i in 5:15){
    if (!i %% 2){
      next
    }
    lines(get(paste(nameOfTheFile,"ant", i, sep=""))$X1,
          get(paste(nameOfTheFile,"ant", i, sep=""))$X3, 
          type="l", col=colors[(i-3)/2], cex=0.8, lwd=3)
    legendLabels <- c(legendLabels, paste("Ant Colony algorithm with", i, "ants"))
  }
  legend("topright", legend=legendLabels, col=c("orange", colors), lwd=3)
}

plottingFunctionBeta<-function(nameOfTheFile) {
  upperBound <- c()
  lowerBound <- c()
  for (i in 2:22){
    if (i %% 5 != 2){
      next
    }
    upperBound <- c(upperBound, head(get(paste(nameOfTheFile,"beta", i, sep=""))$X3, n=1))
    lowerBound <- c(lowerBound, tail(get(paste(nameOfTheFile,"beta", i, sep=""))$X3, n=1))
  }
  
  plot(get(paste(nameOfTheFile,"beta2", sep=""))$X1,
       get(paste(nameOfTheFile,"beta2", sep=""))$X3, 
       ylim = c(min(lowerBound), max(upperBound)+200),
       main=paste("Ant Colony Algorithm depending on beta coefficient (calculated in the first 50 iterations on", 
                  nameOfTheFile, "file)"), ylab="Calculated distance", 
       xlab="Iterations per ant", type="l", col="orange", lty=1:2, lwd=3, log="y")
  
  legendLabels <- c("Beta parameter = 2")
  for (i in 7:22){
    if (i %% 5 !=2){
      next
    }
    lines(get(paste(nameOfTheFile,"beta", i, sep=""))$X1,
          get(paste(nameOfTheFile,"beta", i, sep=""))$X3, 
          type="l", col=colors[(i-2)/5], cex=0.8, lwd=3)
    legendLabels <- c(legendLabels, paste("Beta parameter =", i))
  }
  legend("topright", legend=legendLabels, col=c("orange", colors), lwd=3)
}

plottingFunctionAlpha<-function(nameOfTheFile) {
  upperBound <- c()
  lowerBound <- c()
  for (i in 1:9){
    if (i %% 2 != 1){
      next
    }
    upperBound <- c(upperBound, head(get(paste(nameOfTheFile,"alpha", i, sep=""))$X3, n=1))
    lowerBound <- c(lowerBound, tail(get(paste(nameOfTheFile,"alpha", i, sep=""))$X3, n=1))
  }
  
  plot(get(paste(nameOfTheFile,"alpha1", sep=""))$X1,
       get(paste(nameOfTheFile,"alpha1", sep=""))$X3, 
       ylim = c(min(lowerBound), max(upperBound)),
       main=paste("Ant Colony Algorithm depending on alpha coefficient (calculated in the first 50 iterations on", 
                  nameOfTheFile, "file)"), ylab="Calculated distance", 
       xlab="Iterations per ant", type="l", col="orange", lty=1:2, lwd=3, log="y")
  
  legendLabels <- c("Alpha parameter = .1")
  for (i in 3:9){
    if (i %% 2 != 1){
      next
    }
    lines(get(paste(nameOfTheFile,"alpha", i, sep=""))$X1,
          get(paste(nameOfTheFile,"alpha", i, sep=""))$X3, 
          type="l", col=colors[(i-1)/2], cex=0.8, lwd=3)
    legendLabels <- c(legendLabels, paste("Alpha parameter = .", i, sep=""))
  }
  legend("topright", legend=legendLabels, col=c("orange", colors), lwd=3)
}

plottingFunctionCustom<-function(nameOfTheFile) {
  upperBound <- c()
  lowerBound <- c()
  for (i in 1:5){
    upperBound <- c(upperBound, head(get(paste(nameOfTheFile,"custom", i, sep=""))$X3, n=1))
    lowerBound <- c(lowerBound, tail(get(paste(nameOfTheFile,"custom", i, sep=""))$X3, n=1))
  }
  
  plot(get(paste(nameOfTheFile,"custom1", sep=""))$X1,
       get(paste(nameOfTheFile,"custom1", sep=""))$X3, 
       ylim = c(min(lowerBound), max(upperBound)),
       main=paste("Ant Colony Algorithm depending on other coefficients (calculated in the first 50 iterations on", 
                  nameOfTheFile, "file)"), ylab="Calculated distance", 
       xlab="Iterations per ant", type="l", col="orange", lty=1:2, lwd=3, log="y")
  
  legendLabels <- c("q0=0.1, rho=0.99", "q0=0.3, rho=0.6", "q0=0.5, rho=0.5", "q0=0.6, rho=0.3", "q0=0.99, rho=0.1")
  for (i in 2:5){
    lines(get(paste(nameOfTheFile,"custom", i, sep=""))$X1,
          get(paste(nameOfTheFile,"custom", i, sep=""))$X3, 
          type="l", col=colors[(i-1)], cex=0.8, lwd=3)
  }
  legend("topright", legend=legendLabels, col=c("orange", colors), lwd=3)
}

plottingFunction("pka379")
plottingFunction("xql662")
plottingFunctionBeta("pka379")
plottingFunctionAlpha("pka379")
plottingFunctionCustom("pka379")
