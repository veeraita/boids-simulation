'''
Created on Mar 16, 2017

@author: Veera
'''
import random
from PyQt5.QtGui import QVector2D, QBrush
from PyQt5.Qt import QGraphicsEllipseItem

MAX_SPEED = 5.0
RADIUS = 75.0
BOID_RADIUS = 7.0
WALL_FORCE = 5.0
SCREEN_WIDTH = 450.0
SCREEN_HEIGHT = 450.0

class Boid(QGraphicsEllipseItem):
    '''
    Luokka edustaa parven yksiloita
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(Boid, self).__init__()
        
        self.xcoord = random.uniform(0.0, SCREEN_WIDTH)
        self.ycoord = random.uniform(0.0, SCREEN_HEIGHT)
        self.setPos(self.xcoord, self.ycoord)
        self.position = QVector2D(self.pos())
        
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
        #etaisyys toiseen lintuun       
        d_vector = other_boid.position - self.position
        return d_vector.length()
        
    def bounceWall(self):
        pass
    
    def separation(self):
        pass
    
    def alignment(self):
        pass
    
    def cohesion(self):
        pass
    
    def changeVelocity(self):
        pass