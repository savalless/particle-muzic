from __future__ import print_function
import numpy as np
import random

from particletools.tables import PYTHIAParticleData
pythia = PYTHIAParticleData()

from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.particle import ParticleDT
from phenomena.particles.kinematics.collisionBC.collision_channel import CollisionChannel
from phenomena.particles.kinematics.collisionBC.collision_calculations import CollisionCalc
from phenomena.particles.particle_collisionBC import ParticleCollision


class ParticleBC(object):
    def __init__(self, particle, **kwargs):
        self.part1 = particle
        self.m1 = pythia.mass(self.part1)
        self._set_part2()
        self._set_args(**kwargs)
        self.E = (self.p ** 2 + self.m1 ** 2) ** (1/2.)
        self.collision = ParticleCollision(self.part1,self.part2,self.p,self.theta)


    def _set_part2(self):
        k = random.random()
        if k < 0.5:
            self.part2 = 'e-'
        else:
            self.part2 = 'p+'
        self.m2 = pythia.mass(self.part2)


    def _set_args(self, **kwargs):
        self.p = kwargs.get('p',None)
        self.theta = kwargs.get('theta',0)
