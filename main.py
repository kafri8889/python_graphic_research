from renderer.ParticleSystem import ParticleSystem
from foundation.Particle import Particle
from foundation.Shape import Shape
import pygame

movement = 5

if __name__ == '__main__':
    # init
    pygame.init()

    # create display
    display = pygame.display.set_mode((1000, 1000))

    running = True

    # circle = Shape.circle(500, 500, 7, pygame.color.Color(255, 0, 0))
    # circle = Particle(shape=Shape.circle(500, 500, 7, pygame.color.Color(255, 0, 0)), )
    # circle2 = Particle(shape=Shape.circle(600, 500, 7, pygame.color.Color(255, 0, 0)), )
    ps = ParticleSystem(500, 500, 7, pygame.color.Color(255, 0, 0))

    pygame.display.update()

    while running:
        pygame.time.delay(25)
        ps.run()
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     pygame.time.wait(25)
        #     circle.move_particle()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ps.run()
                    # circle.move_particle()
                if event.key == pygame.K_ESCAPE:
                    running = False


        pygame.display.flip()



    pygame.quit()