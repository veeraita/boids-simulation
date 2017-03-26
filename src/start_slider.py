'''
Created on Mar 16, 2017

@author: Veera
'''
from PyQt5.QtWidgets import QWidget, QSlider, QVBoxLayout, QLCDNumber, QPushButton
from PyQt5.QtCore import Qt

class Slider(QWidget):
    
    def __init__(self):
        
        super(Slider, self).__init__()
        
        lcd = QLCDNumber()
        self.sld = QSlider(Qt.Horizontal, self)
        btn = QPushButton('Done', self)
        btn.clicked.connect(self.buttonClicked)
        
        self.sld.setMaximum(30)
        
        layout = QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(self.sld)
        layout.addWidget(btn)

        self.setLayout(layout)
        self.sld.valueChanged.connect(lcd.display)
        
        self.setGeometry(800, 500, 800, 300)
        self.setWindowTitle('Determine the number of boids.')
        
    def buttonClicked(self):
        
        self.boids_number = self.sld.value()
        self.close()