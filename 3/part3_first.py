import xarray as xr
import matplotlib.pyplot as plt

file_path = "ECMWF_prognozes.nc"
data = xr.open_dataset(file_path)
lat = data.latitude.values
lon = data.longitude.values
time_steps = [0, 14, 21]
ssr_data = data.ssr.isel(time=time_steps)

for i, time_idx in enumerate(time_steps):
    time_value = data.time.isel(time=time_idx).values
    ssr_values = ssr_data.isel(time=i).values
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(lon, lat, ssr_values, shading='auto')
    plt.colorbar(label="J m**-2")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title(f"SSR - {time_value}")
    plt.grid(True)
    plt.show()
