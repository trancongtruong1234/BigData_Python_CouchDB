# Truy vấn các document trong một database
def query (_query_str, couchdb_server, _database_name) :
    query_str=_query_str
    database_name=_database_name

    db = couchdb_server[database_name]
    # In ra thông tin các document thỏa mãn điều kiện truy vấn
    for doc in db.find(query_str):
        print(doc)