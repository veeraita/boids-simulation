'''
Created on Mar 16, 2017

@author: Veera
'''
import sys
import time
from threading import Thread

from layout import SimulationLayout
from start_slider import Slider
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
        
    def moveBoids(self):
        
        while True:
            time.sleep(0.2)
            QApplication.processEvents()
            for boid in self.form.boids:
                boid.moveBy(boid.velocity.x(), boid.velocity.y())
                boid.updatePosVector()
                
      
            
def main():
    
    app1 = QApplication(sys.argv)
    slider_window = Slider()
    slider_window.show()
    app1.exec_()
    
    app2 = QApplication(sys.argv)
    simulation = BoidsSimulation(slider_window.boids_number) 
    simulation.show()
    
    boids = simulation.form.boids

    # Kaynnista saikeet lintujen nopeuden muutoksen laskemiseksi
    for boid in boids:
        thread = Thread(target=boid.changeVelocity, args=(boids,))
        thread.start()
        
    simulation.moveBoids() # Linnut lentamaan
     
    app2.exec_()
    
        
if __name__ == '__main__':
    
    sys.exit(main())