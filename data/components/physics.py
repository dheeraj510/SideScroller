__author__ = 'justinarmstrong'

class Physics(object):
    """A simplified physics class.  Pseudo gravity is often good enough"""
    def __init__(self):
        self.x_vel = self.y_vel = 0
        self.grav = 0.4
        self.fall = False

    def physics_update(self):
        if self.fall:
            self.y_vel += self.grav
        else:
            self.y_vel = 0


