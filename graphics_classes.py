# just some play tests to start with

import pygame

# Initialize Pygame
pygame.init()

# Set screen size (adjust based on your preference)
screen_width = 200
screen_height = 100
screen = pygame.display.set_mode((screen_width, screen_height))

# Load your four animation frames (replace with your filenames)
frame1 = pygame.image.load("sheep_standing.png").convert_alpha()
frame2 = pygame.image.load("sheep_lifting_leg.png").convert_alpha()
frame3 = pygame.image.load("sheep_mid_step.png").convert_alpha()
frame4 = pygame.image.load("sheep_landing.png").convert_alpha()


class Animation:
  def __init__(self, frames, animation_speed):
    self.frames = frames
    self.current_frame = 0
    self.animation_speed = animation_speed
    self.image = self.frames[self.current_frame]
    self.time_elapsed = 0

  def update(self, dt):
    self.time_elapsed += dt
    if self.time_elapsed >= self.animation_speed:
      self.current_frame = (self.current_frame + 1) % len(self.frames)
      self.image = self.frames[self.current_frame]
      self.time_elapsed = 0
      


clock = pygame.time.Clock()
animation = Animation([frame1, frame2, frame3, frame4], 5)  # Adjust speed as needed

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Update animation
  dt = clock.tick(60)  # Update delta time (time passed since last frame)
  animation.update(dt)

  # Clear screen and draw animation
  screen.fill((0, 0, 0))  # Replace with desired background color
  screen.blit(animation.image, (0, 0))  # Adjust position if needed

  pygame.display.flip()




pygame.quit()