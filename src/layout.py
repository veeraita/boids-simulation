'''
Created on Mar 16, 2017

@author: Veera
'''
from boid import Boid, SCENE_WIDTH, SCENE_HEIGHT, BOID_RADIUS
from weightslider import WeightSlider
from start_slider import Slider
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.Qt import Qt, QGraphicsRectItem
import random

class SimulationLayout(QWidget):

    def __init__(self, boids_number):
        
        super(SimulationLayout, self).__init__()
        self.init_slider = Slider()
        self.boids_number = boids_number
        self.boids = []
        # Lisataan haluttu maara boid-yksiloita listaan
        for i in range(self.boids_number):
            self.boids.append(Boid())
        self.__layout()
        
        
    def __layout(self):
        
        self.sld1 = WeightSlider('Separation')
        self.sld2 = WeightSlider('Alignment')
        self.sld3 = WeightSlider('Cohesion')
        
        self.startbtn = QPushButton("Start")
        
        scene = self.setScene()
        self.view = QGraphicsView(scene)
        self.view.adjustSize()
        # Estetaan scroll barit
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.vertical = QVBoxLayout()
        self.horizontal1 = QHBoxLayout()
        self.horizontal2 = QHBoxLayout()
        
        self.horizontal1.addWidget(self.view)
        self.horizontal1.addWidget(self.startbtn)
        self.vertical.addLayout(self.horizontal1)
        # Lisataan ikkunaan graphicsviewin alapuolelle kolme painokerroin-slideria
        self.horizontal2.addWidget(self.sld1)
        self.horizontal2.addWidget(self.sld2)
        self.horizontal2.addWidget(self.sld3)
        
        self.vertical.addWidget(QLabel('Muokkaa painokertoimia'))
        self.vertical.addLayout(self.horizontal2)
        
        self.setLayout(self.vertical)
        
    def setScene(self):
        #lisaa parven yksilot sceneen
        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, SCENE_WIDTH, SCENE_HEIGHT)
        scene.addItem(QGraphicsRectItem(0, 0, SCENE_WIDTH, SCENE_HEIGHT))
        for boid in self.boids:
            scene.addItem(boid)
            boid.setGraphics()
            boid.updatePosVector()

        return scene