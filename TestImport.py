import cppAdd
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QValidator, QDoubleValidator, QIntValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QHBoxLayout, QWidget
i=5
j=15

#k = cppAdd.add(i,j)
#help(cppAdd)

#print(k)

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()



        self.setMaximumSize(QSize(800,600))
        self.setWindowTitle("C++ Port Test")

        self.counter = 0
        self.input1Val = None
        self.input2Val = None
        
        self.button = QPushButton("Push")
        self.input1 = QLineEdit()
        self.input1.setInputMask('00000;_')

        self.input2 = QLineEdit()
        self.input2.setInputMask('00000;_')

        self.output = QLabel("Durr")

        layout = QHBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(self.button)
        layout.addWidget(self.output)

        mainWidget = QWidget()
        mainWidget.setLayout(layout)




        self.input1.textChanged.connect(self.input1Received)
        self.input2.textChanged.connect(self.input2Received)
        self.button.clicked.connect(self.button_click)
        

        self. setCentralWidget(mainWidget)
    def input1Received(self,inputVal):
        self.input1Val = int(inputVal)
        #print(self.input1Val)
    
    def input2Received(self,inputVal):
        self.input2Val = int(inputVal)
        #print(self.input2Val)
    
    def button_click(self):
            self.counter += 1
            self.button.setText("The count is {count}".format(count = self.counter))
            if (self.input1Val != None and self.input2Val != None):
                result = cppAdd.add(self.input1Val, self.input2Val)
                self.output.setText("{result}".format(result = result))
            else:
                print("The input values are not defined")
    
            

app = QApplication([])

window = AppWindow()
window.show()

#This is an infinite event loop
app.exec()


#This will not be reached
