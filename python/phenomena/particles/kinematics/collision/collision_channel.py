from phenomena.particles.particle_virtual import VirtualChannel
from phenomena.particles.kinematics.collision.cross_section import CrossSection

class CollisionChannel(VirtualChannel):

    def __init__(self,p1,p2,energy,impact):
