'''
Created on Mar 16, 2017

@author: Veera
'''
import sys
import time
from threading import Thread

from layout import SimulationLayout
from start_slider import Slider
from move_thread import MoveThread
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication
from PyQt5.QtCore import QObject, QThread, pyqtSignal

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
        '''
        for boid in boids:
            #boid_object = BoidRunner(boid, boids)
            thread = QThread()
            #boid_object.moveToThread(thread)
            #self.form.startbtn.clicked.connect(thread.start)
            #thread.started.connect(boid_object.keep_running)
            #boid_object.temp_velocity.connect(boid.move)
            thread.start()
        '''
        '''
        for boid in boids:
            thread = MoveThread(boid, boids)
            thread.temp_velocity.connect(boid.move)
            thread.start()
        '''  
'''
class BoidRunner(QObject):
    
    temp_velocity = pyqtSignal(object)
    
    def __init__(self, boid, boids):
        super(BoidRunner, self).__init__()
        self.boid = boid
        self.boids = boids
        
    def keep_running(self):
        
        while True:        
            # Laske muutos
            time.sleep(1)
            self.boid.change_velocity(self.boids)
            #self.temp_velocity.emit(temp)
'''    
class BoidRunner2(QObject):
    
    temp_velocity = pyqtSignal(object)
    
    def __init__(self, boids):
        super(BoidRunner2, self).__init__()
        self.boids = boids
        
    def keep_running(self):
        
        while True:        
            '''
            # Laske muutos
            '''
            time.sleep(1)
            for boid in self.boids:
                boid.change_velocity(self.boids)
                #self.temp_velocity.emit(temp) 
                continue       
            
def main():
    
    app1 = QApplication(sys.argv)
    slider_window = Slider()
    slider_window.show()
    app1.exec_()
    
    app2 = QApplication(sys.argv)
    simulation = BoidsSimulation(slider_window.boids_number) 
    simulation.show()
    #simulation.moveBoids()
    boids = simulation.form.boids
    '''
    for boid in boids:
        thread = QThread()
        worker_object = BoidRunner(boid, boids)
        worker_object.moveToThread(thread)
        thread.started.connect(worker_object.keep_running)
        worker_object.temp_velocity.connect(boid.move)
        thread.start()
    '''
    # Kaynnista saikeet lintujen nopeuden muutoksen laskemiseksi
    for boid in boids:
        thread = Thread(target=boid.changeVelocity, args=(boids,))
        thread.start()
     
    app2.exec_()
    
        
if __name__ == '__main__':
    
    sys.exit(main())