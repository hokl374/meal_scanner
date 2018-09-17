# -*- coding: utf-8 -*-
"""
Flight Manager, Meal Scheduler, Meal Option Scanner
"""

from db_connector import db_connector
from meal_scanner import meal_scanner

def listify(item):
    if type(item) == list:
        return item
    elif type(item) == tuple:
        return list(item)
    else:
        return [item]

class base_manager:
    
    def __init__(self, user, password):
        #Launch various maangers, initiate connector
        self.db_connector = db_connector(user,password)
        self.flight_manager = flight_manager(self.db_connector)
        self.meal_schedule_manager = meal_schedule_manager(self.db_connector, self.flight_manager)
        self.meal_option_manager = meal_option_manager(self.db_connector, self.flight_manager, self.meal_schedule_manager)
        return


class flight_manager:
    
    def __init__(self, db_connector):
        self.db_connector = db_connector
    
    def create_flight(self,flight_number,departure_airport_iata,arrival_airport_iata,departure_datetime,scheduled_arrival_datetime,\
                      estimated_arrival_datetime, number_passengers = None):
        fields = ("flight_number", "departure_airport_iata", "arrival_airport_iata", "departure_datetime", \
                  "scheduled_arrival_datetime", "estimated_arrival_datetime", "number_passengers")
        
        values = (flight_number,departure_airport_iata,arrival_airport_iata,departure_datetime,scheduled_arrival_datetime,\
                      estimated_arrival_datetime, number_passengers)
        
        record_id = self.db_connector.create_single_record("flight",fields,values)
        print("Added flight record! Flight ID = " + str(record_id))
        return record_id
    
    def edit_flight_from_ids(self,flight_id,fields,values): #Add input fields
        
        flight_id = listify(flight_id)
        fields = listify(fields)
        values = listify(values)
        values = list(map(listify, values))
        
        num_rows_updated = self.db_connector.edit_records_from_id('flight', 'flight_id', flight_id,fields,values)
        print("Successfully updated!" if num_rows_updated == 1 else "No rows updated!")
        return num_rows_updated
    
    def get_flight_ids(self, condition_text = None, orderby_text = None, rows_returned = None):
        result = self.db_connector.read_records('flight',['flight_id'],condition_text, orderby_text, rows_returned)
        return list(map(lambda x: x[0], result))
    
    #Build get_flight_ids from flight number and departure time
    
    def get_flight_details(self, get_fields, flight_ids, orderby_text = None, rows_returned = None):
        get_fields = ['flight_id'] + listify(get_fields) if get_fields != '*' else listify(get_fields)
        flight_ids = listify(flight_ids)
        
        flight_ids = list(map(lambda x: str(x), flight_ids))
        condition_text = ",".join(flight_ids)
        
        result = self.db_connector.read_records('flight', get_fields, 'flight_id IN (' + condition_text +")", orderby_text, rows_returned)
        return list(result)


class meal_schedule_manager:
    
    def __init__(self, db_connector, flight_manager):
        self.db_connector = db_connector
        self.flight_manager = flight_manager
    
    def create_meal(self,flight_id,meal_type,time_served = None):
        fields = ("flight_id", "meal_type", "time_served")
        
        values = (flight_id,meal_type,time_served)
        
        record_id = self.db_connector.create_single_record("meal_schedule",fields,values)
        print("Added meal schedule record! Meal ID = " + str(record_id))
        return record_id
    
    def edit_meal(self,meal_id,fields,values):
        meal_id = listify(meal_id)
        fields = listify(fields)
        values = listify(values)
        
        num_rows_updated = self.db_connector.edit_records_from_id('meal_schedule', 'meal_id', meal_id,fields,values)
        print("Successfully updated!" if num_rows_updated == 1 else "No rows updated!")
        return
    
    def get_meal_ids(self, condition_text):
        result = self.db_connector.read_records('meal_schedule',['meal_id'],condition_text)
        return list(map(lambda x: x[0], result))
    
    def get_meal_ids_from_flight_id(self, flight_id):
        return self.get_meal_ids("flight_id = %s" % str(flight_id))
    
    def get_meal_details(self,get_fields,meal_ids):
        get_fields = ['meal_id'] + listify(get_fields)
        meal_ids = listify(meal_ids)
        
        meal_ids = list(map(lambda x: str(x), meal_ids))
        condition_text = ",".join(meal_ids)
        
        result = self.db_connector.read_records('meal_schedule', get_fields, 'meal_id IN (' + condition_text +")")
        return list(result)
    

class meal_option_manager:
    
    def __init__(self, db_connector, flight_manager, meal_schedule_manager):
        self.db_connector = db_connector
        self.flight_manager = flight_manager
        self.meal_schedule_manager = meal_schedule_manager
    
    def create_meal_option(self,meal_id,option_choice, option_name = None,units_uplifted = None,units_leftover = None,option_description = None):
        #option_choice refers to number of people who opt for this option
        fields = ("meal_id", "option_name", "option_description", "option_choice", "units_uplifted", "units_leftover")
        
        values = (meal_id, option_name, option_description, option_choice, units_uplifted, units_leftover)
        
        record_id = self.db_connector.create_single_record("meal_options",fields,values)
        print("Added meal schedule record! Meal Option ID = " + str(record_id))
        return record_id
    
    def edit_meal_option(self,option_id,fields,values):
        option_id = listify(option_id)
        fields = listify(fields)
        values = listify(values)
        
        num_rows_updated = self.db_connector.edit_records_from_id('meal_options', 'option_id', option_id,fields,values)
        print("Successfully updated!" if num_rows_updated == 1 else "No rows updated!")
        return
    
    def get_meal_option_ids(self,condition_text):
        result = self.db_connector.read_records('meal_options',['option_id'],condition_text)
        return list(map(lambda x: x[0], result))
    
    def get_meal_option_ids_from_meal_id(self,meal_id):
        return self.get_meal_option_ids("meal_id = %s" % str(meal_id))
    
    def get_meal_option_details(self,get_fields,option_ids):
        get_fields = ['option_id'] + listify(get_fields)
        option_ids = listify(option_ids)
        
        option_ids = list(map(lambda x: str(x), option_ids))
        condition_text = ",".join(option_ids)
        
        result = self.db_connector.read_records('meal_options', get_fields, 'option_id IN (' + condition_text +")")
        return list(result)
    
    
    def upload_leftovers(self, records, meal_id):
        tabulator = {}
        
        for x in records:
                meal_type = x[-2:-1]
                meal_option_type = int(x[-1:])
                
                if meal_type not in tabulator:
                    tabulator[meal_type] = {}
                
                if meal_option_type in tabulator[meal_type]:
                    tabulator[meal_type][meal_option_type] += 1
                else:
                    tabulator[meal_type][meal_option_type] = 1
                
        #INSERT VALUES FROM TABULATOR INTO MYSQL DATABASE
        #Check if value is already in database
        meal_type = self.meal_schedule_manager.get_meal_details('meal_type',meal_id)[0][1]
        meal_options_from_db = self.get_meal_option_ids_from_meal_id(meal_id)
        
        if meal_options_from_db == []:
            listMealOptions = []
        else:
            listMealOptions = self.get_meal_option_details(["option_choice","units_leftover"],meal_options_from_db)
        listMealOptionsChoice = set(map(lambda x: x[1], listMealOptions))
        
        newOptions = list(filter(lambda x: x[0] not in listMealOptionsChoice, tabulator[meal_type].items()))
        oldOptions = list(filter(lambda x: x[0] in listMealOptionsChoice, tabulator[meal_type].items()))
        
        errors = []
        
        #Add into database
        for opt,val in newOptions:
            try:
                self.create_meal_option(meal_id, opt, units_leftover = val)
            except Exception as ex:
                errors.append((meal_type + str(opt),val, type(ex).__name__))
        
        for opt,val in oldOptions:
            try:
                firstMatchingOption = list(filter(lambda x: x[1] == opt, listMealOptions))[0]
                opt_id = firstMatchingOption[0]
                val += firstMatchingOption[2]
                self.edit_meal_option(opt_id,"units_leftover",val)
            except Exception as ex:
                errors.append((meal_type + str(opt),val, type(ex).__name__))
        
        del tabulator[meal_type]
        
        #Throw as errors for meal_type != meal_type for given meal_id
        for meal_type, option_dict in tabulator.items():
            for k,v in option_dict.items():
                errors.append((meal_type + str(k), v, "Wrong meal_type"))
        
        
        if errors:
            print("Errors in uploading values!")
            print(errors)
            return
        else:
            print("Success!")
            return
                
    def manual_add_leftovers(self, meal_id = None):
        i = 1
        records = []
        
        if meal_id == None:
            meal_id = int(input("Please enter meal id: "))
        
        print("Type \"complete\" after scanning is complete. \n Please start scanning: \n")
        
        while True:

            x = input("Record %s: " % str(i))
            
            if x == "complete":
                break
            else:
                records.append(x)
            
            i += 1
        
        return self.upload_leftovers(records, meal_id)
    
    def scan_leftovers(self, meal_id = None):
        if meal_id == None:
            meal_id = int(input("Please enter meal id: "))
        
        scanner = meal_scanner()
        records = scanner.scan_codes()
        
        return self.upload_leftovers(records,meal_id)

    
    
    
    
    
    