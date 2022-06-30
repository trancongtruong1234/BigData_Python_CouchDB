# Kết nối với couchdb
def connect (_username,_password) :
    import couchdb
    try:
        username = _username
        password = _password
        host = "127.0.0.1:5984"
        couchdb_server = couchdb.Server('http://' + host)
        couchdb_server.resource.credentials = (username, password)
        return couchdb_server
    except Exception as ex:
        print(str(ex))
        return