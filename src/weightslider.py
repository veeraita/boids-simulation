'''
Created on Mar 16, 2017

@author: Veera
'''
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class WeightSlider(QWidget):
    '''
    Sliderit, joilla muokataan parven liikkumissaantojen painokertoimia
    '''

    def __init__(self, title, default, val_range):
        
        super(WeightSlider, self).__init__()
        
        self.title = title
        self.default = default
        self.range = val_range
        self.initUI()
        
    def initUI(self):
        
        slider_title = QLabel(self.title)
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(self.default - self.range, self.default + self.range)
        self.slider.setValue(self.default)
        
        layout = QVBoxLayout()
        layout.addWidget(slider_title)
        layout.addWidget(self.slider)
        
        self.setLayout(layout)
        