from __future__ import division
import math, random
import collections

from particle import Particle, ParticleDT, toDictionary
from particletools.tables import PYTHIAParticleData as pythia

from phenomena.particles.kinematics.decay.calculations import DecayCalc
from phenomena.particles.kinematics.parameters import boostParams
from phenomena.particles.kinematics.collision.collision_channel import CollisionChannel
from phenomena.particles.particle_boosted import ParticleBoosted

# Check that all imports are necessary

NO_PARENT = -1
class ParticleCollision(ParticleBoosted):
    c= 299792458 #m/s

    def __init__(p1,p2,energy,impact):

        VirtualChannel = CollisionChannel(p1,p2,energy,impact)
        self._set_name(VirtualChannel._name)
        self._set_id() # Class Counter
        self._set_pdgid(VirtualChannel._name) # Id from PDG, taken from pypdt
        self._mass = energy # Mass of the virtual particle in GeV taken from the arguments
        self._set_charge() # Charge of the particle, taken from pypdt
        self._set_lifetime() # Lifetime of the particle, taken from pypdt
        # Virtual particles have lifetimes that are too short, so we make them large. This can be changed to a more realistic approach
        self._lifetime *= 5.e9 #!!CHECK!!#
        # Decay channels are not needed, as we already know which one we want to assign
        self._decay = [p1,p2] # Particle decay channel chosen
        self._set_type() # Particle Type (quark, lepton, bosoon, meson, baryon) taken from json
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...] taken from json.
        self._set_lifetime_ren() #Renormalization of the lifetime THIS SHOULD BE DONE AT THE NODES and brought back with callback
        self._set_time_to_decay()  # Particle time lived before decay, renormalized
        self._setParent(parent)

        self._set_masses(p1,p2)


    def _set_masses(p1,p2):
        self._masses = [pythia.mass(p1),pythia.mass(p2)]
        
