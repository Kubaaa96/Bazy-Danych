import time
import rethinkdb as r


class Rethink_db:
    def __init__(self, n):
        'RethinkDB init part'
        self.n = n
        self.rdb = r.RethinkDB()
        self.rdb.connect('localhost', 28015).repl()
        self.insert_time = 0
        self.select_time = 0
        self.update_time = 0
        self.delete_time = 0
        # self.rdb.db_create('clinic_rethink').run()
        # self.drop_tables()
        'Table init part'
        'CREATE instuction'
        begin = time.perf_counter()
        self.rdb.db("clinic_rethink").table_create("pacjenci").run()
        self.rdb.db("clinic_rethink").table_create("doktorzy").run()
        self.rdb.db("clinic_rethink").table_create("wizyty").run()
        self.rdb.db("clinic_rethink").table_create("dawki_i_leki").run()
        self.rdb.db("clinic_rethink").table_create("dok_i_spec").run()
        self.rdb.db("clinic_rethink").table_create("leki").run()
        self.rdb.db("clinic_rethink").table_create("dawki").run()
        self.rdb.db("clinic_rethink").table_create("specjalizacje").run()
        self.rdb.db("clinic_rethink").table_create("wiz_i_dawki_i_leki").run()

        end = time.perf_counter()
        print(f"CREATE run in loop end after {end - begin:0.4f} seconds")

        'CRUD part'
        self.insert("pacjenci")
        self.select("pacjenci")
        self.update_table("pacjenci")
        self.delete_from_table("pacjenci")
        self.drop_tables()

    def insert(self, table: str):
        begin = time.perf_counter()
        for i in range(1, self.n + 1):
            self.rdb.db("clinic_rethink").table(table).insert(
                [{
                    'idp':            i,
                    'imie':           'Dawid',
                    'nazwisko':       'Mrosek',
                    'pesel':          '97090605938',
                    'plec':           'Mężczyzna',
                    'data_urodzenia': '1997-09-06',
                    'adres':          'Pilsudskiego 2121',
                    'telefon':        '123'
                }]
            ).run()

        # self.rdb.db("clinic_rethink").table('pacjenci').insert([
        # {'idp': 1,'imie': 'Dawid', 'nazwisko': 'Mrosek', 'pesel': '97090605938', 'plec': 'Mężczyzna', 'data_urodzenia': '1997-09-06', 'adres': 'Pilsudskiego 2121', 'telefon': '123'}
        # ]).run()

        end = time.perf_counter()
        self.insert_time = end - begin
        print(f"INSERT run {self.n} times in loop end after {self.insert_time:0.4f} seconds")

    def select(self, table: str):
        begin = time.perf_counter()
        for i in range(1, self.n + 1):
            self.rdb.db("clinic_rethink").table(table).run()
        end = time.perf_counter()
        self.select_time = end - begin
        print(f"SELECT run {self.n} times in loop end after {self.select_time:0.4f} seconds")

    def update_table(self, table: str):
        begin = time.perf_counter()
        number = 123
        for i in range(0, self.n):
            number = number + 1
            self.rdb.db("clinic_rethink").table('pacjenci').update({"telefon": "number"}).run()
        end = time.perf_counter()
        self.update_time = end - begin
        print(f"UPDATE run {self.n} times in loop end after {self.update_time:0.4f} seconds")

    def delete_from_table(self, table: str):
        if self.rdb.db("clinic_rethink").table(table).is_empty().run():
            print("Empty")
        begin = time.perf_counter()
        self.rdb.db('clinic_rethink').table(table).delete().run()
        end = time.perf_counter()
        self.delete_time = end - begin
        print(f"DELETE run {self.n} times in loop end after {self.delete_time:0.4f} seconds")

    def drop_tables(self):
        self.rdb.db('clinic_rethink').table_drop('pacjenci').run()
        self.rdb.db('clinic_rethink').table_drop('doktorzy').run()
        self.rdb.db('clinic_rethink').table_drop('wizyty').run()

        self.rdb.db('clinic_rethink').table_drop('dawki_i_leki').run()
        self.rdb.db('clinic_rethink').table_drop('dok_i_spec').run()
        self.rdb.db('clinic_rethink').table_drop('leki').run()

        self.rdb.db('clinic_rethink').table_drop('dawki').run()
        self.rdb.db('clinic_rethink').table_drop('specjalizacje').run()
        self.rdb.db('clinic_rethink').table_drop('wiz_i_dawki_i_leki').run()


def main():
    test_val3 = Rethink_db(100)

if __name__ == "__main__":
    main()
