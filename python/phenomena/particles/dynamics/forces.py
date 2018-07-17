import math

from skhep.math.vectors import Vector3D
from skhep.constants import c_light as c
from phenomena.particles.dynamics.fields import field

class Bforce(object):
    def __init__(self, velocity):
        self.vel = velocity
        self._set_B_force()

    def _set_B_force(self):
        self.F = 1.6e-19 * self.vel.cross(field().B)


class Eforce(object):
    def __init__(self):
        self._set_E_force()

    def _set_E_force(self):
        self.F = 1.6e-19 * self.vel.cross(field().E)

class DragForce(object):
    def __init__(self, velocity):
        self.vel = velocity
        self._set_DragForce()

    def _set_DragForce(self):
        assert self.vel.mag <= c
        if self.vel.mag >= 0.9 * c:
            mod = 0.27
        else:
            mod = 1. / self.vel.mag2
        self.F = -1 * self.vel.unit() * mod


class RadiativeForce(object):
    def __init__(self, velocity, acceleration, charge):
        self.vel4 = LorentzVector(velocity, c)
        self.betad = acceleration.mag / c
        self.gamma = self.vel4.gamma

    def _set_RadiativeForce(self):
        P = self.charge ** 2 * self.gamma ** 4 * self.betad ** 2 / (6 * math.pi * 8.85e-12 * c)
