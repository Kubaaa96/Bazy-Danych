import pymongo
import time

class Mongo_db:
    def __init__(self, n):
        self.n = n
        print('\nMongoDB')
        self.client = pymongo.MongoClient("mongodb://localhost:27017/", connect=False)
        # print(self.client.list_database_names())
        self.db = self.client["clinic_monogo"]

        self.insert_time = 0
        self.select_time = 0
        self.update_time = 0
        self.delete_time = 0

        'Table init part'
        'CREATE instuction'
        begin = time.perf_counter()
        self.pacjenci = self.db["pacjenci"]
        self.doktorzy = self.db["doktorzy"]
        self.wizyty = self.db["wizyty"]
        self.dawki_i_leki = self.db["dawki_i_leki"]
        self.dok_i_spec = self.db["dok_i_spec"]
        self.leki = self.db["leki"]
        self.dawki = self.db["dawki"]
        self.specjalizacje = self.db["specjalizacje"]
        self.wiz_i_dawki_i_leki = self.db["wiz_i_dawki_i_leki"]

        end = time.perf_counter()
        print(f"CREATE run in loop end after {end - begin:0.4f} seconds")

        #mylist = [
        #{'idp': 1,'imie': 'Dawid', 'nazwisko': 'Mrosek', 'pesel': '97090605938', 'plec': 'Mężczyzna', 'data_urodzenia': '1997-09-06', 'adres': 'Pilsudskiego 2121', 'telefon': '123'},
        #{'idp': 2,'imie': 'Dawid', 'nazwisko': 'Mrosek', 'pesel': '97090605938', 'plec': 'Mężczyzna', 'data_urodzenia': '1997-09-06', 'adres': 'Pilsudskiego 2121', 'telefon': '123'}
        #]

        'CRUD part'
        self.insert()
        self.select()
        self.update()
        self.delete()

        self.drop_tables()

    def insert(self):
        begin = time.perf_counter()
        for i in range(1, self.n+1):
            value = [{'idp': " + str(i) + ",'imie': 'Dawid', 'nazwisko': 'Mrosek', 'pesel': '97090605938', 'plec': 'Mężczyzna', 'data_urodzenia': '1997-09-06', 'adres': 'Pilsudskiego 2121', 'telefon': '123'}]
            self.pacjenci.insert_many(value)
            #self.pacjenci.insert_many(mylist)

        end = time.perf_counter()
        self.insert_time = end - begin
        print(f"INSERT run {self.n} times in loop end after {self.insert_time:0.4f} seconds")

    def select(self):
        begin = time.perf_counter()
        for i in self.pacjenci.find():
            pass
        end = time.perf_counter()
        self.select_time = end - begin
        print(f"SELECT run {self.n} times in loop end after {self.select_time:0.4f} seconds")

    def update(self):
        begin = time.perf_counter()
        number = 123
        for i in range(0, self.n):
            number = number + 1
            self.pacjenci.update_many({}, {"$set": {"telefon": number}})
        end = time.perf_counter()
        self.update_time = end - begin
        print(f"UPDATE run {self.n} times in loop end after {self.update_time:0.4f} seconds")

    def delete(self):
        'DELETE instruction'
        begin = time.perf_counter()
        self.pacjenci.delete_many({})
        end = time.perf_counter()
        self.delete_time = end - begin
        print(f"DELETE run {self.n} times in loop end after {self.delete_time:0.4f} seconds")

    def drop_tables(self):
        'Table drop part'
        self.db.pacjenci.drop()
        self.db.doktorzy.drop()
        self.db.wizyty.drop()
        self.db.dawki_i_leki.drop()
        self.db.dok_i_spec.drop()
        self.db.leki.drop()
        self.db.dawki.drop()
        self.db.specjalizacje.drop()
        self.db.wiz_i_dawki_i_leki.drop()


def main():
    test_val2 = Mongo_db(100)


if __name__ == "__main__":
    main()
