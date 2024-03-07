# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 617)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(10, 10, 345, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2 0")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.output_label.setFont(font)
#         self.output_label.setStyleSheet(" \n"
# "Font: 48pt \"MS Shell Dlg 2 0\"")
        self.output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_label.setMidLineWidth(1)
        self.output_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_label.setIndent(7)
        self.output_label.setObjectName("output_label")
        self.percentage_button = QtWidgets.QPushButton(self.centralwidget,
                                                       clicked = lambda : self.press_it("%"))
        self.percentage_button.setGeometry(QtCore.QRect(10, 120, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentage_button.setFont(font)
        self.percentage_button.setObjectName("percentage_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked = lambda : self.press_it("C"))
        self.clear_button.setGeometry(QtCore.QRect(100, 120, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.divide_button = QtWidgets.QPushButton(self.centralwidget,
                                                   clicked = lambda : self.press_it("/"))
        self.divide_button.setGeometry(QtCore.QRect(280, 120, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divide_button.setFont(font)
        self.divide_button.setObjectName("divide_button")
        self.arrow_button = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked = lambda : self.arrow_it())
        self.arrow_button.setGeometry(QtCore.QRect(190, 120, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrow_button.setFont(font)
        self.arrow_button.setObjectName("arrow_button")
        self.eight_button = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked = lambda : self.press_it("8"))
        self.eight_button.setGeometry(QtCore.QRect(100, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        self.mul_button = QtWidgets.QPushButton(self.centralwidget,
                                                clicked = lambda : self.press_it("*"))
        self.mul_button.setGeometry(QtCore.QRect(280, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.mul_button.setFont(font)
        self.mul_button.setObjectName("mul_button")
        self.nine_button = QtWidgets.QPushButton(self.centralwidget,
                                                 clicked = lambda : self.press_it("9"))
        self.nine_button.setGeometry(QtCore.QRect(190, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        self.seven_button = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked = lambda : self.press_it("7"))
        self.seven_button.setGeometry(QtCore.QRect(10, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        self.six_button = QtWidgets.QPushButton(self.centralwidget,
                                                clicked = lambda : self.press_it("6"))
        self.six_button.setGeometry(QtCore.QRect(190, 300, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        self.four_button = QtWidgets.QPushButton(self.centralwidget,
                                                 clicked = lambda : self.press_it("4"))
        self.four_button.setGeometry(QtCore.QRect(10, 300, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        self.minus_button = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked = lambda : self.press_it("-"))
        self.minus_button.setGeometry(QtCore.QRect(280, 300, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minus_button.setFont(font)
        self.minus_button.setObjectName("minus_button")
        self.five_button = QtWidgets.QPushButton(self.centralwidget,
                                                 clicked = lambda : self.press_it("5"))
        self.five_button.setGeometry(QtCore.QRect(100, 300, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        self.three_button = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked = lambda : self.press_it("3"))
        self.three_button.setGeometry(QtCore.QRect(190, 390, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        self.plus_button = QtWidgets.QPushButton(self.centralwidget,
                                                 clicked = lambda : self.press_it("+"))
        self.plus_button.setGeometry(QtCore.QRect(280, 390, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plus_button.setFont(font)
        self.plus_button.setObjectName("plus_button")
        self.one_button = QtWidgets.QPushButton(self.centralwidget,
                                                clicked = lambda : self.press_it("1"))
        self.one_button.setGeometry(QtCore.QRect(10, 390, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        self.two_button = QtWidgets.QPushButton(self.centralwidget,
                                                clicked = lambda : self.press_it("2"))
        self.two_button.setGeometry(QtCore.QRect(100, 390, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        self.dot_button = QtWidgets.QPushButton(self.centralwidget,
                                                clicked = lambda : self.dot_it())
        self.dot_button.setGeometry(QtCore.QRect(190, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.dot_button.setFont(font)
        self.dot_button.setObjectName("dot_button")
        self.plusminus_button = QtWidgets.QPushButton(self.centralwidget,
                                                      clicked = lambda : self.plusminus_it())
        self.plusminus_button.setGeometry(QtCore.QRect(10, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminus_button.setFont(font)
        self.plusminus_button.setObjectName("plusminus_button")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget,
                                                 clicked = lambda : self.press_it("0"))
        self.zero_button.setGeometry(QtCore.QRect(100, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        self.equal_button = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked = lambda : self.equal_it())
        self.equal_button.setGeometry(QtCore.QRect(280, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 364, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def plusminus_it(self):
        screen = self.output_label.text()
        if "-" in screen :
            self.output_label.setText(screen.replace("-","+"))
        else:
            if screen == "0":
                self.output_label.setText("0")
            else:
                self.output_label.setText(f"-{screen}")
            
    def arrow_it(self):
         screen = self.output_label.text()
         display = screen[:-1]
         self.output_label.setText(f"{display}")
    
    def equal_it(self):
        screen = self.output_label.text()
        result = eval(screen)
        self.output_label.setText(f"{result}")

    def dot_it(self):
        screen = self.output_label.text()
        try:
            if "." in screen:
                screen_1 = (f"{self.output_label.text()}.")
                if eval(screen_1):
                    self.output_label.setText(f"{screen}.")
            else:
                self.output_label.setText(f"{screen}.")
        except Exception:
             self.output_label.setText(f"{screen}")

        # screen =  self.output_label.text()
        # if "." in screen:
        #     pass
        # else: 
        #      self.output_label.setText(f"{screen}.")

    def press_it(self,pressed):
        if pressed == "C":
            self.output_label.setText("0")
        else:
            if  self.output_label.text() == "0":
                self.output_label.setText("")

            self.output_label.setText(f"{self.output_label.text()}{pressed}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.output_label.setText(_translate("MainWindow", "0"))
        self.percentage_button.setText(_translate("MainWindow", "%"))
        self.clear_button.setText(_translate("MainWindow", "C"))
        self.divide_button.setText(_translate("MainWindow", "/"))
        self.arrow_button.setText(_translate("MainWindow", "<<"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.mul_button.setText(_translate("MainWindow", "x"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.minus_button.setText(_translate("MainWindow", "-"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.plus_button.setText(_translate("MainWindow", "+"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.dot_button.setText(_translate("MainWindow", "."))
        self.plusminus_button.setText(_translate("MainWindow", "+/-"))
        self.zero_button.setText(_translate("MainWindow", "0"))
        self.equal_button.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
