# Xuất một database thành file Json
def exportDatabaseToJson(db_name, couch_server):
    import json
    try :
        db = couch_server[db_name]
        list = []
        for item in db:
            a = db.get(item)
            list.append(a)

        jsonFile = open("data.json", "w")
        for item in list:
            jsonString = json.dumps(item)
            jsonFile.write(jsonString)
            jsonFile.write('\n')
        jsonFile.close()
        return "Xuất file thành công !"
    except :
        return "Xuất file thất bại !"