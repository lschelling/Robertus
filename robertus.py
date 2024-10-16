import pgzrun
import pygame

WIDTH = 1024*2
HEIGHT = 640*2
robertus_frames = ["200200_face_editor" , "200x200_face_closed_eyes_editor"]
robertus= Actor(robertus_frames[0]) 


frame_index = 0
frame_duration = 0.5  # Time in seconds for each frame
time_elapsed = 0

background = pygame.image.load("images/1024x640_editor_background.png")
scaled_background = pygame.transform.scale(background, (WIDTH, HEIGHT))

def update(dt):
    global frame_index, time_elapsed

  # Update time elapsed
    time_elapsed += dt

    # Switch frame when the duration is exceeded
    if time_elapsed >= frame_duration:
        frame_index = (frame_index + 1) % len(robertus_frames)
        robertus.image = robertus_frames[frame_index]
        time_elapsed = 0  # Reset the timer

def draw():
    screen.clear()
    # Blit the scaled background
    screen.surface.blit(scaled_background, (0, 0))
    robertus.draw()

def on_mouse_move(pos):
    # Überprüfen, ob die linke Maustaste gedrückt wird
    if mouse.LEFT:
        robertus.pos = pos  # Setzt die Position des Actors auf die Mausposition

pgzrun.go()