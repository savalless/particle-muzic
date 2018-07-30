from __future__ import print_function
import sys
import unittest
import numpy as np

python_path = 'C:\Users\Santi\Documents\GitHub\particle-muzic\python'
sys.path.append(python_path)

from particletools.tables import PYTHIAParticleData
pythia = PYTHIAParticleData()

from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.particle_collision import ParticleCollision
from phenomena.particles.particle import ParticleDT
from phenomena.particles.kinematics.collisionBC.collision_channel import CollisionChannel
from phenomena.particles.kinematics.collisionBC.collision_calculations import CollisionCalc

# Test for different parts of the electron positron collision implementation
class MyTest(unittest.TestCase):
    def test(self):
        part1 = 'gamma'
        part2 = 'p+'
        energy = 3.097 # Square root of s in GeV
#        impact = 1.e-6 # In mb

        part2_mass = pythia.mass(part2)
        part1_mass = pythia.mass(part1)

        # Giving momentum
        self._momenta = [10,0]
        self._angles = [0,0]
        if self._momenta[1] == 0:
            values = ParticleCollision(part1,part2,self._momenta[0],self._angles[0])
        else:
            values = ParticleCollision(part1,part2,self._momenta[0],self._angles[0],self._momenta[1],self._angles[1])
        print(values.decayvalues)
        p = self._momenta
        theta = self._angles
        En = [values.E, (self._momenta[1]**2 + part2_mass**2)**(1/2.)]

        # Giving system energy
#        values = ParticleCollision(part1,part2,E=energy)
#        p = [values.p,values.p]
#        theta = [values.theta,values.theta+np.pi]
#        En = [values.E,values.E]

        # This part is the same for both options
        for i in range(len(values.decayvalues)):
            p.append(values.decayvalues[i]['p'])
            theta.append(values.decayvalues[i]['theta'])
            En.append(values.decayvalues[i]['E'])


        px = p * np.cos(theta)
        py = p * np.sin(theta)


        self.assertEqual(round(sum(px[:2]), 5), round(sum(px[2:]), 5))
        self.assertEqual(round(sum(py[:2]), 5), round(sum(py[2:]), 5))
        self.assertEqual(round(sum(En[:2]), 5), round(sum(En[2:]), 5))

        # # Gets the decay channel
        # channels = CollisionChannel(part1,part2,energy,impact)
        # for particle in range(len(channels._cross_section)):
        #     print(channels._virtual_list[particle],'\t',channels._cross_section[particle])
        # print(channels._channel)
        # self._particles = [part1,part2]
        # self._channel = channels._channel
        # self._momenta = [1,1]
        # self._angles = [0,np.pi]
        # self._masses = [ParticleDT.getmass(particle) for particle in self._particles]
        #
        # # Calculates the outgoing particle momentum and energy
        # self._values = CollisionCalc(self._particles,self._channel,self._momenta,self._angles).values

        # collision = ParticleCollision(Energy,ImpactPar,part1,part2)

        # print(collision.virtual['name'])
        # print(collision.virtual['p'])
        # print(collision.virtual['E'])

        # Check energy and momenta conservation
        # px = [self._values['p'] * np.cos(self._values['theta'])]
        # py = [self._values['p'] * np.sin(self._values['theta'])]
        # En = [self._values['E']]
        # for index in range(len(self._particles)):
        #     px.append(self._momenta[index]*np.cos(self._angles[index]))
        #     py.append(self._momenta[index]*np.sin(self._angles[index]))
        #     En.append((self._momenta[index]**2+self._masses[index]**2)**(1/2))

        #
        # self.assertEqual(round(sum(px[1:]), 5), round(px[0], 5))
        # self.assertEqual(round(sum(py[1:]), 5), round(py[0], 5))
        # self.assertEqual(round(sum(En[1:]), 5), round(En[0], 5))

unittest.main()
