'''
Created on Mar 16, 2017

@author: Veera
'''
from PyQt5.QtWidgets import QWidget, QSlider, QVBoxLayout, QLCDNumber, QPushButton, QApplication
from PyQt5.QtCore import Qt
import sys
from run_simulation import BoidsSimulation

class Start(QWidget):
    
    def __init__(self):
        
        super(Start, self).__init__()
        
        lcd = QLCDNumber()
        self.sld = QSlider(Qt.Horizontal, self)
        btn = QPushButton('Done', self)
        btn.clicked.connect(self.buttonClicked)
        
        self.sld.valueChanged.connect(lcd.display)
        self.sld.setRange(5, 70)
        
        layout = QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(self.sld)
        layout.addWidget(btn)

        self.setLayout(layout)
        
        self.setGeometry(800, 500, 800, 300)
        self.setWindowTitle('Determine the number of boids.')
        
        self.show()
        
    def buttonClicked(self):
        
        self.boids_number = self.sld.value()
        self.close()
        
        simulation = BoidsSimulation(self.boids_number)
        
        simulation.moveBoids()
        
def main():
    
    app = QApplication(sys.argv)
    start_sim = Start()
    app.exec_()
    
    
if __name__ == '__main__':
    
    sys.exit(main())
        