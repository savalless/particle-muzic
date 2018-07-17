from __future__ import print_function
import sys
import unittest
import numpy as np

python_path = 'C:\Users\Sergi\Desktop\IFAE\particle-muzic\python'
sys.path.append(python_path)

from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.particle import ParticleDT
from phenomena.particles.particle_collision import ParticleCollision

class MyTest(unittest.TestCase):
    def test(self):
        part1 = 'e-'
        part2 = 'e+'
        Energy = 1 # In GeV
        ImpactPar = 0.1 # In mb
        collision = ParticleCollision(Energy,ImpactPar,part1,part2)

        # print(collision.virtual['name'])
        # print(collision.virtual['p'])
        # print(collision.virtual['E'])

        p = [0]
        theta = [0]
        En = [collision.E]
        for particle in collision.decayvalues:
            p.append(particle['p'])
            theta.append(particle['theta'])
            En.append(particle['E'])

        px = p * np.cos(theta)
        py = p * np.sin(theta)

        self.assertEqual(round(sum(px[1:]), 5), round(px[0], 5))
        self.assertEqual(round(sum(py[1:]), 5), round(py[0], 5))
        self.assertEqual(round(sum(En[1:]), 5), round(En[0], 5))

unittest.main()
