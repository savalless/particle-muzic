from __future__ import print_function
import sys
import unittest
import numpy as np

python_path = 'C:\Users\Santi\Documents\GitHub\particle-muzic\python'
sys.path.append(python_path)

from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.ParticleBC import ParticleBC

#Santi was here

class MyTest(unittest.TestCase):
    def test(self):
#        part = ParticleBoosted({'name':'W+', 'mass':500, 'decay':['mu+', 'nu_mubar']}, p=1)
        part = ParticleBC('gamma', p=10)
        p = [part.p, 0]
        theta = [part.theta, 0]
        En = [part.E, part.m2]
        print(part.collision.decayvalues)
        for particle in part.collision.decayvalues:
            p.append(particle['p'])
            theta.append(particle['theta'])
            En.append(particle['E'])



        px = p * np.cos(theta)
        py = p * np.sin(theta)

#        print(p)
#        print(theta)
#        print(px)
#        print(py)
#        print(E)
#        print('\n')
#        print(round(px[0], 5) - round(sum(px[1:]), 5))
#        print(round(py[0], 5) - round(sum(py[1:]), 5))


        self.assertEqual(round(sum(px[:2]), 5), round(sum(px[2:]), 5))
        self.assertEqual(round(sum(py[:2]), 5), round(sum(py[2:]), 5))
        self.assertEqual(round(sum(En[:2]), 5), round(sum(En[2:]), 5))

unittest.main()
