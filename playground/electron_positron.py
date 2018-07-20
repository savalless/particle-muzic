from __future__ import print_function
import sys
import unittest
import numpy as np

python_path = 'C:\Users\Sergi\Desktop\IFAE\particle-muzic\python'
sys.path.append(python_path)

from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.particle import ParticleDT
from phenomena.particles.kinematics.collision.collision_channel import CollisionChannel
from phenomena.particles.kinematics.collision.collision_calculations import CollisionCalc
from phenomena.particles.particle import ParticleDT

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
        self._particles = [part1,part2]
        self._channel = channels._channel
        self._momenta = [1,1]
        self._angles = [0,np.pi]
        self._masses = [ParticleDT.getmass(particle) for particle in self._particles]

        self._values = CollisionCalc(self._particles,self._channel,self._momenta,self._angles).values

        # collision = ParticleCollision(Energy,ImpactPar,part1,part2)

        # print(collision.virtual['name'])
        # print(collision.virtual['p'])
        # print(collision.virtual['E'])

        px = [self._values['p'] * np.cos(self._values['theta'])]
        py = [self._values['p'] * np.sin(self._values['theta'])]
        En = [self._values['E']]
        for index in range(len(self._particles)):
            px.append(self._momenta[index]*np.cos(self._angles[index]))
            py.append(self._momenta[index]*np.sin(self._angles[index]))
            En.append((self._momenta[index]**2+self._masses[index]**2)**(1/2))


        self.assertEqual(round(sum(px[1:]), 5), round(px[0], 5))
        self.assertEqual(round(sum(py[1:]), 5), round(py[0], 5))
        self.assertEqual(round(sum(En[1:]), 5), round(En[0], 5))

unittest.main()
