file = open("wi_coords.txt", "r")
entries = file.readlines()
file.close()
cleaned = open("wi_cleaned.txt", "w")
southern = 42.249498
western = -92.865933
northern = 46.969128
eastern = -86.198203

for entry in entries:
    entry = entry.replace("\n", "")
    parts = entry.split(";")
    parts[0] = parts[0].replace(" ", "")
    lat_long = parts[0].split(",")

    if float(lat_long[0]) < southern or float(lat_long[0]) > northern \
        or float(lat_long[1]) < western or float(lat_long[1]) > eastern:
        pass
    else:
        cleaned.writelines(entry + "\n")

cleaned.close()
