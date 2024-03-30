# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TabsDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1675, 919)
        MainWindow.setMinimumSize(QtCore.QSize(1380, 778))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lock_door_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lock_door_button.setFont(font)
        self.lock_door_button.setObjectName("lock_door_button")
        self.verticalLayout_3.addWidget(self.lock_door_button)
        self.unlock_door_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.unlock_door_button.setFont(font)
        self.unlock_door_button.setObjectName("unlock_door_button")
        self.verticalLayout_3.addWidget(self.unlock_door_button)
        self.arm_alarm_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.arm_alarm_button.setFont(font)
        self.arm_alarm_button.setObjectName("arm_alarm_button")
        self.verticalLayout_3.addWidget(self.arm_alarm_button)
        self.disarm_alarm_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.disarm_alarm_button.setFont(font)
        self.disarm_alarm_button.setObjectName("disarm_alarm_button")
        self.verticalLayout_3.addWidget(self.disarm_alarm_button)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.control = QtWidgets.QWidget()
        self.control.setObjectName("control")
        self.gridLayout = QtWidgets.QGridLayout(self.control)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.bottom_floor_activate_on = QtWidgets.QLabel(self.control)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_activate_on.setFont(font)
        self.bottom_floor_activate_on.setObjectName("bottom_floor_activate_on")
        self.gridLayout_4.addWidget(self.bottom_floor_activate_on, 8, 1, 1, 1)
        self.middle_floor_hvac_dial = QtWidgets.QDial(self.control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_floor_hvac_dial.sizePolicy().hasHeightForWidth())
        self.middle_floor_hvac_dial.setSizePolicy(sizePolicy)
        self.middle_floor_hvac_dial.setObjectName("middle_floor_hvac_dial")
        self.gridLayout_4.addWidget(self.middle_floor_hvac_dial, 6, 1, 1, 1)
        self.top_floor_elevator_request = QtWidgets.QPushButton(self.control)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_elevator_request.setFont(font)
        self.top_floor_elevator_request.setObjectName("top_floor_elevator_request")
        self.gridLayout_4.addWidget(self.top_floor_elevator_request, 2, 3, 1, 1)
        self.middle_floor_temp = QtWidgets.QPushButton(self.control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_floor_temp.sizePolicy().hasHeightForWidth())
        self.middle_floor_temp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_temp.setFont(font)
        self.middle_floor_temp.setStyleSheet("border: 3px solid grey;\n"
"border-radius: 40px;\n"
"background-color: lightGrey;\n"
"")
        self.middle_floor_temp.setObjectName("middle_floor_temp")
        self.gridLayout_4.addWidget(self.middle_floor_temp, 4, 1, 1, 1)
        self.top_floor_activate_on = QtWidgets.QLabel(self.control)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_activate_on.setFont(font)
        self.top_floor_activate_on.setObjectName("top_floor_activate_on")
        self.gridLayout_4.addWidget(self.top_floor_activate_on, 2, 1, 1, 1)
        self.top_floor_hvac_dial = QtWidgets.QDial(self.control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_floor_hvac_dial.sizePolicy().hasHeightForWidth())
        self.top_floor_hvac_dial.setSizePolicy(sizePolicy)
        self.top_floor_hvac_dial.setObjectName("top_floor_hvac_dial")
        self.gridLayout_4.addWidget(self.top_floor_hvac_dial, 3, 1, 1, 1)
        self.motion_column_label = QtWidgets.QPushButton(self.control)
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
"background-color: aliceblue;\n"
"\n"
"")
        self.motion_column_label.setObjectName("motion_column_label")
        self.gridLayout_4.addWidget(self.motion_column_label, 0, 2, 1, 1)
        self.hvac_column_label = QtWidgets.QPushButton(self.control)
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
"background-color: aliceblue;\n"
"\n"
"\n"
"")
        self.hvac_column_label.setObjectName("hvac_column_label")
        self.gridLayout_4.addWidget(self.hvac_column_label, 0, 1, 1, 1)
        self.middle_floor_motion = QtWidgets.QPushButton(self.control)
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
        self.gridLayout_4.addWidget(self.middle_floor_motion, 4, 2, 1, 1)
        self.middle_floor_elevator = QtWidgets.QPushButton(self.control)
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
        self.gridLayout_4.addWidget(self.middle_floor_elevator, 4, 3, 1, 1)
        self.bottom_floor_elevator_request = QtWidgets.QPushButton(self.control)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_elevator_request.setFont(font)
        self.bottom_floor_elevator_request.setObjectName("bottom_floor_elevator_request")
        self.gridLayout_4.addWidget(self.bottom_floor_elevator_request, 8, 3, 1, 1)
        self.bottom_floor_hvac_dial = QtWidgets.QDial(self.control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_hvac_dial.sizePolicy().hasHeightForWidth())
        self.bottom_floor_hvac_dial.setSizePolicy(sizePolicy)
        self.bottom_floor_hvac_dial.setObjectName("bottom_floor_hvac_dial")
        self.gridLayout_4.addWidget(self.bottom_floor_hvac_dial, 9, 1, 1, 1)
        self.top_floor_motion = QtWidgets.QPushButton(self.control)
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
        self.gridLayout_4.addWidget(self.top_floor_motion, 1, 2, 1, 1)
        self.middle_floor_elevator_request = QtWidgets.QPushButton(self.control)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_elevator_request.setFont(font)
        self.middle_floor_elevator_request.setObjectName("middle_floor_elevator_request")
        self.gridLayout_4.addWidget(self.middle_floor_elevator_request, 5, 3, 1, 1)
        self.top_floor_elevator = QtWidgets.QPushButton(self.control)
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
        self.gridLayout_4.addWidget(self.top_floor_elevator, 1, 3, 1, 1)
        self.bottom_floor_elevator = QtWidgets.QPushButton(self.control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_elevator.sizePolicy().hasHeightForWidth())
        self.bottom_floor_elevator.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_elevator.setFont(font)
        self.bottom_floor_elevator.setStyleSheet("border: 3px solid grey;\n"
"border-radius: 40px;\n"
"background-color: lightGrey;")
        self.bottom_floor_elevator.setObjectName("bottom_floor_elevator")
        self.gridLayout_4.addWidget(self.bottom_floor_elevator, 7, 3, 1, 1)
        self.bottom_floor_temp = QtWidgets.QPushButton(self.control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_temp.sizePolicy().hasHeightForWidth())
        self.bottom_floor_temp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_temp.setFont(font)
        self.bottom_floor_temp.setStyleSheet("border: 3px solid grey;\n"
"border-radius: 40px;\n"
"background-color: lightGrey;\n"
"")
        self.bottom_floor_temp.setObjectName("bottom_floor_temp")
        self.gridLayout_4.addWidget(self.bottom_floor_temp, 7, 1, 1, 1)
        self.middle_floor_activate_on = QtWidgets.QLabel(self.control)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_activate_on.setFont(font)
        self.middle_floor_activate_on.setObjectName("middle_floor_activate_on")
        self.gridLayout_4.addWidget(self.middle_floor_activate_on, 5, 1, 1, 1)
        self.bottom_floor_motion = QtWidgets.QPushButton(self.control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_motion.sizePolicy().hasHeightForWidth())
        self.bottom_floor_motion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_motion.setFont(font)
        self.bottom_floor_motion.setStyleSheet("border: 3px solid grey;\n"
"border-radius: 40px;\n"
"background-color: lightGrey;")
        self.bottom_floor_motion.setObjectName("bottom_floor_motion")
        self.gridLayout_4.addWidget(self.bottom_floor_motion, 7, 2, 1, 1)
        self.top_floor_temp = QtWidgets.QPushButton(self.control)
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
        self.gridLayout_4.addWidget(self.top_floor_temp, 1, 1, 1, 1)
        self.elevator_column_label = QtWidgets.QPushButton(self.control)
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
"background-color: aliceblue;\n"
"")
        self.elevator_column_label.setObjectName("elevator_column_label")
        self.gridLayout_4.addWidget(self.elevator_column_label, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.control)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.control)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.control)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 7, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.control, "")
        self.logs = QtWidgets.QWidget()
        self.logs.setObjectName("logs")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.logs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.logs_list = QtWidgets.QListWidget(self.logs)
        self.logs_list.setObjectName("logs_list")
        self.gridLayout_2.addWidget(self.logs_list, 0, 0, 1, 1)
        self.tabWidget.addTab(self.logs, "")
        self.split = QtWidgets.QWidget()
        self.split.setObjectName("split")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.split)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.top_floor_elevator_request_split = QtWidgets.QPushButton(self.split)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_elevator_request_split.setFont(font)
        self.top_floor_elevator_request_split.setObjectName("top_floor_elevator_request_split")
        self.gridLayout_5.addWidget(self.top_floor_elevator_request_split, 2, 3, 1, 1)
        self.bottom_floor_elevator_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_elevator_split.sizePolicy().hasHeightForWidth())
        self.bottom_floor_elevator_split.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_elevator_split.setFont(font)
        self.bottom_floor_elevator_split.setStyleSheet("border: 3px solid grey;\n"
"border-radius: 40px;\n"
"background-color: lightGrey;")
        self.bottom_floor_elevator_split.setObjectName("bottom_floor_elevator_split")
        self.gridLayout_5.addWidget(self.bottom_floor_elevator_split, 7, 3, 1, 1)
        self.motion_column_label_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motion_column_label_split.sizePolicy().hasHeightForWidth())
        self.motion_column_label_split.setSizePolicy(sizePolicy)
        self.motion_column_label_split.setMaximumSize(QtCore.QSize(16777215, 125))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.motion_column_label_split.setFont(font)
        self.motion_column_label_split.setStyleSheet("border: 3px solid black;\n"
"border-radius: 20px;\n"
"background-color: aliceblue;\n"
"")
        self.motion_column_label_split.setObjectName("motion_column_label_split")
        self.gridLayout_5.addWidget(self.motion_column_label_split, 0, 2, 1, 1)
        self.middle_floor_temp_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_floor_temp_split.sizePolicy().hasHeightForWidth())
        self.middle_floor_temp_split.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_temp_split.setFont(font)
        self.middle_floor_temp_split.setStyleSheet("border: 3px solid grey;\n"
"border-radius: 40px;\n"
"background-color: lightGrey;\n"
"\n"
"")
        self.middle_floor_temp_split.setObjectName("middle_floor_temp_split")
        self.gridLayout_5.addWidget(self.middle_floor_temp_split, 4, 1, 1, 1)
        self.middle_floor_elevator_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_floor_elevator_split.sizePolicy().hasHeightForWidth())
        self.middle_floor_elevator_split.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_elevator_split.setFont(font)
        self.middle_floor_elevator_split.setStyleSheet("border: 3px solid green;\n"
"border-radius: 40px;\n"
"background-color: lightGreen;\n"
"")
        self.middle_floor_elevator_split.setObjectName("middle_floor_elevator_split")
        self.gridLayout_5.addWidget(self.middle_floor_elevator_split, 4, 3, 1, 1)
        self.top_floor_temp_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_floor_temp_split.sizePolicy().hasHeightForWidth())
        self.top_floor_temp_split.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_temp_split.setFont(font)
        self.top_floor_temp_split.setStyleSheet("border: 3px solid green;\n"
"border-radius: 40px;\n"
"background-color: lightGreen;\n"
"")
        self.top_floor_temp_split.setObjectName("top_floor_temp_split")
        self.gridLayout_5.addWidget(self.top_floor_temp_split, 1, 1, 1, 1)
        self.bottom_floor_hvac_dial_split = QtWidgets.QDial(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_hvac_dial_split.sizePolicy().hasHeightForWidth())
        self.bottom_floor_hvac_dial_split.setSizePolicy(sizePolicy)
        self.bottom_floor_hvac_dial_split.setObjectName("bottom_floor_hvac_dial_split")
        self.gridLayout_5.addWidget(self.bottom_floor_hvac_dial_split, 9, 1, 1, 1)
        self.top_floor_motion_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_floor_motion_split.sizePolicy().hasHeightForWidth())
        self.top_floor_motion_split.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_motion_split.setFont(font)
        self.top_floor_motion_split.setStyleSheet("border: 3px solid green;\n"
"border-radius: 40px;\n"
"background-color: lightGreen;\n"
"")
        self.top_floor_motion_split.setObjectName("top_floor_motion_split")
        self.gridLayout_5.addWidget(self.top_floor_motion_split, 1, 2, 1, 1)
        self.middle_floor_motion_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_floor_motion_split.sizePolicy().hasHeightForWidth())
        self.middle_floor_motion_split.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_motion_split.setFont(font)
        self.middle_floor_motion_split.setStyleSheet("border: 3px solid green;\n"
"border-radius: 40px;\n"
"background-color: lightGreen;\n"
"")
        self.middle_floor_motion_split.setObjectName("middle_floor_motion_split")
        self.gridLayout_5.addWidget(self.middle_floor_motion_split, 4, 2, 1, 1)
        self.top_floor_activate_on_split = QtWidgets.QLabel(self.split)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_activate_on_split.setFont(font)
        self.top_floor_activate_on_split.setObjectName("top_floor_activate_on_split")
        self.gridLayout_5.addWidget(self.top_floor_activate_on_split, 2, 1, 1, 1)
        self.middle_floor_elevator_request_split = QtWidgets.QPushButton(self.split)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_elevator_request_split.setFont(font)
        self.middle_floor_elevator_request_split.setObjectName("middle_floor_elevator_request_split")
        self.gridLayout_5.addWidget(self.middle_floor_elevator_request_split, 5, 3, 1, 1)
        self.middle_floor_hvac_dial_split = QtWidgets.QDial(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_floor_hvac_dial_split.sizePolicy().hasHeightForWidth())
        self.middle_floor_hvac_dial_split.setSizePolicy(sizePolicy)
        self.middle_floor_hvac_dial_split.setObjectName("middle_floor_hvac_dial_split")
        self.gridLayout_5.addWidget(self.middle_floor_hvac_dial_split, 6, 1, 1, 1)
        self.bottom_floor_motion_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_motion_split.sizePolicy().hasHeightForWidth())
        self.bottom_floor_motion_split.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_motion_split.setFont(font)
        self.bottom_floor_motion_split.setStyleSheet("border: 3px solid grey;\n"
"border-radius: 40px;\n"
"background-color: lightGrey;")
        self.bottom_floor_motion_split.setObjectName("bottom_floor_motion_split")
        self.gridLayout_5.addWidget(self.bottom_floor_motion_split, 7, 2, 1, 1)
        self.hvac_column_label_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hvac_column_label_split.sizePolicy().hasHeightForWidth())
        self.hvac_column_label_split.setSizePolicy(sizePolicy)
        self.hvac_column_label_split.setMaximumSize(QtCore.QSize(16777215, 125))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.hvac_column_label_split.setFont(font)
        self.hvac_column_label_split.setStyleSheet("border: 3px solid black;\n"
"border-radius: 20px;\n"
"background-color: aliceblue;\n"
"\n"
"")
        self.hvac_column_label_split.setObjectName("hvac_column_label_split")
        self.gridLayout_5.addWidget(self.hvac_column_label_split, 0, 1, 1, 1)
        self.bottom_floor_elevator_request_split = QtWidgets.QPushButton(self.split)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_elevator_request_split.setFont(font)
        self.bottom_floor_elevator_request_split.setObjectName("bottom_floor_elevator_request_split")
        self.gridLayout_5.addWidget(self.bottom_floor_elevator_request_split, 8, 3, 1, 1)
        self.bottom_floor_activate_on_split = QtWidgets.QLabel(self.split)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_activate_on_split.setFont(font)
        self.bottom_floor_activate_on_split.setObjectName("bottom_floor_activate_on_split")
        self.gridLayout_5.addWidget(self.bottom_floor_activate_on_split, 8, 1, 1, 1)
        self.middle_floor_activate_on_split = QtWidgets.QLabel(self.split)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.middle_floor_activate_on_split.setFont(font)
        self.middle_floor_activate_on_split.setObjectName("middle_floor_activate_on_split")
        self.gridLayout_5.addWidget(self.middle_floor_activate_on_split, 5, 1, 1, 1)
        self.top_floor_hvac_dial_split = QtWidgets.QDial(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_floor_hvac_dial_split.sizePolicy().hasHeightForWidth())
        self.top_floor_hvac_dial_split.setSizePolicy(sizePolicy)
        self.top_floor_hvac_dial_split.setObjectName("top_floor_hvac_dial_split")
        self.gridLayout_5.addWidget(self.top_floor_hvac_dial_split, 3, 1, 1, 1)
        self.top_floor_elevator_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_floor_elevator_split.sizePolicy().hasHeightForWidth())
        self.top_floor_elevator_split.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.top_floor_elevator_split.setFont(font)
        self.top_floor_elevator_split.setStyleSheet("border: 3px solid yellow;\n"
"border-radius: 40px;\n"
"background-color: lightYellow;\n"
"")
        self.top_floor_elevator_split.setObjectName("top_floor_elevator_split")
        self.gridLayout_5.addWidget(self.top_floor_elevator_split, 1, 3, 1, 1)
        self.elevator_column_label_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elevator_column_label_split.sizePolicy().hasHeightForWidth())
        self.elevator_column_label_split.setSizePolicy(sizePolicy)
        self.elevator_column_label_split.setMaximumSize(QtCore.QSize(16777215, 125))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.elevator_column_label_split.setFont(font)
        self.elevator_column_label_split.setStyleSheet("border: 3px solid black;\n"
"border-radius: 20px;\n"
"background-color: aliceblue;\n"
"")
        self.elevator_column_label_split.setObjectName("elevator_column_label_split")
        self.gridLayout_5.addWidget(self.elevator_column_label_split, 0, 3, 1, 1)
        self.bottom_floor_temp_split = QtWidgets.QPushButton(self.split)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_floor_temp_split.sizePolicy().hasHeightForWidth())
        self.bottom_floor_temp_split.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.bottom_floor_temp_split.setFont(font)
        self.bottom_floor_temp_split.setStyleSheet("border: 3px solid grey;\n"
"border-radius: 40px;\n"
"background-color: lightGrey;\n"
"")
        self.bottom_floor_temp_split.setObjectName("bottom_floor_temp_split")
        self.gridLayout_5.addWidget(self.bottom_floor_temp_split, 7, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.split)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.split)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.split)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 7, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_5)
        self.logs_list_split = QtWidgets.QListWidget(self.split)
        self.logs_list_split.setObjectName("logs_list_split")
        item = QtWidgets.QListWidgetItem()
        self.logs_list_split.addItem(item)
        self.horizontalLayout_2.addWidget(self.logs_list_split)
        self.tabWidget.addTab(self.split, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lock_door_button.setText(_translate("MainWindow", "Lock Door"))
        self.unlock_door_button.setText(_translate("MainWindow", "Unlock Door"))
        self.arm_alarm_button.setText(_translate("MainWindow", "Arm Alarm"))
        self.disarm_alarm_button.setText(_translate("MainWindow", "Disarm Alarm"))
        self.bottom_floor_activate_on.setText(_translate("MainWindow", "Cool To: xx°F"))
        self.top_floor_elevator_request.setText(_translate("MainWindow", "Request Elevator"))
        self.middle_floor_temp.setText(_translate("MainWindow", "xx°F OFF"))
        self.top_floor_activate_on.setText(_translate("MainWindow", "Cool To:  xx°F"))
        self.motion_column_label.setText(_translate("MainWindow", "MOTION"))
        self.hvac_column_label.setText(_translate("MainWindow", "HVAC"))
        self.middle_floor_motion.setText(_translate("MainWindow", "MOTION DETECTED"))
        self.middle_floor_elevator.setText(_translate("MainWindow", "Here"))
        self.bottom_floor_elevator_request.setText(_translate("MainWindow", "Request Elevator"))
        self.top_floor_motion.setText(_translate("MainWindow", "MOTION DETECTED"))
        self.middle_floor_elevator_request.setText(_translate("MainWindow", "Request Elevator"))
        self.top_floor_elevator.setText(_translate("MainWindow", "Requested"))
        self.bottom_floor_elevator.setText(_translate("MainWindow", "Not Here"))
        self.bottom_floor_temp.setText(_translate("MainWindow", "Not Connected"))
        self.middle_floor_activate_on.setText(_translate("MainWindow", "Cool To: xx°F"))
        self.bottom_floor_motion.setText(_translate("MainWindow", "NO MOTION"))
        self.top_floor_temp.setText(_translate("MainWindow", "xx°F ON"))
        self.elevator_column_label.setText(_translate("MainWindow", "ELEVATOR"))
        self.label.setText(_translate("MainWindow", "F3"))
        self.label_2.setText(_translate("MainWindow", "F2"))
        self.label_3.setText(_translate("MainWindow", "F1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.control), _translate("MainWindow", "Control"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logs), _translate("MainWindow", "Logs"))
        self.top_floor_elevator_request_split.setText(_translate("MainWindow", "REQ"))
        self.bottom_floor_elevator_split.setText(_translate("MainWindow", "NOT HERE"))
        self.motion_column_label_split.setText(_translate("MainWindow", "MOTION"))
        self.middle_floor_temp_split.setText(_translate("MainWindow", "xx°F"))
        self.middle_floor_elevator_split.setText(_translate("MainWindow", "Here"))
        self.top_floor_temp_split.setText(_translate("MainWindow", "xx°F"))
        self.top_floor_motion_split.setText(_translate("MainWindow", "MOTION"))
        self.middle_floor_motion_split.setText(_translate("MainWindow", "MOTION"))
        self.top_floor_activate_on_split.setText(_translate("MainWindow", "xx°F"))
        self.middle_floor_elevator_request_split.setText(_translate("MainWindow", "REQ"))
        self.bottom_floor_motion_split.setText(_translate("MainWindow", "NONE"))
        self.hvac_column_label_split.setText(_translate("MainWindow", "HVAC"))
        self.bottom_floor_elevator_request_split.setText(_translate("MainWindow", "REQ"))
        self.bottom_floor_activate_on_split.setText(_translate("MainWindow", "xx°F"))
        self.middle_floor_activate_on_split.setText(_translate("MainWindow", "xx°F"))
        self.top_floor_elevator_split.setText(_translate("MainWindow", "REQ"))
        self.elevator_column_label_split.setText(_translate("MainWindow", "ELEVATOR"))
        self.bottom_floor_temp_split.setText(_translate("MainWindow", "NC"))
        self.label_4.setText(_translate("MainWindow", "F1"))
        self.label_5.setText(_translate("MainWindow", "F2"))
        self.label_6.setText(_translate("MainWindow", "F3"))
        __sortingEnabled = self.logs_list_split.isSortingEnabled()
        self.logs_list_split.setSortingEnabled(False)
        item = self.logs_list_split.item(0)
        item.setText(_translate("MainWindow", "Sample"))
        self.logs_list_split.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.split), _translate("MainWindow", "Split View"))
