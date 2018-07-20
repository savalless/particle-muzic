import numpy as np
import math

from skhep.math.vectors import Vector3D
from skhep.constants import c_light as c
from phenomena.particles.dynamics.fields import field


class TotalAcc(object):
    def __init__(self, velocity, dist, energy, charge, mass, name):
        self.acc = (Bforce(velocity, charge).F + Eforce(charge).F - DragForce(velocity).F - Bremstrahlung(velocity, dist, energy, name).F) / mass


class Bforce(object):
    def __init__(self, velocity, charge):
        self.vel = velocity
        self.charge = charge
        self._set_B_force()

    def _set_B_force(self):
        self.F = self.charge * self.vel.cross(field().B)


class Eforce(object):
    def __init__(self, charge):
        self.charge = charge
        self._set_E_force()

    def _set_E_force(self):
        self.F = self.charge * field().E

class DragForce(object):
    def __init__(self, velocity):
        self.vel = velocity
        self._set_DragForce()

    def _set_DragForce(self):
        #assert self.vel.mag <= c
        self.F = self.vel.unit() * 100



class Bremstrahlung(object):
    def __init__(self, velocity, dist, energy, name):
        self.d = dist
        self.vel = velocity
        self.energy = energy
        self.name = name
        self._set_Bremstrahlung()

    def _set_Bremstrahlung(self):
        if self.name is 'e+' or self.name is 'e-':
            k = 20000000.
            self.F = self.energy * math.exp(-self.d / k) / k * self.vel.unit()
        else:
            self.F = 0 * self.vel.unit()
