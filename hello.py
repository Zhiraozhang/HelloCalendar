# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, hello):
        hello.setObjectName("hello")
        hello.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.calendarWidget = QtWidgets.QCalendarWidget(hello)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(hello)
        QtCore.QMetaObject.connectSlotsByName(hello)

    def retranslateUi(self, hello):
        _translate = QtCore.QCoreApplication.translate
        hello.setWindowTitle(_translate("Dialog", "HelloCalendar"))
