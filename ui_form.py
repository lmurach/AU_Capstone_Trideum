"""
Author  : pyuic5    (auto generation command ran by Wesley Cooke) 
Date    : 02/12/24
Purpose : This file is auto generated using the command 
          'pyuic5 -o ui_form.py FRCS.py'
          This tells pyuic to generate a file named 'ui_form'
          from the ui design file named 'FRCS.py' 
          
          Make sure pyqt5 and required tools are properlly installed. 
          
          I reiterate Pyuic's warning: 
          Any manual changes made to this file will be lost when pyuic5 is
          run again. Do not edit this file unless you know what you are doing!
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FRCS.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1382, 757))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.top_floor_elevator_request = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_elevator_request.setFont(font)
        self.top_floor_elevator_request.setObjectName("top_floor_elevator_request")
        self.gridLayout.addWidget(self.top_floor_elevator_request, 2, 3, 1, 1)
        self.top_floor_activate_on = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_activate_on.setFont(font)
        self.top_floor_activate_on.setObjectName("top_floor_activate_on")
        self.gridLayout.addWidget(self.top_floor_activate_on, 2, 1, 1, 1)
        self.top_floor_temp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_floor_temp.sizePolicy().hasHeightForWidth())
        self.top_floor_temp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_temp.setFont(font)
        self.top_floor_temp.setStyleSheet("border: 3px solid green;\n"
"border-radius: 40px;\n"
"background-color: lightGreen;\n"
"")
        self.top_floor_temp.setObjectName("top_floor_temp")
        self.gridLayout.addWidget(self.top_floor_temp, 1, 1, 1, 1)
        self.bottom_floor_elevator = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_elevator.sizePolicy().hasHeightForWidth())
        self.bottom_floor_elevator.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_elevator.setFont(font)
        self.bottom_floor_elevator.setStyleSheet("border: 3px solid red;\n"
"border-radius: 40px;\n"
"background-color: pink\n"
";\n"
"")
        self.bottom_floor_elevator.setObjectName("bottom_floor_elevator")
        self.gridLayout.addWidget(self.bottom_floor_elevator, 7, 3, 1, 1)
        self.middle_floor_temp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_floor_temp.sizePolicy().hasHeightForWidth())
        self.middle_floor_temp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_temp.setFont(font)
        self.middle_floor_temp.setStyleSheet("border: 3px solid green;\n"
"border-radius: 40px;\n"
"background-color: lightGreen;\n"
"")
        self.middle_floor_temp.setObjectName("middle_floor_temp")
        self.gridLayout.addWidget(self.middle_floor_temp, 4, 1, 1, 1)
        self.middle_floor_motion = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_floor_motion.sizePolicy().hasHeightForWidth())
        self.middle_floor_motion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_motion.setFont(font)
        self.middle_floor_motion.setStyleSheet("border: 3px solid green;\n"
"border-radius: 40px;\n"
"background-color: lightGreen;\n"
"")
        self.middle_floor_motion.setObjectName("middle_floor_motion")
        self.gridLayout.addWidget(self.middle_floor_motion, 4, 2, 1, 1)
        self.top_floor_elevator = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_floor_elevator.sizePolicy().hasHeightForWidth())
        self.top_floor_elevator.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_elevator.setFont(font)
        self.top_floor_elevator.setStyleSheet("border: 3px solid yellow;\n"
"border-radius: 40px;\n"
"background-color: lightYellow;\n"
"")
        self.top_floor_elevator.setObjectName("top_floor_elevator")
        self.gridLayout.addWidget(self.top_floor_elevator, 1, 3, 1, 1)
        self.bottom_floor_motion = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_motion.sizePolicy().hasHeightForWidth())
        self.bottom_floor_motion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_motion.setFont(font)
        self.bottom_floor_motion.setStyleSheet("border: 3px solid red;\n"
"border-radius: 40px;\n"
"background-color: pink;\n"
"")
        self.bottom_floor_motion.setObjectName("bottom_floor_motion")
        self.gridLayout.addWidget(self.bottom_floor_motion, 7, 2, 1, 1)
        self.bottom_floor_temp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_temp.sizePolicy().hasHeightForWidth())
        self.bottom_floor_temp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_temp.setFont(font)
        self.bottom_floor_temp.setStyleSheet("border: 3px solid red;\n"
"border-radius: 40px;\n"
"background-color: pink;\n"
"")
        self.bottom_floor_temp.setObjectName("bottom_floor_temp")
        self.gridLayout.addWidget(self.bottom_floor_temp, 7, 1, 1, 1)
        self.middle_floor_activate_on = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_activate_on.setFont(font)
        self.middle_floor_activate_on.setObjectName("middle_floor_activate_on")
        self.gridLayout.addWidget(self.middle_floor_activate_on, 5, 1, 1, 1)
        self.middle_floor_elevator_request = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_elevator_request.setFont(font)
        self.middle_floor_elevator_request.setObjectName("middle_floor_elevator_request")
        self.gridLayout.addWidget(self.middle_floor_elevator_request, 5, 3, 1, 1)
        self.bottom_floor_elevator_request = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_elevator_request.setFont(font)
        self.bottom_floor_elevator_request.setObjectName("bottom_floor_elevator_request")
        self.gridLayout.addWidget(self.bottom_floor_elevator_request, 8, 3, 1, 1)
        self.middle_floor_elevator = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_floor_elevator.sizePolicy().hasHeightForWidth())
        self.middle_floor_elevator.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_elevator.setFont(font)
        self.middle_floor_elevator.setStyleSheet("border: 3px solid green;\n"
"border-radius: 40px;\n"
"background-color: lightGreen;\n"
"")
        self.middle_floor_elevator.setObjectName("middle_floor_elevator")
        self.gridLayout.addWidget(self.middle_floor_elevator, 4, 3, 1, 1)
        self.elevator_column_label = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elevator_column_label.sizePolicy().hasHeightForWidth())
        self.elevator_column_label.setSizePolicy(sizePolicy)
        self.elevator_column_label.setMaximumSize(QtCore.QSize(16777215, 125))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.elevator_column_label.setFont(font)
        self.elevator_column_label.setStyleSheet("border: 3px solid black;\n"
"border-radius: 20px;\n"
"")
        self.elevator_column_label.setObjectName("elevator_column_label")
        self.gridLayout.addWidget(self.elevator_column_label, 0, 3, 1, 1)
        self.motion_column_label = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motion_column_label.sizePolicy().hasHeightForWidth())
        self.motion_column_label.setSizePolicy(sizePolicy)
        self.motion_column_label.setMaximumSize(QtCore.QSize(16777215, 125))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.motion_column_label.setFont(font)
        self.motion_column_label.setStyleSheet("border: 3px solid black;\n"
"border-radius: 20px;\n"
"")
        self.motion_column_label.setObjectName("motion_column_label")
        self.gridLayout.addWidget(self.motion_column_label, 0, 2, 1, 1)
        self.hvac_column_label = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hvac_column_label.sizePolicy().hasHeightForWidth())
        self.hvac_column_label.setSizePolicy(sizePolicy)
        self.hvac_column_label.setMaximumSize(QtCore.QSize(16777215, 125))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.hvac_column_label.setFont(font)
        self.hvac_column_label.setStyleSheet("border: 3px solid black;\n"
"border-radius: 20px;\n"
"\n"
"")
        self.hvac_column_label.setObjectName("hvac_column_label")
        self.gridLayout.addWidget(self.hvac_column_label, 0, 1, 1, 1)
        self.top_floor_motion = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_floor_motion.sizePolicy().hasHeightForWidth())
        self.top_floor_motion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_motion.setFont(font)
        self.top_floor_motion.setStyleSheet("border: 3px solid green;\n"
"border-radius: 40px;\n"
"background-color: lightGreen;\n"
"")
        self.top_floor_motion.setObjectName("top_floor_motion")
        self.gridLayout.addWidget(self.top_floor_motion, 1, 2, 1, 1)
        self.middle_floor_hvac_dial = QtWidgets.QDial(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_floor_hvac_dial.sizePolicy().hasHeightForWidth())
        self.middle_floor_hvac_dial.setSizePolicy(sizePolicy)
        self.middle_floor_hvac_dial.setObjectName("middle_floor_hvac_dial")
        self.gridLayout.addWidget(self.middle_floor_hvac_dial, 6, 1, 1, 1)
        self.bottom_floor_hvac_dial = QtWidgets.QDial(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_hvac_dial.sizePolicy().hasHeightForWidth())
        self.bottom_floor_hvac_dial.setSizePolicy(sizePolicy)
        self.bottom_floor_hvac_dial.setObjectName("bottom_floor_hvac_dial")
        self.gridLayout.addWidget(self.bottom_floor_hvac_dial, 9, 1, 1, 1)
        self.bottom_floor_activate_on = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_activate_on.setFont(font)
        self.bottom_floor_activate_on.setObjectName("bottom_floor_activate_on")
        self.gridLayout.addWidget(self.bottom_floor_activate_on, 8, 1, 1, 1)
        self.arm_alarm_button = QtWidgets.QPushButton(self.centralwidget)
        self.arm_alarm_button.setObjectName("arm_alarm_button")
        self.gridLayout.addWidget(self.arm_alarm_button, 1, 0, 1, 1)
        self.unlock_door_button = QtWidgets.QPushButton(self.centralwidget)
        self.unlock_door_button.setObjectName("unlock_door_button")
        self.gridLayout.addWidget(self.unlock_door_button, 4, 0, 1, 1)
        self.lock_door_button = QtWidgets.QPushButton(self.centralwidget)
        self.lock_door_button.setObjectName("lock_door_button")
        self.gridLayout.addWidget(self.lock_door_button, 3, 0, 1, 1)
        self.disarm_alarm_button = QtWidgets.QPushButton(self.centralwidget)
        self.disarm_alarm_button.setObjectName("disarm_alarm_button")
        self.gridLayout.addWidget(self.disarm_alarm_button, 2, 0, 1, 1)
        self.top_floor_hvac_dial = QtWidgets.QDial(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_floor_hvac_dial.sizePolicy().hasHeightForWidth())
        self.top_floor_hvac_dial.setSizePolicy(sizePolicy)
        self.top_floor_hvac_dial.setObjectName("top_floor_hvac_dial")
        self.gridLayout.addWidget(self.top_floor_hvac_dial, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.log_list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_list.sizePolicy().hasHeightForWidth())
        self.log_list.setSizePolicy(sizePolicy)
        self.log_list.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.log_list.setFont(font)
        self.log_list.setObjectName("log_list")
        item = QtWidgets.QListWidgetItem()
        self.log_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.log_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.log_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.log_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.log_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.log_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.log_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.log_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.log_list.addItem(item)
        self.horizontalLayout.addWidget(self.log_list)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.top_floor_elevator_request.setText(_translate("MainWindow", "Request Elevator"))
        self.top_floor_activate_on.setText(_translate("MainWindow", "Active on:  xx.xx"))
        self.top_floor_temp.setText(_translate("MainWindow", "xx.xx"))
        self.bottom_floor_elevator.setText(_translate("MainWindow", "Not Here"))
        self.middle_floor_temp.setText(_translate("MainWindow", "xx.xx"))
        self.middle_floor_motion.setText(_translate("MainWindow", "ON"))
        self.top_floor_elevator.setText(_translate("MainWindow", "Requested"))
        self.bottom_floor_motion.setText(_translate("MainWindow", "OFF"))
        self.bottom_floor_temp.setText(_translate("MainWindow", "xx.xx"))
        self.middle_floor_activate_on.setText(_translate("MainWindow", "Active on: xx.xx"))
        self.middle_floor_elevator_request.setText(_translate("MainWindow", "Request Elevator"))
        self.bottom_floor_elevator_request.setText(_translate("MainWindow", "Request Elevator"))
        self.middle_floor_elevator.setText(_translate("MainWindow", "Here"))
        self.elevator_column_label.setText(_translate("MainWindow", "ELEVATOR"))
        self.motion_column_label.setText(_translate("MainWindow", "MOTION"))
        self.hvac_column_label.setText(_translate("MainWindow", "HVAC"))
        self.top_floor_motion.setText(_translate("MainWindow", "ON"))
        self.bottom_floor_activate_on.setText(_translate("MainWindow", "Active on: xx.xx"))
        self.arm_alarm_button.setText(_translate("MainWindow", "Arm Alarm"))
        self.unlock_door_button.setText(_translate("MainWindow", "Unlock Door"))
        self.lock_door_button.setText(_translate("MainWindow", "Lock Door"))
        self.disarm_alarm_button.setText(_translate("MainWindow", "Disarm Alarm"))
        __sortingEnabled = self.log_list.isSortingEnabled()
        self.log_list.setSortingEnabled(False)
        item = self.log_list.item(0)
        item.setText(_translate("MainWindow", "01/22/24"))
        item = self.log_list.item(1)
        item.setText(_translate("MainWindow", "16:00:00 System Startup"))
        item = self.log_list.item(2)
        item.setText(_translate("MainWindow", "16:01:01 HVAC F2 ON"))
        item = self.log_list.item(3)
        item.setText(_translate("MainWindow", "16:02:02 COOKE RFID GRANTED"))
        item = self.log_list.item(4)
        item.setText(_translate("MainWindow", "16:02:02 XIANG RFID DENIED"))
        item = self.log_list.item(5)
        item.setText(_translate("MainWindow", "16:0404 HVAC F1 OFF"))
        item = self.log_list.item(6)
        item.setText(_translate("MainWindow", "16:05:05 F3 MOTION"))
        item = self.log_list.item(7)
        item.setText(_translate("MainWindow", "16:05:20 F3 ELEVATOR REQUEST"))
        item = self.log_list.item(8)
        item.setText(_translate("MainWindow", "16:06:06 F2 T SET 72"))
        self.log_list.setSortingEnabled(__sortingEnabled)

