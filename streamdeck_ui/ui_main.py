# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(890, 860)
        MainWindow.setMinimumSize(QSize(890, 860))
        MainWindow.setStyleSheet(u"background-color: #2C2C2C;\n"
"color: #FFF;")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDocs = QAction(MainWindow)
        self.actionDocs.setObjectName(u"actionDocs")
        self.actionGithub = QAction(MainWindow)
        self.actionGithub.setObjectName(u"actionGithub")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_horizontalLayout = QHBoxLayout()
        self.main_horizontalLayout.setSpacing(0)
        self.main_horizontalLayout.setObjectName(u"main_horizontalLayout")
        self.main_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_verticalLayout = QVBoxLayout()
        self.left_verticalLayout.setSpacing(0)
        self.left_verticalLayout.setObjectName(u"left_verticalLayout")
        self.left_verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.left_verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.deviceSettings_horizontalLayout = QHBoxLayout()
        self.deviceSettings_horizontalLayout.setObjectName(u"deviceSettings_horizontalLayout")
        self.deviceSettings_horizontalLayout.setContentsMargins(0, 0, 0, 6)
        self.device_list = QComboBox(self.centralwidget)
        self.device_list.setObjectName(u"device_list")
        self.device_list.setMinimumSize(QSize(580, 25))
        self.device_list.setStyleSheet(u"background-color:#2C2C2C;border: none;")

        self.deviceSettings_horizontalLayout.addWidget(self.device_list)

        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy)
        self.settingsButton.setMinimumSize(QSize(0, 0))
        self.settingsButton.setMaximumSize(QSize(30, 16777215))
        self.settingsButton.setLayoutDirection(Qt.LeftToRight)
        self.settingsButton.setStyleSheet(u"border:none;margin-left:5;margin-right:5;color: #999998;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon)
        self.settingsButton.setIconSize(QSize(20, 20))

        self.deviceSettings_horizontalLayout.addWidget(self.settingsButton)


        self.left_verticalLayout.addLayout(self.deviceSettings_horizontalLayout)

        self.pages = QTabWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy1)
        self.pages.setMinimumSize(QSize(580, 400))
        self.pages.setAutoFillBackground(False)
        self.pages.setStyleSheet(u"background-color:#2C2C2C;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-top: none;\n"
"border-bottom: 1;\n"
"border-bottom-color: #1C1C1C;")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"background-color:#2C2C2C;border: none;")
        self.gridLayout_2 = QGridLayout(self.page_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.pages.addTab(self.page_1, "")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color:#2C2C2C;border: none;")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pages.addTab(self.page_2, "")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background-color:#2C2C2C;border: none;")
        self.gridLayout_11 = QGridLayout(self.page_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pages.addTab(self.page_3, "")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"background-color:#2C2C2C;border: none;")
        self.gridLayout_10 = QGridLayout(self.page_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pages.addTab(self.page_4, "")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"background-color:#2C2C2C;border: none;")
        self.gridLayout_9 = QGridLayout(self.page_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pages.addTab(self.page_5, "")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setStyleSheet(u"background-color:#2C2C2C;border: none;")
        self.gridLayout_8 = QGridLayout(self.page_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pages.addTab(self.page_6, "")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setStyleSheet(u"background-color:#2C2C2C;border: none;")
        self.gridLayout_7 = QGridLayout(self.page_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pages.addTab(self.page_7, "")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setStyleSheet(u"background-color:#2C2C2C;border: none;")
        self.gridLayout_6 = QGridLayout(self.page_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pages.addTab(self.page_8, "")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.page_9.setStyleSheet(u"background-color:#2C2C2C;border: none;")
        self.gridLayout_5 = QGridLayout(self.page_9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pages.addTab(self.page_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tab_10.setStyleSheet(u"background-color:#2C2C2C;border: none;")
        self.gridLayout_4 = QGridLayout(self.tab_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pages.addTab(self.tab_10, "")

        self.left_verticalLayout.addWidget(self.pages)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(580, 368))
        self.groupBox.setStyleSheet(u"background-color: #292929;border: none;")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(10, 20, 10, 20)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #818079")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imageButton = QPushButton(self.groupBox)
        self.imageButton.setObjectName(u"imageButton")
        self.imageButton.setMinimumSize(QSize(0, 25))
        self.imageButton.setStyleSheet(u"background-color:#3D3D3D;border: none;")

        self.horizontalLayout_2.addWidget(self.imageButton)

        self.removeButton = QPushButton(self.groupBox)
        self.removeButton.setObjectName(u"removeButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy2)
        self.removeButton.setMaximumSize(QSize(30, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.removeButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.removeButton)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #818079")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #818079")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.command = QLineEdit(self.groupBox)
        self.command.setObjectName(u"command")
        self.command.setMinimumSize(QSize(0, 25))
        self.command.setStyleSheet(u"background-color:#3D3D3D;border: none;")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.command)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: #818079")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.keys = QComboBox(self.groupBox)
        self.keys.addItem(u"")
        self.keys.addItem(u"F11")
        self.keys.addItem(u"alt+F4")
        self.keys.addItem(u"ctrl+w")
        self.keys.addItem(u"cmd+left")
        self.keys.addItem(u"alt+plus")
        self.keys.addItem(u"alt+delay+F3")
        self.keys.addItem(u"backspace")
        self.keys.addItem(u"right")
        self.keys.addItem(u"page_up")
        self.keys.addItem(u"media_volume_up")
        self.keys.addItem(u"media_volume_down")
        self.keys.addItem(u"media_volume_mute")
        self.keys.addItem(u"media_previous")
        self.keys.addItem(u"media_next")
        self.keys.addItem(u"media_play_pause")
        self.keys.setObjectName(u"keys")
        self.keys.setMinimumSize(QSize(0, 25))
        self.keys.setStyleSheet(u"background-color:#3D3D3D;border: none;")
        self.keys.setEditable(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.keys)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: #818079")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.switch_page = QSpinBox(self.groupBox)
        self.switch_page.setObjectName(u"switch_page")
        self.switch_page.setMinimumSize(QSize(0, 25))
        self.switch_page.setStyleSheet(u"background-color:#3D3D3D;border: none;")
        self.switch_page.setMinimum(0)
        self.switch_page.setMaximum(10)
        self.switch_page.setValue(0)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.switch_page)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: #818079")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.change_brightness = QSpinBox(self.groupBox)
        self.change_brightness.setObjectName(u"change_brightness")
        self.change_brightness.setMinimumSize(QSize(0, 25))
        self.change_brightness.setStyleSheet(u"background-color:#3D3D3D;border: none;")
        self.change_brightness.setMinimum(-99)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.change_brightness)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: #818079")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.write = QPlainTextEdit(self.groupBox)
        self.write.setObjectName(u"write")
        self.write.setStyleSheet(u"background-color:#3D3D3D;border: none;")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.write)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.text = QLineEdit(self.groupBox)
        self.text.setObjectName(u"text")
        self.text.setMinimumSize(QSize(0, 25))
        self.text.setStyleSheet(u"background-color:#3D3D3D;border: none;")

        self.horizontalLayout_3.addWidget(self.text)

        self.textButton = QPushButton(self.groupBox)
        self.textButton.setObjectName(u"textButton")
        self.textButton.setMinimumSize(QSize(30, 0))
        self.textButton.setMaximumSize(QSize(30, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/vertical-align.png", QSize(), QIcon.Normal, QIcon.Off)
        self.textButton.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.textButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.left_verticalLayout.addWidget(self.groupBox)

        self.left_verticalLayout.setStretch(1, 1)

        self.main_horizontalLayout.addLayout(self.left_verticalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(250, 0))
        self.groupBox_2.setStyleSheet(u"background-color:#242424;border: none;")
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(0, 0, 250, 35))
        self.lineEdit_2.setMinimumSize(QSize(0, 35))
        self.lineEdit_2.setSizeIncrement(QSize(0, 35))
        self.lineEdit_2.setBaseSize(QSize(0, 35))
        self.lineEdit_2.setStyleSheet(u"background-color:#383838;margin:5;border-radius:5;")

        self.verticalLayout.addWidget(self.groupBox_2)


        self.main_horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.main_horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 890, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.device_list, self.settingsButton)
        QWidget.setTabOrder(self.settingsButton, self.pages)
        QWidget.setTabOrder(self.pages, self.imageButton)
        QWidget.setTabOrder(self.imageButton, self.removeButton)
        QWidget.setTabOrder(self.removeButton, self.text)
        QWidget.setTabOrder(self.text, self.textButton)
        QWidget.setTabOrder(self.textButton, self.command)
        QWidget.setTabOrder(self.command, self.keys)
        QWidget.setTabOrder(self.keys, self.switch_page)
        QWidget.setTabOrder(self.switch_page, self.change_brightness)
        QWidget.setTabOrder(self.change_brightness, self.write)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDocs)
        self.menuHelp.addAction(self.actionGithub)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"STREAM DECK UI", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionDocs.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionGithub.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About...", None))
        self.settingsButton.setText("")
        self.pages.setTabText(self.pages.indexOf(self.page_1), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.pages.setTabText(self.pages.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"2", None))
        self.pages.setTabText(self.pages.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"3", None))
        self.pages.setTabText(self.pages.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"4", None))
        self.pages.setTabText(self.pages.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"5", None))
        self.pages.setTabText(self.pages.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"6", None))
        self.pages.setTabText(self.pages.indexOf(self.page_7), QCoreApplication.translate("MainWindow", u"7", None))
        self.pages.setTabText(self.pages.indexOf(self.page_8), QCoreApplication.translate("MainWindow", u"8", None))
        self.pages.setTabText(self.pages.indexOf(self.page_9), QCoreApplication.translate("MainWindow", u"9", None))
        self.pages.setTabText(self.pages.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"10", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
        self.imageButton.setText(QCoreApplication.translate("MainWindow", u"Image...", None))
#if QT_CONFIG(tooltip)
        self.removeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Remove the image from the button", None))
#endif // QT_CONFIG(tooltip)
        self.removeButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Label:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Command:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Press Keys:", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Switch Page:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Brightness +/-:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Write Text:", None))
#if QT_CONFIG(tooltip)
        self.textButton.setToolTip(QCoreApplication.translate("MainWindow", u"Text vertical alignment", None))
#endif // QT_CONFIG(tooltip)
        self.textButton.setText("")
        self.groupBox_2.setTitle("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

