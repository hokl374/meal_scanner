# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:01:51 2018

@author: hokl3
"""

import sys
from PyQt5 import QtGui, uic, QtWidgets, QtCore
from manager import base_manager, listify
import pymysql
import datetime

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
    
    with open('loginGUI.py', 'w+') as fout:
        uic.compileUi('loginGUI.ui', fout)
    
    with open('managerGUI.py', 'w+') as fout:
        uic.compileUi('managerGUI.ui', fout)
    
    with open('createFlightGUI.py', 'w+') as fout:
        uic.compileUi('createFlightGUI.ui', fout)
        
    with open('searchFlightGUI.py', 'w+') as fout:
        uic.compileUi('searchFlightGUI.ui', fout)
    
    from loginGUI import Ui_loginDialog
    from managerGUI import Ui_MainWindow
    from createFlightGUI import Ui_createFlightDialog
    from searchFlightGUI import Ui_searchFlightDialog
    
    mem = {}
    
    class QStandardItemCustom(QtGui.QStandardItem):
        #Suitable for int, float, datetime, str
        def __init__(self, data = None, itemType = str):
            super().__init__()
            self.itemType = itemType
            from_str_reference = {int:int, str:str, float:float, datetime.datetime: lambda x: datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S')}
            none_repr = {int:0, str:'', float: 0.0, datetime.datetime: datetime.datetime(9999,12,31,23,59,59)}
            self.convert_none = lambda x: x if x != None else none_repr[itemType]
            self.from_string = from_str_reference[itemType]
            if data:
                self.setData(data)
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
        def __init__(self, manager, parent = None):
            self.models = {}
            self.headers = {'flight': ['Flight ID', 'Flight Number', 'Departure Airport', 'Arrival Airport', 'Departure', 'Scheduled Arrival', 'Estimated Arrival', 'Number of Passengers']}
            self.fields = {'flight': ['flight_id','flight_number', 'departure_airport_iata', 'arrival_airport_iata', 'departure_datetime', 'scheduled_arrival_datetime', 'estimated_arrival_datetime','number_passengers']}
            self.itemTypes = {'flight': [int,int,str,str,datetime.datetime,datetime.datetime,datetime.datetime,int]}
            self.changelog = []
            
            super().__init__(parent = parent)
            self.manager = manager
            self.setupUi(self)
            self.setupFlightTable()
            
            self.Flight_CreateButton.clicked.connect(self.openCreateFlightDialog)
            self.Flight_SearchButton.clicked.connect(self.openSearchFlightDialog)
            self.Flight_UpdateButton.clicked.connect(self.updateFlights)
                      
            self.show()
        
        def log_change(self,item):
            self.changelog.append(item)
        
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
            data = self.manager.flight_manager.get_flight_details('*', flight_ids, orderby_text = 'departure_datetime DESC', rows_returned = 200)
            
            for rec in data:
                item = QStandardItemCustom(rec[0],itemType = self.itemTypes['flight'][0])
                item.setEditable(False)
                items = [item]
                for i in range(1,len(rec)):
                    el = rec[i]
                    item = QStandardItemCustom(el, itemType = self.itemTypes['flight'][i])
                    item.setEditable(True)
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
            
            for rec in data:
                item = QStandardItemCustom(rec[0],itemType = self.itemTypes['flight'][0])
                item.setEditable(False)
                items = [item]
                for i in range(1,len(rec)):
                    el = rec[i]
                    item = QStandardItemCustom(el, itemType = self.itemTypes['flight'][i])
                    item.setEditable(True)
                    items.append(item)
                self.models['flight'].appendRow(items)
            
            self.Flight_Table.setModel(self.models['flight'])
            
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
            
    class createFlightDialog(QtWidgets.QDialog, Ui_createFlightDialog):
        def __init__(self,parent = None):
            super().__init__(parent = parent)
            self.openNewUi()

        
        def openNewUi(self):
            self.setupUi(self)
            
            self.buttonBox.accepted.connect(self.upload_flight)
            
            self.show()
        
        def upload_flight(self):
            params = {'flight_number': self.flightNumberLineEdit.text(), 'departure_airport_iata': self.departureAirportLineEdit.text(), 'arrival_airport_iata': self.arrivalAirportLineEdit.text(),\
                      'departure_datetime': self.departureDateTimeEdit.dateTime().toPyDateTime(),'scheduled_arrival_datetime': self.scheduledArrivalDateTimeEdit.dateTime().toPyDateTime(), 'estimated_arrival_datetime': self.estimatedArrivalDateTimeEdit.dateTime().toPyDateTime(),\
                      'number_passengers': self.numberOfPassengersSpinBox.value()}
            
            try:
                record_id = self.parent().manager.flight_manager.create_flight(**params)
                QtWidgets.QMessageBox.information(self, 'Record Added', "Added flight record! Flight ID = " + str(record_id))
            
            except Exception as ex:
                QtWidgets.QMessageBox.warning(self, 'Error', ex.__str__())
    
    
    class searchFlightDialog(QtWidgets.QDialog, Ui_searchFlightDialog):
        savedParams = {'flight_id':None,'flight_number': None, 'departure_airport_iata': None, 'arrival_airport_iata': None,'departure_datetime': None,\
                      'scheduled_arrival_datetime': None, 'estimated_arrival_datetime': None,'number_passengers': None}
        savedFields = {'flight_id':0,'flight_number': 0, 'departure_airport_iata': 0, 'arrival_airport_iata': 0,'departure_datetime': 0,\
                      'scheduled_arrival_datetime': 0, 'estimated_arrival_datetime': 0,'number_passengers': 0}
        
        def __init__(self,parent = None):
            super().__init__(parent = parent)
            self.setupUi(self)
            
            checkBoxes = {'flight_id': self.flightIdCheckBox, 'flight_number': self.flightNumberCheckBox, 'departure_airport_iata': self.departureAirportCheckBox, 'arrival_airport_iata': self.arrivalAirportLabelCheckBox,\
                      'departure_datetime': self.departureDateTimeCheckBox, 'scheduled_arrival_datetime': self.scheduledArrivalCheckBox,\
                      'estimated_arrival_datetime': self.estimatedArrivalCheckBox, 'number_passengers': self.numberOfPassengersCheckBox}
            
            for f,v in self.savedFields.items():
                checkBoxes[f].setCheckState(v)
            
            self.buttonBox.accepted.connect(self.search_flight)
            
            self.show()
            return
        
        def search_flight(self):
            params = {'flight_id':self.flightIdLineEdit.text(),'flight_number': self.flightNumberLineEdit.text(), 'departure_airport_iata': self.departureAirportLineEdit.text(), 'arrival_airport_iata': self.arrivalAirportLineEdit.text(),\
                      'departure_datetime': (self.departureDateTimeEdit.dateTime().toPyDateTime(),self.departureDateTimeEdit_2.dateTime().toPyDateTime()),\
                      'scheduled_arrival_datetime': (self.scheduledArrivalDateTimeEdit.dateTime().toPyDateTime(),self.scheduledArrivalDateTimeEdit_2.dateTime().toPyDateTime()),\
                      'estimated_arrival_datetime': (self.estimatedArrivalDateTimeEdit.dateTime().toPyDateTime(), self.estimatedArrivalDateTimeEdit_2.dateTime().toPyDateTime()),\
                      'number_passengers': (self.numberOfPassengersSpinBox.value(),self.numberOfPassengersSpinBox_2.value())}
            
            fields = {'flight_id': self.flightIdCheckBox.checkState(), 'flight_number': self.flightNumberCheckBox.checkState(), 'departure_airport_iata': self.departureAirportCheckBox.checkState(), 'arrival_airport_iata': self.arrivalAirportLabelCheckBox.checkState(),\
                      'departure_datetime': self.departureDateTimeCheckBox.checkState(), 'scheduled_arrival_datetime': self.scheduledArrivalCheckBox.checkState(),\
                      'estimated_arrival_datetime': self.estimatedArrivalCheckBox.checkState(), 'number_passengers': self.numberOfPassengersCheckBox.checkState()}
            
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
                    flight_ids = self.parent().manager.flight_manager.get_flight_ids(orderby_text = 'departure_datetime DESC', rows_returned = 200)
                else:
                    flight_ids = self.parent().manager.flight_manager.get_flight_ids(condition_text = condition_text)
                data = self.parent().manager.flight_manager.get_flight_details('*', flight_ids, orderby_text = 'departure_datetime DESC')
                self.parent().updateFlightTable(data)
            except Exception as ex:
                QtWidgets.QMessageBox.warning(self, 'Error', ex.__str__())
                
            #Remember to save current search fields and parameters
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
                #NEED TO LAUNCH NEXT SECTION
                #self.close()
            except pymysql.MySQLError as ex:
                #NEED TO HANDLE THIS
                QtWidgets.QMessageBox.warning(self, 'Error', 'Bad user, password or connection')
                
            except Exception as ex:
                print(ex.__str__)
    
        def quitProgram(self):
            self.close()
            


        
    loginUI = LoginMain()
    loginUI.show()
    sys.exit(app.exec_())