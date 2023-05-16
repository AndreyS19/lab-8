from PyQt6 import QtCore, QtGui, QtWidgets

dfsd
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(177, 159)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 158, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.VL = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.VL.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.VL.setContentsMargins(0, 0, 0, 0)
        self.VL.setObjectName("VL")
        self.Passenger = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.Passenger.setObjectName("Passenger")
        self.VL.addWidget(self.Passenger)
        self.Driver = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.Driver.setObjectName("Driver")
        self.VL.addWidget(self.Driver)
        self.OK = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.OK.setObjectName("OK")
        self.VL.addWidget(self.OK)
        self.close = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.close.setObjectName("close")
        self.VL.addWidget(self.close)

        self.retranslateUi(Dialog)
        self.close.clicked.connect(Dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Passenger.setText(_translate("Dialog", "Товар"))
        self.Driver.setText(_translate("Dialog", "Работники"))
        self.OK.setText(_translate("Dialog", "ок"))
        self.close.setText(_translate("Dialog", "отмена"))
