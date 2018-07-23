from skhep.math.vectors import Vector3D
from skhep.constants import c_light as c
import numpy as np
import matplotlib.pyplot as plt
from phenomena.particles.dynamics.MyDynamics2 import Dynamics
from phenomena.particles.particle_boosted import ParticleBoosted


class BubbleChamber(object):
    def __init__(self, particles):
        self.dt = 0.001
        self.array_pos = np.array([[particles[0]._pos]])
        self.array_vel = np.array([[particles[0]._beta * Vector3D(np.cos(particles[0]._theta), np.sin(particles[0]._theta), 0) * c]])
        d = [0.]
        t = self.dt
        tmax = 10
        for i in range(1, len(particles)):
            self.array_pos = np.append(self.array_pos, [[particles[i]._pos]], axis = 0)
            self.array_vel = np.append(self.array_vel,[[particles[i]._beta * Vector3D(np.cos(particles[i]._theta), np.sin(particles[i]._theta), 0) * c]], axis = 0)
            d.append(0.)
        while t <= tmax:
            p = np.array([[[0,0,0]]])
            v = np.array([[[0,0,0]]])
            for i in range(len(particles)):
                n = Dynamics(Vector3D(self.array_pos[i][-1][0], self.array_pos[i][-1][1], self.array_pos[i][-1][2]), Vector3D(self.array_vel[i][-1][0], self.array_vel[i][-1][1], self.array_vel[i][-1][2]), particles[i], d[i], self.dt)
                p = np.append(p, [[n.pos]], axis = 0)
                v = np.append(v, [[n.vel]], axis = 0)
                try:
                    d[i] += abs(Vector3D(self.array_pos[i][-1][0], self.array_pos[i][-1][1], self.array_pos[i][-1][2]).mag - Vector3D(self.array_pos[i][-2][0], self.array_pos[i][-2][1], self.array_pos[i][-2][2]).mag)
                except:
                    d[i] += abs(Vector3D(self.array_pos[i][-1][0], self.array_pos[i][-1][1], self.array_pos[i][-1][2]).mag - particles[i]._pos.mag)
            p = np.delete(p, 0,0)
            v = np.delete(v, 0,0)
            self.array_pos = np.append(self.array_pos, p, axis = 1)
            t += self.dt

        print(d)
        print(self.array_pos)
        self.print_pos()

    def print_pos(self):
        fig, a = plt.subplots()
        a.plot(self.array_pos[0][ : , 0], self.array_pos[0][ : , 1])
        plt.show()
