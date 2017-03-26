'''
Created on Mar 16, 2017

@author: Veera
'''

from layout import SimulationLayout
from start_slider import Slider
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication
from move_boids import BoidMover
import sys

class BoidsSimulation(QMainWindow):
    
    def __init__(self, boids_number):
        
        super(BoidsSimulation, self).__init__()
        
        self.setWindowTitle('Parvisimulaatio')
        #self.boids_numer = boids_number
        
        self.form = SimulationLayout(boids_number)
        
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.form)
        
        self.setCentralWidget(widget)
        
        self.resize(1200, 1200)
        
    def move_boids(self):
        
        boids = self.form.boids
        for boid in boids:
            thread = BoidMover(boid, boids)
            thread.start()
            
            
def main():
    
    app1 = QApplication(sys.argv)
    slider_window = Slider()
    slider_window.show()
    app1.exec_()
    
    app2 = QApplication(sys.argv)
    simulation = BoidsSimulation(slider_window.boids_number) 
    simulation.move_boids()  
    simulation.show()
    app2.exec_()   
    
        
if __name__ == '__main__':
    
    sys.exit(main())