from __future__ import division
import math

from particletools.tables import PYTHIAParticleData as pythia
from phenomena.particles.kinematics.decay.Breit_Wigner import lim_nonrel_breit_wigner_gen, lim_rel_breit_wigner_gen

class CrossSection(Object):

    def __init__(self,p1,p2,energy):

        self._choose_virtual(p1,p2)

        masses = {}
        mwidth = {}

    def _choose_virtual(self,p1,p2):
        self._virtual = 
