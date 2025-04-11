import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(split_angle)
        v2 = self.velocity.rotate(-split_angle)
        a1 = Asteroid(self.position.x,self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        a2 = Asteroid(self.position.x,self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt