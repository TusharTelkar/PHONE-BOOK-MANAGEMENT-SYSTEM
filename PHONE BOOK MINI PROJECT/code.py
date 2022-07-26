# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'contactSOQqRH.ui'
##
# Created by: Qt User Interface Compiler version 5.14.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

import icon_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(937, 673)
        MainWindow.setStyleSheet(u"border:1px solid black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMargin(10)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 100))
        self.label_2.setMaximumSize(QSize(100, 100))
        self.label_2.setPixmap(QPixmap(u":/icon/icons8-contacts.svg"))
        self.label_2.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icon/icons/add-50.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/version-update-6.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)

        self.gridLayout_3.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_3.addWidget(self.label_6, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_3.addWidget(self.label_5, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/delete-374.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/search-189.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/info-57.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.pushButton_5, 4, 0, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_3.addWidget(self.label_7, 4, 1, 1, 1)

        self.horizontalLayout_2.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_15 = QFrame(self.page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_15)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget_4 = QTableWidget(self.frame_15)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2)
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2)
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2)
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2)
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2)
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setMaximumSize(QSize(590, 16777215))
        self.tableWidget_4.setIconSize(QSize(10000, 10000))

        self.gridLayout_6.addWidget(self.tableWidget_4, 0, 0, 1, 1)

        self.verticalLayout_6.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_16)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_10 = QPushButton(self.frame_16)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font2)

        self.gridLayout_5.addWidget(self.pushButton_10, 0, 0, 1, 1)

        self.verticalLayout_6.addWidget(
            self.frame_16, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_8 = QGridLayout(self.page_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_17 = QFrame(self.page_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(600, 0))
        self.frame_17.setMaximumSize(QSize(600, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_17)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.gridLayout_7.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.frame_17)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.gridLayout_7.addWidget(self.label_15, 2, 0, 1, 1)

        self.label_16 = QLabel(self.frame_17)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.gridLayout_7.addWidget(self.label_16, 3, 0, 1, 1)

        self.label_17 = QLabel(self.frame_17)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.gridLayout_7.addWidget(self.label_17, 1, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_17)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_7.setFont(font2)

        self.gridLayout_7.addWidget(self.lineEdit_7, 3, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_17)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_8.setFont(font2)

        self.gridLayout_7.addWidget(self.lineEdit_8, 2, 1, 1, 1)

        self.label_18 = QLabel(self.frame_17)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.gridLayout_7.addWidget(self.label_18, 4, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_17)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_9.setFont(font2)

        self.gridLayout_7.addWidget(self.lineEdit_9, 1, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_17)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_10.setFont(font2)

        self.gridLayout_7.addWidget(self.lineEdit_10, 0, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_17)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(300, 50))
        self.lineEdit_11.setMaximumSize(QSize(300, 300))

        self.gridLayout_7.addWidget(self.lineEdit_11, 4, 1, 1, 1)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_11 = QPushButton(self.frame_18)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font2)

        self.horizontalLayout_11.addWidget(self.pushButton_11)

        self.gridLayout_7.addWidget(self.frame_18, 5, 0, 1, 2, Qt.AlignHCenter)

        self.gridLayout_8.addWidget(self.frame_17, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_7 = QVBoxLayout(self.page_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_19 = QFrame(self.page_3)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_19)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(self.frame_21)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.lineEdit_12 = QLineEdit(self.frame_21)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        font3 = QFont()
        font3.setPointSize(10)
        self.lineEdit_12.setFont(font3)

        self.horizontalLayout_12.addWidget(self.lineEdit_12)

        self.pushButton_12 = QPushButton(self.frame_21)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font2)
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/search-185.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.pushButton_12)

        self.gridLayout_9.addWidget(self.frame_21, 0, 0, 1, 1)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_22)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pushButton_13 = QPushButton(self.frame_22)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font2)

        self.gridLayout_10.addWidget(self.pushButton_13, 0, 0, 1, 1)

        self.gridLayout_9.addWidget(
            self.frame_22, 1, 0, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.page_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_20)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tableWidget_5 = QTableWidget(self.frame_20)
        if (self.tableWidget_5.columnCount() < 5):
            self.tableWidget_5.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2)
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2)
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2)
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2)
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2)
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_5.setObjectName(u"tableWidget_5")

        self.gridLayout_11.addWidget(self.tableWidget_5, 0, 0, 1, 1)

        self.verticalLayout_7.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.page_3)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.verticalLayout_4 = QVBoxLayout(self.search)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_10 = QFrame(self.search)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_7 = QPushButton(self.frame_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font2)

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font2)

        self.horizontalLayout_5.addWidget(self.pushButton_8)

        self.verticalLayout_4.addWidget(self.frame_10, 0, Qt.AlignTop)

        self.frame_11 = QFrame(self.search)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(
            self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.stackedWidget_2 = QStackedWidget(self.frame_11)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.single_search = QWidget()
        self.single_search.setObjectName(u"single_search")
        self.verticalLayout_5 = QVBoxLayout(self.single_search)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_12 = QFrame(self.single_search)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.lineEdit_6 = QLineEdit(self.frame_12)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font3)

        self.horizontalLayout_7.addWidget(self.lineEdit_6)

        self.pushButton_9 = QPushButton(self.frame_12)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font2)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.pushButton_9)

        self.verticalLayout_5.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.frame_13 = QFrame(self.single_search)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(
            self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tableWidget_2 = QTableWidget(self.frame_13)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2)
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font2)
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font2)
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font2)
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font2)
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.horizontalLayout_8.addWidget(self.tableWidget_2)

        self.verticalLayout_5.addWidget(self.frame_13)

        self.stackedWidget_2.addWidget(self.single_search)
        self.all_search = QWidget()
        self.all_search.setObjectName(u"all_search")
        self.horizontalLayout_10 = QHBoxLayout(self.all_search)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_14 = QFrame(self.all_search)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tableWidget_3 = QTableWidget(self.frame_14)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font2)
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font2)
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font2)
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font2)
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font2)
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.horizontalLayout_9.addWidget(self.tableWidget_3)

        self.horizontalLayout_10.addWidget(self.frame_14)

        self.stackedWidget_2.addWidget(self.all_search)

        self.horizontalLayout_6.addWidget(self.stackedWidget_2)

        self.verticalLayout_4.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.search)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_8 = QVBoxLayout(self.page_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_23 = QFrame(self.page_4)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.page_4)
        self.insert = QWidget()
        self.insert.setObjectName(u"insert")
        self.verticalLayout_3 = QVBoxLayout(self.insert)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_7 = QFrame(self.insert)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(600, 0))
        self.frame_7.setMaximumSize(QSize(600, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.gridLayout_4.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_4.setFont(font2)

        self.gridLayout_4.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_3.setFont(font2)

        self.gridLayout_4.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_7)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_2.setFont(font2)

        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(250, 16777215))
        self.lineEdit.setFont(font2)

        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_7)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(300, 50))
        self.lineEdit_5.setMaximumSize(QSize(300, 300))

        self.gridLayout_4.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_6 = QPushButton(self.frame_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font2)

        self.horizontalLayout_4.addWidget(self.pushButton_6)

        self.gridLayout_4.addWidget(self.frame_9, 5, 0, 1, 2, Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.insert)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.frame_8)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font2)
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font2)
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font2)
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font2)
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font2)
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.verticalLayout_3.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.insert)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.horizontalLayout.addWidget(self.frame_5)

        self.verticalLayout.addWidget(self.frame_3)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget_2.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"PHONE BOOK", None))
        self.label_2.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Update Contact", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Search Contact", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Delete Contact", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Add New Contact", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"About", None))
        ___qtablewidgetitem = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem1 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate(
            "MainWindow", u"Phone Number", None))
        ___qtablewidgetitem2 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"Email", None))
        ___qtablewidgetitem3 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"Work", None))
        ___qtablewidgetitem4 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"Address", None))
        self.pushButton_10.setText(
            QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_14.setText(QCoreApplication.translate(
            "MainWindow", u"Name", None))
        self.label_15.setText(QCoreApplication.translate(
            "MainWindow", u"Email", None))
        self.label_16.setText(QCoreApplication.translate(
            "MainWindow", u"Work", None))
        self.label_17.setText(QCoreApplication.translate(
            "MainWindow", u"Phone Number", None))
        self.label_18.setText(QCoreApplication.translate(
            "MainWindow", u"Address", None))
        self.pushButton_11.setText(
            QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.label_19.setText(QCoreApplication.translate(
            "MainWindow", u"Name/Phone number", None))
        self.pushButton_12.setText(
            QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_13.setText(
            QCoreApplication.translate("MainWindow", u"DELETE", None))
        ___qtablewidgetitem5 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem6 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate(
            "MainWindow", u"Phone Number", None))
        ___qtablewidgetitem7 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", u"Email", None))
        ___qtablewidgetitem8 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate("MainWindow", u"Work", None))
        ___qtablewidgetitem9 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", u"Address", None))
        self.pushButton_7.setText(
            QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_8.setText(QCoreApplication.translate(
            "MainWindow", u"All Contact", None))
        self.label_13.setText(QCoreApplication.translate(
            "MainWindow", u"Name/Phone number", None))
        self.pushButton_9.setText(
            QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate(
            "MainWindow", u"Phone Number", None))
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate("MainWindow", u"Email", None))
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(
            QCoreApplication.translate("MainWindow", u"Work", None))
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(
            QCoreApplication.translate("MainWindow", u"Address", None))
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate(
            "MainWindow", u"Phone Number", None))
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(
            QCoreApplication.translate("MainWindow", u"Email", None))
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(
            QCoreApplication.translate("MainWindow", u"Work", None))
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(
            QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Name", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Email", None))
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"Work", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Phone Number", None))
        self.label_12.setText(QCoreApplication.translate(
            "MainWindow", u"Address", None))
        self.pushButton_6.setText(
            QCoreApplication.translate("MainWindow", u"ADD", None))
        ___qtablewidgetitem20 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem21 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate(
            "MainWindow", u"Phone Number", None))
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(
            QCoreApplication.translate("MainWindow", u"Email", None))
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(
            QCoreApplication.translate("MainWindow", u"Work", None))
        ___qtablewidgetitem24 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(
            QCoreApplication.translate("MainWindow", u"Address", None))
    # retranslateUi
