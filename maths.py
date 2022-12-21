from . import particule


def fade_color(particle: particule.Particle, color: tuple[int, int, int], progress: float) -> tuple[int, int, int]:
    calculated_color = (int(particle.shape.orig_color()[i] + (color[i] - particle.shape.orig_color()[i]) * progress) for i in range(3))
    return tuple(calculated_color)

def fade_alpha(particle: particule.Particle, alpha: int, progress: float) -> int:
    return int(particle.shape.orig_alpha() + (alpha - particle.shape.orig_alpha()) * progress)

def fade_alpha_exp(particle: particule.Particle, alpha: int, progress: float) -> int:
    return int(particle.shape.orig_alpha() + (alpha - particle.shape.orig_alpha()) * progress ** 3)