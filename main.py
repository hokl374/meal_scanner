# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:01:51 2018

@author: hokl3
"""

import sys
from PyQt5 import QtGui, uic, QtWidgets, QtCore
from manager import base_manager
import pymysql
import datetime
import csv

#if __name__ == "__main__":
#    app = QtWidgets.QApplication(sys.argv)
#    loginUI = uic.loadUi('login.ui')
#    
#    mem = []
#    def create_manager():
#        #manager =  = base_manager(loginUI.usernameLineEdit.text,loginUI.passwordLineEdit.text)
#        mem.append(base_manager("siauser1","password"))
#        
#    def close(self):
#        self.close()
#        
#    loginUI.close = close
#    
#    loginUI.buttonBox.accepted.connect(create_manager)
#    loginUI.buttonBox.rejected.connect(loginUI.close)
#    loginUI.show()
#    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
#    guiModules = [('loginGUI.py','loginGUI.ui'), ('managerGUI.py', 'managerGUI.ui'), ('createFlightGUI.py', 'createFlightGUI.ui'),('searchFlightGUI.py','searchFlightGUI.ui')]
    
#    with open('loginGUI.py', 'w+') as fout:
#        uic.compileUi('loginGUI.ui', fout)
#    
#    with open('managerGUI.py', 'w+') as fout:
#        uic.compileUi('managerGUI.ui', fout)
#    
#    with open('createFlightGUI.py', 'w+') as fout:
#        uic.compileUi('createFlightGUI.ui', fout)
#        
#    with open('searchFlightGUI.py', 'w+') as fout:
#        uic.compileUi('searchFlightGUI.ui', fout)
#    
#    with open('createMealScheduleGUI.py','w+') as fout:
#        uic.compileUi('createMealScheduleGUI.ui', fout)
#
#    with open('searchMealScheduleGUI.py','w+') as fout:
#        uic.compileUi('searchMealScheduleGUI.ui', fout)
#        
#    with open('createMealOptionGUI.py','w+') as fout:
#        uic.compileUi('createMealOptionGUI.ui', fout)
#
#    with open('searchMealOptionGUI.py','w+') as fout:
#        uic.compileUi('searchMealOptionGUI.ui', fout)
#    
    
    from loginGUI import Ui_loginDialog
    from managerGUI import Ui_MainWindow
    from createFlightGUI import Ui_createFlightDialog
    from searchFlightGUI import Ui_searchFlightDialog
    from createMealScheduleGUI import Ui_createMealScheduleDialog
    from searchMealScheduleGUI import Ui_searchMealScheduleDialog
    from createMealOptionGUI import Ui_createMealOptionDialog
    from searchMealOptionGUI import Ui_searchMealOptionDialog
    
    mem = {}
    
    class QStandardItemCustom(QtGui.QStandardItem):
        #Suitable for int, float, datetime, str
        def __init__(self, data = None, itemType = str, colourRange = None):
            #colourRange takes a tuple/list of 2 numbers (a,b). From a to between a & b to b --> Red, Yellow, Green
            super().__init__()
            self.itemType = itemType
            from_str_reference = {int:int, str:str, float:float, datetime.datetime: lambda x: datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S')}
            none_repr = {int:0, str:'', float: 0.0, datetime.datetime: datetime.datetime(9999,12,31,23,59,59)}
            self.convert_none = lambda x: x if x != None else none_repr[itemType]
            self.from_string = from_str_reference[itemType]
            if data:
                self.setData(data)
            if colourRange:
                a,b = colourRange
                redBrush,yellowBrush,greenBrush = QtGui.QBrush(QtGui.QColor(255,107,107)),QtGui.QBrush(QtGui.QColor(255,234,128)),QtGui.QBrush(QtGui.QColor(77,255,77))
                clean_data = self.convert_none(data)
                if a<=b:
                    if clean_data<a:
                        self.setData(redBrush,QtCore.Qt.BackgroundRole)
                    elif clean_data<b:
                        self.setData(yellowBrush,QtCore.Qt.BackgroundRole)
                    else:
                        self.setData(greenBrush,QtCore.Qt.BackgroundRole)
                else:
                    if clean_data>a:
                        self.setData(redBrush,QtCore.Qt.BackgroundRole)
                    elif clean_data>b:
                        self.setData(yellowBrush,QtCore.Qt.BackgroundRole)
                    else:
                        self.setData(greenBrush,QtCore.Qt.BackgroundRole)
            return
        
        def data(self, role = QtCore.Qt.UserRole+1):
            if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
                return str(self.data())
            else:
                return super().data(role)
        
        def setData(self, data, role = QtCore.Qt.UserRole+1):
            data = self.from_string(data) if type(data) == str else data
            if role == QtCore.Qt.EditRole:
                super().setData(data)
            else:          
                super().setData(data,role)
            
        def __lt__(self,other):
            self_data = self.convert_none(self.data())
            other_data = self.convert_none(other.data())
            return self_data < other_data

        

    class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        
        ## MAIN WINDOW METHODS ##
        def __init__(self, manager, parent = None):
            self.models = {}
            self.headers = {'flight': ['Flight ID', 'Flight Number', 'Departure Airport', 'Arrival Airport', 'Departure Date/Time', 'Arrival Date/Time', 'Total Passengers', 'Passengers: First', 'Passengers: Business', 'Passengers: Economy','% Wastage'],\
                            'schedule': ['Meal ID', 'Flight ID','Booking Class','Meal Type','Service Order','Time Served', '% Wastage'],\
                            'option': ['Option ID', 'Meal ID', 'Option Code', 'Option Name', 'Weight (g)', 'Colour', 'Units Uplifted', 'Units Leftover', '% Wastage']}
            self.fields = {'flight': ['flight_id','flight_number', 'departure_airport_iata', 'arrival_airport_iata', 'departure_datetime', 'arrival_datetime', 'number_passengers_economy + number_passengers_first + number_passengers_business','number_passengers_first','number_passengers_business','number_passengers_economy'],\
                           'schedule':['meal_id','flight_id','booking_class','meal_type','service_order','time_served'],\
                           'option': ['option_id', 'meal_id', 'option_code', 'option_name', 'weight', 'colour', 'units_uplifted','units_leftover','ROUND(units_leftover/units_uplifted*100)']}
            self.itemTypes = {'flight': [int,int,str,str,datetime.datetime,datetime.datetime,int,int,int,int,int],\
                              'schedule':[int,int,str,str,int,datetime.datetime,int],\
                              'option': [int,int,str,str,int,str,int,int,int]}
            self.editable = {'flight':[False,True,True,True,True,True,False,True,True,True,False],\
                             'schedule': [False,True,True,True,True,True,False],\
                             'option':[False,True,True,True,True,True,True,True,False]}
            self.colourRange = {'flight':[None]*10 + [(25,10)],\
                                'schedule':[None]*6 + [(25,10)],\
                                'option': [None]*8 + [(25,10)]}
            self.changelog = []
            
            super().__init__(parent = parent)
            self.setupUi(self)
            self.show()
            self.manager = manager
            self.setupFlightTable()
            self.setupScheduleTable()
            self.setupOptionTable()
            
            self.Flight_CreateButton.clicked.connect(self.openCreateFlightDialog)
            self.Flight_SearchButton.clicked.connect(self.openSearchFlightDialog)
            self.Flight_RefreshButton.clicked.connect(self.refreshFlightTable)
            self.Flight_UpdateButton.clicked.connect(self.updateFlights)
            self.scanLeftoversButton.clicked.connect(self.scanLeftovers)
            self.Flight_ViewMealScheduleButton.clicked.connect(self.viewMealSchedule)
            self.MealSchedule_CreateButton.clicked.connect(self.openCreateScheduleDialog)
            self.MealSchedule_SearchButton.clicked.connect(self.openSearchScheduleDialog)
            self.MealSchedule_RefreshButton.clicked.connect(self.refreshScheduleTable)
            self.MealSchedule_UpdateButton.clicked.connect(self.updateSchedule)
            self.MealSchedule_ViewMealOptionButton.clicked.connect(self.viewMealOption)
            self.MealOption_CreateButton.clicked.connect(self.openCreateOptionDialog)
            self.MealOption_SearchButton.clicked.connect(self.openSearchOptionDialog)
            self.MealOption_RefreshButton.clicked.connect(self.refreshOptionTable)
            self.MealOption_UpdateButton.clicked.connect(self.updateOption)
        
        def log_change(self,item):
            self.changelog.append(item)
        
        ## FLIGHT MANAGER METHODS ##
        
        def openCreateFlightDialog(self):
            if 'createflightdialog' not in mem:
                mem['createflightdialog'] = createFlightDialog(parent = self)
            else:
                mem['createflightdialog'].openNewUi()
        
        def openSearchFlightDialog(self):
            if 'searchflightdialog' not in mem:
                mem['searchflightdialog'] = searchFlightDialog(parent = self)
            else:
                mem['searchflightdialog'].show()
        
        def setupFlightTable(self):
            flightModel = QtGui.QStandardItemModel()
            flightModel.setHorizontalHeaderLabels(self.headers['flight'])
            
            flight_ids = self.manager.flight_manager.get_flight_ids(orderby_text = 'departure_datetime DESC', rows_returned = 200)
            data = self.manager.flight_manager.get_flight_details(self.fields['flight'][1:], flight_ids, orderby_text = 'departure_datetime DESC', rows_returned = 200)
            
            sql = 'SELECT ROUND(SUM(meals.leftover)/SUM(meals.uplift)*100) FROM flight LEFT JOIN (SELECT meal_schedule.meal_id, meal_schedule.flight_id, SUM(meal_options.units_uplifted) AS uplift, SUM(meal_options.units_leftover) AS leftover FROM meal_schedule LEFT JOIN meal_options ON meal_schedule.meal_id = meal_options.meal_id GROUP BY meal_schedule.meal_id) AS meals ON flight.flight_id = meals.flight_id\
                    WHERE flight.flight_id <=> %s GROUP BY flight.flight_id'
            
            with self.manager.db_connector.connection.cursor() as cursor:
                for rec in data:
                    rec = list(rec)
                    cursor.execute(sql%str(rec[0]))
                    wastage = cursor.fetchone()[0]
                    rec.append(wastage)
                    items = []
                    for i in range(len(rec)):
                        el = rec[i]
                        item = QStandardItemCustom(el, itemType = self.itemTypes['flight'][i], colourRange = self.colourRange['flight'][i])
                        item.setEditable(self.editable['flight'][i])
                        items.append(item)
                    
                    flightModel.appendRow(items)
            
            def update_data(item):
                self.log_change(item)
            
            
            flightModel.itemChanged.connect(update_data)
            
            flightProxyModel = QtCore.QSortFilterProxyModel()
            flightProxyModel.setSourceModel(flightModel)
            
            self.Flight_Table.setModel(flightModel)
            self.Flight_Table.setSortingEnabled(True)
            self.models['flight'] = flightModel
                
            return
        
        def updateFlightTable(self,data):
            self.models['flight'].removeRows(0,self.models['flight'].rowCount())  
            sql = 'SELECT ROUND(SUM(meals.leftover)/SUM(meals.uplift)*100) FROM flight LEFT JOIN (SELECT meal_schedule.meal_id, meal_schedule.flight_id, SUM(meal_options.units_uplifted) AS uplift, SUM(meal_options.units_leftover) AS leftover FROM meal_schedule LEFT JOIN meal_options ON meal_schedule.meal_id = meal_options.meal_id GROUP BY meal_schedule.meal_id) AS meals ON flight.flight_id = meals.flight_id\
            WHERE flight.flight_id <=> %s GROUP BY flight.flight_id'
            with self.manager.db_connector.connection.cursor() as cursor:
                for rec in data:
                    rec = list(rec)
                    cursor.execute(sql%str(rec[0]))
                    wastage = cursor.fetchone()[0]
                    rec.append(wastage)
                    items = []
                    for i in range(len(rec)):
                        el = rec[i]
                        item = QStandardItemCustom(el, itemType = self.itemTypes['flight'][i], colourRange = self.colourRange['flight'][i])
                        item.setEditable(self.editable['flight'][i])
                        items.append(item)
                    
                    self.models['flight'].appendRow(items)
            
            self.Flight_Table.setModel(self.models['flight'])
            
            return
        
        def refreshFlightTable(self):
            flight_ids = self.manager.flight_manager.get_flight_ids(rows_returned = 200)
            if flight_ids == []:
                data = []
            else:
                data = self.manager.flight_manager.get_flight_details(self.fields['flight'][1:], flight_ids, orderby_text = 'flight_id DESC')
            self.updateFlightTable(data)
            return
            
        
        def updateFlights(self):
            flightModel = self.models['flight']
            itemsChanged = list(filter(lambda x: x.model() == flightModel,self.changelog))
            while itemsChanged:
                el = itemsChanged[0]
                elrow= el.row()
                sameid = list(filter(lambda x: x.row() == elrow, itemsChanged[1:]))
                fields,values = [self.fields['flight'][el.column()]], [el.data()]
                for r in sameid:
                    f,v = self.fields['flight'][r.column()], r.data()
                    if f not in fields:
                        fields.append(f)
                        values.append(v)
                flight_id = flightModel.item(elrow,column = 0).data()
                self.manager.flight_manager.edit_flight_from_ids(flight_id,fields,values)
                for x in sameid:
                    itemsChanged.remove(x)
                itemsChanged.remove(el)
            QtWidgets.QMessageBox.information(self, 'Updated Flights', "Successfully updated flight records!")
            return
        
        def scanLeftovers(self):
            select = self.Flight_Table.selectionModel()
            selectedRows = select.selectedRows()
            if len(selectedRows) != 1:
                QtWidgets.QMessageBox.information(self, 'Scan Leftovers', "Please select one flight to scan!")
                return
            
            flight_id = selectedRows[0].data()
            meal_ids = self.manager.meal_schedule_manager.get_meal_ids_from_flight_id(flight_id)
            
            QtWidgets.QMessageBox.information(self, 'Scan Leftovers', "Start scanning when video appears.\nPlease press \'Q\' when complete.")
            unknownOptions = self.manager.meal_option_manager.scan_leftovers(meal_ids)
            if unknownOptions == None:
                newOptions, errors = None, None
            else:
                newOptions, errors =  unknownOptions.newOptions, unknownOptions.errors
            
            if newOptions or errors:
                QtWidgets.QMessageBox.warning(self, 'Errors Detected!', "Errors in uploading some leftovers! Please view erroneous meal options in \"errorlog.csv\"")
                with open('errorlog.csv', 'a' ,newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames = ['meal_option_code', 'units_leftover', 'error_type', str(datetime.datetime.now())], dialect = csv.excel)
                    writer.writeheader()
                    for code,val in newOptions:
                        writer.writerow({'meal_option_code': code, 'units_leftover': val})
                    for code,val,error in errors:
                        writer.writerow({'meal_option_code': code, 'units_leftover': val, 'error_type':error})
            else:
                QtWidgets.QMessageBox.information(self, 'Done!', "All leftovers successfully uploaded!")
            return
        
        def viewMealSchedule(self):
            select = self.Flight_Table.selectionModel()
            selectedRows = select.selectedRows()
            
            if len(selectedRows) < 1:
                QtWidgets.QMessageBox.information(self, 'View Meal Schedule', "Please select at least one flight to view!")
                return
            flight_ids = list(map(lambda x: x.data(), selectedRows))
            meal_ids = []
            for flight_id in flight_ids:
                meal_ids.extend(self.manager.meal_schedule_manager.get_meal_ids_from_flight_id(flight_id))
            if meal_ids == []:
                QtWidgets.QMessageBox.warning(self, 'No records found!', 'No records found!')
            else:
                data = self.manager.meal_schedule_manager.get_meal_details(self.fields['schedule'][1:], meal_ids, orderby_text = 'meal_id DESC')
                self.updateScheduleTable(data)
                self.tabWidget.setCurrentIndex(1)
            return
        
        ## MEAL SCHEDULE MANAGER METHODS ##
        def openCreateScheduleDialog(self):
            if 'createscheduledialog' not in mem:
                mem['createscheduledialog'] = createScheduleDialog(parent = self)
            else:
                mem['createscheduledialog'].openNewUi()
        
        def openSearchScheduleDialog(self):
            if 'searchscheduledialog' not in mem:
                mem['searchscheduledialog'] = searchScheduleDialog(parent = self)
            else:
                mem['searchscheduledialog'].show()
        
        
        def setupScheduleTable(self):
            scheduleModel = QtGui.QStandardItemModel()
            scheduleModel.setHorizontalHeaderLabels(self.headers['schedule'])
            
            meal_ids = self.manager.meal_schedule_manager.get_meal_ids(rows_returned = 200)
            data = self.manager.meal_schedule_manager.get_meal_details(self.fields['schedule'][1:], meal_ids, orderby_text = 'meal_id DESC', rows_returned = 200)
            
            sql = 'SELECT ROUND(SUM(meal_options.units_leftover)/SUM(meal_options.units_uplifted)*100) FROM meal_schedule LEFT JOIN meal_options ON meal_schedule.meal_id = meal_options.meal_id WHERE meal_schedule.meal_id = %s GROUP BY meal_schedule.meal_id'
            
            with self.manager.db_connector.connection.cursor() as cursor:
                for rec in data:
                    rec = list(rec)
                    cursor.execute(sql%str(rec[0]))
                    wastage = cursor.fetchone()[0]
                    rec.append(wastage)
                    items = []
                    for i in range(len(rec)):
                        el = rec[i]
                        item = QStandardItemCustom(el, itemType = self.itemTypes['schedule'][i], colourRange = self.colourRange['schedule'][i])
                        item.setEditable(self.editable['schedule'][i])
                        items.append(item)
                    scheduleModel.appendRow(items)
            
            def update_data(item):
                self.log_change(item)
            
            
            scheduleModel.itemChanged.connect(update_data)
            
            scheduleProxyModel = QtCore.QSortFilterProxyModel()
            scheduleProxyModel.setSourceModel(scheduleModel)
            
            self.MealSchedule_Table.setModel(scheduleModel)
            self.MealSchedule_Table.setSortingEnabled(True)
            self.models['schedule'] = scheduleModel
            return
        
        def updateScheduleTable(self,data):
            self.models['schedule'].removeRows(0,self.models['schedule'].rowCount())
            sql = 'SELECT ROUND(SUM(meal_options.units_leftover)/SUM(meal_options.units_uplifted)*100) FROM meal_schedule LEFT JOIN meal_options ON meal_schedule.meal_id = meal_options.meal_id WHERE meal_schedule.meal_id = %s GROUP BY meal_schedule.meal_id'
            with self.manager.db_connector.connection.cursor() as cursor:
                for rec in data:
                    rec = list(rec)
                    cursor.execute(sql%str(rec[0]))
                    wastage = cursor.fetchone()[0]
                    rec.append(wastage)
                    items = []
                    for i in range(len(rec)):
                        el = rec[i]
                        item = QStandardItemCustom(el, itemType = self.itemTypes['schedule'][i], colourRange = self.colourRange['schedule'][i])
                        item.setEditable(self.editable['schedule'][i])
                        items.append(item)
                    self.models['schedule'].appendRow(items)

            self.MealSchedule_Table.setModel(self.models['schedule'])
            
            return
        
        def refreshScheduleTable(self):
            meal_ids = self.manager.meal_schedule_manager.get_meal_ids(rows_returned = 200)
            if meal_ids == []:
                data = []
            else:
                data = self.manager.meal_schedule_manager.get_meal_details(self.fields['schedule'][1:], meal_ids, orderby_text = 'meal_id DESC')
            self.updateScheduleTable(data)
            return
        
        def updateSchedule(self):
            scheduleModel = self.models['schedule']
            itemsChanged = list(filter(lambda x: x.model() == scheduleModel,self.changelog))
            while itemsChanged:
                el = itemsChanged[0]
                elrow= el.row()
                sameid = list(filter(lambda x: x.row() == elrow, itemsChanged[1:]))
                fields,values = [self.fields['schedule'][el.column()]], [el.data()]
                for r in sameid:
                    f,v = self.fields['schedule'][r.column()], r.data()
                    if f not in fields:
                        fields.append(f)
                        values.append(v)
                meal_id = scheduleModel.item(elrow,column = 0).data()
                self.manager.meal_schedule_manager.edit_meal_from_ids(meal_id,fields,values)
                for x in sameid:
                    itemsChanged.remove(x)
                itemsChanged.remove(el)
            QtWidgets.QMessageBox.information(self, 'Updated Meal Schedule', "Successfully updated meal schedule records!")
            return
        
        def viewMealOption(self):
            select = self.MealSchedule_Table.selectionModel()
            selectedRows = select.selectedRows()
            if len(selectedRows) < 1:
                QtWidgets.QMessageBox.information(self, 'View Meal Option', "Please select at least meal to view!")
                return
            meal_ids = list(map(lambda x: x.data(), selectedRows))
            option_ids = []
            for meal_id in meal_ids:
                option_ids.extend(self.manager.meal_option_manager.get_meal_option_ids_from_meal_ids(meal_id))
            
            if option_ids == []:
                QtWidgets.QMessageBox.warning(self, 'No records found!', 'No records found!')
            else:
                data = self.manager.meal_option_manager.get_meal_option_details(self.fields['option'][1:], option_ids, orderby_text = 'option_id DESC')
                self.updateOptionTable(data)
                self.tabWidget.setCurrentIndex(2)
            return
        
        ## MEAL OPTION MANAGER METHODS ##
        def openCreateOptionDialog(self):
            if 'createoptiondialog' not in mem:
                mem['createoptiondialog'] = createOptionDialog(parent = self)
            else:
                mem['createoptiondialog'].openNewUi()
        
        def openSearchOptionDialog(self):
            if 'searchoptiondialog' not in mem:
                mem['searchoptiondialog'] = searchOptionDialog(parent = self)
            else:
                mem['searchoptiondialog'].show()
        
        
        def setupOptionTable(self):
            optionModel = QtGui.QStandardItemModel()
            optionModel.setHorizontalHeaderLabels(self.headers['option'])
            
            option_ids = self.manager.meal_option_manager.get_meal_option_ids(rows_returned = 200)
            data = self.manager.meal_option_manager.get_meal_option_details(self.fields['option'][1:], option_ids, orderby_text = 'option_id DESC', rows_returned = 200)
            
            for rec in data:
                items = []
                for i in range(len(rec)):
                    el = rec[i]
                    item = QStandardItemCustom(el, itemType = self.itemTypes['option'][i], colourRange = self.colourRange['option'][i])
                    item.setEditable(self.editable['option'][i])
                    items.append(item)
                optionModel.appendRow(items)
            
            def update_data(item):
                self.log_change(item)
            
            
            optionModel.itemChanged.connect(update_data)
            
            optionProxyModel = QtCore.QSortFilterProxyModel()
            optionProxyModel.setSourceModel(optionModel)
            
            self.MealOption_Table.setModel(optionModel)
            self.MealOption_Table.setSortingEnabled(True)
            self.models['option'] = optionModel
            return
        
        def updateOptionTable(self,data):
            self.models['option'].removeRows(0,self.models['option'].rowCount())
            
            for rec in data:
                items = []
                for i in range(len(rec)):
                    el = rec[i]
                    item = QStandardItemCustom(el, itemType = self.itemTypes['option'][i], colourRange = self.colourRange['option'][i])
                    item.setEditable(self.editable['option'][i])
                    items.append(item)
                self.models['option'].appendRow(items)
            
            self.MealOption_Table.setModel(self.models['option'])
            
            return
        
        def refreshOptionTable(self):
            option_ids = self.manager.meal_option_manager.get_meal_option_ids(rows_returned = 200)
            if option_ids == []:
                data = []
            else:
                data = self.manager.meal_option_manager.get_meal_option_details(self.fields['option'][1:], option_ids, orderby_text = 'option_id DESC')
            self.updateOptionTable(data)
            return
        
        def updateOption(self):
            optionModel = self.models['option']
            itemsChanged = list(filter(lambda x: x.model() == optionModel,self.changelog))
            while itemsChanged:
                el = itemsChanged[0]
                elrow= el.row()
                sameid = list(filter(lambda x: x.row() == elrow, itemsChanged[1:]))
                fields,values = [self.fields['option'][el.column()]], [el.data()]
                for r in sameid:
                    f,v = self.fields['option'][r.column()], r.data()
                    if f not in fields:
                        fields.append(f)
                        values.append(v)
                option_id = optionModel.item(elrow,column = 0).data()
                self.manager.meal_option_manager.edit_meal_option_from_ids(option_id,fields,values)
                for x in sameid:
                    itemsChanged.remove(x)
                itemsChanged.remove(el)
            QtWidgets.QMessageBox.information(self, 'Updated Meal Options', "Successfully updated meal option records!")
            return
            

    ## INHERITED CLASSES FOR FLIGHT DIALOGS ##
    class createFlightDialog(QtWidgets.QDialog, Ui_createFlightDialog):
        def __init__(self,parent = None):
            super().__init__(parent = parent)
            self.openNewUi()

        
        def openNewUi(self):
            self.setupUi(self)
            
            self.buttonBox.accepted.connect(self.upload_flight)
            self.autoFillButton.clicked.connect(self.populate_fields)
            
            self.show()
        
        def populate_fields(self):
            
            flight_details = self.parent().manager.flight_manager.get_api_flight_details(self.departureAirportLineEdit.text(),self.arrivalAirportLineEdit.text(),self.departureDateTimeEdit.dateTime().toPyDateTime().date())
            if flight_details == None:
                QtWidgets.QMessageBox.information(self, 'Information Unavailable!', 'Flight information not available for requested flight!')
            else:
                self.flightNumberLineEdit.setText(str(flight_details['flightNumber']))
                self.departureDateTimeEdit.setDateTime(flight_details['actualDepartureTime'])
                self.arrivalDateTimeEdit.setDateTime(flight_details['actualArrivalTime'])
            
            passenger_stats = self.parent().manager.flight_manager.get_api_passenger_statistics(self.flightNumberLineEdit.text(),self.departureDateTimeEdit.dateTime().toPyDateTime().date())
            if passenger_stats == None:
                QtWidgets.QMessageBox.information(self, 'Information Unavailable!', 'Passenger statistics not available for requested flight!')
            else:
                self.passengersEconomySpinBox.setValue(passenger_stats['Economy']['checkin'])
                self.passengersBusinessSpinBox.setValue(passenger_stats['Business']['checkin'])
                self.passengersFirstSpinBox.setValue(passenger_stats['First']['checkin'])
            
            return
        
        def upload_flight(self):
            params = {'flight_number': self.flightNumberLineEdit.text(), 'departure_airport_iata': self.departureAirportLineEdit.text(), 'arrival_airport_iata': self.arrivalAirportLineEdit.text(),\
                      'departure_datetime': self.departureDateTimeEdit.dateTime().toPyDateTime(),'arrival_datetime': self.arrivalDateTimeEdit.dateTime().toPyDateTime(), 
                      'number_passengers_economy': self.passengersEconomySpinBox.value(), 'number_passengers_business': self.passengersBusinessSpinBox.value(), 'number_passengers_first': self.passengersFirstSpinBox.value()}
            
            try:
                record_id = self.parent().manager.flight_manager.create_flight(**params)
                self.parent().refreshFlightTable()
                QtWidgets.QMessageBox.information(self, 'Record Added', "Added flight record! Flight ID = " + str(record_id) + ". Click OK to fetch information on meals...")
                
                data = self.parent().manager.meal_option_manager.get_api_meal_options(record_id)
                if data == None:
                    QtWidgets.QMessageBox.information(self, 'No Meals Found', "No meals found for Flight ID = " + str(record_id) + ".")
                else:
                    self.parent().manager.meal_option_manager.initial_upload_meal_options(record_id,data)              
                    QtWidgets.QMessageBox.information(self, 'Meals Added', "Added meals for Flight ID = " + str(record_id) + ".")
                    self.parent().refreshScheduleTable()
                    self.parent().refreshOptionTable()

            except Exception as ex:
                QtWidgets.QMessageBox.warning(self, 'Error', ex.__str__())
    
    class searchFlightDialog(QtWidgets.QDialog, Ui_searchFlightDialog):
#        savedParams = {'flight_id':None,'flight_number': None, 'departure_airport_iata': None, 'arrival_airport_iata': None,'departure_datetime': None,\
#                      'scheduled_arrival_datetime': None, 'estimated_arrival_datetime': None,'number_passengers': None}
#        savedFields = {'flight_id':0,'flight_number': 0, 'departure_airport_iata': 0, 'arrival_airport_iata': 0,'departure_datetime': 0,\
#                      'scheduled_arrival_datetime': 0, 'estimated_arrival_datetime': 0,'number_passengers': 0}
        
        def __init__(self,parent = None):
            super().__init__(parent = parent)
            self.setupUi(self)
            
#            checkBoxes = {'flight_id': self.flightIdCheckBox, 'flight_number': self.flightNumberCheckBox, 'departure_airport_iata': self.departureAirportCheckBox, 'arrival_airport_iata': self.arrivalAirportLabelCheckBox,\
#                      'departure_datetime': self.departureDateTimeCheckBox, 'arrival_datetime': self.arrivalCheckBox,\
#                      'number_passengers_economy': self.passengersEconomyCheckBox, 'number_passengers_business': self.passengersBusinessCheckBox, 'number_passengers_first': self.passengersFirstCheckBox}
            
#            for f,v in self.savedFields.items():
#                checkBoxes[f].setCheckState(v)
            
            self.buttonBox.accepted.connect(self.search_flight)
            
            self.show()
            return
        
        def search_flight(self):
            params = {'flight_id':self.flightIdLineEdit.text(),'flight_number': self.flightNumberLineEdit.text(), 'departure_airport_iata': self.departureAirportLineEdit.text(), 'arrival_airport_iata': self.arrivalAirportLineEdit.text(),\
                      'departure_datetime': (self.departureDateTimeEdit.dateTime().toPyDateTime(),self.departureDateTimeEdit_2.dateTime().toPyDateTime()),\
                      'arrival_datetime': (self.arrivalDateTimeEdit.dateTime().toPyDateTime(),self.arrivalDateTimeEdit_2.dateTime().toPyDateTime()),\
                      'number_passengers_economy': (self.passengersEconomySpinBox.value(),self.passengersEconomySpinBox_2.value()),'number_passengers_business': (self.passengersBusinessSpinBox.value(),self.passengersBusinessSpinBox_2.value()),\
                      'number_passengers_first': (self.passengersFirstSpinBox.value(),self.passengersFirstSpinBox_2.value())}
            
            fields = {'flight_id': self.flightIdCheckBox.checkState(), 'flight_number': self.flightNumberCheckBox.checkState(), 'departure_airport_iata': self.departureAirportCheckBox.checkState(), 'arrival_airport_iata': self.arrivalAirportLabelCheckBox.checkState(),\
                      'departure_datetime': self.departureDateTimeCheckBox.checkState(), 'arrival_datetime': self.arrivalCheckBox.checkState(),\
                      'number_passengers_economy': self.passengersEconomyCheckBox.checkState(), 'number_passengers_business': self.passengersBusinessCheckBox.checkState(), 'number_passengers_first': self.passengersFirstCheckBox.checkState()}
            
            #checkState() returns 2 if checkbox is selected, returns 0 if not selected
            
            searchFields = list(map(lambda x: x[0], filter(lambda x: x[1] == 2, fields.items())))
            
            condition_text = ''
            for field in searchFields:
                search_param = params[field]
                condition_text += '('
                if type(search_param) == tuple:
                    condition_text += field + ' BETWEEN \'' + str(search_param[0]) + '\' AND \'' + str(search_param[1]) + '\''
                else:
                    condition_text += field + ' = \'' + str(search_param) + '\''
                condition_text += ') AND '
            condition_text = condition_text[:-5]
            
            try:
                if searchFields == []:
                    flight_ids = self.parent().manager.flight_manager.get_flight_ids(orderby_text = 'flight_id DESC', rows_returned = 200)
                else:
                    flight_ids = self.parent().manager.flight_manager.get_flight_ids(condition_text = condition_text)
                
                if flight_ids == []:
                    QtWidgets.QMessageBox.warning(self, 'No records found!', 'No records found!')
                else:
                    data = self.parent().manager.flight_manager.get_flight_details(self.parent().fields['flight'][1:], flight_ids, orderby_text = 'flight_id DESC')
                    self.parent().updateFlightTable(data)
            except Exception as ex:
                QtWidgets.QMessageBox.warning(self, 'Error', ex.__str__())
                
            return


    ## INHERITED CLASSES FOR SCHEDULE DIALOGS ##    
    class createScheduleDialog(QtWidgets.QDialog, Ui_createMealScheduleDialog):
        def __init__(self,parent = None):
            super().__init__(parent = parent)
            self.openNewUi()

        
        def openNewUi(self):
            self.setupUi(self)
            
            self.buttonBox.accepted.connect(self.upload_schedule)
            
            self.show()
        
        def upload_schedule(self):
            params = {'flight_id': self.flightIdLineEdit.text(), 'booking_class': self.classComboBox.currentText(), 'meal_type': self.mealTypeComboBox.currentText(),\
                      'time_served': self.timeServedDateTimeEdit.dateTime().toPyDateTime(), 'service_order': self.serviceOrderSpinBox.value()}
            
            try:
                record_id = self.parent().manager.meal_schedule_manager.create_meal(**params)
                QtWidgets.QMessageBox.information(self, 'Record Added', "Added meal schedule record! Meal ID = " + str(record_id))
                self.parent().refreshScheduleTable()
            except Exception as ex:
                QtWidgets.QMessageBox.warning(self, 'Error', ex.__str__())
    
    
    class searchScheduleDialog(QtWidgets.QDialog, Ui_searchMealScheduleDialog):
        
        def __init__(self,parent = None):
            super().__init__(parent = parent)
            self.setupUi(self)
            
            self.buttonBox.accepted.connect(self.search_schedule)
            
            self.show()
            return
        
        def search_schedule(self):
            params = {'flight_id':self.flightIdLineEdit.text(),'meal_id': self.mealIdLineEdit.text(), 'meal_type': self.mealTypeComboBox.currentText(),\
                      'time_served': (self.timeServedDateTimeEdit.dateTime().toPyDateTime(),self.timeServedDateTimeEdit_2.dateTime().toPyDateTime())}
            
            fields = {'flight_id': self.flightIdCheckBox.checkState(), 'meal_id': self.mealIdCheckBox.checkState(), 'meal_type': self.mealTypeCheckBox.checkState(), 'time_served': self.timeServedCheckBox.checkState()}
            
            #checkState() returns 2 if checkbox is selected, returns 0 if not selected
            
            searchFields = list(map(lambda x: x[0], filter(lambda x: x[1] == 2, fields.items())))
            
            condition_text = ''
            for field in searchFields:
                search_param = params[field]
                condition_text += '('
                if type(search_param) == tuple:
                    condition_text += field + ' BETWEEN \'' + str(search_param[0]) + '\' AND \'' + str(search_param[1]) + '\''
                else:
                    condition_text += field + ' = \'' + str(search_param) + '\''
                condition_text += ') AND '
            condition_text = condition_text[:-5]
            
            try:
                if searchFields == []:
                    meal_ids = self.parent().manager.meal_schedule_manager.get_meal_ids(rows_returned = 200)
                else:
                    meal_ids = self.parent().manager.meal_schedule_manager.get_meal_ids(condition_text = condition_text)
                
                if meal_ids == []:
                    QtWidgets.QMessageBox.warning(self, 'No records found!', 'No records found!')
                else:
                    data = self.parent().manager.meal_schedule_manager.get_meal_details(self.parent().fields['schedule'][1:], meal_ids, orderby_text = 'meal_id DESC')
                    self.parent().updateScheduleTable(data)
            except Exception as ex:
                QtWidgets.QMessageBox.warning(self, 'Error', ex.__str__())
                
            return
        
    
    ## INHERITED CLASSES FOR OPTION DIALOGS ##    
    class createOptionDialog(QtWidgets.QDialog, Ui_createMealOptionDialog):
        def __init__(self,parent = None):
            super().__init__(parent = parent)
            self.openNewUi()
        
        def openNewUi(self):
            self.setupUi(self)
            
            self.buttonBox.accepted.connect(self.upload_option)
            
            self.show()
        
        def upload_option(self):
            params = {'meal_id': self.mealIdLineEdit.text(), 'option_name': self.optionNameLineEdit.text(), 'option_code': self.optionCodeLineEdit.text(),\
                      'weight': self.weightSpinBox.value(), 'colour': self.colourLineEdit.text(), 'units_uplifted': self.unitsUpliftedSpinBox.value(), 'units_leftover': self.unitsLeftoverSpinBox.value() if self.unitsLeftoverCheckBox.checkState() == 2 else None}
            
            try:
                record_id = self.parent().manager.meal_option_manager.create_meal_option(**params)
                QtWidgets.QMessageBox.information(self, 'Record Added', "Added meal option record! Option ID = " + str(record_id))
                self.parent().refreshScheduleTable()
            except Exception as ex:
                QtWidgets.QMessageBox.warning(self, 'Error', ex.__str__())
    
    
    class searchOptionDialog(QtWidgets.QDialog, Ui_searchMealOptionDialog):
        
        def __init__(self,parent = None):
            super().__init__(parent = parent)
            self.setupUi(self)
            
            self.buttonBox.accepted.connect(self.search_options)
            
            self.show()
            return
        
        def search_options(self):
            params = {'meal_id':self.mealIdLineEdit.text(),'option_name': self.optionNameLineEdit.text(), 'option_code': self.optionCodeLineEdit.text(),\
                      'colour':self.colourLineEdit.text(), 'weight': (self.weightSpinBox.value(),self.weightSpinBox_2.value()),\
                      'units_uplifted': (self.unitsUpliftedSpinBox.value(),self.unitsUpliftedSpinBox_2.value()),\
                      'units_leftover': (self.unitsLeftoverSpinBox.value(),self.unitsLeftoverSpinBox_2.value()),\
                      'units_leftover/units_uplifted': (self.wastageSpinBox.value()/100,self.wastageSpinBox_2.value()/100)}
            
            fields = {'meal_id': self.mealIdCheckBox.checkState(), 'option_name': self.optionNameCheckBox.checkState(), 'option_code': self.optionCodeCheckBox.checkState(), 'colour': self.colourCheckBox.checkState(),\
                      'weight': self.weightCheckBox.checkState(), 'units_uplifted': self.unitsUpliftedCheckBox.checkState(), 'units_leftover': self.unitsLeftoverCheckBox.checkState(), 'units_leftover/units_uplifted': self.wastageCheckBox.checkState()}
            
            #checkState() returns 2 if checkbox is selected, returns 0 if not selected
            
            searchFields = list(map(lambda x: x[0], filter(lambda x: x[1] == 2, fields.items())))
            
            condition_text = ''
            for field in searchFields:
                search_param = params[field]
                condition_text += '('
                if type(search_param) == tuple:
                    condition_text += field + ' BETWEEN \'' + str(search_param[0]) + '\' AND \'' + str(search_param[1]) + '\''
                else:
                    condition_text += field + ' = \'' + str(search_param) + '\''
                condition_text += ') AND '
            condition_text = condition_text[:-5]
            
            try:
                if searchFields == []:
                    option_ids = self.parent().manager.meal_option_manager.get_meal_option_ids(rows_returned = 200)
                else:
                    option_ids = self.parent().manager.meal_option_manager.get_meal_option_ids(condition_text = condition_text)
                
                if option_ids == []:
                    QtWidgets.QMessageBox.warning(self, 'No records found!', 'No records found!')
                else:
                    data = self.parent().manager.meal_option_manager.get_meal_option_details(self.parent().fields['option'][1:], option_ids, orderby_text = 'option_id DESC')
                    self.parent().updateOptionTable(data)
            except Exception as ex:
                QtWidgets.QMessageBox.warning(self, 'Error', ex.__str__())
                
            return
    
    
    class LoginMain(QtWidgets.QDialog, Ui_loginDialog):
        def __init__(self, parent=None):
            super().__init__(parent=parent)
            self.setupUi(self)
            self.buttonBox.accepted.connect(self.create_manager)
            self.buttonBox.rejected.connect(self.quitProgram)
    
        def create_manager(self):
            try:
                mem['manager'] = base_manager(self.usernameLineEdit.text(),self.passwordLineEdit.text())
                mem['mainwindow'] = MainWindow(mem['manager'])
                
            except pymysql.MySQLError as ex:
                QtWidgets.QMessageBox.warning(self, 'Error', 'Bad user, password or connection')

            except Exception as ex:
                QtWidgets.QMessageBox.warning(self, 'Error', 'Unknown Exception:' + ex.__str__())
    
        def quitProgram(self):
            self.close()
            


        
    loginUI = LoginMain()
    loginUI.show()
    sys.exit(app.exec_())