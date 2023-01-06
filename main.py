import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QFont
from design import Ui_MainwWindow
from Imgame import Imgame

game = Imgame()
font = QFont()
font.setPointSize(56)

class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainwWindow()
        self.ui.setupUi(self)
        self.Turn = u"X"
        self.notTurn = u"O"

        self.ui.button_1.clicked.connect(lambda: self.ui.textBrowser.setHtml(QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                                               u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                                               "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                                               "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                               "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                                               "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                                               "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(self.notTurn)+"'s turn!"+"</p></body></html>",
                                                                None)) if not game.cell_is_occupied(0) else self.ui.textBrowser.setHtml(QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                                               u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                                               "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                                               "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                               "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                                               "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                                               "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This cell is occupied!</p></body></html>",
                                                                None)))
        self.ui.button_1.clicked.connect(lambda: self.simple_func(0) if not game.cell_is_occupied(0) else 0)
        self.ui.button_1.clicked.connect(lambda: self.ui.button_1.setStyleSheet(
            u"QPushButton {color: rgb(255, 0, 0);}") if self.Turn == u"X" else self.ui.button_1.setStyleSheet(
            u"QPushButton {color: rgb(0, 0, 255);}"))

        self.ui.button_2.clicked.connect(lambda: self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + str(
                    self.notTurn) + "'s turn!" + "</p></body></html>",
                                           None)) if not game.cell_is_occupied(1) else self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This cell is occupied!</p></body></html>",
                                           None)))
        self.ui.button_2.clicked.connect(lambda: self.simple_func(1) if not game.cell_is_occupied(1) else 0)
        self.ui.button_2.clicked.connect(lambda: self.ui.button_2.setStyleSheet(
            u"QPushButton {color: rgb(255, 0, 0);}") if self.Turn == u"X" else self.ui.button_2.setStyleSheet(
            u"QPushButton {color: rgb(0, 0, 255);}"))

        self.ui.button_3.clicked.connect(lambda: self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + str(
                    self.notTurn) + "'s turn!" + "</p></body></html>",
                                           None)) if not game.cell_is_occupied(2) else self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This cell is occupied!</p></body></html>",
                                           None)))
        self.ui.button_3.clicked.connect(lambda: self.simple_func(2) if not game.cell_is_occupied(2) else 0)
        self.ui.button_3.clicked.connect(lambda: self.ui.button_3.setStyleSheet(
            u"QPushButton {color: rgb(255, 0, 0);}") if self.Turn == u"X" else self.ui.button_3.setStyleSheet(
            u"QPushButton {color: rgb(0, 0, 255);}"))

        self.ui.button_4.clicked.connect(lambda: self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + str(
                    self.notTurn) + "'s turn!" + "</p></body></html>",
                                           None)) if not game.cell_is_occupied(3) else self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This cell is occupied!</p></body></html>",
                                           None)))
        self.ui.button_4.clicked.connect(lambda: self.simple_func(3) if not game.cell_is_occupied(3) else 0)
        self.ui.button_4.clicked.connect(lambda: self.ui.button_4.setStyleSheet(
            u"QPushButton {color: rgb(255, 0, 0);}") if self.Turn == u"X" else self.ui.button_4.setStyleSheet(
            u"QPushButton {color: rgb(0, 0, 255);}"))

        self.ui.button_5.clicked.connect(lambda: self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + str(
                    self.notTurn) + "'s turn!" + "</p></body></html>",
                                           None)) if not game.cell_is_occupied(4) else self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This cell is occupied!</p></body></html>",
                                           None)))
        self.ui.button_5.clicked.connect(lambda: self.simple_func(4) if not game.cell_is_occupied(4) else 0)
        self.ui.button_5.clicked.connect(lambda: self.ui.button_5.setStyleSheet(
            u"QPushButton {color: rgb(255, 0, 0);}") if self.Turn == u"X" else self.ui.button_5.setStyleSheet(
            u"QPushButton {color: rgb(0, 0, 255);}"))

        self.ui.button_6.clicked.connect(lambda: self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + str(
                    self.notTurn) + "'s turn!" + "</p></body></html>",
                                           None)) if not game.cell_is_occupied(5) else self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This cell is occupied!</p></body></html>",
                                           None)))
        self.ui.button_6.clicked.connect(lambda: self.simple_func(5) if not game.cell_is_occupied(5) else 0)
        self.ui.button_6.clicked.connect(lambda: self.ui.button_6.setStyleSheet(
            u"QPushButton {color: rgb(255, 0, 0);}") if self.Turn == u"X" else self.ui.button_6.setStyleSheet(
            u"QPushButton {color: rgb(0, 0, 255);}"))

        self.ui.button_7.clicked.connect(lambda: self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + str(
                    self.notTurn) + "'s turn!" + "</p></body></html>",
                                           None)) if not game.cell_is_occupied(6) else self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This cell is occupied!</p></body></html>",
                                           None)))
        self.ui.button_7.clicked.connect(lambda: self.simple_func(6) if not game.cell_is_occupied(6) else 0)
        self.ui.button_7.clicked.connect(lambda: self.ui.button_7.setStyleSheet(
            u"QPushButton {color: rgb(255, 0, 0);}") if self.Turn == u"X" else self.ui.button_7.setStyleSheet(
            u"QPushButton {color: rgb(0, 0, 255);}"))

        self.ui.button_8.clicked.connect(lambda: self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + str(
                    self.notTurn) + "'s turn!" + "</p></body></html>",
                                           None)) if not game.cell_is_occupied(7) else self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This cell is occupied!</p></body></html>",
                                           None)))
        self.ui.button_8.clicked.connect(lambda: self.simple_func(7) if not game.cell_is_occupied(7) else 0)
        self.ui.button_8.clicked.connect(lambda: self.ui.button_8.setStyleSheet(
            u"QPushButton {color: rgb(255, 0, 0);}") if self.Turn == u"X" else self.ui.button_8.setStyleSheet(
            u"QPushButton {color: rgb(0, 0, 255);}"))

        self.ui.button_9.clicked.connect(lambda: self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + str(
                    self.notTurn) + "'s turn!" + "</p></body></html>",
                                           None)) if not game.cell_is_occupied(8) else self.ui.textBrowser.setHtml(
                QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                          u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                          "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                          "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This cell is occupied!</p></body></html>",
                                           None)))
        self.ui.button_9.clicked.connect(lambda: self.simple_func(8) if not game.cell_is_occupied(8) else 0)
        self.ui.button_9.clicked.connect(lambda: self.ui.button_9.setStyleSheet(
            u"QPushButton {color: rgb(255, 0, 0);}") if self.Turn == u"X" else self.ui.button_9.setStyleSheet(
            u"QPushButton {color: rgb(0, 0, 255);}"))

        self.ui.repeatbutton.clicked.connect(lambda : self.clear_all())
        self.ui.repeatbutton.clicked.connect(lambda: game.restart())
        self.ui.Exitbutton.clicked.connect(lambda: sys.exit(app.exec()))

    def clear_all(self):
        self.ui.retranslateUi(self)
        self.Turn = u"X"
        self.notTurn = u"O"
        self.activeall()

    def toggle(self):
        if self.Turn == u"X":
            self.Turn = u"O"
            self.notTurn = u"X"
        else:
            self.Turn = u"X"
            self.notTurn = u"O"

    def simple_func(self,i):
        exec('self.ui.button_'+str(i+1)+'.setText(QCoreApplication.translate("MainwWindow", self.Turn, None))')
        self.everything_at_once(i)

    def activeall(self):
        self.ui.button_1.setEnabled(True)
        self.ui.button_2.setEnabled(True)
        self.ui.button_3.setEnabled(True)
        self.ui.button_4.setEnabled(True)
        self.ui.button_5.setEnabled(True)
        self.ui.button_6.setEnabled(True)
        self.ui.button_7.setEnabled(True)
        self.ui.button_8.setEnabled(True)
        self.ui.button_9.setEnabled(True)


    def deactiveall(self):
        self.ui.button_1.setDisabled(True)
        self.ui.button_2.setDisabled(True)
        self.ui.button_3.setDisabled(True)
        self.ui.button_4.setDisabled(True)
        self.ui.button_5.setDisabled(True)
        self.ui.button_6.setDisabled(True)
        self.ui.button_7.setDisabled(True)
        self.ui.button_8.setDisabled(True)
        self.ui.button_9.setDisabled(True)


    def everything_at_once(self,i):
        self.toggle()
        exec('self.ui.button_'+str(i+1)+'.setFont(font)')
        game.fill_the_cell(i)
        print(game.field)
        if game.check_the_game_stats() == "X wins":
            self.ui.textBrowser.setHtml(QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                                           u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                                           "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                                           "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                           "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                                           "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                                           "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X wins!</p></body></html>",
                                                            None))
            self.deactiveall()

        if game.check_the_game_stats() == "O wins":
            self.ui.textBrowser.setHtml(QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                                           u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                                           "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                                           "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                           "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                                           "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                                           "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">O wins!</p></body></html>",
                                                            None))
            self.deactiveall()


        if game.check_the_game_stats() == "Draw":
            self.ui.textBrowser.setHtml(QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                                           u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
                                                                           "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
                                                                           "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                           "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
                                                                           "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
                                                                           "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Draw!</p></body></html>",
                                                            None))
            self.deactiveall()



if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = App()
    window.show()


    sys.exit(app.exec())