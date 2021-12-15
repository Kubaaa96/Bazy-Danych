from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget, QPushButton, QFrame
from PyQt6.QtCore import QSize, QPoint, Qt
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_window()
        self.init_gui()

    def setup_window(self):
        default_size = QSize(500, 700)

        self.resize(default_size)
        starting_location = QPoint(300, 100)
        self.move(starting_location)

        maximum_size = QSize(600, 800)
        self.setMaximumSize(maximum_size)

        minimum_size = QSize(300, 500)
        self.setMinimumSize(minimum_size)

        title = 'Bazy Danych'
        self.setWindowTitle(title)

    def init_gui(self):
        main_layout = QVBoxLayout()

        main_label = QLabel("Program do wywolywania polecen do bazy")
        my_font = QFont("Arial", 18)
        main_label.setFont(my_font)
        # main_label.setWordWrap(True)
        main_layout.addWidget(main_label, alignment=Qt.AlignmentFlag.AlignCenter)

        mysql_frame = QFrame()
        mysql_layout = QVBoxLayout()

        mysql_label = QLabel("MySqL")
        mysql_label.setWordWrap(True)
        mysql_layout.addWidget(mysql_label, alignment=Qt.AlignmentFlag.AlignCenter)

        mysql_result_label = QLabel("Time is 00:00:00")
        mysql_result_label.setWordWrap(True)
        mysql_layout.addWidget(mysql_result_label, alignment=Qt.AlignmentFlag.AlignCenter)

        mysql_frame.setLayout(mysql_layout)
        mysql_frame.setStyleSheet("border: 1px solid black; margin: 0px; padding: 0px;")

        main_layout.addWidget(mysql_frame)

        rethinkdb_frame = QFrame()
        rethinkdb_layout = QVBoxLayout()

        rethingdb_label = QLabel("RethinkDB")
        rethingdb_label.setWordWrap(True)
        rethinkdb_layout.addWidget(rethingdb_label, alignment=Qt.AlignmentFlag.AlignCenter)

        rethingdb_result_label = QLabel("Time is 00:00:00")
        rethingdb_result_label.setWordWrap(True)
        rethinkdb_layout.addWidget(rethingdb_result_label, alignment=Qt.AlignmentFlag.AlignCenter)

        rethinkdb_frame.setLayout(rethinkdb_layout)
        rethinkdb_frame.setStyleSheet("border: 1px solid black; margin: 0px; padding: 0px;")
        main_layout.addWidget(rethinkdb_frame)


        mongodb_frame = QFrame()

        mongodb_layout = QVBoxLayout()

        mongodb_label = QLabel("MongoDB")
        mongodb_label.setWordWrap(True)
        mongodb_layout.addWidget(mongodb_label, alignment=Qt.AlignmentFlag.AlignCenter)

        mongodb_result_label = QLabel("Time is 00:00:00")
        mongodb_result_label.setWordWrap(True)
        mongodb_layout.addWidget(mongodb_result_label, alignment=Qt.AlignmentFlag.AlignCenter)

        mongodb_frame.setLayout(mongodb_layout)
        mongodb_frame.setStyleSheet("border: 1px solid black; margin: 0px; padding: 0px;")

        main_layout.addWidget(mongodb_frame)

        execute_button = QPushButton("Execute")
        main_layout.addWidget(execute_button)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)




