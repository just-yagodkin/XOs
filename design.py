from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QSizePolicy, QTextBrowser, QWidget, QLabel)
import files_rc

class Ui_MainwWindow(object):

    def setupUi(self, MainwWindow):
        if not MainwWindow.objectName():
            MainwWindow.setObjectName(u"MainwWindow")
        MainwWindow.resize(430, 420)
        MainwWindow.setMinimumSize(QSize(430, 420))
        MainwWindow.setWindowIcon(QIcon("pictures/XOs.png"))
        MainwWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.centralwidget = QWidget(MainwWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_1.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: white;\n"
                                    "    border: none;\n"
                                    "}")
        self.gridLayout.addWidget(self.button_1, 0, 0, 1, 1)


        self.button_2 = QPushButton(self.centralwidget)
        self.button_2.setObjectName(u"button_2")
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_2.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: white;\n"
                                    "    border: none;\n"
                                    "}")
        self.gridLayout.addWidget(self.button_2, 0, 1, 1, 1)


        self.button_3 = QPushButton(self.centralwidget)
        self.button_3.setObjectName(u"button_3")
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_3.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: white;\n"
                                    "    border: none;\n"
                                    "}")
        self.gridLayout.addWidget(self.button_3, 0, 2, 1, 1)


        self.button_4 = QPushButton(self.centralwidget)
        self.button_4.setObjectName(u"button_4")
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_4.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: white;\n"
                                    "    border: none;\n"
                                    "}")
        self.gridLayout.addWidget(self.button_4, 1, 0, 1, 1)


        self.button_5 = QPushButton(self.centralwidget)
        self.button_5.setObjectName(u"button_5")
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_5.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: white;\n"
                                    "    border: none;\n"
                                    "}")
        self.gridLayout.addWidget(self.button_5, 1, 1, 1, 1)


        self.button_6 = QPushButton(self.centralwidget)
        self.button_6.setObjectName(u"button_6")
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_6.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: white;\n"
                                    "    border: none;\n"
                                    "}")
        self.gridLayout.addWidget(self.button_6, 1, 2, 1, 1)


        self.button_7 = QPushButton(self.centralwidget)
        self.button_7.setObjectName(u"button_7")
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_7.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: white;\n"
                                    "    border: none;\n"
                                    "}")
        self.gridLayout.addWidget(self.button_7, 2, 0, 1, 1)


        self.button_8 = QPushButton(self.centralwidget)
        self.button_8.setObjectName(u"button_8")
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_8.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: white;\n"
                                    "    border: none;\n"
                                    "}")
        self.gridLayout.addWidget(self.button_8, 2, 1, 1, 1)


        self.button_9 = QPushButton(self.centralwidget)
        self.button_9.setObjectName(u"button_9")
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_9.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: white;\n"
                                    "    border: none;\n"
                                    "}")
        self.gridLayout.addWidget(self.button_9, 2, 2, 1, 1)



        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy1)
        self.textBrowser.setMinimumSize(QSize(10, 50))
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
                                       "    background-color: transparent;\n"
                                       "	font: 700 14pt \"Segoe Print\";\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "")

        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 2, 1)

        self.repeatbutton = QPushButton(self.centralwidget)
        self.repeatbutton.setObjectName(u"repeatbutton")
        self.repeatbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.repeatbutton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.repeatbutton, 1, 1, 1, 1)

        self.Exitbutton = QPushButton(self.centralwidget)
        self.Exitbutton.setObjectName(u"Exitbutton")
        self.Exitbutton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.Exitbutton, 2, 1, 1, 1)

        MainwWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainwWindow)

        QMetaObject.connectSlotsByName(MainwWindow)

    def retranslateUi(self, MainwWindow):
        font = QFont()
        font.setPointSize(9)
        MainwWindow.setWindowTitle(QCoreApplication.translate("MainwWindow", u"TicTacToe", None))
        self.button_1.setText(QCoreApplication.translate("MainwWindow", u"", None))
        self.button_1.setShortcut(QCoreApplication.translate("MainwWindow", u"Home", None))
        self.button_2.setText(QCoreApplication.translate("MainwWindow", u"", None))
        self.button_2.setShortcut(QCoreApplication.translate("MainwWindow", u"Up", None))
        self.button_3.setText(QCoreApplication.translate("MainwWindow", u"", None))
        self.button_3.setShortcut(QCoreApplication.translate("MainwWindow", u"PgUp", None))
        self.button_4.setText(QCoreApplication.translate("MainwWindow", u"", None))
        self.button_4.setShortcut(QCoreApplication.translate("MainwWindow", u"Left", None))
        self.button_5.setText(QCoreApplication.translate("MainwWindow", u"", None))
        self.button_5.setShortcut(QCoreApplication.translate("MainwWindow", u"Clear", None))
        self.button_6.setText(QCoreApplication.translate("MainwWindow", u"", None))
        self.button_6.setShortcut(QCoreApplication.translate("MainwWindow", u"Right", None))
        self.button_7.setText(QCoreApplication.translate("MainwWindow", u"", None))
        self.button_7.setShortcut(QCoreApplication.translate("MainwWindow", u"End", None))
        self.button_8.setText(QCoreApplication.translate("MainwWindow", u"", None))
        self.button_8.setShortcut(QCoreApplication.translate("MainwWindow", u"Down", None))
        self.button_9.setText(QCoreApplication.translate("MainwWindow", u"", None))
        self.button_9.setShortcut(QCoreApplication.translate("MainwWindow", u"PgDown", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainwWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
        u"4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" "
        "content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n""li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n""</style></head><body style=\" font-family:'Segoe Print';"
        "font-size:14pt; font-weight:700; font-style:normal;\">\n""<p align=\"center\" style=\" margin-top:0px;"
        "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Started!</p></body></html>", None))

        self.button_1.setFont(font)
        self.button_2.setFont(font)
        self.button_3.setFont(font)
        self.button_4.setFont(font)
        self.button_5.setFont(font)
        self.button_6.setFont(font)
        self.button_7.setFont(font)
        self.button_8.setFont(font)
        self.button_9.setFont(font)

        self.repeatbutton.setText(QCoreApplication.translate("MainwWindow", u"Play again", None))
        self.repeatbutton.setShortcut(QCoreApplication.translate("MainwWindow", u"Ins", None))
        self.Exitbutton.setText(QCoreApplication.translate("MainwWindow", u"Exit", None))
        self.Exitbutton.setShortcut(QCoreApplication.translate("MainwWindow", u"Del", None))

