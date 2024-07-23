from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QWidget , QVBoxLayout
from PySide6.QtGui import Qt
import sys
import time
from prime_sss import Prime

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.prime = Prime()
        self.setWindowTitle("素因数分解")

        #ウィンドウサイズの調整
        self.windowWidth = 350   # ウィンドウの横幅
        self.windowHeight = 100  # ウィンドウの高さ
        self.setFixedSize(self.windowWidth, self.windowHeight)

        self.SetLabel1()
        self.SetLineedit()
        self.SetLabel2()

        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.label1)
        vlayout.addWidget(self.lineEdit)
        vlayout.addWidget(self.label2)

    def SetLabel1(self):
        self.label1 = QLabel(self)
        self.label1.setText("素因数分解したい数を入力")
        self.label1.setAlignment(Qt.AlignCenter)

    def SetLabel2(self):
        self.label2 = QLabel(self)
        self.label2.setText("")
        self.label2.setAlignment(Qt.AlignCenter)

    def SetLineedit(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.resize(200, 25)   # 入力欄のサイズを変更
        self.lineEdit.returnPressed.connect(self.Push_EnterKey)

    # 入力欄でEnterキーが押されたら実行する処理
    def Push_EnterKey(self):
        add_text = ""
        answer = self.prime.process_first(self.lineEdit.text())
        self.label2.setText("")
        QApplication.processEvents()
        time.sleep(0.2)
        answer = list(answer)
        for i in range (len(answer)):
            time.sleep(0.01)
            add_text += answer[i]
            self.label2.setText(add_text)
            QApplication.processEvents()


if __name__ == "__main__":
    app = QApplication(sys.argv)    # PySide6の実行
    window = MainWindow()           # ユーザがコーディングしたクラス
    window.show()                   # PySide6のウィンドウを表示
    sys.exit(app.exec())            # PySide6の終了