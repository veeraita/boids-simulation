'''
Created on Mar 16, 2017

@author: Veera
'''

import time
from layout import SimulationLayout
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication

class BoidsSimulation(QMainWindow):
    
    def __init__(self, boids_number):
        
        super(BoidsSimulation, self).__init__()
        
        self.setWindowTitle('Boids Simulation')
        self.setGeometry(100, 100, 1200, 1100)
        
        self.form = SimulationLayout(boids_number)
        
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.form)
        
        self.setCentralWidget(widget)
        
        self.continue_running = True
        
        self.show()
        
    def moveBoids(self):
        
        while self.continue_running:
            
            time.sleep(0.1)
            QApplication.processEvents()
            
            for boid in self.form.boids:
                boid.changeVelocity(self.form.boids)
                boid.moveBy(boid.velocity.x(), boid.velocity.y())
                boid.updatePosVector()
                
    def closeEvent(self, event):

        self.continue_running = False
        event.accept()
                