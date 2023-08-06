import csv
import requests

volc1_url = 'https://wis.wmo.int/operational-info/VolumeC1/VolC1.txt'
eswiroca_url = 'https://wis.wmo.int/operational-info/GTS_routeing/ESWI/ESWIroca.txt'
volc1_file_path = 'VolC1.txt'
eswiroca_file_path = 'ESWIroca.txt'

response = requests.get(volc1_url)
with open(volc1_file_path, 'wb') as file:
    file.write(response.content)

response = requests.get(eswiroca_url)
with open(eswiroca_file_path, 'wb') as file:
    file.write(response.content)


with open(volc1_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    volc1_data = [row for row in reader]


with open(eswiroca_file_path, 'r') as file:
    lines = file.readlines()
    date = lines[0].strip()
    eswiroca_data = [line.strip().split(',') for line in lines[1:]]


print("Data from VolC1.txt:")
for entry in volc1_data:
    print(entry)

print("\nDate from ESWIroca.txt:", date)
print("Data from ESWIroca.txt:")
for entry in eswiroca_data:
    print(entry)
