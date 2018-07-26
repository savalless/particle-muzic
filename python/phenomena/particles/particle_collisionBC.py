from __future__ import division
import math, random
import collections

from particle import Particle, ParticleDT, toDictionary
from particletools.tables import PYTHIAParticleData
pythia = PYTHIAParticleData()

from phenomena.particles.kinematics.collisionBC.collision_calculations import CollisionCalc
from phenomena.particles.kinematics.collisionBC.collision_channel import CollisionChannel
from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.kinematics.parameters import boostParams

# Check that all imports are necessary

# Given two particles and the momentum of at least the first, makes all necessary calculations to create the first particle with a 'decay'
# that represents the product of its collision to particle 2 (without representing the second one). Lifetime is set artificially low for
# stable particles to be able to collide as well.

# !!!! Lifetime can ve changed to a probability dependent parameter (preferably calculated through a different class method in a different
# file that considers how unlikely it is to collide with particle 2 (and thus how long it will take) !!!! (Perfect for Santi)

NO_PARENT = -1
class ParticleCollision(ParticleBoosted):
    c= 299792458 #m/s

    def __init__(self,part1,part2, *args, **kwargs):

        # Momenta and angles are initialized inside this argument check. Also raises specific error codes if arguments don't match
        self._check_args(*args,**kwargs)

        self._inc_particles = [part1,part2]
        self._set_name(part1)
        self._set_id() # Class Counter
        self._set_pdgid(part1) # Id from PDG, taken from pypdt
        self._set_mass() # Mass of the virtual particle in GeV taken from the arguments
        self._set_charge() # Charge of the particle, taken from pypdt
        # We set the lifetime as is in PDG but we'll modify the time left for decay (so it collides even if it has infinite lifetime)
        self._set_lifetime()
        # Collision Channel is chosen after calculations for the mass.
        self._decay = [{}] # it's a list so it fits the particle_boosted format
        self._set_type() # Particle Type (quark, lepton, bosoon, meson, baryon) taken from json
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...] taken from json.
        self._set_lifetime_ren() #Renormalization of the lifetime THIS SHOULD BE DONE AT THE NODES and brought back with callback
        self._set_time_to_decay()  # Particle time lived before decay, renormalized
        self._collision_decay()
        self._setParent(NO_PARENT)

        if self._CMenergy == None:
            self.decayvalues = CollisionCalc(self._inc_particles,self._momenta,self._angles).values
            self._setBoostedParameters({'p':self._momenta[0],'theta':self._angles[0]})
        else:
            self.decayvalues = CollisionCalc(self._inc_particles,self._CMenergy).values
            self._E = self.decayvalues['E1'] # In this case we make an extra calculation for the incoming particle energy
            self._setBoostedParameters({'E':self._E})
        # CollisionChannel without an impact parameter should never be used here, as it leaves the choice of channel open. It will be useful
        # when checking whether there is a collision through classes other than particle_collision
#        self._decay[0]['name'] = CollisionChannel(part1,part2,self._decay[0]['mass'],self._impact).channel
        # Also, at this point we could check if part2 is a list, and in that case make a weighted choice for which particle it will collide
        # with before choosing the channel

        self._lifetime *= self._gamma

    def _check_args(self,*args,**kwargs):
        self._CMenergy = kwargs.get('E',None)
        self._impact = kwargs.get('impact',0)
        if self._CMenergy == None:
            try:
                p1 = args[0]
                theta1 = args[1]
                try:
                    p2 = args[2]
                    theta2 = args[3]
                except:
                    p2 = 0
                    theta2 = 0
                self._momenta = [p1,p2]
                self._angles = [theta1, theta2]
            except:
                print('If no energy ("'"E"'"= X GeV) is provided, at least one particle must have momentum')
        else:
            print('Momentum will be calculated with given energy in a centre of mass scenario')


    def _collision_decay(self): # We want the collision to happen even if its lifetime is infinite
        if self._time_to_decay == ParticleDT.STABLE:
            self._time_to_decay = 0.6

    def _setBoostedParameters(self,kwargs):
        self._params = boostParams(self._name,p=kwargs.get('p',None),E=kwargs.get('E',None)) # sets boosted parameters for this instance
        self._p = self._params.p
        self._E = self._params.E
        self._gamma = self._params.gamma
        self._beta = self._params.beta
        self._T = self._params.T
        self._theta = kwargs.get('theta',0)

    @property
    def p(self):
        return self._p

    @property
    def E(self):
        return self._E

    @property
    def gamma(self):
        return self._gamma

    @property
    def beta(self):
        return self._beta

    @property
    def theta(self):
        return self._theta

    @property
    def T(self):
        return self._T

    def toDictionary(self):
        return toDictionary(self)
