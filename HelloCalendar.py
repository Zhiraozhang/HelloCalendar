import sys
import hello
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mUi_Dialog = QDialog()
    ui = hello.Ui_Dialog()
    ui.setupUi(mUi_Dialog)
    mUi_Dialog.show()
    sys.exit(app.exec_())
