from circleshape import *
from constants import *


class Shot(CircleShape):

    def __init__(self, x:float, y:float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,1)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)