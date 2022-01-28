import time
import rethinkdb as r

class Rethink_db:
  def __init__(self, n):
    'RethinkDB init part'
    self.rdb = r.RethinkDB()
    self.rdb.connect('localhost', 28015).repl()

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
    'INSERT instuction'
    begin = time.perf_counter()
    for i in range(1, n+1):
      self.rdb.db("clinic_rethink").table('pacjenci').insert([
        {'idp': i,'imie': 'Dawid', 'nazwisko': 'Mrosek', 'pesel': '97090605938', 'plec': 'Mężczyzna', 'data_urodzenia': '1997-09-06', 'adres': 'Pilsudskiego 2121', 'telefon': '123'}
        ]).run()

    #self.rdb.db("clinic_rethink").table('pacjenci').insert([
        #{'idp': 1,'imie': 'Dawid', 'nazwisko': 'Mrosek', 'pesel': '97090605938', 'plec': 'Mężczyzna', 'data_urodzenia': '1997-09-06', 'adres': 'Pilsudskiego 2121', 'telefon': '123'}
    #]).run()

    end = time.perf_counter()
    print(f"INSERT run {n} times in loop end after {end - begin:0.4f} seconds")

    'SELECT instuction'
    begin = time.perf_counter()
    for i in range(1, n+1):
      self.rdb.db("clinic_rethink").table("pacjenci").run()
      #print(self.rdb.db("clinic_rethink").table("pacjenci").run())
    end = time.perf_counter()
    print(f"SELECT run {n} times in loop end after {end - begin:0.4f} seconds")

    'UPDATE instuction'
    begin = time.perf_counter()
    number = 123
    for i in range(0, n):
      number = number + 1
      self.rdb.db("clinic_rethink").table('pacjenci').update({"telefon": "number"}).run()
    end = time.perf_counter()
    print(f"UPDATE run {n} times in loop end after {end - begin:0.4f} seconds")


    'Table drop part'
    self.rdb.db('clinic_rethink').table_drop('pacjenci').run()
    self.rdb.db('clinic_rethink').table_drop('doktorzy').run()
    self.rdb.db('clinic_rethink').table_drop('wizyty').run()

    self.rdb.db('clinic_rethink').table_drop('dawki_i_leki').run()
    self.rdb.db('clinic_rethink').table_drop('dok_i_spec').run()
    self.rdb.db('clinic_rethink').table_drop('leki').run()

    self.rdb.db('clinic_rethink').table_drop('dawki').run()
    self.rdb.db('clinic_rethink').table_drop('specjalizacje').run()
    self.rdb.db('clinic_rethink').table_drop('wiz_i_dawki_i_leki').run()

test_val3 = Rethink_db(100)