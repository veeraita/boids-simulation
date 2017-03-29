'''
Created on Mar 16, 2017

@author: Veera
'''
import random
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
        self.pos_vector = QVector2D(self.xcoord,self.ycoord)
       
    def setGraphics(self):
        
        width = 2*BOID_RADIUS
        height = 2*BOID_RADIUS
        
        self.setRect(0, 0, width, height)
        self.setPos(self.xcoord, self.ycoord)
        
        brush = QBrush(1)
        self.setBrush(brush)
    
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
        pass
    
    def alignment(self, boids):
        # Lenna samaa nopeutta kuin muu parvi keskimaarin    
        pass
    
    def cohesion(self, boids):
        # Pyri kohti parven keskipistetta 
        pass
    
    def changeVelocity(self, boids):
        # Muodosta linnun nopeutta muuttava vektori    
        v1 = self.separation(boids)
        v2 = self.alignment(boids)
        v3 = self.cohesion(boids)
        change = v1 + v2 + v3
        return change
    
    def move(self, boids):
        #change = self.changeVelocity(boids)
        self.bounceWall()
        self.limitSpeed()
        self.moveBy(self.velocity.x(), self.velocity.y())