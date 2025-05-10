# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updateable_players = pygame.sprite.Group()
	drawable_players = pygame.sprite.Group()
	Player.containers = (updateable_players, drawable_players)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	
	updateable_asteroid = pygame.sprite.Group()
	drawable_asteroid = pygame.sprite.Group()
	Asteroid.containers = (updateable_asteroid, drawable_asteroid)

	updateable_asteroidfield = pygame.sprite.Group()
	AsteroidField.containers = (updateable_asteroidfield)
	AsteroidField()

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updateable_asteroidfield.update(dt)
		updateable_asteroid.update(dt)
		updateable_players.update(dt)

		for asteroid in drawable_asteroid:
			if asteroid.collision(player):
				print("Game over!")
				exit()
				

		screen.fill("black")
		for player in drawable_players:
			player.draw(screen)
		for asteroid in drawable_asteroid:
			asteroid.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()