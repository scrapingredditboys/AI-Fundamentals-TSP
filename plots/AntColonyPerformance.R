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

plottingFunction("pka379")
