import abc

class C12MCalc(object):
# For 3body decay this RF for the CM of particles 1 and 2 is useful
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def dalitz(masses):
        """Returns the randomized dalitz plot variable m12"""

    @abc.abstractmethod
    def E(masses,dalitz):
        """Returns list of child particles energies"""

    @abc.abstractmethod
    def P(masses,dalitz):
        """Returns list of child particles momentum"""

    @abc.abstractmethod
    def pxy(masses,dalitz,angles):
        """Returns list of dictonaries of child particles momentum components"""
        pass

class CMCalc(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def values(self):
        """Returns list of dictonaries of parent particles' momentum, angle and energy"""
        pass


class LabCalc(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def values(self):
        """Returns list of dictonaries of child particle's momentum, angle and energy"""
        pass
