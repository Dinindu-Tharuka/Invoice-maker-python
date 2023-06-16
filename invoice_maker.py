from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton, QComboBox, QTableWidget, QLineEdit, QLabel
from PyQt5 import uic, QtGui
import sys

# from invoice_pdf import Invoice
import sqlite3
from pathlib import Path
from data.data import prices, companies, products, customers

# importiing invoice maker
from invoice_pdf import Invoice;

address = """
BILLING TO:
Client Name:
Street Avenue 0000
Maimi, FL
"""


class InvoiceMaker(QMainWindow):  

    
    # Table
    row_count = 0   

    # Database 
    INSERT_DATA_INTO_DATABASE = 'INSERT'
    GET_ALL_DATA_FROM_DATABASE = 'FETCH_ALL'
    DELETE_ALL_DATA = 'DELETE_ALL'
    DELETE_SELECTED_DATA = 'DELETE_SELECTED'

    def __init__(self):
        super(InvoiceMaker, self).__init__()
        uic.loadUi("invoice_maker.ui", self)

        # title
        self.setWindowTitle("Invoice Maker")
        self.setWindowIcon(QtGui.QIcon('bill.png'))           

        # Invoice Maker Data
        self.product_type = ''
        self.product = ''
        self.unit_price = 0
        self.item_count = 0
        self.row_total = 0
        self.payment = 0
        self.customer_name = ''
        self.customer_address = ''

        # Function Calling
        self.initial_set_data()
        self.set_product()               

        self.show()

    def initial_set_data(self):
        self.lineEdit_unit_price.setPlaceholderText("Unit Price")
        self.payment_input_box.setPlaceholderText("Payment")
        self.lineEdit_customer.setPlaceholderText("Customer Name")

        # ComboBox
        self.comboBox_product_type.addItems(companies())
        self.comboBox_product.addItems(products(type=companies()[0]))
        self.lineEdit_unit_price.setText(str(prices(0)))
        self.comboBox_unit_count.addItems([str(x) for x in range(1, 11)])

        # Connect ComboBox
        self.comboBox_product_type.activated.connect(self.set_product)        
        self.comboBox_product.activated.connect(self.set_unit_price)
        self.comboBox_unit_count.activated.connect(self.calculate_row_total)

        # Connect Push Buttons
        self.button_add.clicked.connect(self.create_table)
        self.button_delete.clicked.connect(self.delete)
        self.button_clear_all.clicked.connect(self.clear_all)        
        self.button_print.clicked.connect(self.make_pdf)
        self.button_clear_all.clicked.connect(self.clear_all)

        # Initialize 
        self.payment_input_box : QLineEdit
        self.button_delete: QPushButton
        self.comboBox_product_type: QComboBox
        self.comboBox_unit_count: QComboBox
        self.lineEdit_unit_price: QLineEdit
        self.comboBox_product: QComboBox
        self.tableWidget: QTableWidget
        self.label_selected_total : QLabel
        self.button_add : QPushButton 
        self.button_print : QPushButton  
        self.button_clear_all : QPushButton 

        # Getting all data from database
        self.initiate_table()
        
        
        

        

    def set_product(self):
        company: list = companies()
        index = company.index(self.comboBox_product_type.currentText())       

        # Set Product to Combo Box
        self.comboBox_product.clear()
        self.comboBox_product.addItems(products(type=companies()[index]))

        # Set Unit Price
        self.lineEdit_unit_price.setText(f'{prices(index)}')

        # call Row total
        self.calculate_row_total()

    def initiate_table(self):
        items = self.database(self.GET_ALL_DATA_FROM_DATABASE) 
        
        print(f'database items {items}')
        if len(items) > 0:

            # create the initial table
            for item in items:
                self.first_time = True
                self.product = item[1]                     
                self.unit_price = item[2]               
                self.item_count = item[3]     
                self.row_total = item[2] * item[3]
                self.create_table()
        else:
            self.first_time = False
        

    def set_unit_price(self):
        index = products(product_name=self.comboBox_product.currentText())         
        self.lineEdit_unit_price.setText(str(prices(index)))
        self.calculate_row_total()

    def calculate_row_total(self):
        self.unit_price = float(self.lineEdit_unit_price.text())
        self.item_count = int(self.comboBox_unit_count.currentText())        
        self.row_total = self.unit_price * self.item_count        
        self.label_selected_total.setText(str(self.row_total))

    def create_table(self):       
        
        self.tableWidget.setColumnCount(4)
        self.set_column_width()

        self.tableWidget.setHorizontalHeaderLabels(
            ['PRODUCT', 'PRICE', 'QTY', 'TOTAL'])

        # Add table data
        self.row_count += 1
        self.tableWidget.setRowCount(self.row_count)
        self.tableWidget.setItem((self.row_count-1), 0, QTableWidgetItem(self.product))
        self.tableWidget.setItem((self.row_count-1), 1, QTableWidgetItem(str(self.unit_price)))
        self.tableWidget.setItem((self.row_count-1), 2, QTableWidgetItem(str(self.item_count)))
        self.tableWidget.setItem((self.row_count-1), 3, QTableWidgetItem(str(self.row_total)))

        

        if not self.first_time:
            self.get_data()            
            self.database(self.INSERT_DATA_INTO_DATABASE)            

        self.first_time = False
        

    def set_column_width(self):
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 165)
        self.tableWidget.setColumnWidth(2, 165)
        self.tableWidget.setColumnWidth(3, 165)

    def get_data(self):
        try:
            self.product = self.comboBox_product.currentText()
            self.unit_price = self.lineEdit_unit_price.text()
            self.item_count = self.comboBox_unit_count.currentText()            
            self.payment = self.payment_input_box.text()
            self.row_total = self.label_selected_total.text()
        except:
            print('Value Error')


    def delete(self):
        self.selected_rows = [i.row() for i in self.tableWidget.selectedIndexes() if i.column() == 1]
        print(self.selected_rows)
        self.database(self.DELETE_SELECTED_DATA)
        self.tableWidget.setRowCount(0)
        self.row_count = 0
        self.initiate_table()


        


    def clear_all(self):
         self.row_count = 0
         self.tableWidget.setRowCount(0)
         self.database(self.DELETE_ALL_DATA)

    def make_pdf(self):
        index = self.database(self.GET_ALL_DATA_FROM_DATABASE)
        height = 10 * len(index) + 120
        print(height)
        pdf_document = Invoice("P", "mm", format=(180, height))
        pdf_document.company_details()
        pdf_document.create_table(self.payment)
        pdf_document.create_pdf()
        



    def database(self, command):
        with sqlite3.connect('pdfdata.db') as db:

            cursor = db.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS data(
                              id INTEGER PRIMARY KEY,
                              product TEXT,
                              unit_price INTEGER,
                              item_count INTEGER
            )''')

            if command == self.INSERT_DATA_INTO_DATABASE:
                cursor.execute(F'''INSERT INTO data(
                                  product,
                                  unit_price,
                                  item_count) 
                                  VALUES(
                                        '{self.product}',
                                        {self.unit_price},
                                        {self.item_count}
                                  )''')
                db.commit()
            elif command == self.GET_ALL_DATA_FROM_DATABASE:
                files = cursor.execute('''SELECT * FROM data''')
                return files.fetchall()
            
            elif command == self.DELETE_ALL_DATA:
                cursor.execute('DELETE FROM data')
                db.commit()
            elif command == self.DELETE_SELECTED_DATA:
                row_indexes = self.selected_rows
                ids = cursor.execute('SELECT id FROM data').fetchall()
                print(ids)
                for index in row_indexes:
                    cursor.execute(f'DELETE FROM data WHERE id={ids[index][0]}')
                db.commit()

    
        



app = QApplication(sys.argv)
ui_window = InvoiceMaker()
app.exec_()
