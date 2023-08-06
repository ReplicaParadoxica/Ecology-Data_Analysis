import pandas as pd

data = pd.read_csv('Data_interview.csv',
                   parse_dates=['Datums.un.laiks'], dayfirst=True)

# Can be commented out to produce Cleaned_dataNA.csv
data = data.dropna()

outliers = []
for station in ['x1', 'x2', 'x3']:
    station_data = data[station]
    mean = station_data.mean()
    std = station_data.std()
    lower_bound = mean - 3 * std
    upper_bound = mean + 3 * std
    station_outliers = station_data[(
        station_data < lower_bound) | (station_data > upper_bound)]
    outliers.extend(station_outliers.index.tolist())

data = data.drop(outliers)

#if NA is not ommitted:
#data.to_csv('Cleaned_data.csvNA', index=False)

data.to_csv('Cleaned_data.csv', index=False)
