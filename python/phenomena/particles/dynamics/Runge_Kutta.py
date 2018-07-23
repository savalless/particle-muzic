from skhep.math.vectors import Vector3D
from phenomena.particles.dynamics.forces import TotalAcc

class RK4(object):
    def __init__(self, p, v, d, E, delta_t, charge, mass, name):
        assert type(p) is Vector3D
        assert type(v) is Vector3D
        self.init_pos = p
        self.init_vel = v
        self.total_d = d
        self.init_E = E
        self.delta_t = delta_t
        self.charge = charge
        self.mass = mass
        self.name = name
        self._RK4()

    def _RK4(self):
        self.acc = TotalAcc(self.init_vel, self.total_d, self.init_E, self.charge, self.mass, self.name).acc
        z1 = Vector3D(self.aux(self.init_pos.x, self.init_vel.x, 1), self.aux(self.init_pos.y, self.init_vel.y, 1), self.aux(self.init_pos.z, self.init_vel.z, 1))
        vz1 = Vector3D(self.aux(self.init_vel.x, self.acc.x, 1), self.aux(self.init_vel.y, self.acc.y, 1), self.aux(self.init_vel.z, self.acc.z, 1))

        k1 = TotalAcc(vz1, self.total_d, self.init_E, self.charge, self.mass, self.name).acc
        z2 = Vector3D(self.aux(self.init_pos.x, vz1.x, 1), self.aux(self.init_pos.y, vz1.y, 1), self.aux(self.init_pos.z, vz1.z, 1))
        vz2 = Vector3D(self.aux(self.init_vel.x, k1.x, 1), self.aux(self.init_vel.y, k1.y, 1), self.aux(self.init_vel.z, k1.z, 1))

        k2 = TotalAcc(vz2, self.total_d, self.init_E, self.charge, self.mass, self.name).acc
        z3 = Vector3D(self.aux(self.init_pos.x, vz2.x, 3), self.aux(self.init_pos.y, vz2.y, 3), self.aux(self.init_pos.z, vz2.z, 3))
        vz3 = Vector3D(self.aux(self.init_vel.x, k2.x, 3), self.aux(self.init_vel.y, k2.y, 3), self.aux(self.init_vel.z, k2.z, 3))

        k3 = TotalAcc(vz3, self.total_d, self.init_E, self.charge, self.mass, self.name).acc
        self.pos = self.init_pos + self.delta_t / 6 * (self.init_vel + 2 * vz1 + 2 * vz2 + vz3)
        self.vel = self.init_vel + self.delta_t / 6 * (self.acc + 2 * k1 + 2 * k2 + k3)

    def aux(self, a, b, c):
        if c == 1:  #This is used for the z1, z2, vz1 and vz2 functions
            z = a + self.delta_t * b / 2
        else:       #This is used for the z3 and vz3 functions
            z = a + self.delta_t * b
        return z
