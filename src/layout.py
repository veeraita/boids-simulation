'''
Created on Mar 16, 2017

@author: Veera
'''
from boid import Boid
from weightslider import WeightSlider
from start_slider import Slider
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QHBoxLayout, QVBoxLayout, QLabel

class SimulationLayout(QWidget):

    def __init__(self, boids_number):
        
        super(SimulationLayout, self).__init__()
        self.init_slider = Slider()
        self.boids_number = boids_number
        self.boids = []
        for i in range(self.boids_number):
            self.boids.append(Boid())
        self.__layout()
        
    def __layout(self):
        
        sld1 = WeightSlider('Separation')
        sld2 = WeightSlider('Alignment')
        sld3 = WeightSlider('Cohesion')
        
        self.view = QGraphicsView(self.setScene())
        
        self.vertical = QVBoxLayout()
        self.horizontal1 = QHBoxLayout()
        self.horizontal2 = QHBoxLayout()
        
        self.horizontal1.addWidget(sld1)
        self.horizontal1.addWidget(sld2)
        self.horizontal1.addWidget(sld3)
        
        self.vertical.addWidget(QLabel('Boids Simulation'))
        self.vertical.addLayout(self.horizontal1)
        
        self.horizontal2.addWidget(self.view)
        self.vertical.addLayout(self.horizontal2)
        
        self.setLayout(self.vertical)
        
    def setScene(self):
        
        scene = QGraphicsScene()
        for boid in self.boids:
            scene.addItem(boid)
        
        return scene