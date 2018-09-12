# -*- coding: utf-8 -*-
"""
mySQL Connection Scripts

#Placeholder Details [TO BE REMOVED]:
user_name = "siauser1"
password = "password"


"""
host_path = "db4free.net"
db_name = "siayond"

import pymysql
import pymysql.cursors

class db_connector:
    
    def __init__(self, user_name, password):
        # Connect to the database
        self.connection = pymysql.connect(host=host_path,
                             user=user_name,
                             password=password,
                             db=db_name,
                             port = 3306,
                             charset='utf8mb4',
                             #cursorclass=pymysql.cursors.DictCursor
                             )
        
    def create_single_record(self,table,fields,values):
        
        #Input Validation
        if len(fields) != len(values):
            raise ValueError ("Length of fields and values are different!")
            return
        
        #Execute mySQL
        with self.connection.cursor() as cursor:
            field_text = "(" + ", ".join(fields) + ")"
            values_text = "(" + ("%s," * len(values))[:-1] + ")"
            
            sql = ("INSERT INTO %s " % table ) + field_text +  " VALUES " + values_text
            cursor.execute(sql, values)
        self.connection.commit()
        
        with self.connection.cursor() as cursor:
            sql = "SELECT LAST_INSERT_ID()"
            cursor.execute(sql)
            return cursor.fetchone()[0]
        
    def create_multiple_records(self,table,fields,values):
        
        #Input Validation
        fields_length = len(fields)
        
        if False in [len(x) == fields_length for x in values]:
            raise ValueError ("Length of fields and values are different!")
            return
        
        #Execute mySQL
        with self.connection.cursor() as cursor:
            
            field_text = "(" + ", ".join(fields) + ")"
            values_text = "(" + ("%s," * len(fields))[:-1] + ")"
            
            sql = ("INSERT INTO %s " % table ) + field_text +  " VALUES " + values_text
            cursor.executemany(sql, values)
        self.connection.commit()
    
    def read_records(self, table, read_fields, condition_text):
        
        with self.connection.cursor() as cursor:
            read_text = ", ".join(read_fields)
            sql = ("SELECT %s " % read_text) + ("FROM %s WHERE (" % table) + condition_text + ")"
            cursor.execute(sql)      
            result = cursor.fetchall()
        
        return result
    
    def edit_records_from_id(self, table, record_id_name, record_ids, fields, *values):
        
        #Values = [[Field1Rec1, Field1Rec2, Field1Rec3...], [Field2Rec1, Field2Rec2, Field2Rec3...]...]
        
        with self.connection.cursor() as cursor:
            
            condition_text = record_id_name + " <=> %s"
            
            update_text = " SET " + "%s = \'%s\'" * len(fields)
            
            new_fields = [[x]*len(values[0]) for x in fields]
            field_value_lst = []
            
            for i in range(len(fields)):
                field_value_lst.append(new_fields[i])
                field_value_lst.append(values[i])
            
            field_value_lst.append(record_ids)
            zipped_inputs = list(zip(*field_value_lst))
            
            sql = "UPDATE " + table + update_text + " WHERE " + condition_text
            rows_updated = 0
            for qry in zipped_inputs:
                rows_updated += cursor.execute(sql%qry)
            
        self.connection.commit()
        
        print(str(rows_updated) + " rows updated!")
        return rows_updated
            
            
            
            
            

        