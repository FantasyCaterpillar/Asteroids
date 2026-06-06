
import pygame,random
from logger import log_state,log_event
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x:float, y:float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            asteroid1_speed = self.velocity.rotate(angle)
            asteroid2_speed = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = asteroid1_speed * 1.2
            asteroid2.velocity = asteroid2_speed * 1.2






