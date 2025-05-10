import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self):
		pygame.draw.circle(self.position, self.radius, 2)

	def update(self):
		self.position += self.velocity * dt