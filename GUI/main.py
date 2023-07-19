from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import sys
import os
from mainconsole import Ui_MainWindow

import requests
# import zipfile


class MainWindow(QtWidgets.QMainWindow):
    dlg = None
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.textEdit.setText(self.URL)
        self.ui.startButton.clicked.connect(self.start_reading)
        self.ui.stoplButton.clicked.connect(self.stop_reading)
        self.ui.settingButton.clicked.connect(self.cmdsettings)
        self.ui.shutDownButton_2.clicked.connect(self.cmdshutdown)
        self.ui.pushButton.clicked.connect(self.tare_weight)
        
        

    def cmdsettings(self):
        print("settings")
         #print(url)
    
    def cmdshutdown(self):
         print("cancle")
         self.close()
    
    def start_reading(self):
        print("start")
        
    def stop_reading(self):
        print("stop")
        

    def tare_weight(self):
        print("tare")

   
    
 

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    
   
    window.showMaximized()
    sys.exit(app.exec_())
