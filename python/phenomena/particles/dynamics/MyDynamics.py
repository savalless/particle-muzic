from skhep.math.vectors import Vector3D
from skhep.constants import c_light as c
from phenomena.particles.dynamics.forces import *
from phenomena.particles.dynamics.Runge_Kutta import RK4
from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.kinematics.parameters import boostParams
import numpy as np
import matplotlib.pyplot as plt


class Dynamics(object):
    def __init__(self, pos, particle):
        assert type(particle) is ParticleBoosted
        self.init_pos = pos
        self.init_theta = particle._theta
        self.init_vel = particle._beta * Vector3D(np.cos(self.init_theta), np.sin(self.init_theta), 0) * c
        self.init_E = particle._E
        self.init_p = particle._p
        self.decay_time = particle.decay_time
        assert self.init_E == boostParams.E_from_p(self.init_vel.mag / c, self.init_p)
        self.charge = particle.charge
        self.mass = particle.mass
        self.name = particle.name

        self._set_array_pos()
        self.print_pos()

    def _set_array_pos(self):
        self.array_pos = np.array([[self.init_pos.x, self.init_pos.y, self.init_pos.z]])
        pos = self.init_pos.copy()
        vel = self.init_vel.copy()
        d = 0
        tmax = 1
        t = 0
        h = 0.001
        while t <= tmax:
            if t >= self.decay_time: break
            pos1 = pos.copy()
            vel1 = vel.copy()
            RK = RK4(pos, vel, d, self.init_E, h, self.charge, self.mass, self.name)
            pos = RK.pos
            vel = RK.vel
            d += abs(pos.mag - pos1.mag)
            assert vel1.mag >= vel.mag
            self.array_pos = np.append(self.array_pos, [pos], axis = 0)
            t += h

    def print_pos(self):
        fig, a = plt.subplots()
        a.plot(self.array_pos[ : , 0], self.array_pos[ : , 1])
        plt.show()
