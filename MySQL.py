import pymysql
import time


class MySQL_db:
    def __init__(self, n):
        self.n = n
        'MySQL DB init part'
        self.db = pymysql.connect(host="localhost", user="python", passwd="", database="testowa")
        self.cursor = self.db.cursor()

        self.insert_time = 0
        self.select_time = 0
        self.update_time = 0
        self.delete_time = 0

        'CRUD part'
        self.__select()

        'INSERT instuction'
        # self.__insert()
        # self.retrieve = "INSERT INTO `dawki` (`idd`, `ile`) VALUES (5, '3x dziennie');"
        # self.cursor.execute(self.retrieve)

        # rows = self.cursor.fetchall()
        # for row in rows:
        #     print(row)


    def __select(self):
        begin = time.perf_counter()
        for i in range(0, self.n):
            self.retrieve = "SELECT * FROM pacjenci"
            self.cursor.execute(self.retrieve)
        end = time.perf_counter()
        self.select_time = end - begin
        print(f"SELECT run {self.n} times in loop end after {self.select_time:0.4f} seconds")

    def __insert(self):
        begin = time.perf_counter()
        pesel = 97090605938
        value = 0
        gabinet = 1
        for i in range(0, self.n):
            print(value)
            value = value + 14  # because of last key
            gabinet = gabinet + 1
            pesel = pesel + 1
            self.retrieve = "INSERT INTO `doktorzy` (`idd`, `imie`, `nazwisko`, `pesel`, `telefon`, `gabinet`, `godziny`) VALUES (%s, 'Dawid', 'Mrosek', %s, '290010010', %s, 'poranne');"
            self.cursor.execute(self.retrieve, (value, pesel, gabinet))
        end = time.perf_counter()
        self.insert_time = end - begin
        print(f"INSERT run {self.n} times in loop end after {self.insert_time:0.4f} seconds")


def main():
    test_val1 = MySQL_db(100)


if __name__ == "__main__":
    main()
