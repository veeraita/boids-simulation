'''
Created on Mar 16, 2017

@author: Veera
'''
from boid import *
from weightslider import WeightSlider
from start_slider import Slider
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.Qt import Qt, QGraphicsRectItem

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
        
        self.ws = DEFAULT_S
        self.wa = DEFAULT_A
        self.wc = DEFAULT_C
        
        
    def __layout(self):
        
        self.sld1 = WeightSlider('Separation', DEFAULT_S, RANGE_S)
        self.sld1.slider.valueChanged.connect(lambda: get_ws(self.sld1.slider.value()))
        
        self.sld2 = WeightSlider('Alignment', DEFAULT_A, RANGE_A)
        self.sld2.slider.valueChanged.connect(lambda: get_wa(self.sld2.slider.value()))
        
        self.sld3 = WeightSlider('Cohesion', DEFAULT_C, RANGE_C)
        self.sld3.slider.valueChanged.connect(lambda: get_wc(self.sld3.slider.value()))
        
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
        self.vertical.addLayout(self.horizontal1)
        # Lisataan ikkunaan graphicsviewin alapuolelle kolme painokerroin-slideria
        self.horizontal2.addWidget(self.sld1)
        self.horizontal2.addWidget(self.sld2)
        self.horizontal2.addWidget(self.sld3)
        
        self.vertical.addWidget(QLabel('Adjust parameters'))
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
    
    
        
        