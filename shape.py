from pygame import SRCALPHA, transform, draw
from pygame.surface import Surface


def _rotate(surface: Surface, angle: float):
    return transform.rotate(surface, angle)

class Shape:
    def __init__(self, alpha: int = 255, color: tuple[int, int, int] = (255, 255, 255), angle: float = 0):
        self.alpha, self._orig_alpha = alpha, alpha
        self.angle, self._orig_angle = angle, angle
        self.color, self._orig_color = color, color

        self.surface: Surface

    def orig_alpha(self):
        return self._orig_alpha

    def orig_angle(self):
        return self._orig_angle
    
    def orig_color(self):
        return self._orig_color

    def check_size_above_zero(self) -> bool:
        raise NotImplementedError

    def get_progress(self) -> tuple[float, float]:
        raise NotImplementedError

    def decrease(self, delta: float) -> None:
        raise NotImplementedError

    def make_surface(self) -> Surface:
        raise NotImplementedError

    def make_shape(self) -> None:
        raise NotImplementedError


class BaseForm(Shape):
    def __init__(self, radius: float, color: tuple[int, int, int], alpha: int = 255, angle: float = 0):
        super().__init__(alpha=alpha, color=color, angle=angle)

        self.radius = radius
        self._orig_radius = self.radius

        self.color, self._orig_color = color, color

        self.make_surface()

    def orig_radius(self):
        return self._orig_radius

    def orig_color(self):
        return self._orig_color

    def check_size_above_zero(self):
        if self.radius > 0:
            return True
        else:
            return False

    def get_progress(self) -> tuple[float, float]:
        progress = self.radius / self._orig_radius
        return progress, 1 - progress

    def decrease(self, delta: float):
        self.radius -= delta
        if self.radius < 0:
            self.radius = 0

    def make_surface(self) -> Surface:
        self.surface = Surface((self.radius * 2, self.radius * 2), SRCALPHA)
        self.surface.set_alpha(self.alpha)
        self.make_shape()
        self.surface = _rotate(surface=self.surface, angle=self.angle)
        return self.surface

    def make_shape(self) -> None:
        raise NotImplementedError


class Circle(BaseForm):
    def __init__(self, radius: float, color: tuple[int, int, int], alpha: int = 255, angle: float = 0):
        super().__init__(radius, color, alpha, angle)

    def make_shape(self):
        draw.circle(self.surface, self.color, (self.radius, self.radius), self.radius)


class Rect(BaseForm):
    def __init__(self, radius: float, color: tuple[int, int, int], alpha: int = 255, angle: float = 0):
        super().__init__(radius, color, alpha, angle)

    def make_shape(self):
        self.surface.fill(self.color)