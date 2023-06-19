import sqlite3

class Database():

    # Database 
    INSERT_DATA_INTO_DATABASE = 'INSERT'
    GET_ALL_DATA_FROM_DATABASE = 'FETCH_ALL'
    DELETE_ALL_DATA = 'DELETE_ALL'
    DELETE_SELECTED_DATA = 'DELETE_SELECTED'
    
    def read(self, command):
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