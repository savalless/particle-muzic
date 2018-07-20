from skhep.math.vectors import Vector3D
from skhep.constants import c_light as c
from phenomena.particles.dynamics.forces import *
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
        assert self.init_E == boostParams.E_from_p(self.init_vel.mag / c, self.init_p)
        self.charge = particle.charge
        self.mass = particle.mass

        self._set_k()
        self._set_array_pos()
        self.print_pos()

    def _set_k(self):
        B = field().B.mag
        self.k = self.charge * B / self.mass

    def _set_drag(self, v):
        return DragForce(v).F

    def _set_array_pos(self):
        C = self._set_drag(self.init_vel)
        self.array_pos = np.array([[self.init_pos.x, self.init_pos.y, self.init_pos.z]])
        pos = self.init_pos.copy()
        vel = self.init_vel.copy()
        tmax = 1
        t = 0
        while t <= tmax:
            x = (self.init_vel.x / self.k + C.y / self.k ** 2) * np.sin(self.k * t) - (self.init_vel.y / self.k - C.x / self.k ** 2) * np.cos(self.k * t) - C.y / self.k * t + self.init_pos.x - C.x / self.k ** 2 + self.init_vel.y / self.k
            y = (self.init_vel.y / self.k - C.x / self.k ** 2) * np.sin(self.k * t) + (self.init_vel.x / self.k + C.y / self.k ** 2) * np.cos(self.k * t) + C.x / self.k * t + self.init_pos.y - C.y / self.k ** 2 - self.init_vel.x / self.k
            vx = (self.init_vel.x + C.y / self.k) * np.cos(self.k * t) + (self.init_vel.y - C.x / self.k) * np.sin(self.k * t) - C.y / self.k
            vy = (self.init_vel.y - C.x / self.k) * np.cos(self.k * t) - (self.init_vel.x + C.y / self.k) * np.sin(self.k * t) + C.x / self.k

            vel1 = vel.copy()
            vel = Vector3D(vx, vy, 0)
            pos = np.array([x, y, 0])
            C = self._set_drag(vel)
            assert vel1.mag >= vel.mag


            print(vel, C, t)

            self.array_pos = np.append(self.array_pos, [pos], axis = 0)
            t += 0.001

    def print_pos(self):

        fig, a = plt.subplots()
        a.plot(self.array_pos[ : , 0], self.array_pos[ : , 1])
        plt.show()
