'''
Created on Mar 16, 2017

@author: Veera
'''
from boid import Boid
from threading import Thread
import time

class BoidMover(Thread):
    
    def __init__(self, boid, boids):
        
        super(BoidMover, self).__init__()
        self.boid = boid
        self.boids = boids
        
    def run(self):
        
        while True:
            
            time.sleep(0.2)

            self.boid.limitSpeed()
            self.boid.bounceWall()
            
            #self.boid.changeVelocity(self.boids, 0.1, 0.1, 0.1)

            self.boid.moveBy(self.boid.velocity.x(), self.boid.velocity.y())
            #self.boid.moveBy(5, 5)
            
            