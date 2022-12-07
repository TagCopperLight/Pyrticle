import particule


def fade_color(particle: particule.Particle, color: tuple[int, int, int], progress: float) -> list:
    return [particle.shape.orig_color()[i] + (color[i] - particle.shape.orig_color()[i]) * progress for i in range(3)]


def fade_alpha(particle: particule.Particle, alpha: int, progress: float) -> float:
    return particle.shape.orig_alpha() + (alpha - particle.shape.orig_alpha()) * progress
