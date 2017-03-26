'''
Created on Mar 16, 2017

@author: Veera
'''
from boid import Boid, SCREEN_WIDTH, SCREEN_HEIGHT
from weightslider import WeightSlider
from start_slider import Slider
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QHBoxLayout, QVBoxLayout, QLabel

class SimulationLayout(QWidget):

    def __init__(self, boids_number):
        
        super(SimulationLayout, self).__init__()
        self.init_slider = Slider()
        self.boids_number = boids_number
        self.boids = []
        # lisataan haluttu maara boid-yksiloita listaan
        for i in range(self.boids_number):
            self.boids.append(Boid())
        #self.setGeometry(100, 100, 800, 800)
        self.__layout()
        
    def __layout(self):
        
        sld1 = WeightSlider('Separation')
        sld2 = WeightSlider('Alignment')
        sld3 = WeightSlider('Cohesion')
        
        scene = self.setScene()
        self.view = QGraphicsView(scene)
        #self.view.setSceneRect(scene.sceneRect()) # estaa ruudun scrollaamisen
        self.view.adjustSize()
        
        self.vertical = QVBoxLayout()
        self.horizontal1 = QHBoxLayout()
        self.horizontal2 = QHBoxLayout()
        
        #lisataan ikkunaan graphicsviewin ylapuolelle kolme painokerroin-slideria
        self.horizontal1.addWidget(sld1)
        self.horizontal1.addWidget(sld2)
        self.horizontal1.addWidget(sld3)
        
        self.vertical.addWidget(QLabel('Boids Simulation'))
        self.vertical.addLayout(self.horizontal1)
        
        self.horizontal2.addWidget(self.view)
        self.vertical.addLayout(self.horizontal2)
        
        self.setLayout(self.vertical)
        
    def setScene(self):
        #lisaa parven yksilot sceneen
        scene = QGraphicsScene()
        for boid in self.boids:
            scene.addItem(boid)
        #scene.setSceneRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        return scene