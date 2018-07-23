from skhep.math.vectors import Vector3D


class field(object):
    def __init__(self):
        self._set_field_B()
        self._set_field_E()

    def _set_field_B(self):
        self.B = Vector3D(0,0,1)

    def _set_field_E(self):
        self.E = Vector3D(0,0,0)
