'''
Created on Mar 31, 2017

@author: Veera
'''
import threading
import time

from PyQt5.QtCore import QThread, pyqtSignal

class MoveThread(QThread):
    
    temp_velocity = pyqtSignal(object)
    
    def __init__(self, boid, boids):
        
        super(MoveThread, self).__init__()
        self.boid = boid
        self.boids = boids
        
    def run(self):
        
        while True:
            
            time.sleep(0.2)

            #self.boid.move(self.boids)
            temp = self.boid.change_velocity(self.boids)
            self.temp_velocity.emit(temp)
        