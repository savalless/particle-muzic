from skhep.math.vectors import Vector3D
from skhep.constants import c_light as c
from phenomena.particles.dynamics.forces import *
from phenomena.particles.dynamics.Runge_Kutta import RK4
from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.kinematics.parameters import boostParams
import numpy as np
import matplotlib.pyplot as plt


class Dynamics(object):
    def __init__(self, pos, vel, particle, d, h):
        assert type(particle) is ParticleBoosted
        assert type(pos) is Vector3D
        assert type(vel) is Vector3D
        self.delta_t = h
        self.d = d
        self.init_theta = particle._theta
        self.init_E = particle._E
        self.init_p = particle._p
        self.decay_time = particle.decay_time
        self.charge = particle.charge
        self.mass = particle.mass
        self.name = particle.name

        self._set_pos(pos, vel)

    def _set_pos(self, pos, vel):
        RK = RK4(pos, vel, self.d, self.init_E, self.delta_t, self.charge, self.mass, self.name)
        self.pos = RK.pos
        self.vel = RK.vel
        assert vel.mag >= self.vel.mag
