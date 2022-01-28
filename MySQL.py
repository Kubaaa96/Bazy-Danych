import pymysql
import time


class MySQL_db:
    def __init__(self, n):
        self.n = n
        print("\nMySQL")
        self.db = pymysql.connect(host="localhost", user="python", passwd="", database="testowa")
        self.cursor = self.db.cursor()

        self.insert_time = 0
        self.select_time = 0
        self.update_time = 0
        self.delete_time = 0

        'CRUD part'
        self.__select()
        self.__insert()
        self.__update()
        self.__delete()

    def __select(self):
        begin = time.perf_counter()
        for i in range(0, self.n):
            self.retrieve = "SELECT * FROM pacjenci"
            self.cursor.execute(self.retrieve)
            result = self.cursor.fetchall()
        self.db.commit()
        end = time.perf_counter()
        self.select_time = end - begin
        print(f"SELECT run {self.n} times in loop end after {self.select_time:0.4f} seconds")

    def __insert(self):
        begin = time.perf_counter()
        pesel = 97090605938
        value = 1
        gabinet = 1
        for i in range(0, self.n):
            value = value + 1  # because of last key
            gabinet = gabinet + 1
            pesel = pesel + 1
            self.retrieve = "INSERT INTO `doktorzy` (`idd`, `imie`, `nazwisko`, `pesel`, `telefon`, `gabinet`, `godziny`) VALUES (%s, 'Dawid', 'Mrosek', %s, '290010010', %s, 'poranne');"
            self.cursor.execute(self.retrieve, (value, pesel, gabinet))
        self.db.commit()
        end = time.perf_counter()
        self.insert_time = end - begin
        print(f"INSERT run {self.n} times in loop end after {self.insert_time:0.4f} seconds")

    def __update(self):
        begin = time.perf_counter()
        value = 1
        for i in range(0, self.n):
            value = value + 1
            self.retrieve = "UPDATE `doktorzy` SET imie = 'Bartek' WHERE idd= %s"
            self.cursor.execute(self.retrieve, value)

        self.db.commit()
        end = time.perf_counter()
        self.update_time = end - begin
        print(f"UPDATE run {self.n} times in loop end after {self.update_time:0.4f} seconds")

    def __delete(self):
        begin = time.perf_counter()
        self.retrieve = "DELETE FROM `doktorzy`"
        self.cursor.execute(self.retrieve)
        self.db.commit()
        end = time.perf_counter()
        self.delete_time = end - begin
        print(f"DELETE run {self.n} times in loop end after {self.delete_time:0.4f} seconds")


def main():
    test_val1 = MySQL_db(1)


if __name__ == "__main__":
    main()
