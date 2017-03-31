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
        
        separation_vector = QVector2D()
        
        for boid in boids:
            
            if boid is not self:
                
                dist = self.getDistance(boid)
                if dist < RADIUS and dist > 0:
                    
                    force = (self.pos_vector - boid.pos_vector)
                    #print(force)
                    force /= (dist ** 2)
                    
                    separation_vector += force
        #print(separation_vector)
                    
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
                    
        alignment_vector = avg_vel
        #print(alignment_vector)
        
        return alignment_vector
    
    def cohesion(self, boids):
        # Pyri kohti parven keskipistetta 
        
        avg_x = 0
        avg_y = 0
        # Lasketaan parven "massakeskipiste"
        for boid in boids:
            
            if boid is not self:
                
                if self.distance(boid) < RADIUS:
                    
                    avg_x += (self.x() - boid.x())
                    avg_y += (self.y() - boid.y())
        
        avg_x /= len(boids)
        avg_y /= len(boids)
        
        avg_position = QVector2D(avg_x, avg_y)
        
        cohesion_vector = (avg_position - self.pos_vector)
        #print(cohesion_vector)
        
        return cohesion_vector
    
    def changeVelocity(self, boids):
        # Muodosta linnun nopeutta muuttava vektori    
        v1 = self.separation(boids)
        v2 = self.alignment(boids)
        v3 = self.cohesion(boids)
        change = v1 + v2 + v3
        self.velocity += change
    
    def move(self, boids):
        #self.velocity += self.changeVelocity(boids)
        self.bounceWall()
        self.limitSpeed()
        #self.moveBy(self.velocity.x(), self.velocity.y())
        self.moveBy(5, 5)
        