import pymysql
import time

class MySQL_db:
  def __init__(self, n):
    'MySQL DB init part'
    self.db = pymysql.connect(host="localhost", user="root", passwd="", database="testowa")
    self.cursor = self.db.cursor()

    'CRUD part'
    'SELECT instruction'
    begin = time.perf_counter()
    for i in range(0, n):
      self.retrieve = "SELECT * FROM pacjenci"
      self.cursor.execute(self.retrieve)
    end = time.perf_counter()
    print(f"SELECT run {n} times in loop end after {end - begin:0.4f} seconds")

    'INSERT instuction'
    begin = time.perf_counter()
    pesel = 97090605938
    for i in range(0, n):
      value = n + 14 #because of last key
      pesel = pesel + 1
      self.retrieve = "INSERT INTO `doktorzy` (`idd`, `imie`, `nazwisko`, `pesel`, `telefon`, `gabinet`, `godziny`) VALUES (%s, 'Dawid', 'Mrosek', %s, '290010010', 1, 'poranne');"
      self.cursor.execute(self.retrieve, (value, pesel))
    end = time.perf_counter()
    print(f"INSERT run {n} times in loop end after {end - begin:0.4f} seconds")

    #self.retrieve = "INSERT INTO `dawki` (`idd`, `ile`) VALUES (5, '3x dziennie');"
    #self.cursor.execute(self.retrieve)

    rows = self.cursor.fetchall()
    for row in rows:
        print(row)


test_val1 = MySQL_db(100)