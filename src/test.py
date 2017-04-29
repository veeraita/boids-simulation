'''
Created on Apr 12, 2017

@author: Veera
'''
import unittest
import sys
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication
from run_simulation import BoidsSimulation
from boid import *


class Test(unittest.TestCase):
    
    app = QApplication(sys.argv)
    
    def setUp(self):
        self.sim = BoidsSimulation(10)
    
    def test_adding_items(self):
        self.assertEqual(len(self.sim.form.view.items()), 11, "QGraphicsViewin scenen tulisi sis‰lt‰‰ 11 itemi‰: 10 lintua sek‰ rajoittava suorakulmio.")
           
    def test_defaults(self):
        self.assertEqual(self.sim.form.sld1.slider.value(), DEFAULT_S)
        
        self.assertEqual(self.sim.form.sld2.slider.value(), DEFAULT_A)
        
        self.assertEqual(self.sim.form.sld3.slider.value(), DEFAULT_C)
    
    def test_weightsliders(self):
        self.sim.form.sld1.slider.setValue(0)
        self.assertEqual(self.sim.form.sld1.slider.value(), DEFAULT_S - RANGE_S, "Sld1:n arvo ei saa olla pienempi kuin minimi.")
        
        self.sim.form.sld2.slider.setValue(0)
        self.assertEqual(self.sim.form.sld2.slider.value(), DEFAULT_A - RANGE_A, "Sld2:n arvo ei saa olla pienempi kuin minimi.")
        
        self.sim.form.sld3.slider.setValue(0)
        self.assertEqual(self.sim.form.sld3.slider.value(), DEFAULT_C - RANGE_C, "Sld3:n arvo ei saa olla pienempi kuin minimi.")


if __name__ == "__main__":
    unittest.main()