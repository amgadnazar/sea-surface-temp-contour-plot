
import netCDF4 as nc                      
import numpy as np                        
import matplotlib.pyplot as plt           
import os                                 


file_path = os.path.expanduser('~/Downloads/SeaSurfaceTemp.nc')

dataset = nc.Dataset(file_path)


print("Global Attributes:")
for attr in dataset.ncattrs():
    print(f"{attr}: {getattr(dataset, attr)}")

print("\nDimensions:")
for dim in dataset.dimensions.values():
    print(f"{dim.name}: size = {len(dim)}")

print("\nVariables:")
for var in dataset.variables.values():
    print(f"{var.name}: dimensions = {var.dimensions}, dtype = {var.dtype}")


lat = dataset.variables['lat'][:]       
lon = dataset.variables['lon'][:]       


sst_raw = dataset.variables['sst'][0, :, :]   


sst = np.ma.masked_where(sst_raw < -1000, sst_raw)

print(f"\nMasked {np.sum(sst.mask)} missing SST values.")


lon_grid, lat_grid = np.meshgrid(lon, lat)

plt.figure(figsize=(12, 6))  

contour = plt.contourf(lon_grid, lat_grid, sst, levels=20, cmap='coolwarm')

plt.title('Sea Surface Temperature - Month 1', fontsize=14)
plt.xlabel('Longitude (degrees)', fontsize=12)
plt.ylabel('Latitude (degrees)', fontsize=12)

cbar = plt.colorbar(contour)
cbar.set_label('Temperature (°C)', fontsize=12)

plt.grid(True)

plt.show()

