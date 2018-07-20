import abc

class CMCalc(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def E(energy,masses):
        """Returns list of child virtual particle energy"""

    @abc.abstractmethod
    def P():
        """Returns list of child virtual particle momentum"""


class LabCalc(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def values(self):
        """Returns list of dictonaries of child particles momentum, angle and energy"""
        pass
