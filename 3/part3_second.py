import xarray as xr
import numpy as np
import matplotlib.pyplot as plt


def find_closest_index(array, value):
    return int(np.argmin(np.abs(array - value)))


file_path = "ECMWF_prognozes.nc"
data = xr.open_dataset(file_path)

cities = {
    "Liepāja": {"latitude": 56.51667, "longitude": 21.01667},
    "Alūksne": {"latitude": 57.41667, "longitude": 27.00000},
    "Dagda": {"latitude": 56.09512, "longitude": 27.53723}
}

radiation_data = {}
for city, coords in cities.items():
    lat_idx = find_closest_index(data.latitude.values, coords["latitude"])
    lon_idx = find_closest_index(data.longitude.values, coords["longitude"])
    ssr_data = data.ssr[:, lat_idx, lon_idx]
    radiation_data[city] = ssr_data

for city, ssr_data in radiation_data.items():
    radiation_data[city] = ssr_data / 3600

plt.figure(figsize=(12, 6))
for city, ssr_data in radiation_data.items():
    plt.plot(data.time, ssr_data, label=city)
plt.xlabel("Time")
plt.ylabel("Solar Radiation (W/m²)")
plt.legend()
plt.grid(True)
plt.show()
