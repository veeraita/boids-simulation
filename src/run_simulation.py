'''
Created on Mar 16, 2017

@author: Veera
'''

from layout import SimulationLayout
from start_slider import Slider
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication
from PyQt5.QtCore import QObject, QThread
import sys, time

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
        
    def moveBoids(self):
        
        boids = self.form.boids
        
        for boid in boids:
            boid_object = BoidRunner(boid)
            thread = QThread()
            boid_object.moveToThread(thread)
            #self.form.startbtn.clicked.connect(thread.start)
            thread.started.connect(boid_object.keep_running)
            thread.start()
            print(thread.isRunning())

            
class BoidRunner(QObject):
    
    def __init__(self, boid):
        super(BoidRunner, self).__init__()
        self.boid = boid
        
    def keep_running(self):
        
        while True:
            time.sleep(0.2)
            self.boid.moveBy(5, 5)
            
            
def main():
    
    app1 = QApplication(sys.argv)
    slider_window = Slider()
    slider_window.show()
    app1.exec_()
    
    app2 = QApplication(sys.argv)
    simulation = BoidsSimulation(slider_window.boids_number) 
    simulation.moveBoids()
    simulation.show()
    app2.exec_()
    
        
if __name__ == '__main__':
    
    sys.exit(main())