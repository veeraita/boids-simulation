'''
Created on Mar 16, 2017

@author: Veera
'''
import random
import time

from PyQt5.QtGui import QVector2D, QBrush
from PyQt5.Qt import QGraphicsEllipseItem

MAX_SPEED = 15
RADIUS = 150.0 #yksilon havaintoetaisyys
BOID_RADIUS = 5.0 #maarittaa pisteen koon
WALL_MARGIN = 100
WALL_FORCE = 10000000
SCENE_WIDTH = 900.0
SCENE_HEIGHT = 800.0

DEFAULT_S = 50000
RANGE_S = 30000
DEFAULT_A = 350
RANGE_A = 300
DEFAULT_C = 30
RANGE_C = 25

ws = DEFAULT_S
wa = DEFAULT_A
wc = DEFAULT_C


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
    
    def getDistance(self, other_boid):
        # Etaisyys toiseen lintuun
        self.updatePosVector()
        other_boid.updatePosVector()
        d_vector = other_boid.pos_vector - self.pos_vector
        return d_vector.length()
        
    def bounceWall(self):
        # Valta alueen reunoja
        if self.x() < WALL_MARGIN:
            self.velocity.setX(self.velocity.x() + WALL_FORCE/self.x()**2)
        elif self.x() > SCENE_WIDTH - WALL_MARGIN:
            self.velocity.setX(self.velocity.x() - WALL_FORCE/(SCENE_WIDTH - self.x())**2)
        if self.y() < WALL_MARGIN:
            self.velocity.setY(self.velocity.y() + WALL_FORCE/self.y()**2)
        elif self.y() > SCENE_HEIGHT - WALL_MARGIN:
            self.velocity.setY(self.velocity.y() - WALL_FORCE/(SCENE_HEIGHT - self.y())**2)
            
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
                if dist < RADIUS:
                    
                    separation_vector += ((self.pos_vector - boid.pos_vector)/(dist**2))
                    
        return separation_vector
    
    def alignment(self, boids):
        # Lenna samaa nopeutta kuin muu parvi keskimaarin    
        #lenna samaa nopeutta kuin muu parvi keskimaarin
        #lasketaan lahella olevien lintujen keskimaarainen nopeus
        avg_vel = QVector2D()
        
        for boid in boids:
            
            if boid is not self:
                               
                    avg_vel += boid.velocity
        
        avg_vel /= (len(boids)-1)
        
        return avg_vel
    
    def cohesion(self, boids):
        # Pyri kohti parven keskipistetta 
        
        avg_position = QVector2D()
        # Lasketaan parven "massakeskipiste"
        for boid in boids:
            
            if boid is not self:
                
                avg_position += boid.pos_vector
        
        avg_position /= (len(boids)-1)
        
        return (avg_position - self.pos_vector)
    
    def changeVelocity(self, boids):
        # Muodosta linnun nopeutta muuttava vektori
        global ws
        global wa
        global wc
        
        #while True:
        #time.sleep(0.1)
        #print(self.velocity)
        v1 = self.separation(boids)
        v2 = self.alignment(boids)
        v3 = self.cohesion(boids)

        change = v1*ws + v2*wa + v3*wc
        self.velocity += change
        self.bounceWall()
        self.limitSpeed()
        
def get_ws(value):
    global ws
    ws = value

def get_wa(value):
    global wa
    wa = value

def get_wc(value):
    global wc
    wc = value

            
    