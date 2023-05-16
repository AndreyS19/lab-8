import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

import dialogggg
import Driver_Base
import Driver_Base2

Form, Window = uic.loadUiType("dialogggg.ui")
Form, WinDriv = uic.loadUiType("Driver_Base.ui")
Form, WinDriv2 = uic.loadUiType("Driver_Base2.ui")
f = open("fileB.txt", 'a')
f1 = open("fileA.txt", 'a')
Driv = False
Pass = False
true = True
false = False

appDr = QApplication([])  # создаем окошко
uiDr = Driver_Base.Ui_Dialog()
winDriv = WinDriv()
uiDr.setupUi(winDriv)

# appDr2 = QApplication([])  # создаем окошко
# uiDr = Driver_Base2.Ui_Dialog()
# winDriv2 = WinDriv2()
# uiDr.setupUi(winDriv2)

app = QApplication([])  # создаем окошко начальное
ui = dialogggg.Ui_Dialog()
window = Window()
ui.setupUi(window)


def Dr_Cl():
    print("click Driver")
    global Driv
    global Pass
    Driv = true
    Pass = false


def OK_Cl():
    print("click OK")
    if (Driv):
        winDriv.show()  # выводим окошко водителя



def Pass_Cl():
    print("click tovar")
    global Driv
    global Pass
    Pass = true
    Driv = false


def DriverB_OK():
    print("ЗАнес в базу: ")
    print("ФИО: " + uiDr.FIO.text(), file=f)
    print("Adress: " + uiDr.Adress.text(), file=f)
    print("Contact " + uiDr.Contact.text(), file=f)
    print("notes: " + uiDr.notes.text(), file=f)
    print("category: " + uiDr.category.text(), file=f)

    f.close()


ui.Driver.clicked.connect(Dr_Cl)
ui.OK.clicked.connect(OK_Cl)
ui.Passenger.clicked.connect(Pass_Cl)

uiDr.Ok.clicked.connect(DriverB_OK)

# form = Form()
# print(ui.Driver.text())
# ui.OK.isCheckable()
# ui.Driver.show()
# form.setupUi(window)

window.show()  # Выводим начальное окошко
app.exec()
appDr.exec()
f.close()
