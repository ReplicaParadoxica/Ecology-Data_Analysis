library(dplyr)
# You can use getwd() for file path or file.choose()
# This is a cleaned file with NA values
data <- read.csv("Cleaned_dataNA.csv", header = TRUE)


data$Datums.un.laiks <- as.POSIXct(data$Datums.un.laiks, format = "%m.%d %H:%M")
monthly_averages <- data %>%
  mutate(year_month = format(Datums.un.laiks, "%Y-%m")) %>%
  group_by(year_month) %>%
  summarise(
    x1_avg = ifelse(mean(!is.na(x1)) >= 0.8, mean(x1, na.rm = TRUE), NA),
    x2_avg = ifelse(mean(!is.na(x2)) >= 0.8, mean(x2, na.rm = TRUE), NA),
    x3_avg = ifelse(mean(!is.na(x3)) >= 0.8, mean(x3, na.rm = TRUE), NA)
  ) %>%
  na.omit()
print(monthly_averages)
