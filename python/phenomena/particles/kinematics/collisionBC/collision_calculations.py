from __future__ import division, print_function
import math
import abc
import collections
import six

from phenomena.particles.particle import ParticleDT
from phenomena.particles.kinematics.collisionBC._2bodycollision import Lab2ColCalc, CM2ColCalc
from phenomena.particles.kinematics.collisionBC._3bodycollision import LAB3BodyColCalc
from phenomena.particles.kinematics.parameters import boostParams


# Fetches de masses of incoming particles in PDG data and manages the calculation for a collision. Only 2-body collision is implemented
class CollisionCalc(object):
    """ Checks number of collision particles and assigns appropriate calculation.
        Creates array of values:
            - masses of incoming particles = [m0, m1, m2,....mn]
            - values of outgoing particle = [{'name':, 'p':, 'theta':},]
    """

    def __init__(self, particles, *args):

#        self._setMassArray(particles)
        self._setInitialMass(particles, *args)

        self._setCalculation(particles, *args)


    def _setInitialMass(self, particles, *args):
        m1 = ParticleDT.getmass(particles[0])
        m2 = ParticleDT.getmass(particles[1])
        p1 = args[0][0]
        p2 = args[0][1]
        E1 = (m1**2 + p1**2)**(1/2.)
        E2 = (m2**2 + p2**2)**(1/2.)
        self._mass = ((E1 + E2)**2 - (p1 + p2)**2)**(1/2.)

    def _setMassArray(self,particles):
        masses = [self._mass]  # array of masses for incoming particles
        for particle in particles:
            if isinstance(particle, collections.Mapping):
                masses.append(particle['mass'])
            elif isinstance(particle, six.string_types):
                masses.append(ParticleDT.getmass(particle))
        self._masses = masses

    def _setCalculation(self, particles, *args):
        if len(particles) == 2 and particles[0] is 'gamma' and args[0][1] == 0:
            if particles[1] == 'e-':
                decay = ['e-', 'e+', 'e-']
                self._setMassArray(decay)
                gamma = boostParams.gamma_from_p(self._masses[0], args[0][0])
                self._values = LAB3BodyColCalc(decay, self._masses, args[1][0], gamma).values

            if particles[1] == 'p+':
                decay = ['e-', 'e+', 'p+']
                self._setMassArray(decay)
                gamma = boostParams.gamma_from_p(self._masses[0], args[0][0])
                self._values = LAB3BodyColCalc(decay, self._masses, args[1][0], gamma).values

        else:
            print('We only accept gammas')



#            if len(args) == 2:
#                self._values = Lab2ColCalc(particles,args[0],args[1],masses).values
#            else:
#                self._values = CM2ColCalc(particles,args[0],masses).values


    @property
    def values(self):
        return self._values
