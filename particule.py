from pygame.math import Vector2
from pygame.surface import Surface

import .shape


class Particle:
    def __init__(self, shape: shape.Shape, position: Vector2, velocity: Vector2, delta_radius: float, alive: bool = True):
        self.shape = shape

        self.position = position
        self.velocity = velocity

        self.delta_radius = delta_radius

        self.progress, self.inverted_progress = self.shape.get_progress()

        self.alive = alive

    def kill(self):
        self.alive = False

    def update(self, delta_t: float, gravity: Vector2 = Vector2()):
        self.shape.decrease(self.delta_radius)

        if self.shape.check_size_above_zero():
            if self.alive:
                self.velocity += gravity * delta_t
                self.position += self.velocity * delta_t

                self.progress, self.inverted_progress = self.shape.get_progress()
        else:
            self.kill()

    def render(self, surface: Surface):
        if self.alive:
            surface.blit(self.shape.surface, self.position - Vector2(self.shape.surface.get_size()) / 2)


class ParticleSystem:
    def __init__(self):
        self.particles: list[Particle] = []

    def emit(self, particle: Particle):
        self.particles.append(particle)

    def clear(self):
        self.particles.clear()

    def update(self, delta_t: float, gravity: Vector2 = Vector2()):
        for particle in self.particles:
            particle.update(delta_t, gravity)

            if not particle.alive:
                self.particles.remove(particle)

    def make_shape(self):
        for particle in self.particles:
            particle.shape.make_surface()

    def render(self, surface: Surface):
        for particle in self.particles:
            particle.render(surface)
