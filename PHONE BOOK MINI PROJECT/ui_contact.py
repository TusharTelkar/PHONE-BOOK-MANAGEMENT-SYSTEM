# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contactcyvZtc.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
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
        MainWindow.resize(1615, 848)
        MainWindow.setStyleSheet(u"border:1px solid black;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_33 = QFrame(self.centralwidget)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.frame_33)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.horizontalLayout_13 = QHBoxLayout(self.main_page)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame = QFrame(self.main_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 100))
        self.label_2.setMaximumSize(QSize(120, 100))
        self.label_2.setPixmap(QPixmap(u":/icon/icons/agenda.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.label_2)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMargin(10)

        self.horizontalLayout_19.addWidget(self.label)

        self.logout = QPushButton(self.frame_2)
        self.logout.setObjectName(u"logout")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.logout.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icon/icons/logout_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout.setIcon(icon)
        self.logout.setIconSize(QSize(40, 40))

        self.horizontalLayout_19.addWidget(self.logout, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.update_btn = QPushButton(self.frame_6)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setMaximumSize(QSize(16777215, 40))
        self.update_btn.setFont(font1)

        self.gridLayout_3.addWidget(self.update_btn, 3, 1, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(20, 20))
        self.label_7.setMaximumSize(QSize(40, 40))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_7.setFont(font2)
        self.label_7.setPixmap(QPixmap(u":/icon/icons/home_icon.svg"))
        self.label_7.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.delete_btn = QPushButton(self.frame_6)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMaximumSize(QSize(16777215, 40))
        self.delete_btn.setFont(font1)

        self.gridLayout_3.addWidget(self.delete_btn, 4, 1, 1, 1)

        self.home_btn = QPushButton(self.frame_6)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(0, 0))
        self.home_btn.setMaximumSize(QSize(16777215, 40))
        self.home_btn.setFont(font1)

        self.gridLayout_3.addWidget(self.home_btn, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(20, 20))
        self.label_5.setMaximumSize(QSize(40, 40))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_5.setFont(font3)
        self.label_5.setPixmap(QPixmap(u":/icon/icons/delete_icon.svg"))
        self.label_5.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.restore_2 = QPushButton(self.frame_6)
        self.restore_2.setObjectName(u"restore_2")
        self.restore_2.setMaximumSize(QSize(16777215, 40))
        self.restore_2.setFont(font1)

        self.gridLayout_3.addWidget(self.restore_2, 6, 1, 1, 1)

        self.insert_btn = QPushButton(self.frame_6)
        self.insert_btn.setObjectName(u"insert_btn")
        self.insert_btn.setMaximumSize(QSize(16777215, 40))
        self.insert_btn.setFont(font1)

        self.gridLayout_3.addWidget(self.insert_btn, 1, 1, 1, 1)

        self.search_btn = QPushButton(self.frame_6)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMaximumSize(QSize(16777215, 40))
        self.search_btn.setFont(font1)

        self.gridLayout_3.addWidget(self.search_btn, 5, 1, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(20, 20))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setFont(font3)
        self.label_6.setPixmap(QPixmap(u":/icon/icons/search_icon.svg"))
        self.label_6.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(20, 20))
        self.label_3.setMaximumSize(QSize(40, 40))
        self.label_3.setFont(font3)
        self.label_3.setPixmap(QPixmap(u":/icon/icons/add_icon.svg"))
        self.label_3.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(20, 20))
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setFont(font3)
        self.label_4.setPixmap(QPixmap(u":/icon/icons/update_icon.svg"))
        self.label_4.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(20, 20))
        self.label_16.setMaximumSize(QSize(40, 40))
        self.label_16.setPixmap(QPixmap(u"icons/icons8-upward-arrow-64.png"))
        self.label_16.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_16, 3, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_6, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.update = QWidget()
        self.update.setObjectName(u"update")
        self.horizontalLayout_16 = QHBoxLayout(self.update)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_34 = QFrame(self.update)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_34)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_34)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_60 = QLabel(self.frame_38)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(170, 16777215))
        self.label_60.setFont(font1)

        self.horizontalLayout_24.addWidget(self.label_60)

        self.u_search_bar_3 = QLineEdit(self.frame_38)
        self.u_search_bar_3.setObjectName(u"u_search_bar_3")
        self.u_search_bar_3.setMinimumSize(QSize(225, 0))
        self.u_search_bar_3.setMaximumSize(QSize(300, 16777215))
        font4 = QFont()
        font4.setPointSize(10)
        self.u_search_bar_3.setFont(font4)

        self.horizontalLayout_24.addWidget(self.u_search_bar_3)

        self.u_search_btn_3 = QPushButton(self.frame_38)
        self.u_search_btn_3.setObjectName(u"u_search_btn_3")
        self.u_search_btn_3.setMaximumSize(QSize(150, 150))
        self.u_search_btn_3.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/search-185.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.u_search_btn_3.setIcon(icon1)
        self.u_search_btn_3.setIconSize(QSize(35, 35))

        self.horizontalLayout_24.addWidget(self.u_search_btn_3)


        self.verticalLayout_23.addWidget(self.frame_38, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_47 = QFrame(self.frame_34)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy1.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy1)
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_65 = QFrame(self.frame_47)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(600, 0))
        self.frame_65.setMaximumSize(QSize(600, 16777215))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_65)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.u_dob_3 = QLabel(self.frame_65)
        self.u_dob_3.setObjectName(u"u_dob_3")

        self.gridLayout_20.addWidget(self.u_dob_3, 5, 1, 1, 1)

        self.label_72 = QLabel(self.frame_65)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font1)

        self.gridLayout_20.addWidget(self.label_72, 0, 0, 1, 1)

        self.label_73 = QLabel(self.frame_65)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font1)

        self.gridLayout_20.addWidget(self.label_73, 5, 0, 1, 1)

        self.label_62 = QLabel(self.frame_65)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font1)

        self.gridLayout_20.addWidget(self.label_62, 1, 0, 1, 1)

        self.u_phno_3 = QLabel(self.frame_65)
        self.u_phno_3.setObjectName(u"u_phno_3")

        self.gridLayout_20.addWidget(self.u_phno_3, 1, 1, 1, 1)

        self.u_type_3 = QLabel(self.frame_65)
        self.u_type_3.setObjectName(u"u_type_3")

        self.gridLayout_20.addWidget(self.u_type_3, 4, 1, 1, 1)

        self.label_74 = QLabel(self.frame_65)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font1)

        self.gridLayout_20.addWidget(self.label_74, 3, 2, 1, 1)

        self.u_relationship_3 = QLabel(self.frame_65)
        self.u_relationship_3.setObjectName(u"u_relationship_3")

        self.gridLayout_20.addWidget(self.u_relationship_3, 3, 1, 1, 1)

        self.u_name_3 = QLabel(self.frame_65)
        self.u_name_3.setObjectName(u"u_name_3")

        self.gridLayout_20.addWidget(self.u_name_3, 0, 1, 1, 1)

        self.label_75 = QLabel(self.frame_65)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font1)

        self.gridLayout_20.addWidget(self.label_75, 1, 2, 1, 1)

        self.label_76 = QLabel(self.frame_65)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font1)

        self.gridLayout_20.addWidget(self.label_76, 0, 2, 1, 1)

        self.label_77 = QLabel(self.frame_65)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font1)

        self.gridLayout_20.addWidget(self.label_77, 2, 0, 1, 1)

        self.u_email_3 = QLabel(self.frame_65)
        self.u_email_3.setObjectName(u"u_email_3")

        self.gridLayout_20.addWidget(self.u_email_3, 2, 1, 1, 1)

        self.label_78 = QLabel(self.frame_65)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font1)

        self.gridLayout_20.addWidget(self.label_78, 3, 0, 1, 1)

        self.label_79 = QLabel(self.frame_65)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font1)

        self.gridLayout_20.addWidget(self.label_79, 4, 0, 1, 1)

        self.label_80 = QLabel(self.frame_65)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font1)

        self.gridLayout_20.addWidget(self.label_80, 2, 2, 1, 1)

        self.u_hno_3 = QLabel(self.frame_65)
        self.u_hno_3.setObjectName(u"u_hno_3")

        self.gridLayout_20.addWidget(self.u_hno_3, 0, 3, 1, 1)

        self.u_hname_3 = QLabel(self.frame_65)
        self.u_hname_3.setObjectName(u"u_hname_3")

        self.gridLayout_20.addWidget(self.u_hname_3, 1, 3, 1, 1)

        self.u_area_3 = QLabel(self.frame_65)
        self.u_area_3.setObjectName(u"u_area_3")

        self.gridLayout_20.addWidget(self.u_area_3, 2, 3, 1, 1)

        self.label_81 = QLabel(self.frame_65)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font1)

        self.gridLayout_20.addWidget(self.label_81, 4, 2, 1, 1)

        self.u_city_3 = QLabel(self.frame_65)
        self.u_city_3.setObjectName(u"u_city_3")

        self.gridLayout_20.addWidget(self.u_city_3, 3, 3, 1, 1)

        self.u_state_3 = QLabel(self.frame_65)
        self.u_state_3.setObjectName(u"u_state_3")

        self.gridLayout_20.addWidget(self.u_state_3, 4, 3, 1, 1)

        self.label_82 = QLabel(self.frame_65)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font1)

        self.gridLayout_20.addWidget(self.label_82, 5, 2, 1, 1)

        self.u_pincode_3 = QLabel(self.frame_65)
        self.u_pincode_3.setObjectName(u"u_pincode_3")

        self.gridLayout_20.addWidget(self.u_pincode_3, 5, 3, 1, 1)


        self.horizontalLayout_40.addWidget(self.frame_65)


        self.verticalLayout_23.addWidget(self.frame_47)

        self.frame_66 = QFrame(self.frame_34)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_97 = QLabel(self.frame_66)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(50, 20))
        self.label_97.setMaximumSize(QSize(100, 50))
        self.label_97.setFont(font1)

        self.horizontalLayout_41.addWidget(self.label_97, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.update_combo = QComboBox(self.frame_66)
        self.update_combo.addItem("")
        self.update_combo.addItem("")
        self.update_combo.addItem("")
        self.update_combo.addItem("")
        self.update_combo.addItem("")
        self.update_combo.setObjectName(u"update_combo")
        self.update_combo.setMinimumSize(QSize(200, 0))
        self.update_combo.setFont(font1)

        self.horizontalLayout_41.addWidget(self.update_combo)

        self.update_item = QLineEdit(self.frame_66)
        self.update_item.setObjectName(u"update_item")
        self.update_item.setMinimumSize(QSize(200, 25))

        self.horizontalLayout_41.addWidget(self.update_item)

        self.u_update_btn_3 = QPushButton(self.frame_66)
        self.u_update_btn_3.setObjectName(u"u_update_btn_3")
        self.u_update_btn_3.setFont(font1)

        self.horizontalLayout_41.addWidget(self.u_update_btn_3)

        self.u_clear_btn_3 = QPushButton(self.frame_66)
        self.u_clear_btn_3.setObjectName(u"u_clear_btn_3")
        self.u_clear_btn_3.setFont(font1)

        self.horizontalLayout_41.addWidget(self.u_clear_btn_3)


        self.verticalLayout_23.addWidget(self.frame_66, 0, Qt.AlignHCenter)


        self.horizontalLayout_16.addWidget(self.frame_34)

        self.stackedWidget.addWidget(self.update)
        self.delete_2 = QWidget()
        self.delete_2.setObjectName(u"delete_2")
        self.verticalLayout_7 = QVBoxLayout(self.delete_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_19 = QFrame(self.delete_2)
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
        self.d_search_item = QComboBox(self.frame_21)
        self.d_search_item.addItem("")
        self.d_search_item.addItem("")
        self.d_search_item.setObjectName(u"d_search_item")
        self.d_search_item.setMinimumSize(QSize(170, 0))
        self.d_search_item.setMaximumSize(QSize(160, 16777215))
        font5 = QFont()
        font5.setPointSize(12)
        self.d_search_item.setFont(font5)

        self.horizontalLayout_12.addWidget(self.d_search_item)

        self.d_search_value = QLineEdit(self.frame_21)
        self.d_search_value.setObjectName(u"d_search_value")
        self.d_search_value.setMaximumSize(QSize(16777215, 16777215))
        self.d_search_value.setFont(font4)
        self.d_search_value.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_12.addWidget(self.d_search_value)

        self.d_search = QPushButton(self.frame_21)
        self.d_search.setObjectName(u"d_search")
        self.d_search.setFont(font1)
        self.d_search.setIcon(icon1)
        self.d_search.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.d_search)


        self.gridLayout_9.addWidget(self.frame_21, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_22)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.restore = QPushButton(self.frame_22)
        self.restore.setObjectName(u"restore")
        self.restore.setFont(font1)

        self.gridLayout_10.addWidget(self.restore, 0, 1, 1, 1)

        self.d_delete_btn = QPushButton(self.frame_22)
        self.d_delete_btn.setObjectName(u"d_delete_btn")
        self.d_delete_btn.setFont(font1)

        self.gridLayout_10.addWidget(self.d_delete_btn, 0, 0, 1, 1)

        self.p_delete = QPushButton(self.frame_22)
        self.p_delete.setObjectName(u"p_delete")
        self.p_delete.setFont(font1)

        self.gridLayout_10.addWidget(self.p_delete, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.frame_22, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.delete_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.tableWidget_8 = QTableWidget(self.frame_20)
        if (self.tableWidget_8.columnCount() < 17):
            self.tableWidget_8.setColumnCount(17)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font1);
        self.tableWidget_8.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        self.tableWidget_8.setObjectName(u"tableWidget_8")

        self.horizontalLayout_14.addWidget(self.tableWidget_8)


        self.verticalLayout_7.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.delete_2)
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
        self.search_2 = QPushButton(self.frame_10)
        self.search_2.setObjectName(u"search_2")
        self.search_2.setMinimumSize(QSize(350, 0))
        self.search_2.setMaximumSize(QSize(250, 16777215))
        self.search_2.setFont(font1)

        self.horizontalLayout_5.addWidget(self.search_2)

        self.search_all = QPushButton(self.frame_10)
        self.search_all.setObjectName(u"search_all")
        self.search_all.setMinimumSize(QSize(350, 0))
        self.search_all.setMaximumSize(QSize(350, 16777215))
        self.search_all.setFont(font1)

        self.horizontalLayout_5.addWidget(self.search_all)


        self.verticalLayout_4.addWidget(self.frame_10, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_11 = QFrame(self.search)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
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
        self.single_search_item = QComboBox(self.frame_12)
        self.single_search_item.addItem("")
        self.single_search_item.addItem("")
        self.single_search_item.setObjectName(u"single_search_item")
        self.single_search_item.setMaximumSize(QSize(170, 16777215))
        self.single_search_item.setFont(font1)

        self.horizontalLayout_7.addWidget(self.single_search_item)

        self.single_search_value = QLineEdit(self.frame_12)
        self.single_search_value.setObjectName(u"single_search_value")
        self.single_search_value.setMinimumSize(QSize(200, 0))
        self.single_search_value.setMaximumSize(QSize(250, 16777215))
        self.single_search_value.setFont(font4)

        self.horizontalLayout_7.addWidget(self.single_search_value)

        self.single_search_btn = QPushButton(self.frame_12)
        self.single_search_btn.setObjectName(u"single_search_btn")
        self.single_search_btn.setMaximumSize(QSize(125, 16777215))
        self.single_search_btn.setFont(font1)
        self.single_search_btn.setIcon(icon1)
        self.single_search_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.single_search_btn)


        self.verticalLayout_5.addWidget(self.frame_12, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_13 = QFrame(self.single_search)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tableWidget_4 = QTableWidget(self.frame_13)
        if (self.tableWidget_4.columnCount() < 17):
            self.tableWidget_4.setColumnCount(17)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(8, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(9, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(10, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(11, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(12, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(13, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(14, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(15, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font1);
        self.tableWidget_4.setHorizontalHeaderItem(16, __qtablewidgetitem33)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.horizontalLayout_8.addWidget(self.tableWidget_4)


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
        if (self.tableWidget_3.columnCount() < 17):
            self.tableWidget_3.setColumnCount(17)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(9, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(10, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(11, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(12, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(13, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(14, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(15, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(16, __qtablewidgetitem50)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.horizontalLayout_9.addWidget(self.tableWidget_3)


        self.horizontalLayout_10.addWidget(self.frame_14)

        self.stackedWidget_2.addWidget(self.all_search)

        self.horizontalLayout_6.addWidget(self.stackedWidget_2)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.search)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_29 = QFrame(self.page_2)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_29)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.r_show = QPushButton(self.frame_29)
        self.r_show.setObjectName(u"r_show")
        self.r_show.setMinimumSize(QSize(150, 0))
        self.r_show.setMaximumSize(QSize(150, 16777215))
        self.r_show.setFont(font1)

        self.gridLayout_2.addWidget(self.r_show, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_29, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_28 = QFrame(self.page_2)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy1.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy1)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.tableWidget_7 = QTableWidget(self.frame_28)
        if (self.tableWidget_7.columnCount() < 17):
            self.tableWidget_7.setColumnCount(17)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(5, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(6, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(7, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(8, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(9, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(10, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(11, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(12, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(13, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(14, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(15, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setFont(font1);
        self.tableWidget_7.setHorizontalHeaderItem(16, __qtablewidgetitem67)
        self.tableWidget_7.setObjectName(u"tableWidget_7")

        self.horizontalLayout_25.addWidget(self.tableWidget_7)


        self.verticalLayout_3.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.page_2)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_8 = QVBoxLayout(self.home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_15 = QFrame(self.home)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_15)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_15)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.home_combo = QComboBox(self.frame_24)
        self.home_combo.addItem("")
        self.home_combo.addItem("")
        self.home_combo.setObjectName(u"home_combo")
        self.home_combo.setMaximumSize(QSize(250, 16777215))
        self.home_combo.setFont(font1)

        self.horizontalLayout_15.addWidget(self.home_combo)

        self.home_show = QPushButton(self.frame_24)
        self.home_show.setObjectName(u"home_show")
        self.home_show.setMinimumSize(QSize(250, 0))
        self.home_show.setMaximumSize(QSize(250, 16777215))
        self.home_show.setFont(font1)

        self.horizontalLayout_15.addWidget(self.home_show)


        self.verticalLayout_6.addWidget(self.frame_24, 0, Qt.AlignHCenter)

        self.frame_25 = QFrame(self.frame_15)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.tableWidget_6 = QTableWidget(self.frame_25)
        if (self.tableWidget_6.columnCount() < 17):
            self.tableWidget_6.setColumnCount(17)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(6, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(7, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(8, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(9, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(10, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(11, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(12, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(13, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(14, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(15, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setFont(font1);
        self.tableWidget_6.setHorizontalHeaderItem(16, __qtablewidgetitem84)
        self.tableWidget_6.setObjectName(u"tableWidget_6")

        self.horizontalLayout_18.addWidget(self.tableWidget_6)


        self.verticalLayout_6.addWidget(self.frame_25)


        self.verticalLayout_8.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.home)
        self.insert = QWidget()
        self.insert.setObjectName(u"insert")
        self.gridLayout_5 = QGridLayout(self.insert)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_8 = QFrame(self.insert)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(600, 0))
        self.frame_18.setMaximumSize(QSize(600, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_18)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_9 = QLabel(self.frame_18)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_4.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_19 = QLabel(self.frame_18)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_4.addWidget(self.label_19, 5, 0, 1, 1)

        self.company = QLabel(self.frame_18)
        self.company.setObjectName(u"company")

        self.gridLayout_4.addWidget(self.company, 4, 1, 1, 1)

        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_4.addWidget(self.label_11, 7, 0, 1, 1)

        self.label_12 = QLabel(self.frame_18)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_4.addWidget(self.label_12, 8, 0, 1, 1)

        self.time_zone = QLabel(self.frame_18)
        self.time_zone.setObjectName(u"time_zone")

        self.gridLayout_4.addWidget(self.time_zone, 3, 1, 1, 1)

        self.location = QLabel(self.frame_18)
        self.location.setObjectName(u"location")

        self.gridLayout_4.addWidget(self.location, 5, 1, 1, 1)

        self.label_8 = QLabel(self.frame_18)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_14 = QLabel(self.frame_18)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_4.addWidget(self.label_14, 4, 0, 1, 1)

        self.i_phno = QLineEdit(self.frame_18)
        self.i_phno.setObjectName(u"i_phno")
        self.i_phno.setMaximumSize(QSize(250, 16777215))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setWeight(50)
        self.i_phno.setFont(font6)
        self.i_phno.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.i_phno, 2, 1, 1, 1)

        self.check = QPushButton(self.frame_18)
        self.check.setObjectName(u"check")
        self.check.setMinimumSize(QSize(0, 25))
        self.check.setIcon(icon1)

        self.gridLayout_4.addWidget(self.check, 2, 2, 1, 1)

        self.i_type = QComboBox(self.frame_18)
        self.i_type.addItem("")
        self.i_type.addItem("")
        self.i_type.setObjectName(u"i_type")
        self.i_type.setFont(font5)

        self.gridLayout_4.addWidget(self.i_type, 8, 1, 1, 1)

        self.i_relationship = QComboBox(self.frame_18)
        self.i_relationship.addItem("")
        self.i_relationship.addItem("")
        self.i_relationship.addItem("")
        self.i_relationship.addItem("")
        self.i_relationship.setObjectName(u"i_relationship")
        self.i_relationship.setFont(font5)

        self.gridLayout_4.addWidget(self.i_relationship, 7, 1, 1, 1)

        self.comboBox = QComboBox(self.frame_18)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 0))
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox.setFont(font1)

        self.gridLayout_4.addWidget(self.comboBox, 2, 0, 1, 1)

        self.i_name = QLineEdit(self.frame_18)
        self.i_name.setObjectName(u"i_name")
        self.i_name.setMaximumSize(QSize(250, 16777215))
        self.i_name.setFont(font6)
        self.i_name.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.i_name, 0, 1, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy2)
        self.frame_17.setMinimumSize(QSize(600, 0))
        self.frame_17.setMaximumSize(QSize(600, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_17)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.i_hname = QLineEdit(self.frame_17)
        self.i_hname.setObjectName(u"i_hname")
        self.i_hname.setMinimumSize(QSize(0, 0))
        self.i_hname.setMaximumSize(QSize(250, 16777215))
        self.i_hname.setFont(font5)
        self.i_hname.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.i_hname, 6, 1, 1, 1)

        self.i_email = QLineEdit(self.frame_17)
        self.i_email.setObjectName(u"i_email")
        self.i_email.setMaximumSize(QSize(250, 16777215))
        self.i_email.setFont(font6)
        self.i_email.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.i_email, 1, 1, 1, 1)

        self.label_24 = QLabel(self.frame_17)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.gridLayout_6.addWidget(self.label_24, 6, 0, 1, 1)

        self.label_25 = QLabel(self.frame_17)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.gridLayout_6.addWidget(self.label_25, 7, 0, 1, 1)

        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 1)

        self.i_pincode = QLineEdit(self.frame_17)
        self.i_pincode.setObjectName(u"i_pincode")
        self.i_pincode.setMinimumSize(QSize(0, 0))
        self.i_pincode.setMaximumSize(QSize(250, 16777215))
        self.i_pincode.setFont(font5)
        self.i_pincode.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.i_pincode, 8, 1, 1, 1)

        self.i_area = QLineEdit(self.frame_17)
        self.i_area.setObjectName(u"i_area")
        self.i_area.setMinimumSize(QSize(0, 0))
        self.i_area.setMaximumSize(QSize(250, 16777215))
        self.i_area.setFont(font5)
        self.i_area.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.i_area, 7, 1, 1, 1)

        self.i_hno = QLineEdit(self.frame_17)
        self.i_hno.setObjectName(u"i_hno")
        self.i_hno.setMinimumSize(QSize(0, 0))
        self.i_hno.setMaximumSize(QSize(250, 16777215))
        self.i_hno.setFont(font5)
        self.i_hno.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.i_hno, 5, 1, 1, 1)

        self.label_23 = QLabel(self.frame_17)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.gridLayout_6.addWidget(self.label_23, 5, 0, 1, 1)

        self.label_28 = QLabel(self.frame_17)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.gridLayout_6.addWidget(self.label_28, 8, 0, 1, 1)

        self.label_59 = QLabel(self.frame_17)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font1)

        self.gridLayout_6.addWidget(self.label_59, 0, 0, 1, 1)

        self.i_dob = QDateEdit(self.frame_17)
        self.i_dob.setObjectName(u"i_dob")
        self.i_dob.setFont(font6)

        self.gridLayout_6.addWidget(self.i_dob, 0, 1, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_17)


        self.verticalLayout_12.addWidget(self.frame_16)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_9)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.i_add = QPushButton(self.frame_23)
        self.i_add.setObjectName(u"i_add")
        self.i_add.setFont(font1)

        self.horizontalLayout_4.addWidget(self.i_add)

        self.i_clear_btn = QPushButton(self.frame_23)
        self.i_clear_btn.setObjectName(u"i_clear_btn")
        self.i_clear_btn.setFont(font1)

        self.horizontalLayout_4.addWidget(self.i_clear_btn)


        self.horizontalLayout_3.addWidget(self.frame_23)


        self.verticalLayout_12.addWidget(self.frame_9, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_7, 0, Qt.AlignLeft)

        self.frame_26 = QFrame(self.frame_8)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.tableWidget_9 = QTableWidget(self.frame_26)
        if (self.tableWidget_9.columnCount() < 17):
            self.tableWidget_9.setColumnCount(17)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(0, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(1, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(2, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(3, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(4, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(5, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(6, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(7, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(8, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(9, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(10, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(11, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(12, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(13, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(14, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(15, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setFont(font1);
        self.tableWidget_9.setHorizontalHeaderItem(16, __qtablewidgetitem101)
        self.tableWidget_9.setObjectName(u"tableWidget_9")

        self.horizontalLayout_20.addWidget(self.tableWidget_9)


        self.verticalLayout_11.addWidget(self.frame_26)


        self.gridLayout_5.addWidget(self.frame_8, 2, 0, 1, 2)

        self.stackedWidget.addWidget(self.insert)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_13.addWidget(self.frame)

        self.stackedWidget_3.addWidget(self.main_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_37 = QHBoxLayout(self.page)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.stackedWidget_3.addWidget(self.page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.horizontalLayout_23 = QHBoxLayout(self.login_page)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_41 = QFrame(self.login_page)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"border:none;\n"
"background-color: rgb(224, 254, 255);\n"
"")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_27 = QFrame(self.frame_41)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"border:none;\n"
"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_13 = QLabel(self.frame_27)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"border-radius:10px;")
        self.label_13.setPixmap(QPixmap(u"icons/19101755522phonebook.jpg"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_13)


        self.horizontalLayout_22.addWidget(self.frame_27)

        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(600, 500))
        self.frame_42.setMaximumSize(QSize(600, 600))
        self.frame_42.setStyleSheet(u"")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setGeometry(QRect(150, 140, 300, 250))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy3)
        self.frame_43.setMinimumSize(QSize(300, 250))
        self.frame_43.setMaximumSize(QSize(600, 100))
        self.frame_43.setStyleSheet(u"border:1px solid black;\n"
"border-radius:25px;\n"
"background-color: rgb(229, 255, 255);")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.user_login = QLineEdit(self.frame_43)
        self.user_login.setObjectName(u"user_login")
        self.user_login.setGeometry(QRect(70, 89, 210, 31))
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(40)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.user_login.sizePolicy().hasHeightForWidth())
        self.user_login.setSizePolicy(sizePolicy4)
        self.user_login.setMinimumSize(QSize(40, 20))
        self.user_login.setFont(font4)
        self.user_login.setStyleSheet(u"	background-color: transparent;\n"
"background-color: rgb(253, 225, 255);\n"
"color: rgb(0, 0, 0);")
        self.password_login = QLineEdit(self.frame_43)
        self.password_login.setObjectName(u"password_login")
        self.password_login.setGeometry(QRect(70, 159, 210, 31))
        self.password_login.setMinimumSize(QSize(0, 20))
        self.password_login.setBaseSize(QSize(20, 20))
        self.password_login.setFont(font4)
        self.password_login.setStyleSheet(u"	background-color: transparent;\n"
"background-color: rgb(255, 220, 255);")
        self.password_login.setEchoMode(QLineEdit.Password)
        self.label_31 = QLabel(self.frame_43)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 80, 50, 50))
        self.label_31.setMinimumSize(QSize(40, 40))
        self.label_31.setMaximumSize(QSize(50, 50))
        self.label_31.setSizeIncrement(QSize(0, 0))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(0, 0, 127);")
        self.label_31.setPixmap(QPixmap(u"im.png"))
        self.label_31.setScaledContents(True)
        self.label_50 = QLabel(self.frame_43)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 150, 50, 50))
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        self.label_50.setMinimumSize(QSize(30, 30))
        self.label_50.setMaximumSize(QSize(50, 50))
        self.label_50.setFont(font1)
        self.label_50.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(0, 0, 127);")
        self.label_50.setPixmap(QPixmap(u"../../Downloads/user (7).png"))
        self.label_50.setScaledContents(True)
        self.label_51 = QLabel(self.frame_43)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(100, -50, 100, 100))
        self.label_51.setMinimumSize(QSize(50, 50))
        self.label_51.setMaximumSize(QSize(100, 100))
        self.label_51.setFont(font1)
        self.label_51.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:50px;")
        self.label_51.setPixmap(QPixmap(u"../../Downloads/user (6).png"))
        self.label_51.setScaledContents(True)
        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setGeometry(QRect(-10, 0, 611, 106))
        self.frame_44.setMinimumSize(QSize(100, 100))
        font7 = QFont()
        font7.setPointSize(23)
        self.frame_44.setFont(font7)
        self.frame_44.setStyleSheet(u"border:none;\n"
"background-color: transparent;")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_44)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 20, 591, 81))
        font8 = QFont()
        font8.setPointSize(23)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_15.setFont(font8)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.frame_45 = QFrame(self.frame_42)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setGeometry(QRect(210, 410, 191, 44))
        self.frame_45.setStyleSheet(u"border:1px solid black;\n"
"border-radius:20px;\n"
"background-color:rgb(218,218,218);")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_45)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.login_btn_3 = QPushButton(self.frame_45)
        self.login_btn_3.setObjectName(u"login_btn_3")
        self.login_btn_3.setFont(font1)
        self.login_btn_3.setStyleSheet(u"border-radius:10px;\n"
"color: rgb(0, 0, 0);\n"
"border:none;")

        self.gridLayout_16.addWidget(self.login_btn_3, 0, 0, 1, 1)

        self.label_52 = QLabel(self.frame_42)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(250, 90, 100, 100))
        self.label_52.setMinimumSize(QSize(50, 50))
        self.label_52.setMaximumSize(QSize(100, 100))
        self.label_52.setFont(font1)
        self.label_52.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:50px;")
        self.label_52.setPixmap(QPixmap(u"../../Downloads/user (6).png"))
        self.label_52.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.frame_42, 0, Qt.AlignHCenter)


        self.horizontalLayout_23.addWidget(self.frame_41)

        self.stackedWidget_3.addWidget(self.login_page)

        self.horizontalLayout_17.addWidget(self.stackedWidget_3)


        self.gridLayout.addWidget(self.frame_33, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_3.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"PHONE BOOK", None))
        self.logout.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_7.setText("")
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_5.setText("")
        self.restore_2.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
        self.insert_btn.setText(QCoreApplication.translate("MainWindow", u"Add contact ", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_6.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_16.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Number", None))
        self.u_search_bar_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"911234567890", None))
        self.u_search_btn_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.u_dob_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Date_of_Birth", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Number", None))
        self.u_phno_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.u_type_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.u_relationship_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.u_name_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"HouseName", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"HouseNo", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.u_email_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Relationship", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.u_hno_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.u_hname_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.u_area_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.u_city_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.u_state_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Pincode", None))
        self.u_pincode_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.update_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.update_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Email", None))
        self.update_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"HouseNo", None))
        self.update_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"HouseName", None))
        self.update_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"Area", None))

        self.update_item.setText("")
        self.u_update_btn_3.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.u_clear_btn_3.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.d_search_item.setItemText(0, QCoreApplication.translate("MainWindow", u"Mobile Number", None))
        self.d_search_item.setItemText(1, QCoreApplication.translate("MainWindow", u"C_id", None))

        self.d_search_value.setPlaceholderText("")
        self.d_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.restore.setText(QCoreApplication.translate("MainWindow", u"RESTORE", None))
        self.d_delete_btn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.p_delete.setText(QCoreApplication.translate("MainWindow", u"PERMANENT DELETE", None))
        ___qtablewidgetitem = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C_id", None));
        ___qtablewidgetitem1 = self.tableWidget_8.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget_8.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.tableWidget_8.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem4 = self.tableWidget_8.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Relationship", None));
        ___qtablewidgetitem5 = self.tableWidget_8.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem6 = self.tableWidget_8.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Date_of_Birth", None));
        ___qtablewidgetitem7 = self.tableWidget_8.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Hno", None));
        ___qtablewidgetitem8 = self.tableWidget_8.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Hname", None));
        ___qtablewidgetitem9 = self.tableWidget_8.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Area", None));
        ___qtablewidgetitem10 = self.tableWidget_8.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem11 = self.tableWidget_8.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem12 = self.tableWidget_8.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"PinCode", None));
        ___qtablewidgetitem13 = self.tableWidget_8.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Zone", None));
        ___qtablewidgetitem14 = self.tableWidget_8.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem15 = self.tableWidget_8.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem16 = self.tableWidget_8.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Phone_Type", None));
        self.search_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_all.setText(QCoreApplication.translate("MainWindow", u"All Contact", None))
        self.single_search_item.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.single_search_item.setItemText(1, QCoreApplication.translate("MainWindow", u"Mobile Number", None))

        self.single_search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem17 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"C_id", None));
        ___qtablewidgetitem18 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Relationship", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem23 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Date_of_Birth", None));
        ___qtablewidgetitem24 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Hno", None));
        ___qtablewidgetitem25 = self.tableWidget_4.horizontalHeaderItem(8)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Hname", None));
        ___qtablewidgetitem26 = self.tableWidget_4.horizontalHeaderItem(9)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Area", None));
        ___qtablewidgetitem27 = self.tableWidget_4.horizontalHeaderItem(10)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem28 = self.tableWidget_4.horizontalHeaderItem(11)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem29 = self.tableWidget_4.horizontalHeaderItem(12)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"PinCode", None));
        ___qtablewidgetitem30 = self.tableWidget_4.horizontalHeaderItem(13)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Zone", None));
        ___qtablewidgetitem31 = self.tableWidget_4.horizontalHeaderItem(14)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem32 = self.tableWidget_4.horizontalHeaderItem(15)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem33 = self.tableWidget_4.horizontalHeaderItem(16)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Phone_Type", None));
        ___qtablewidgetitem34 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"C_id", None));
        ___qtablewidgetitem35 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem36 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem37 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem38 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Relationship", None));
        ___qtablewidgetitem39 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem40 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Date_of_Birth", None));
        ___qtablewidgetitem41 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Hno", None));
        ___qtablewidgetitem42 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Hname", None));
        ___qtablewidgetitem43 = self.tableWidget_3.horizontalHeaderItem(9)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Area", None));
        ___qtablewidgetitem44 = self.tableWidget_3.horizontalHeaderItem(10)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem45 = self.tableWidget_3.horizontalHeaderItem(11)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem46 = self.tableWidget_3.horizontalHeaderItem(12)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"PinCode", None));
        ___qtablewidgetitem47 = self.tableWidget_3.horizontalHeaderItem(13)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Zone", None));
        ___qtablewidgetitem48 = self.tableWidget_3.horizontalHeaderItem(14)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem49 = self.tableWidget_3.horizontalHeaderItem(15)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem50 = self.tableWidget_3.horizontalHeaderItem(16)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Phone_Type", None));
        self.r_show.setText(QCoreApplication.translate("MainWindow", u"SHOW", None))
        ___qtablewidgetitem51 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"C_id", None));
        ___qtablewidgetitem52 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem53 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem54 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem55 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Relationship", None));
        ___qtablewidgetitem56 = self.tableWidget_7.horizontalHeaderItem(5)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem57 = self.tableWidget_7.horizontalHeaderItem(6)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Date_of_Birth", None));
        ___qtablewidgetitem58 = self.tableWidget_7.horizontalHeaderItem(7)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Hno", None));
        ___qtablewidgetitem59 = self.tableWidget_7.horizontalHeaderItem(8)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Hname", None));
        ___qtablewidgetitem60 = self.tableWidget_7.horizontalHeaderItem(9)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Area", None));
        ___qtablewidgetitem61 = self.tableWidget_7.horizontalHeaderItem(10)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem62 = self.tableWidget_7.horizontalHeaderItem(11)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem63 = self.tableWidget_7.horizontalHeaderItem(12)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"PinCode", None));
        ___qtablewidgetitem64 = self.tableWidget_7.horizontalHeaderItem(13)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Zone", None));
        ___qtablewidgetitem65 = self.tableWidget_7.horizontalHeaderItem(14)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem66 = self.tableWidget_7.horizontalHeaderItem(15)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem67 = self.tableWidget_7.horizontalHeaderItem(16)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Phone_Type", None));
        self.home_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Mobile Number", None))
        self.home_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Land Line Number", None))

        self.home_show.setText(QCoreApplication.translate("MainWindow", u"SHOW", None))
        ___qtablewidgetitem68 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"C_id", None));
        ___qtablewidgetitem69 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem70 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem71 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem72 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Relationship", None));
        ___qtablewidgetitem73 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem74 = self.tableWidget_6.horizontalHeaderItem(6)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Date_of_Birth", None));
        ___qtablewidgetitem75 = self.tableWidget_6.horizontalHeaderItem(7)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Hno", None));
        ___qtablewidgetitem76 = self.tableWidget_6.horizontalHeaderItem(8)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Hname", None));
        ___qtablewidgetitem77 = self.tableWidget_6.horizontalHeaderItem(9)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Area", None));
        ___qtablewidgetitem78 = self.tableWidget_6.horizontalHeaderItem(10)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem79 = self.tableWidget_6.horizontalHeaderItem(11)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem80 = self.tableWidget_6.horizontalHeaderItem(12)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"PinCode", None));
        ___qtablewidgetitem81 = self.tableWidget_6.horizontalHeaderItem(13)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Zone", None));
        ___qtablewidgetitem82 = self.tableWidget_6.horizontalHeaderItem(14)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem83 = self.tableWidget_6.horizontalHeaderItem(15)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem84 = self.tableWidget_6.horizontalHeaderItem(16)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Phone_Type", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Time Zone", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.company.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Relationship", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.time_zone.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.location.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Company", None))
        self.i_phno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"+0001234567890", None))
        self.check.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.i_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Work", None))
        self.i_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Personal", None))

        self.i_relationship.setItemText(0, QCoreApplication.translate("MainWindow", u"Friends", None))
        self.i_relationship.setItemText(1, QCoreApplication.translate("MainWindow", u"Collegues", None))
        self.i_relationship.setItemText(2, QCoreApplication.translate("MainWindow", u"Family", None))
        self.i_relationship.setItemText(3, QCoreApplication.translate("MainWindow", u"Others", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Mobile Number", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Land Line Number", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"HouseName", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"HouseNo", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Pincode", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Date_of_Birth", None))
        self.i_add.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.i_clear_btn.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        ___qtablewidgetitem85 = self.tableWidget_9.horizontalHeaderItem(0)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"C_id", None));
        ___qtablewidgetitem86 = self.tableWidget_9.horizontalHeaderItem(1)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem87 = self.tableWidget_9.horizontalHeaderItem(2)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem88 = self.tableWidget_9.horizontalHeaderItem(3)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem89 = self.tableWidget_9.horizontalHeaderItem(4)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Relationship", None));
        ___qtablewidgetitem90 = self.tableWidget_9.horizontalHeaderItem(5)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem91 = self.tableWidget_9.horizontalHeaderItem(6)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Date_of_Birth", None));
        ___qtablewidgetitem92 = self.tableWidget_9.horizontalHeaderItem(7)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Hno", None));
        ___qtablewidgetitem93 = self.tableWidget_9.horizontalHeaderItem(8)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Hname", None));
        ___qtablewidgetitem94 = self.tableWidget_9.horizontalHeaderItem(9)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Area", None));
        ___qtablewidgetitem95 = self.tableWidget_9.horizontalHeaderItem(10)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem96 = self.tableWidget_9.horizontalHeaderItem(11)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem97 = self.tableWidget_9.horizontalHeaderItem(12)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"PinCode", None));
        ___qtablewidgetitem98 = self.tableWidget_9.horizontalHeaderItem(13)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Zone", None));
        ___qtablewidgetitem99 = self.tableWidget_9.horizontalHeaderItem(14)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem100 = self.tableWidget_9.horizontalHeaderItem(15)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem101 = self.tableWidget_9.horizontalHeaderItem(16)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Phone_Type", None));
        self.label_13.setText("")
        self.user_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User", None))
        self.password_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_31.setText("")
        self.label_50.setText("")
        self.label_51.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"PHONE BOOK MANAGEMENT", None))
        self.login_btn_3.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_52.setText("")
    # retranslateUi

