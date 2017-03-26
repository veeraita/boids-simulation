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

    def __init__(self, title):
        
        super(WeightSlider, self).__init__()
        
        self.title = title
        self.initUI()
        
    def initUI(self):
        
        slider_title = QLabel(self.title)
        slider = QSlider(Qt.Horizontal, self)
        slider.setMaximum(10)
        slider.setValue(5)
        
        layout = QVBoxLayout()
        layout.addWidget(slider_title)
        layout.addWidget(slider)
        
        self.setLayout(layout)
        