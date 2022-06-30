# Tạo một database với các document từ một file json
def insert_fileJson (_couch_server, _name_file, _database_name) :
    import json
    couch_server=_couch_server
    name_file=_name_file
    database_name=_database_name
    # Nếu databse chưa có thì tiến hành tạo mới
    try:
        db = couch_server[database_name]
    except:
        db = couch_server.create(database_name)

    # đọc từ dòng trong file và import vào database
    try :
        with open(name_file, "r") as jsonfile:
            for row in jsonfile:
                db_entry = json.loads(row)
                db.save(db_entry)
            return "Thành công !"
    except :
        return "Không thành công !"

# Thêm một document vào một database
def insert_Document (_couch_server, _database_name, _doc) :
    couch_server=_couch_server
    database_name=_database_name
    doc=_doc
    # Nếu database chưa có thì tiến hành tạo
    try:
        db = couch_server[database_name]
    except:
        db = couch_server.create(database_name)
    try :
        db.save(doc)
        return "Thêm thành công !"
    except :
        return "Thêm thất bại !"
# update một field của một document
def update_field (_couch_server, _database_name,_id_doc, _field_name, _new_value) :
    couch_server=_couch_server
    database_name=_database_name
    field_name=_field_name
    new_value=_new_value
    id_doc=_id_doc

    try :
        db=couch_server[database_name]
        doc=db.get(id_doc)
        doc[field_name]=new_value
        db.save(doc)
        return "Update thành công !"
    except :
        return "Uodate thất bại !"

# update một field của tất cả các document
def update_all_fields (_couch_server, _database_name, _field_name, _new_value) :
    couch_server = _couch_server
    database_name = _database_name
    field_name = _field_name
    new_value = _new_value
    try :
        db=couch_server[database_name]
        for id_doc in db:
            doc=db.get(id_doc)
            doc[field_name]=new_value
            db.save(doc)
        return "Update thành công !"
    except :
        return "Update thất bại !"

## Xóa một database theo tên
def del_database (_couch_server, _database_name) :
    couchdb_server=_couch_server
    database_name=_database_name

    try :
        del couchdb_server[database_name]
        return "Xóa thành công !"
    except :
        return "Xóa thất bại !"

## Xóa một document theo id
def del_document (_couch_server, _database_name, _id_doc) :
    couchdb_server=_couch_server
    database_name=_database_name
    id_doc=_id_doc

    try :
        db=couchdb_server[database_name]
        db.delete(db[id_doc])
        return " Xóa thành công !"
    except :
        return "Xóa thất bại !"
