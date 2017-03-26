'''
Created on Mar 16, 2017

@author: Veera
'''
import random
from PyQt5.QtGui import QVector2D, QBrush
from PyQt5.Qt import QGraphicsEllipseItem

MAX_SPEED = 30.0
RADIUS = 50.0 #yksilon havaintoetaisyys
BOID_RADIUS = 7.0 #maarittaa pisteen koon
WALL_MARGIN = 10
WALL_FORCE = 5.0
SCREEN_WIDTH = 700.0
SCREEN_HEIGHT = 700.0

class Boid(QGraphicsEllipseItem):
    '''
    Luokka edustaa parven yksiloita
    '''

    def __init__(self):
        '''
        Alustetaan lintujen sijainnit ja nopeudet satunnaisiksi
        '''
        super(Boid, self).__init__()
        
        self.xcoord = random.uniform(0.0, SCREEN_WIDTH)
        self.ycoord = random.uniform(0.0, SCREEN_HEIGHT)
        self.setPos(self.xcoord, self.ycoord)
        self.position = QVector2D(self.pos())
        
        self.speed = random.uniform(10, MAX_SPEED)
        self.velocity = QVector2D(random.uniform(-1,1),random.uniform(-1,1))*self.speed
        
        self._setGraphics(self.xcoord, self.ycoord)
        
    def _setGraphics(self, x, y):
        
        left = self.xcoord - BOID_RADIUS
        top = self.ycoord + BOID_RADIUS
        width = 2*BOID_RADIUS
        height = 2*BOID_RADIUS
        
        self.setRect(left, top, width, height)
        
        brush = QBrush(1)
        self.setBrush(brush)
        
    def getDistance(self, other_boid):
        # Etaisyys toiseen lintuun
        d_vector = other_boid.position - self.position
        return d_vector.length()
        
    def bounceWall(self):
        # Valta alueen reunoja
        if self.scenePos().x() < WALL_MARGIN:
            self.velocity.setX(self.velocity.x() + WALL_FORCE)
        elif self.scenePos().x() > SCREEN_WIDTH - WALL_MARGIN:
            self.velocity.setX(self.velocity.x() - WALL_FORCE)
        if self.scenePos().y() < WALL_MARGIN:
            self.velocity.setY(self.velocity.y() + WALL_FORCE)
        elif self.scenePos().y() > SCREEN_HEIGHT - WALL_MARGIN:
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
        self.change = v1 + v2 + v3
    
    def move(self):
        pass