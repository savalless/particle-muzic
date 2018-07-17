from __future__ import division
import math

from particletools.tables import PYTHIAParticleData as pythia
from phenomena.particles.kinematics.decay.Breit_Wigner import lim_nonrel_breit_wigner_gen, lim_rel_breit_wigner_gen
from phenomena.particles.kinematics.decay.inverse_decay_list import InverseDecayList

class CrossSection(Object):

    def __init__(self,mass,energy):
