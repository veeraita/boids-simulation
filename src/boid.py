'''
Created on Mar 16, 2017

@author: Veera
'''
import random
import time

from PyQt5.QtGui import QVector2D, QBrush
from PyQt5.Qt import QGraphicsEllipseItem

MAX_SPEED = 20.0
RADIUS = 50.0 #yksilon havaintoetaisyys
BOID_RADIUS = 5.0 #maarittaa pisteen koon
WALL_MARGIN = 70
WALL_FORCE = 5.0
SCENE_WIDTH = 900.0
SCENE_HEIGHT = 800.0

class Boid(QGraphicsEllipseItem):
    '''
    Luokka edustaa parven yksiloita
    '''

    def __init__(self):
        '''
        Alustetaan lintujen sijainnit ja nopeudet satunnaisiksi
        '''
        super(Boid, self).__init__()
        
        self.xcoord = random.uniform(50, SCENE_WIDTH-50)
        self.ycoord = random.uniform(50, SCENE_HEIGHT-50)
        
        self.speed = random.uniform(5, MAX_SPEED)
        self.velocity = QVector2D(random.uniform(-1,1),random.uniform(-1,1))*self.speed
        #self.updatePosVector()
       
    def setGraphics(self):
        
        width = 2*BOID_RADIUS
        height = 2*BOID_RADIUS
        
        self.setRect(0, 0, width, height)
        self.setPos(self.xcoord, self.ycoord)
        
        brush = QBrush(1)
        self.setBrush(brush)
        
    def updatePosVector(self):
        self.pos_vector = QVector2D(self.x(), self.y())
        print(self.pos_vector)
    
    def getDistance(self, other_boid):
        # Etaisyys toiseen lintuun
        d_vector = other_boid.pos_vector - self.pos_vector
        return d_vector.length()
        
    def bounceWall(self):
        # Valta alueen reunoja
        if self.x() < WALL_MARGIN:
            self.velocity.setX(self.velocity.x() + WALL_FORCE)
        elif self.x() > SCENE_WIDTH - WALL_MARGIN:
            self.velocity.setX(self.velocity.x() - WALL_FORCE)
        if self.y() < WALL_MARGIN:
            self.velocity.setY(self.velocity.y() + WALL_FORCE)
        elif self.y() > SCENE_HEIGHT - WALL_MARGIN:
            self.velocity.setY(self.velocity.y() - WALL_FORCE)
            
    def limitSpeed(self):
        # Estetaan nopeuden liiallinen kasvu
        if self.velocity.length() > MAX_SPEED:
            self.velocity = self.velocity.normalized() * MAX_SPEED
    
    def separation(self, boids):
        # Valta tormailya muihin lintuihin
        
        separation_vector = QVector2D()
        
        for boid in boids:
            
            if boid is not self:
                
                dist = self.getDistance(boid)
                if dist < RADIUS and dist > 0:
                    
                    force = (self.pos_vector - boid.pos_vector)
                    
                    force /= (dist ** 2)
                    
                    separation_vector += force
                    
        return separation_vector
    
    def alignment(self, boids):
        # Lenna samaa nopeutta kuin muu parvi keskimaarin    
        #lenna samaa nopeutta kuin muu parvi keskimaarin
        #lasketaan lahella olevien lintujen keskimaarainen nopeus
        avg_vel = QVector2D()
        
        for boid in boids:
            
            if boid is not self:
                dist = self.getDistance(boid)
                
                if dist < RADIUS and dist > 0:                
                    avg_vel += boid.velocity
        
        return avg_vel
    
    def cohesion(self, boids):
        # Pyri kohti parven keskipistetta 
        
        avg_position = QVector2D()
        # Lasketaan parven "massakeskipiste"
        for boid in boids:
            
            if boid is not self:
                
                avg_position += boid.pos_vector
        
        avg_position /= (len(boids) -1)
        
        return (avg_position - self.pos_vector)
    
    def changeVelocity(self, boids):
        # Muodosta linnun nopeutta muuttava vektori 
        while True:   
            time.sleep(1)
            #print(self.velocity)
            v1 = self.separation(boids)
            v2 = self.alignment(boids)
            v3 = self.cohesion(boids)
            #print("v1 = ", v1)
            #print("v2 = ", v2)
            print("v3 = ", v3)
            change = v1 + v2 + v3
            self.velocity += change
            self.bounceWall()
            self.limitSpeed()
    
    def move(self):
        while True:
            time.sleep(1)

            self.moveBy(self.velocity.x(), self.velocity.y())
            self.updatePosVector()