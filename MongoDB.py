import pymongo
import time

class Mongo_db:
  def __init__(self, n):
    'MongoDB init part'
    self.client = pymongo.MongoClient("mongodb://localhost:27017/", connect=False)
    print(self.client.list_database_names())
    self.db = self.client["clinic_monogo"]

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
    'INSERT instuction'
    begin = time.perf_counter()
    for i in range(1, n+1):
      value = [{'idp': " + str(i) + ",'imie': 'Dawid', 'nazwisko': 'Mrosek', 'pesel': '97090605938', 'plec': 'Mężczyzna', 'data_urodzenia': '1997-09-06', 'adres': 'Pilsudskiego 2121', 'telefon': '123'}]
      self.pacjenci.insert_many(value)
      #self.pacjenci.insert_many(mylist)

    end = time.perf_counter()
    print(f"INSERT run {n} times in loop end after {end - begin:0.4f} seconds")

    'SELECT instuction'
    begin = time.perf_counter()
    for i in self.pacjenci.find():
      print(i)
    end = time.perf_counter()
    print(f"SELECT run {n} times in loop end after {end - begin:0.4f} seconds")



    'UPDATE instruction'
    begin = time.perf_counter()
    number = 123
    for i in range(0, n):
      number = number + 1
      self.pacjenci.update_many({}, {"$set": {"telefon": number}})
    end = time.perf_counter()
    print(f"UPDATE run {n} times in loop end after {end - begin:0.4f} seconds")

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

test_val2 = Mongo_db(100)