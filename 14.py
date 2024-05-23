import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton


class LandmarkApp(QMainWindow):
    def __init__(self):
        super(LandmarkApp, self).__init__()
        uic.loadUi('karta.ui', self)
        self.setWindowTitle('Country information')

        self.line = self.findChild(QLineEdit, 'line')
        self.Button = self.findChild(QPushButton, 'Button')
        self.label = self.findChild(QLabel, 'label')
        self.line.setPlaceholderText(f"data")

        self.Button.clicked.connect(self.get_landmark)

    def get_landmark(self):
        city = self.line.text()
        landmark = self.find_landmark(city)
        self.label.setText(landmark)

    def find_landmark(self, city):
        landmarks = {
            "Франция": "Площадь: Площадь согласия. Протяженность: 360 м",
            "Рим": "Площадь: Площадь Республики. Протяженность: 80 м",
            "Лондон": "Площадь: Трафальгарская. Протяженность: 166 м",
            "Нью-Йорк": "Площадь: Таймс-Сквер. Протяженность: 140 м"
        }
        return landmarks.get(city, "Информация не найдена")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    landmark_app = LandmarkApp()
    landmark_app.show()
    sys.exit(app.exec_())