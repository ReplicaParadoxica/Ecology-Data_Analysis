import json


def extract_cccc(line):
    parts = line.strip().split('","')
    if len(parts) < 2:
        return None, None
    sender = parts[0].split()[1]
    receivers = [ccc for ccc in parts[1:] if ccc != "XXXX" and ccc != "****"]
    return sender, receivers


eswiroca_data = []
with open("ESWIroca.txt", "r") as file:
    for line in file:
        sender, receivers = extract_cccc(line)
        if sender is None:
            continue
        eswiroca_data.append((sender, receivers))

umrr_received_telegrams = {}
for sender, receivers in eswiroca_data:
    if "UMRR" in receivers:
        count = receivers.count("UMRR")
        umrr_received_telegrams[sender] = count

volc1_countries = {}
with open("VolC1.txt", "r") as file:
    header = file.readline()
    for line in file:
        parts = line.strip().split('","')
        if len(parts) < 7:
            continue
        cccc = parts[6].strip('"')
        country = parts[2].strip('"')
        volc1_countries[cccc] = country

countries_with_telegrams = {}
for sender, count in umrr_received_telegrams.items():
    if sender in volc1_countries:
        country = volc1_countries[sender]
        countries_with_telegrams[country] = countries_with_telegrams.get(
            country, 0) + count


print("Countries that sent telegrams and the number of telegrams sent:")
for country, count in countries_with_telegrams.items():
    print(f"{country}: {count} telegrams")


output_data = {
    "countries": list(countries_with_telegrams.keys()),
    "telegrams_count": list(countries_with_telegrams.values())
}

with open("countries_telegrams.json", "w") as json_file:
    json.dump(output_data, json_file)
