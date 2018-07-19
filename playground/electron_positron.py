from __future__ import print_function
import sys
import unittest
import numpy as np

python_path = 'C:\Users\Sergi\Desktop\IFAE\particle-muzic\python'
sys.path.append(python_path)

from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.particle import ParticleDT
from phenomena.particles.kinematics.collision.collision_channel import CollisionChannel

class MyTest(unittest.TestCase):
    def test(self):
        part1 = 'e-'
        part2 = 'e+'
        energy = 1.02 # Square root of s in GeV
        impact = 1.e-6 # In mb

        channels = CollisionChannel(part1,part2,energy,impact)
        for particle in range(len(channels._cross_section)):
            print(channels._virtual_list[particle],'\t',channels._cross_section[particle])
        print(channels._channel)

        # collision = ParticleCollision(Energy,ImpactPar,part1,part2)

        # print(collision.virtual['name'])
        # print(collision.virtual['p'])
        # print(collision.virtual['E'])

        # p = [0]
        # theta = [0]
        # En = [collision.E]
        # for particle in collision.decayvalues:
        #     p.append(particle['p'])
        #     theta.append(particle['theta'])
        #     En.append(particle['E'])
        #
        # px = p * np.cos(theta)
        # py = p * np.sin(theta)
        #
        # self.assertEqual(round(sum(px[1:]), 5), round(px[0], 5))
        # self.assertEqual(round(sum(py[1:]), 5), round(py[0], 5))
        # self.assertEqual(round(sum(En[1:]), 5), round(En[0], 5))

unittest.main()
