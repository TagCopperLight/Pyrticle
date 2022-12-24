"""
This type stub file was generated by pyright.
"""

from . import shape
from pygame.math import Vector2
from pygame.surface import Surface

class Particle:
    def __init__(self, shape: shape.Shape, position: Vector2, velocity: Vector2, delta_radius: float, alive: bool = ...) -> None:
        self.shape: shape.Shape
        self.progress: float
        self.inverted_progress: float
    
    def kill(self) -> None:
        ...
    
    def update(self, delta_t: float, gravity: Vector2 = ...) -> None:
        ...
    
    def render(self, surface: Surface) -> None:
        ...
    


class ParticleSystem:
    def __init__(self) -> None:
        self.particles: list[Particle]
    
    def emit(self, particle: Particle) -> None:
        ...
    
    def clear(self) -> None:
        ...
    
    def update(self, delta_t: float, gravity: Vector2 = ...) -> None:
        ...
    
    def make_shape(self) -> None:
        ...
    
    def render(self, surface: Surface) -> None:
        ...
    

