from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton, QFrame, QLineEdit
from PyQt6.QtCore import QSize, QPoint, Qt
from PyQt6.QtGui import QFont, QIntValidator

from Rethink import Rethink_db
from MongoDB import Mongo_db
from MySQL import MySQL_db


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__setup_window()
        self.__init_gui()

    def __setup_window(self):
        default_size = QSize(800, 700)

        self.resize(default_size)
        starting_location = QPoint(300, 100)
        self.move(starting_location)

        maximum_size = QSize(1000, 800)
        self.setMaximumSize(maximum_size)

        minimum_size = QSize(600, 500)
        self.setMinimumSize(minimum_size)

        title = 'Bazy Danych'
        self.setWindowTitle(title)

    def __execute(self):
        how_many_rows_str = self.main_line_edit.text()
        if len(how_many_rows_str) == 0:
            print("Fill Line Edit Widget with number")
        else:
            how_many_rows = int(how_many_rows_str)

            mysql_db = MySQL_db(how_many_rows)
            self.__fill_mysql(mysql_db)

            rethink_db = Rethink_db(how_many_rows)
            self.__fill_rethinkdb(rethink_db)

            mongo_db = Mongo_db(how_many_rows)
            self.__fill_mongodb(mongo_db)

    def __fill_mysql(self, mysql_db: MySQL_db):
        select_time = f"{mysql_db.select_time:0.4f}"
        self.mysql_result_label_select.setText(select_time)

        delete_time = f"{mysql_db.delete_time:0.4f}"
        self.mysql_result_label_delete.setText(delete_time)

        insert_time = f"{mysql_db.insert_time:0.4f}"
        self.mysql_result_label_insert.setText(insert_time)

        update_time = f"{mysql_db.update_time:0.4f}"
        self.mysql_result_label_update.setText(update_time)

    def __fill_rethinkdb(self, rethink_db: Rethink_db):
        select_time = f"{rethink_db.select_time:0.4f}"
        self.rethinkdb_result_label_select.setText(select_time)

        delete_time = f"{rethink_db.delete_time:0.4f}"
        self.rethinkdb_result_label_delete.setText(delete_time)

        insert_time = f"{rethink_db.insert_time:0.4f}"
        self.rethinkdb_result_label_insert.setText(insert_time)

        update_time = f"{rethink_db.update_time:0.4f}"
        self.rethinkdb_result_label_update.setText(update_time)

    def __fill_mongodb(self, mongo_db: Mongo_db):
        select_time = f"{mongo_db.select_time:0.4f}"
        self.mongodb_result_label_select.setText(select_time)

        delete_time = f"{mongo_db.delete_time:0.4f}"
        self.mongodb_result_label_delete.setText(delete_time)

        insert_time = f"{mongo_db.insert_time:0.4f}"
        self.mongodb_result_label_insert.setText(insert_time)

        update_time = f"{mongo_db.update_time:0.4f}"
        self.mongodb_result_label_update.setText(update_time)

    def __init_gui(self):
        main_layout = QVBoxLayout()

        main_label = QLabel("Program do wywolywania polecen do bazy")
        my_font = QFont("Arial", 18)
        main_label.setFont(my_font)
        main_layout.addWidget(main_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.main_line_edit = QLineEdit()
        line_edit_font = QFont("Arial", 25)
        self.main_line_edit.setFont(line_edit_font)
        self.main_line_edit.setFixedHeight(150)
        self.main_line_edit.setFixedWidth(300)
        self.main_line_edit.setValidator(QIntValidator(50, 99999))
        main_layout.addWidget(self.main_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.__init_mysql())
        main_layout.addWidget(self.__init_rethinkdb())
        main_layout.addWidget(self.__init_mongodb())

        execute_button = QPushButton("Execute")
        execute_button.clicked.connect(self.__execute)
        main_layout.addWidget(execute_button)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def __init_mysql(self):
        mysql_layout = QVBoxLayout()

        mysql_label = QLabel("MySql")
        mysql_font = QFont("Arial", 16)
        mysql_label.setFont(mysql_font)

        mysql_label.setWordWrap(True)
        mysql_layout.addWidget(mysql_label, alignment=Qt.AlignmentFlag.AlignCenter)

        mysql_inner_layout = QHBoxLayout()
        mysql_insert_layout = QVBoxLayout()

        mysql_label_insert = QLabel("Insert")
        mysql_label_insert.setWordWrap(True)
        mysql_insert_layout.addWidget(mysql_label_insert, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mysql_result_label_insert = QLabel("Time is 00:00:00")
        self.mysql_result_label_insert.setWordWrap(True)
        mysql_insert_layout.addWidget(self.mysql_result_label_insert, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mysql_insert_frame = QFrame()
        self.mysql_insert_frame.setLayout(mysql_insert_layout)
        mysql_inner_layout.addWidget(self.mysql_insert_frame)

        mysql_select_layout = QVBoxLayout()
        mysql_label_select = QLabel("Select")
        mysql_label_select.setWordWrap(True)
        mysql_select_layout.addWidget(mysql_label_select, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mysql_result_label_select = QLabel("Time is 00:00:00")
        self.mysql_result_label_select.setWordWrap(True)
        mysql_select_layout.addWidget(self.mysql_result_label_select, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mysql_select_frame = QFrame()
        self.mysql_select_frame.setLayout(mysql_select_layout)
        mysql_inner_layout.addWidget(self.mysql_select_frame)

        mysql_update_layout = QVBoxLayout()
        mysql_label_update = QLabel("Update")
        mysql_label_update.setWordWrap(True)
        mysql_update_layout.addWidget(mysql_label_update, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mysql_result_label_update = QLabel("Time is 00:00:00")
        self.mysql_result_label_update.setWordWrap(True)
        mysql_update_layout.addWidget(self.mysql_result_label_update, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mysql_update_frame = QFrame()
        self.mysql_update_frame.setLayout(mysql_update_layout)
        mysql_inner_layout.addWidget(self.mysql_update_frame)

        mysql_delete_layout = QVBoxLayout()
        mysql_label_delete = QLabel("Delete")
        mysql_label_delete.setWordWrap(True)
        mysql_delete_layout.addWidget(mysql_label_delete, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mysql_result_label_delete = QLabel("Time is 00:00:00")
        self.mysql_result_label_delete.setWordWrap(True)
        mysql_delete_layout.addWidget(self.mysql_result_label_delete, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mysql_delete_frame = QFrame()
        self.mysql_delete_frame.setLayout(mysql_delete_layout)
        mysql_inner_layout.addWidget(self.mysql_delete_frame)

        mysql_layout.addLayout(mysql_inner_layout)

        mysql_frame = QFrame()
        mysql_frame.setLayout(mysql_layout)
        mysql_frame.setStyleSheet("border: 1px solid black; margin: 0px; padding: 0px;")
        return mysql_frame

    def __init_rethinkdb(self):
        rethinkdb_frame = QFrame()
        rethinkdb_layout = QVBoxLayout()

        rethinkdb_label = QLabel("RethinkDB")
        rethinkdb_font = QFont("Arial", 16)
        rethinkdb_label.setFont(rethinkdb_font)

        rethinkdb_label.setWordWrap(True)
        rethinkdb_layout.addWidget(rethinkdb_label, alignment=Qt.AlignmentFlag.AlignCenter)

        rethinkdb_inner_layout = QHBoxLayout()

        rethinkdb_insert_layout = QVBoxLayout()
        rethinkdb_label_insert = QLabel("Insert")
        rethinkdb_label_insert.setWordWrap(True)
        rethinkdb_insert_layout.addWidget(rethinkdb_label_insert, alignment=Qt.AlignmentFlag.AlignCenter)

        self.rethinkdb_result_label_insert = QLabel("Time is 00:00:00")
        self.rethinkdb_result_label_insert.setWordWrap(True)
        rethinkdb_insert_layout.addWidget(self.rethinkdb_result_label_insert, alignment=Qt.AlignmentFlag.AlignCenter)

        self.rethinkdb_update_frame = QFrame()
        self.rethinkdb_update_frame.setLayout(rethinkdb_insert_layout)
        rethinkdb_inner_layout.addWidget(self.rethinkdb_update_frame)

        rethinkdb_select_layout = QVBoxLayout()
        rethinkdb_label_select = QLabel("Select")
        rethinkdb_label_select.setWordWrap(True)
        rethinkdb_select_layout.addWidget(rethinkdb_label_select, alignment=Qt.AlignmentFlag.AlignCenter)

        self.rethinkdb_result_label_select = QLabel("Time is 00:00:00")
        self.rethinkdb_result_label_select.setWordWrap(True)
        rethinkdb_select_layout.addWidget(self.rethinkdb_result_label_select, alignment=Qt.AlignmentFlag.AlignCenter)

        self.rethinkdb_select_frame = QFrame()
        self.rethinkdb_select_frame.setLayout(rethinkdb_select_layout)
        rethinkdb_inner_layout.addWidget(self.rethinkdb_select_frame)

        rethinkdb_update_layout = QVBoxLayout()
        rethinkdb_label_update = QLabel("Update")
        rethinkdb_label_update.setWordWrap(True)
        rethinkdb_update_layout.addWidget(rethinkdb_label_update, alignment=Qt.AlignmentFlag.AlignCenter)

        self.rethinkdb_result_label_update = QLabel("Time is 00:00:00")
        self.rethinkdb_result_label_update.setWordWrap(True)
        rethinkdb_update_layout.addWidget(self.rethinkdb_result_label_update, alignment=Qt.AlignmentFlag.AlignCenter)

        self.rethinkdb_update_frame = QFrame()
        self.rethinkdb_update_frame.setLayout(rethinkdb_update_layout)
        rethinkdb_inner_layout.addWidget(self.rethinkdb_update_frame)

        rethinkdb_delete_layout = QVBoxLayout()
        rethinkdb_label_delete = QLabel("Delete")
        rethinkdb_label_delete.setWordWrap(True)
        rethinkdb_delete_layout.addWidget(rethinkdb_label_delete, alignment=Qt.AlignmentFlag.AlignCenter)

        self.rethinkdb_result_label_delete = QLabel("Time is 00:00:00")
        self.rethinkdb_result_label_delete.setWordWrap(True)
        rethinkdb_delete_layout.addWidget(self.rethinkdb_result_label_delete, alignment=Qt.AlignmentFlag.AlignCenter)

        self.rethinkdb_delete_frame = QFrame()
        self.rethinkdb_delete_frame.setLayout(rethinkdb_delete_layout)
        rethinkdb_inner_layout.addWidget(self.rethinkdb_delete_frame)

        rethinkdb_layout.addLayout(rethinkdb_inner_layout)

        rethinkdb_frame.setLayout(rethinkdb_layout)
        rethinkdb_frame.setStyleSheet("border: 1px solid black; margin: 0px; padding: 0px;")
        return rethinkdb_frame

    def __init_mongodb(self):
        mongodb_frame = QFrame()
        mongodb_layout = QVBoxLayout()

        mongodb_label = QLabel("MongoDB")
        mongodb_font = QFont("Arial", 16)
        mongodb_label.setFont(mongodb_font)

        mongodb_label.setWordWrap(True)
        mongodb_layout.addWidget(mongodb_label, alignment=Qt.AlignmentFlag.AlignCenter)

        mongodb_inner_layout = QHBoxLayout()

        mongodb_insert_layout = QVBoxLayout()
        mongodb_label_insert = QLabel("Insert")
        mongodb_label_insert.setWordWrap(True)
        mongodb_insert_layout.addWidget(mongodb_label_insert, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mongodb_result_label_insert = QLabel("Time is 00:00:00")
        self.mongodb_result_label_insert.setWordWrap(True)
        mongodb_insert_layout.addWidget(self.mongodb_result_label_insert, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mongodb_insert_frame = QFrame()
        self.mongodb_insert_frame.setLayout(mongodb_insert_layout)
        mongodb_inner_layout.addWidget(self.mongodb_insert_frame)

        mongodb_select_layout = QVBoxLayout()
        mongodb_label_select = QLabel("Select")
        mongodb_label_select.setWordWrap(True)
        mongodb_select_layout.addWidget(mongodb_label_select, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mongodb_result_label_select = QLabel("Time is 00:00:00")
        self.mongodb_result_label_select.setWordWrap(True)
        mongodb_select_layout.addWidget(self.mongodb_result_label_select, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mongodb_select_frame = QFrame()
        self.mongodb_select_frame.setLayout(mongodb_select_layout)
        mongodb_inner_layout.addWidget(self.mongodb_select_frame)

        mongodb_update_layout = QVBoxLayout()
        mongodb_label_update = QLabel("Update")
        mongodb_label_update.setWordWrap(True)
        mongodb_update_layout.addWidget(mongodb_label_update, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mongodb_result_label_update = QLabel("Time is 00:00:00")
        self.mongodb_result_label_update.setWordWrap(True)
        mongodb_update_layout.addWidget(self.mongodb_result_label_update, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mongodb_update_frame = QFrame()
        self.mongodb_update_frame.setLayout(mongodb_update_layout)
        mongodb_inner_layout.addWidget(self.mongodb_update_frame)

        mongodb_delete_layout = QVBoxLayout()
        mongodb_label_delete = QLabel("Delete")
        mongodb_label_delete.setWordWrap(True)
        mongodb_delete_layout.addWidget(mongodb_label_delete, alignment=Qt.AlignmentFlag.AlignCenter)

        self.mongodb_result_label_delete = QLabel("Time is 00:00:00")
        self.mongodb_result_label_delete.setWordWrap(True)
        mongodb_delete_layout.addWidget(self.mongodb_result_label_delete, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mongodb_delete_frame = QFrame()
        self.mongodb_delete_frame.setLayout(mongodb_delete_layout)
        mongodb_inner_layout.addWidget(self.mongodb_delete_frame)

        mongodb_layout.addLayout(mongodb_inner_layout)

        mongodb_frame.setLayout(mongodb_layout)
        mongodb_frame.setStyleSheet("border: 1px solid black; margin: 0px; padding: 0px;")
        return mongodb_frame
