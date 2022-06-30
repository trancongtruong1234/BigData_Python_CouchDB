import json
import couchdb
import crud
from connect import connect
from query import query
from crud import *
import couchdb.mapping as cmap
from exportDatabase import  exportDatabaseToJson
if __name__ == '__main__':
    ## Tạo kết nối
    user_name="admin"
    password="Admin@123"
    couchdb_connect=connect(user_name,password)
    # print(couchdb_connect)
    # ## Truy vấn
    # query_str = {
    #     "selector": {
    #         "category": {
    #             "$eq": 'SCIENCE'
    #         },
    #         "headline": {
    #             "$regex": ".Cats"
    #         }
    #     }
    # }
    # database_name = "category"
    # query(query_str, couchdb_connect, database_name)

    # # Thêm một file json vào database
    # database_name="category"
    # file_name="News_Category_Dataset_v2.json"
    # result=crud.insert_fileJson(couchdb_connect,file_name,database_name)
    # print (result)

    # ## Thêm một document vào database
    # database_name = "category"
    # doc = {
    #     "category": "CongTruong",
    #     "headline": "The Definition of 'Dad'",
    #     "authors": "Wendy Fontaine, Contributor\nmother, writer, yogini",
    #     "link": "https://www.huffingtonpost.com/entry/the-definition-of-dad_us_5b9d422be4b03a1dcc86041b",
    #     "short_description": "James is the man with whom she and I have been living for more than two years now. No, he is not her father -- not in the biological sense, anyway. But he does the things fathers do. Angie found a word for a person who does things like that. Dad.",
    #     "date": "2013-06-15"
    # }
    # result = insert_Document(couchdb_connect, database_name, doc)
    # print(result)

    # ## Update một field trong document
    # database_name="category"
    # field_name="authors"
    # id_doc="1d39c8bec903e1a659daefa23a000813"
    # new_value="Anh Van"
    # result=update_field(couchdb_connect,database_name,id_doc,field_name,new_value)
    # print (result)

    # # Update một field của tất cả các document
    # database_name="category"
    # field_name="authors"
    # new_value="Cao Anh Van"
    # result=update_all_fields(couchdb_connect,database_name,field_name,new_value)
    # print (result)

    # # Xuất database thành file Json
    # database_name="category"
    # result=exportDatabaseToJson(database_name,couchdb_connect)
    # print(result)

    # # Xóa một document theo id
    # database_name="category"
    # id_doc="1d39c8bec903e1a659daefa23a000813"
    # result=del_document(couchdb_connect,database_name,id_doc)
    # print (result)

    # # Xóa một database theo tên
    # database_name="sinhvien"
    # result=del_database(couchdb_connect,database_name)
    # print(result)