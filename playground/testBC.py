from __future__ import print_function
import sys
import unittest
import numpy as np

python_path = 'C:\Users\Santi\Documents\GitHub\particle-muzic\python'
sys.path.append(python_path)

from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.particle_bubble import ParticleBC

#Santi was here

class MyTest(unittest.TestCase):
    def test(self):
#        part = ParticleBC({'name':'W+', 'mass':500, 'decay':['mu+', 'nu_mubar']}, p=1)
        while True:
            part = ParticleBC('eta', p=10)
            if 'pi-' in part.collision._decay:
                break
        if part.isCollision:
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
            self.assertEqual(round(sum(px[:2]), 5), round(sum(px[2:]), 5))
            self.assertEqual(round(sum(py[:2]), 5), round(sum(py[2:]), 5))
            self.assertEqual(round(sum(En[:2]), 5), round(sum(En[2:]), 5))

        else:
            p = [part.p]
            theta = [part.theta]
            En = [part.E]
            print(part.collision.decayvalues)
            for particle in part.collision.decayvalues:
                p.append(particle['p'])
                theta.append(particle['theta'])
                En.append(particle['E'])
            px = p * np.cos(theta)
            py = p * np.sin(theta)
            self.assertEqual(round(sum(px[1:]), 5), round(px[0], 5))
            self.assertEqual(round(sum(py[1:]), 5), round(py[0], 5))
            self.assertEqual(round(sum(En[1:]), 5), round(En[0], 5))





unittest.main()
