import sqlite3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QCompleter, QFileDialog
from d import Ui_Ui_MainWindow

class MyWidget(QMainWindow, Ui_Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.con = sqlite3.connect('coffee.sqlite')
        cur = self.con.cursor()
        self.comboBox.addItems(
            [i[0] for i in
             cur.execute('SELECT name FROM Kofe').fetchall()])
        self.pushButton.clicked.connect(self.run)

    def run(self):
        cur = self.con.cursor()
        result = cur.execute(f"""SELECT id FROM Kofe WHERE name = ?
                             """, (self.comboBox.currentText(),)).fetchall()
        self.lineEdit.setText(str(result[0][0]))
        result = cur.execute(f"""SELECT name FROM Kofe WHERE name = ?
                             """, (self.comboBox.currentText(),)).fetchall()
        self.lineEdit_2.setText(str(result[0][0]))
        result = cur.execute(f"""SELECT roasting FROM Kofe WHERE name = ?
                             """, (self.comboBox.currentText(),)).fetchall()
        self.lineEdit_3.setText(str(result[0][0]))
        result = cur.execute(f"""SELECT grain FROM Kofe WHERE name = ?
                             """, (self.comboBox.currentText(),)).fetchall()
        self.lineEdit_4.setText(str(result[0][0]))
        result = cur.execute(f"""SELECT taste FROM Kofe WHERE name = ?
                             """, (self.comboBox.currentText(),)).fetchall()
        self.lineEdit_5.setText(str(result[0][0]))
        result = cur.execute(f"""SELECT price FROM Kofe WHERE name = ?
                             """, (self.comboBox.currentText(),)).fetchall()
        self.lineEdit_6.setText(str(result[0][0]))
        result = cur.execute(f"""SELECT volume FROM Kofe WHERE name = ?
                             """, (self.comboBox.currentText(),)).fetchall()
        self.lineEdit_7.setText(str(result[0][0]))



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())