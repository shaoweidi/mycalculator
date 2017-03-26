# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:27:25 2017

@author: shao
"""
import sys
from PyQt4 import QtGui,QtCore
#from PyQt4.QtGui import *
#from PyQt4.QtCore import * 

class MyCalculator(QtGui.QWidget):
    
    def __init__(self,parent = None):
        
        super(MyCalculator,self).__init__()#将主方法设定一个名称self
        
        self.setWindowTitle('DD  Calculator')#将windows介面设置title名称

        self.setMinimumSize(300,400)#设置windows大小
        
        grid = QtGui.QGridLayout()#显示出来并设置变数
        
        global lcd#命名文字方块,全域变数
        
        lcd = QtGui.QTextBrowser()#命名文字方块

        lcd.setFixedHeight(30)#设置文字方块宽高
        
        lcd.setFixedWidth(250)
        
        lcd.setFont(QtGui.QFont("Microsoft YaHei", 10))  
        
        lcd.setText('0'.decode('utf-8'))#设置初始值及decode
        
        grid.setSpacing(1)
        
        grid.addWidget(lcd,0,0,1,5)
        
    # ---------------------按钮定义及显示-------------------------  
  
        button_0 = QtGui.QPushButton('0')  
        grid.addWidget(button_0,5,0)  
  
        button_1 = QtGui.QPushButton('1')  
        grid.addWidget(button_1,4,0)  
  
        button_2 = QtGui.QPushButton('2')  
        grid.addWidget(button_2,4,1)  
  
        button_3 = QtGui.QPushButton('3')  
        grid.addWidget(button_3,4,2)  
  
        button_4 = QtGui.QPushButton('4')  
        grid.addWidget(button_4,3,0)  
  
        button_5 = QtGui.QPushButton('5')  
        grid.addWidget(button_5,3,1)  
  
        button_6 = QtGui.QPushButton('6')  
        grid.addWidget(button_6,3,2)  
  
        button_7 = QtGui.QPushButton('7')  
        grid.addWidget(button_7,2,0)  
  
        button_8 = QtGui.QPushButton('8')  
        grid.addWidget(button_8,2,1)  
  
        button_9 = QtGui.QPushButton('9')  
        grid.addWidget(button_9,2,2)  
  
        button_plus = QtGui.QPushButton('+')  
        grid.addWidget(button_plus,2,3)  
  
        button_dec = QtGui.QPushButton('-')  
        grid.addWidget(button_dec,3,3)  
  
        button_mul = QtGui.QPushButton('X')  
        grid.addWidget(button_mul,4,3)  
  
        button_dev = QtGui.QPushButton('/')  
        grid.addWidget(button_dev,5,3)  
  
        button_eq = QtGui.QPushButton('=')  
        grid.addWidget(button_eq,5,2)  
  
        button_point = QtGui.QPushButton('.')  
        grid.addWidget(button_point,5,1)  
  
  
        button_clear = QtGui.QPushButton('Clear')  
        grid.addWidget(button_clear,1,0)  
  
        button_back = QtGui.QPushButton('Back')  
        grid.addWidget(button_back,1,1)
        
        button_close = QtGui.QPushButton('Close')  
        grid.addWidget(button_close,1,3)  
        
        self.setLayout(grid)#显示整个计算器介面  
        self.resize(300, 300)#设置计算器介面宽高
        
        #初始化我的變數與monitor

        self.symbol_variable = 0 #判断符号使用
        self.first_variable = '' #先记住第一个数字
        self.save_first_variable = '' #用来把第一个数字放到等号底下执行的变数
        self.calculator_variable = '' #按下等号之后计算出来的数字
        
        #定義事件
        QtCore.QObject.connect(button_clear,QtCore.SIGNAL("clicked()"),self.func_button_clear)
        QtCore.QObject.connect(button_back,QtCore.SIGNAL("clicked()"),self.func_button_back)
        QtCore.QObject.connect(button_close,QtCore.SIGNAL("clicked()"),self.func_button_close)
        QtCore.QObject.connect(button_1,QtCore.SIGNAL("clicked()"),self.func_button_1)
        QtCore.QObject.connect(button_2,QtCore.SIGNAL("clicked()"),self.func_button_2)
        QtCore.QObject.connect(button_3,QtCore.SIGNAL("clicked()"),self.func_button_3)
        QtCore.QObject.connect(button_4,QtCore.SIGNAL("clicked()"),self.func_button_4)
        QtCore.QObject.connect(button_5,QtCore.SIGNAL("clicked()"),self.func_button_5)
        QtCore.QObject.connect(button_6,QtCore.SIGNAL("clicked()"),self.func_button_6)
        QtCore.QObject.connect(button_7,QtCore.SIGNAL("clicked()"),self.func_button_7)
        QtCore.QObject.connect(button_8,QtCore.SIGNAL("clicked()"),self.func_button_8)
        QtCore.QObject.connect(button_9,QtCore.SIGNAL("clicked()"),self.func_button_9)
        QtCore.QObject.connect(button_0,QtCore.SIGNAL("clicked()"),self.func_button_0)        
        QtCore.QObject.connect(button_plus,QtCore.SIGNAL("clicked()"),self.func_button_plus)
        QtCore.QObject.connect(button_dec,QtCore.SIGNAL("clicked()"),self.func_button_dec)
        QtCore.QObject.connect(button_mul,QtCore.SIGNAL("clicked()"),self.func_button_mul)
        QtCore.QObject.connect(button_dev,QtCore.SIGNAL("clicked()"),self.func_button_dev)
        QtCore.QObject.connect(button_eq,QtCore.SIGNAL("clicked()"),self.func_button_eq)
    
    #清理計算器所有變數    
    def func_button_clear(self):
        
        self.symbol_variable = 0 #判断符号使用
        self.first_variable = '' #先记住第一个数字
        self.save_first_variable = '' #用来把第一个数字放到等号底下执行的变数
        self.calculator_variable = '' #按下等号之后计算出来的数字
        lcd.setText(self.first_variable)
    
    def func_button_back(self):
        
        self.first_variable = self.first_variable[:-1]
        lcd.setText(self.first_variable)
    
    def func_button_close(self):#窗口关闭时的处理，只实现这个函数就可以，不用去调用  
        
        reply = QtGui.QMessageBox.question(self,'Message',"Are you sure to quit?",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)  

        if reply == QtGui.QMessageBox.Yes:  
            app.quit()
            sys.exit(0)
        else:  
            self.ignore()
            
    def func_button_eq(self):

        if self.symbol_variable == 1:
            
            self.calculator_variable = str(int(self.save_first_variable) + int(self.first_variable))
    
            lcd.setText(self.calculator_variable)            
            
        elif self.symbol_variable == 2:
            
            self.calculator_variable = str(int(self.save_first_variable) - int(self.first_variable))
            
            lcd.setText(self.calculator_variable)
            
        elif self.symbol_variable == 3:
            
            self.calculator_variable = str(int(self.save_first_variable) * int(self.first_variable))
            
            lcd.setText(self.calculator_variable)
            
        elif self.symbol_variable == 4:
            
            self.calculator_variable = str(int(self.save_first_variable) / int(self.first_variable))
            
            lcd.setText(self.calculator_variable)
                  
    def func_button_plus(self):
        
        if self.symbol_variable == 0:
            
            self.save_first_variable = self.first_variable

            self.first_variable = ''            
            
            lcd.setText(self.first_variable)           
            
            self.symbol_variable = 1            
            
        elif self.symbol_variable == 1:
            
            self.save_first_variable = str(int(self.save_first_variable) + int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''
            
            self.symbol_variable = 1 

        elif self.symbol_variable == 2:
            
            self.save_first_variable = str(int(self.save_first_variable) - int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 1
    
        elif self.symbol_variable == 3:

            self.save_first_variable = str(int(self.save_first_variable) * int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 1

        elif self.symbol_variable == 4:

            self.save_first_variable = str(int(self.save_first_variable) / int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 1

    def func_button_dec(self):
        
        if self.symbol_variable == 0:
            
            self.save_first_variable = self.first_variable

            self.first_variable = ''            
            
            lcd.setText(self.first_variable)           
            
            self.symbol_variable = 2            
            
        elif self.symbol_variable == 1:
            
            self.save_first_variable = str(int(self.save_first_variable) + int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''
            
            self.symbol_variable = 2 

        elif self.symbol_variable == 2:
            
            self.save_first_variable = str(int(self.save_first_variable) - int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 2
    
        elif self.symbol_variable == 3:

            self.save_first_variable = str(int(self.save_first_variable) * int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 2

        elif self.symbol_variable == 4:

            self.save_first_variable = str(int(self.save_first_variable) / int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 2
            
    def func_button_mul(self):
        
        if self.symbol_variable == 0:
            
            self.save_first_variable = self.first_variable

            self.first_variable = ''            
            
            lcd.setText(self.first_variable)           
            
            self.symbol_variable = 3            
            
        elif self.symbol_variable == 1:
            
            self.save_first_variable = str(int(self.save_first_variable) + int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''
            
            self.symbol_variable = 3 

        elif self.symbol_variable == 2:
            
            self.save_first_variable = str(int(self.save_first_variable) - int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 3
    
        elif self.symbol_variable == 3:

            self.save_first_variable = str(int(self.save_first_variable) * int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 3

        elif self.symbol_variable == 4:

            self.save_first_variable = str(int(self.save_first_variable) / int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 3
            
    def func_button_dev(self):
        
        if self.symbol_variable == 0:
            
            self.save_first_variable = self.first_variable

            self.first_variable = ''            
            
            lcd.setText(self.first_variable)           
            
            self.symbol_variable = 4            
            
        elif self.symbol_variable == 1:
            
            self.save_first_variable = str(int(self.save_first_variable) + int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''
            
            self.symbol_variable = 4 

        elif self.symbol_variable == 2:
            
            self.save_first_variable = str(int(self.save_first_variable) - int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 4
    
        elif self.symbol_variable == 3:

            self.save_first_variable = str(int(self.save_first_variable) * int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 4

        elif self.symbol_variable == 4:

            self.save_first_variable = str(int(self.save_first_variable) / int(self.first_variable))
            
            lcd.setText(self.save_first_variable)
            
            self.first_variable = ''

            self.symbol_variable = 4
            
    def func_button_1(self):
            
        self.first_variable = self.first_variable + '1'
        lcd.setText(self.first_variable)
        
    def func_button_2(self):
        
        self.first_variable = self.first_variable + '2'
        lcd.setText(self.first_variable)
            
    def func_button_3(self):
        
        self.first_variable = self.first_variable + '3'
        lcd.setText(self.first_variable) 

    def func_button_4(self):
        
        self.first_variable = self.first_variable + '4'
        lcd.setText(self.first_variable) 
           
    def func_button_5(self):
        
        self.first_variable = self.first_variable + '5'
        lcd.setText(self.first_variable)         

    def func_button_6(self):
        
        self.first_variable = self.first_variable + '6'
        lcd.setText(self.first_variable)

    def func_button_7(self):
        
        self.first_variable = self.first_variable + '7'
        lcd.setText(self.first_variable)

    def func_button_8(self):
        
        self.first_variable = self.first_variable + '8'
        lcd.setText(self.first_variable) 

    def func_button_9(self):
        
        self.first_variable = self.first_variable + '9'
        lcd.setText(self.first_variable)
            
    def func_button_0(self):
        
        self.first_variable = self.first_variable + '0'
        lcd.setText(self.first_variable)            
            
    
if __name__ == "__main__":
    app = 0
    app = QtGui.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    myapp = MyCalculator()  
    myapp.show()  
    sys.exit(app.exec_())  



