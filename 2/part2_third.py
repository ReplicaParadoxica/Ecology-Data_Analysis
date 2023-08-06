import os


def create_folders_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)


def save_data_to_txt_file(region, rth, country, cccc, ttaaii, time_group):
    folder_path = os.path.join("DataStructure", region, rth, country, cccc)
    create_folders_if_not_exist(folder_path)

    file_name = f"{country}_{ttaaii}_{cccc}_TimeGroup.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write(time_group)


with open("VolC1.txt", "r") as file:
    lines = file.readlines()

lines = lines[1:]

for line in lines:
    parts = line.strip().split(",")

    if len(parts) < 10:
        print(f"Skipping invalid line: {line}")
        continue

    region = parts[1].strip("\"")
    rth = parts[2].strip("\"")
    country = parts[3].strip("\"")
    cccc = parts[6].strip("\"")
    ttaaii = parts[5].strip("\"")
    time_group = parts[9].strip("\"")
    if cccc in ["UMRR", "ESWI", "EEMH"]:
        save_data_to_txt_file(region, rth, country, cccc, ttaaii, time_group)


if not os.path.exists("DataStructure"):
    os.makedirs("DataStructure")


root_dir = "DataStructure"
for region in os.listdir(root_dir):
    for rth in os.listdir(os.path.join(root_dir, region)):
        for country in os.listdir(os.path.join(root_dir, region, rth)):
            for cccc in os.listdir(os.path.join(root_dir, region, rth, country)):
                print(f"{region}/{rth}/{country}/{cccc}")
