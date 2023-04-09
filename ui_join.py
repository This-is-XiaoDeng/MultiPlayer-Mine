# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'join.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QSpinBox,
    QTabWidget, QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(376, 292)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.toolBox = QToolBox(self.tab)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 334, 121))
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.page)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(65535)
        self.spinBox.setValue(12306)

        self.gridLayout.addWidget(self.spinBox, 1, 2, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 2)

        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.page)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 2)

        self.toolBox.addItem(self.page, u"\u52a0\u5165\u6e38\u620f")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 141, 120))
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_3 = QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.page_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(65535)
        self.spinBox_2.setValue(12306)

        self.gridLayout_2.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.lineEdit_4, 2, 1, 1, 1)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.page_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 3, 1, 1, 1)

        self.toolBox.addItem(self.page_2, u"\u53d1\u8d77\u6e38\u620f")

        self.verticalLayout_2.addWidget(self.toolBox)

        self.commandLinkButton = QCommandLinkButton(self.tab)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.verticalLayout_2.addWidget(self.commandLinkButton)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u626b\u96f7\uff08\u591a\u4eba\u6e38\u620f\uff09", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u673a\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u73a9\u5bb6\u540d\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5165\u5bc6\u94a5\uff1a", None))
        self.lineEdit_5.setInputMask("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6ca1\u6709\u53ef\u7559\u7a7a", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u52a0\u5165\u6e38\u620f", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"IP\uff1a", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6ca1\u6709\u53ef\u7559\u7a7a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5165\u5bc6\u94a5\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u73a9\u5bb6\u540d\uff1a", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u53d1\u8d77\u6e38\u620f", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"\u7acb\u5373\u52a0\u5165\uff01", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u52a0\u5165", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

