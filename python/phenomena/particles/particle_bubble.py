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

NO_PARENT = -1
class ParticleBC(object):
    def __init__(self, *args, **kwargs):
        try:
            self._parent = argv[1]
        except:
            self._parent = NO_PARENT

        self.part1 = args[0]
        try:
            self.m1 = pythia.mass(self.part1)
        except:
            self.m1 = self.part1.get('mass')
        self._set_part2()
        self._set_args(kwargs)
        if self.p != None:
            self.E = (self.p ** 2 + self.m1 ** 2) ** (1/2.)
        else:
            self.E = self.m1
        self.collision = ParticleCollision(self._parent,self.part1,self.part2,p=self.p,theta=self.theta)


    def _set_part2(self):
        k = random.random()
        self.isCollision = True
        if self.part1 == 'gamma' and k < 0.5:
            self.part2 = 'e-'
        elif self.part1 == 'gamma':
            self.part2 = 'p+'
        elif self.part1 == 'e-':
            self.part2 = 'e-'
        else:
            self.part2 = None
            self.isCollision = False
        try:
            self.m2 = pythia.mass(self.part2)
        except:
            pass


    def _set_args(self, kwargs):
        self.p = kwargs.get('p',None)
        self.theta = kwargs.get('theta',0)
