from __future__ import division, print_function
import math
import abc
import collections
import six

from phenomena.particles.particle import ParticleDT
from phenomena.particles.kinematics.collision._2bodycollision import Col2BodyCalc

# Fetches de masses of incoming particles in PDG data and manages the calculation for a collision. Only 2-body collision is implemented
class CollisionCalc(object):
    """ Checks number of collision particles and assigns appropriate calculation.
        Creates array of values:
            - masses of incoming particles = [m0, m1, m2,....mn]
            - values of outgoing particle = [{'name':, 'p':, 'theta':},]
    """

    def __init__(self, particles, momenta, angles):
        self._decay = virtual # For processing it later on, we consider the virtual product to be a decay
        self._momenta = momenta
        self._setMassArray(particles)
        self._angles = angles

        self._setCalculation(particles, virtual, self._momenta, self._angles, self._masses)

    def _setMassArray(self,particles):
        masses = []  # array of masses for incoming particles
        for particle in particles:
            if isinstance(particle, collections.Mapping):
                masses.append(particle['mass'])
            elif isinstance(particle, six.string_types):
                masses.append(ParticleDT.getmass(particle))

        self._masses = masses

    def _setCalculation(self, particles, momenta, angles, masses):
        if len(particles) == 2:
            self._values = Col2BodyCalc(particles,virtual,momenta,angles,masses).values
        else:
            print('3 body collisions have not been implemented')

    @property
    def values(self):
        return self._values
