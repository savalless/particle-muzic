from __future__ import division
import math, random

from phenomena.particles.kinematics.parameters import boostParams

import nbodycollision

class Col2BodyCalc(nbodycollision.LabCalc):

    def __init__(self,particles,virtual,momenta,angles,masses):
        self._decay = virtual
        self._inc_particles = particles
        inc_energies = self._set_energies(momenta,masses)
        # From here on, all calculations are for outgoing particle ('virtual')
        self._pExyz = self._set_pExyz(momenta,angles,inc_energies)
        self._p = self._set_p()
        self._mass = self._set_mass(self._p,self._pExyz['E'])
        self._theta = self._set_angle(self._pExyz['x'],self._pExyz['y'])

        self._values = self._set_values()

    def _set_energies(self,momenta,masses):
        E1 = (masses[0]**2+momenta[0]**2)**(1/2) # For 2D
        E2 = (masses[1]**2+momenta[1]**2)**(1/2) # For 2D
        return [E1,E2]

    def _set_pExyz(self,momenta,angles,energies):
        return {
            'x':momenta[0]*math.cos(angles[0])+momenta[1]*math.cos(angles[1]),
            'y':momenta[0]*math.sin(angles[0])+momenta[1]*math.sin(angles[1]),
            'z':0,
            'E':energies[0]+energies[1]
        }

    def _set_p(self):
        return math.sqrt(self._pExyz['x']**2+self._pExyz['y']**2)

    def _set_mass(self,p,E):
        return (E**2-p**2)**(1/2)

    def _set_angle(self,px,py):
        if px != 0:
            angle=math.atan(py/px)
        elif py != 0:
            sign = py/(py**2)**(1/2)
            angle=sign*math.pi/2
        else:
            angle=0
        return angle

    def _set_values(self):
        return  {
                    'name': self._decay,
                    'p': self._p,
                    'theta': self._theta,
                    'E': self._pExyz['E'],
                    'mass': self._mass
                }

    @property
    def values(self):
        return self._values
