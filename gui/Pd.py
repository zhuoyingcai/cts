from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class Pd(QWidget):
    def __init__(self, parent=None):
        super(Pd, self).__init__(parent)

        self.setupUi(self)

    def setupUi(self, QWidget):
        QWidget.setObjectName("QWidget")
        QWidget.resize(486, 579)
        self.PersonalInfo = QtWidgets.QWidget()
        self.PersonalInfo.setObjectName("PersonalInfo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PersonalInfo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.PersonalInfo)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_7 = QtWidgets.QWidget(self.PersonalInfo)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_7.setObjectName("widget_7")
        self.formLayout = QtWidgets.QFormLayout(self.widget_7)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_7)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.widget_7)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget = QtWidgets.QWidget(self.PersonalInfo)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setCheckable(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_2.setCheckable(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget_6)
        self.checkBox_3.setCheckable(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget_6)
        self.checkBox_4.setCheckable(False)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget_5)
        self.checkBox_5.setCheckable(False)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_4.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget_5)
        self.checkBox_6.setCheckable(False)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_4.addWidget(self.checkBox_6)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget)
        self.pushButton_3 = QtWidgets.QPushButton(self.PersonalInfo)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignHCenter)
        QWidget.addTab(self.PersonalInfo, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_5.addWidget(self.textEdit)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignHCenter)
        QWidget.addTab(self.tab, "")

        self.retranslateUi(QWidget)
        QWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(QWidget)

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        QWidget.setWindowTitle(_translate("QWidget", "QWidget"))
        self.label.setText(_translate("QWidget", "TextLabel"))
        self.pushButton_2.setText(_translate("QWidget", "View Resume"))
        self.pushButton.setText(_translate("QWidget", "View Addition Info"))
        self.label_2.setText(_translate("QWidget", "Email:"))
        self.label_3.setText(_translate("QWidget", "Adress:"))
        self.checkBox.setText(_translate("QWidget", "IOS"))
        self.checkBox_2.setText(_translate("QWidget", "Java"))
        self.checkBox_3.setText(_translate("QWidget", "Android"))
        self.checkBox_4.setText(_translate("QWidget", "Python"))
        self.checkBox_5.setText(_translate("QWidget", "DesktopApp"))
        self.checkBox_6.setText(_translate("QWidget", "CPP"))
        self.pushButton_3.setText(_translate("QWidget", "Submit Change"))
        QWidget.setTabText(QWidget.indexOf(self.PersonalInfo), _translate("QWidget", "Tab 1"))
        self.label_4.setText(_translate("QWidget", "Fll in below demand to quit from the system"))
        self.pushButton_4.setText(_translate("QWidget", "Delete Acount"))
        QWidget.setTabText(QWidget.indexOf(self.tab), _translate("QWidget", "Tab 2"))

