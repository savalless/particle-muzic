from __future__ import print_function
import sys
import unittest
import numpy as np
from skhep.math.vectors import Vector3D

python_path = 'C:\Users\Santi\Documents\GitHub\particle-muzic\python'
sys.path.append(python_path)
from phenomena.particles.dynamics.MyDynamics import Dynamics
from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.time_master import *

class MyTest(unittest.TestCase):
    def test(self):
        vel = Vector3D(0, 5., 0)
        pos = Vector3D(3., 0, 0)
        sol = BubbleChamber([ParticleBoosted('mu+', p=1, x=5, y=8, z=0), ParticleBoosted('mu-', p=1, x=6, y=3, z=0)])



#        acc = Vector3D(0, 3., 0)

#        self.assertEqual(Bforce(vel).F.mag * 1e19 , 5. * 1.6e-19 * 500. * 1e19)
#        self.assertEqual(DragForce(vel).F, -1 * Vector3D(0, 1 / 5. ** 2, 0))
#        self.assertEqual(RadiativeForce(vel,acc,-1,), )

unittest.main()
