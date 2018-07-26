from __future__ import division
import math, random
import collections
import six
from skhep.math.vectors import Vector3D

from particle import Particle, ParticleDT, toDictionary

from phenomena.particles.kinematics.decay.calculations import DecayCalc
from phenomena.particles.kinematics.parameters import boostParams
from phenomena.particles.particle_virtual import VirtualChannel

# Sergi was here

NO_PARENT = -1
class ParticleBoosted(ParticleDT):
    c= 299792458 #m/s

    def __init__(self, *argv, **kwargs): #initialize either with momentum (p) or energy (E)

        try:
            self._parent = argv[1]
        except:
            self._parent = NO_PARENT

        if isinstance(argv[0], collections.Mapping):
            self._virtual_init(*argv, **kwargs)
        elif isinstance(argv[0], six.string_types):
            self._real_init(*argv, **kwargs)
        else:
            return None


    # Scenario for handling virtual particles
    def _virtual_init(self, *argv, **kwargs):
        name = argv[0].get('name')
        mass = argv[0].get('mass')

        self._set_name(name)  # Name of the particle pypdt convention
        self._set_id() # Class Counter
        self._set_pdgid(name) # Id from PDG, taken from pypdt
        self._mass = mass # Mass of the particle in GeV
        self._set_charge() # Charge of the particle taken from pypdt
        self._set_lifetime() # Lifetime of the particle, taken from pypdt
        # Virtual particles have lifetimes that are too short, so we make them large. This can be changed to a more realistic approach
        self._lifetime *= 5.e9 #!!CHECK!!#

        try:  # Particle decay channel chosen
            self._decay = argv[0].get('decay')
        except:
            self._set_decay_channels()
            self._deactivate_decay_channels() # for virtual particles, not all channels are allowed
            self._renorm_decay_channels() # remaining channels must have the probability renormalized
            self._set_decay()

        self._set_type() # Particle Type will always be virtual
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...] taken from json.
        self._set_lifetime_ren() #Renormalization of the lifetime THIS SHOULD BE DONE AT THE NODES and brought back with callback
        self._set_time_to_decay()  # Particle time lived before decay, renormalized

        self._setVirtualBoostedParameters(kwargs)
        # increase lifetime by gamma factor
        self._lifetime *= self._gamma

    # Scenario for handling regular particles
    def _real_init(self, *argv, **kwargs):
        name = argv[0]
        super(ParticleBoosted, self).__init__(name,self._parent)#inherit properties from ParticleDT
        self._theta = kwargs.get('theta',0) #the angle of this instance

        masses = []  # array of masses 0: parent particle, 1: first decay particle, ...
        for particle in self._decay:
            masses.append(ParticleDT.getmass(particle))

        self._masses = masses

        #decide if we want the decay to happen through a virtual channel
        if len(self._decay) == 3:
            self._decay = VirtualChannel(self._decay,self.mass, self._masses, self.name)._decay
        #the decay particles and masses have been reset inside ParticleVirtual if necessary
        #calculate and assign boosted parameters
        self._params = boostParams(self._name,p=kwargs.get('p',None),E=kwargs.get('E',None)) # sets boosted parameters for this instance
        self._pos = Vector3D(kwargs.get('x',0), kwargs.get('y',0), kwargs.get('z',0))
        self._p = self._params.p
        self._E = self._params.E
        self._gamma = self._params.gamma
        self._beta = self._params.beta
        self._T = self._params.T

        self.decayvalues = DecayCalc(self._mass,self._gamma,self._theta,self._decay).values # sets values for decay particles

        # increase lifetime by gamma factor
        self._lifetime *= self._gamma

    def _setVirtualBoostedParameters(self,kwargs): # Regular boosted parameters fetches de mass from pdg. For virtual particles it's the wrong mass
        self._p = kwargs.get('p',None)
        self._pos = Vector3D(kwargs.get('x',0), kwargs.get('y',0), kwargs.get('z',0))
        self._gamma = boostParams.gamma_from_p(self.mass,self._p)
        self._beta =  boostParams.beta_from_gamma(self._gamma)
        self._E = boostParams.E_from_p(self._beta,self._p)
        self._T = boostParams.T_from_gamma(self.mass,self._gamma)

        self._theta = kwargs.get('theta',0)
        self.decayvalues = DecayCalc(self._mass,self._gamma,self._theta,self._decay).values # sets values for decay particles

    def _deactivate_decay_channels(self):
        new_decay_channels = []
        for part in self._decay_channels:
            masses = [pythia.mass(self._decay_channels[part][1][x]) for x in self._decay_channels[part][1]]
            if sum(masses) <= self._mass:
                new_decay_channels.append(self._decay_channels[part])

        self._decay_channels = new_decay_channels

    def _renorm_decay_channels(self):
        total = 0
        for particle in self._decay_channels:
            total += sum(particle[0])
        for index in range(len(self._decay_channels)):
            self._decay_channels[index][0]*=(1/total)


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
