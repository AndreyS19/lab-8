from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 339)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 10, 151, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Namevhod = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.Namevhod.setObjectName("Namevhod")
        self.verticalLayout.addWidget(self.Namevhod)
        self.FIO = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.FIO.setObjectName("FIO")
        self.verticalLayout.addWidget(self.FIO)
        self.Adress = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.Adress.setObjectName("Adress")
        self.verticalLayout.addWidget(self.Adress)
        self.Contact = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.Contact.setObjectName("Contact")
        self.verticalLayout.addWidget(self.Contact)
        self.category = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.category.setObjectName("category")
        self.verticalLayout.addWidget(self.category)
        self.notes = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.notes.setObjectName("notes")
        self.verticalLayout.addWidget(self.notes)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 160, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 290, 321, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Clanse = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.Clanse.setObjectName("Clanse")
        self.horizontalLayout.addWidget(self.Clanse)
        self.Ok = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.Ok.setObjectName("Ok")
        self.horizontalLayout.addWidget(self.Ok)

        self.retranslateUi(Dialog)
        self.Clanse.clicked.connect(Dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Имя Входа"))
        self.label_6.setText(_translate("Dialog", "ФИО"))
        self.label_5.setText(_translate("Dialog", "Адрес"))
        self.label_3.setText(_translate("Dialog", "Контакты"))
        self.label_2.setText(_translate("Dialog", "Примечания"))
        self.label.setText(_translate("Dialog", "что то еще"))
        self.Clanse.setText(_translate("Dialog", "Отмена"))
        self.Ok.setText(_translate("Dialog", "Ок"))