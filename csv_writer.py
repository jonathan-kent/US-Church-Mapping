baptist = ["latitude,longitude\n"]
methodist = ["latitude,longitude\n"]
presbyterian = ["latitude,longitude\n"]
orthodox = ["latitude,longitude\n"]
episcopal = ["latitude,longitude\n"]
catholic = ["latitude,longitude\n"]
lutheran = ["latitude,longitude\n"]
reformed = ["latitude,longitude\n"]
calvinist = ["latitude,longitude\n"]
pentecostal = ["latitude,longitude\n"]
adventist = ["latitude,longitude\n"]
mennonite = ["latitude,longitude\n"]
messianic = ["latitude,longitude\n"]
amish = ["latitude,longitude\n"]
quaker = ["latitude,longitude\n"]
protestant = ["latitude,longitude\n"]

def church_writer(state):
    global baptist
    global methodist
    global presbyterian
    global orthodox
    global episcopal
    global catholic
    global lutheran
    global reformed
    global calvinist
    global pentecostal
    global adventist
    global mennonite
    global messianic
    global amish
    global quaker
    global protestant
    
    file = open(state+"_cleaned.txt", "r")
    entries = file.readlines()
    file.close()
    for entry in entries:
        entry = entry.replace("\n", "")
        parts = entry.split(";")
        lat_long = parts[0].replace(" ", "")
        lat_long = lat_long + "\n"
        if parts[2] == "Baptist":
            baptist.append(lat_long)
        if parts[2] == "Methodist":
            methodist.append(lat_long)
        if parts[2] == "Presbyterian":
            presbyterian.append(lat_long)
        if parts[2] == "Orthodox":
            orthodox.append(lat_long)
        if parts[2] == "Episcopal":
            episcopal.append(lat_long)
        if parts[2] == "Catholic":
            catholic.append(lat_long)
        if parts[2] == "Lutheran":
            lutheran.append(lat_long)
        if parts[2] == "Reformed":
            reformed.append(lat_long)
        if parts[2] == "Calvinist":
            calvinist.append(lat_long)
        if parts[2] == "Pentecostal":
            pentecostal.append(lat_long)
        if parts[2] == "Adventist":
            adventist.append(lat_long)
        if parts[2] == "Mennonite":
            mennonite.append(lat_long)
        if parts[2] == "Messianic Jewish":
            messianic.append(lat_long)
        if parts[2] == "Amish":
            amish.append(lat_long)
        if parts[2] == "Quaker":
            quaker.append(lat_long)
        if parts[2] == "Protestant":
            protestant.append(lat_long)

church_writer("al")
church_writer("ak")
church_writer("ar")
church_writer("az")
church_writer("ca")
church_writer("co")
church_writer("ct")
church_writer("de")
church_writer("fl")
church_writer("ga")
church_writer("hi")
church_writer("ia")
church_writer("id")
church_writer("il")
church_writer("in")
church_writer("ks")
church_writer("ky")
church_writer("la")
church_writer("ma")
church_writer("md")
church_writer("me")
church_writer("mi")
church_writer("mn")
church_writer("mo")
church_writer("ms")
church_writer("mt")
church_writer("nc")
church_writer("nd")
church_writer("ne")
church_writer("nh")
church_writer("nj")
church_writer("nm")
church_writer("nv")
church_writer("ny")
church_writer("oh")
church_writer("ok")
church_writer("or")
church_writer("pa")
church_writer("ri")
church_writer("sc")
church_writer("sd")
church_writer("tn")
church_writer("tx")
church_writer("ut")
church_writer("va")
church_writer("vt")
church_writer("wa")
church_writer("wi")
church_writer("wv")
church_writer("wy")

baptist = baptist[:-1]
methodist = methodist[:-1]
presbyterian = presbyterian[:-1]
orthodox = orthodox[:-1]
episcopal = episcopal[:-1]
catholic = catholic[:-1]
lutheran = lutheran[:-1]
reformed = reformed[:-1]
calvinist = calvinist[:-1]
pentecostal = pentecostal[:-1]
adventist = adventist[:-1]
mennonite = mennonite[:-1]
messianic = messianic[:-1]
amish = amish[:-1]
quaker = quaker[:-1]
protestant = protestant[:-1]

output = open("baptist.csv", "w")
output.writelines(baptist)
output.close()
output = open("methodist.csv", "w")
output.writelines(methodist)
output.close()
output = open("presbyterian.csv", "w")
output.writelines(presbyterian)
output.close()
output = open("orthodox.csv", "w")
output.writelines(orthodox)
output.close()
output = open("episcopal.csv", "w")
output.writelines(episcopal)
output.close()
output = open("catholic.csv", "w")
output.writelines(catholic)
output.close()
output = open("lutheran.csv", "w")
output.writelines(lutheran)
output.close()
output = open("reformed.csv", "w")
output.writelines(reformed)
output.close()
output = open("calvinist.csv", "w")
output.writelines(calvinist)
output.close()
output = open("pentecostal.csv", "w")
output.writelines(pentecostal)
output.close()
output = open("adventist.csv", "w")
output.writelines(adventist)
output.close()
output = open("mennonite.csv", "w")
output.writelines(mennonite)
output.close()
output = open("messianic.csv", "w")
output.writelines(messianic)
output.close()
output = open("amish.csv", "w")
output.writelines(amish)
output.close()
output = open("quaker.csv", "w")
output.writelines(quaker)
output.close()
output = open("protestant.csv", "w")
output.writelines(protestant)
output.close()
