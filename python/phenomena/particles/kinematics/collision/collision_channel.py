from __future__ import division
import math

from particletools.tables import PYTHIAParticleData as pythia
from phenomena.particles.kinematics.decay.inverse_decay_list import InverseDecayList
from phenomena.particles.particle_virtual import VirtualChannel
from phenomena.particles.kinematics.collision.cross_section import CrossSection

class CollisionChannel(Object):

    def __init__(self,p1,p2,energy,impact):

        self._choose_virtual(p1,p2)
        self._set_virtual_data(self._virtual_list)




    def _choose_virtual(self,p1,p2): # Fetches possible virtual particles
        self._virtual_list = InverseDecayList(p1,p2)._virtual_list

    def _set_virtual_data(self,virtual_liust):
        GeVfm = 0.19732696312541853
        self._virtual_masses = []
        self._virtual_widths = []
        for particle in virtual_list:
            self._virtual_masses.append(pythia.mass(particle))
            self._virtual_widths.append(GeVfm/pythia.ctau(particle)*1e-15*100.0)
