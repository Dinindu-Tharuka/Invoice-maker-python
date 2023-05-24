from PyQt5.QtCore import Qt, QSortFilterProxyModel, QAbstractListModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton, QComboBox, QTableWidget, QLineEdit, QLabel
from PyQt5 import uic, QtGui
import sys
# from invoice_pdf import Invoice
import sqlite3
from pathlib import Path
from data.data import prices, companies, products, customers

address = """
BILLING TO:
Client Name:
Street Avenue 0000
Maimi, FL
"""


class InvoiceMaker(QMainWindow):

    # Invoice Maker Data
    product_type = ''
    product = ''
    unit_price = 0
    item_count = 0
    row_total = 0
    payment = 0
    customer_name = ''
    customer_address = ''

    # Table
    row_count = 0

    def __init__(self):
        super(InvoiceMaker, self).__init__()
        uic.loadUi("invoice_maker.ui", self)

        # title
        self.setWindowTitle("Invoice Maker")
        self.setWindowIcon(QtGui.QIcon('bill.png'))

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
        self.button_add.clicked.connect(self.add)

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

        self.get_data()
        
        self.tableWidget.setColumnCount(4)
        self.set_column_width()

        self.tableWidget.setHorizontalHeaderLabels(
            ['PRODUCT', 'PRICE', 'QTY', 'TOTAL'])

        # Add table data
        self.row_count += 1
        self.tableWidget.setRowCount(self.row_count)
        self.tableWidget.setItem((self.row_count-1), 0, QTableWidgetItem(self.product))
        self.tableWidget.setItem((self.row_count-1), 1, QTableWidgetItem(self.unit_price))
        self.tableWidget.setItem((self.row_count-1), 2, QTableWidgetItem(self.item_count))
        self.tableWidget.setItem((self.row_count-1), 3, QTableWidgetItem(self.row_total))
        

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


    def delete():
        pass

    def clear_all(self):
        pass

    def add(self):
        pass


app = QApplication(sys.argv)
ui_window = InvoiceMaker()
app.exec_()
