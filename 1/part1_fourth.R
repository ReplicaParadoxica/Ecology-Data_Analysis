# You can use getwd() for file path or file.choose()
data <- read.csv("Cleaned_data.csv", sep=",")
mean_x1 <- mean(data$x1)
mean_x2 <- mean(data$x2)
mean_x3 <- mean(data$x3)

sd_x1 <- sd(data$x1)
sd_x2 <- sd(data$x2)
sd_x3 <- sd(data$x3)
x_values <- seq(-5, 10, 0.1)
bell_curve_x1 <- dnorm(x_values, mean=mean_x1, sd=sd_x1)
bell_curve_x2 <- dnorm(x_values, mean=mean_x2, sd=sd_x2)
bell_curve_x3 <- dnorm(x_values, mean=mean_x3, sd=sd_x3)

plot(x_values, bell_curve_x1, type="l", col="blue", lwd=2, xlab="Parameter", ylab="Probability density", main="Bell Curves for x1, x2, and x3")
lines(x_values, bell_curve_x2, col="red", lwd=2)
lines(x_values, bell_curve_x3, col="green", lwd=2)

legend("topright", legend=c("x1", "x2", "x3"), col=c("blue", "red", "green"), lwd=2)
grid()




library(MASS)
#Also as in previous comment
data <- read.csv("Cleaned_data.csv", sep=",")

x1_data <- data$x1
x2_data <- data$x2
x3_data <- data$x3

fit_normal_distribution <- function(data) {
  fit <- fitdistr(data, "normal")
  return(list(mean = fit$estimate[1], sd = fit$estimate[2]))
}

x1_params <- fit_normal_distribution(x1_data)
x2_params <- fit_normal_distribution(x2_data)
x3_params <- fit_normal_distribution(x3_data)

cat("Station x1 - Mean:", x1_params$mean, ", Standard Deviation:", x1_params$sd, "\n")
cat("Station x2 - Mean:", x2_params$mean, ", Standard Deviation:", x2_params$sd, "\n")
cat("Station x3 - Mean:", x3_params$mean, ", Standard Deviation:", x3_params$sd, "\n")
