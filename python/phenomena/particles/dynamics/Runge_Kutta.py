


class RK4(object):
    def __init__(self):
        self._set_x()
        self._set_y()
        self._set_z()
        self._set_px()
        self._set_py()
        self._set_pz()

    def _RK4(self, p, v, a, delta_t):
        z1 = (aux(p[0], v[0], 1, delta_t), aux(p[1], v[1], 1, delta_t))
        vz1 = (aux(v[0], a[0], 1, delta_t), aux(v[1], a[1], 1, delta_t))

        k1 = SolarSystem.Newton(z1[0], z1[1])
        z2 = (aux(p[0], vz1[0], 1, delta_t), aux(p[1], vz1[1], 1, delta_t))
        vz2 = (aux(v[0], k1[0], 1, delta_t), aux(v[1], k1[1], 1, delta_t))

        k2 = SolarSystem.Newton(z2[0], z2[1])
        z3 = (aux(p[0], vz2[0], 3, delta_t), aux(p[1], vz2[1], 3, delta_t))
        vz3 = (aux(v[0], k2[0], 3, delta_t), aux(v[1], k2[1], 3, delta_t))

        k3 = SolarSystem.Newton(z3[0], z3[1])
        x = p[0] + delta_t / 6 * (v[0] + 2 * vz1[0] + 2 * vz2[0] + vz3[0])
        y = p[1] + delta_t / 6 * (v[1] + 2 * vz1[1] + 2 * vz2[1] + vz3[1])
        vx = v[0] + delta_t / 6 * (a[0] + 2 * k1[0] + 2 * k2[0] + k3[0])
        vy = v[1] + delta_t / 6 * (a[1] + 2 * k1[1] + 2 * k2[1] + k3[1])


    def _forces(self):
        





        kk
