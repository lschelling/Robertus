import pgzrun
import pygame
from actor_group import ActorGroup
from animated_actor import AnimatedActor

WIDTH = 1024*2
HEIGHT = 640*2



# Create an instance of ActorGroup
robertus = ActorGroup()

# Add some animated actors to the group
robertus.add(AnimatedActor(["200200_face_editor" , "200x200_face_closed_eyes_editor"], (100, 100)))
robertus.add(AnimatedActor(["200200_face_editor" , "200x200_face_closed_eyes_editor"], (200, 200)))


background = pygame.image.load("images/1024x640_editor_background.png")
scaled_background = pygame.transform.scale(background, (WIDTH, HEIGHT))
follow=False

def update(dt):
    robertus.update(dt)
    
def draw():
    screen.clear()
    # Blit the scaled background
    screen.surface.blit(scaled_background, (0, 0))
    robertus.draw()

def on_mouse_move(pos):
    global follow
    global robertus


    # Übedrprüfen, ob die linke Maustaste gedrückt wird
    if follow == True:
        robertus.set_position(pos)   # Setzt die Position des Actors auf die Mausposition
        

def on_mouse_down(pos, button):
    global robertus
    global follow

    if button == mouse.LEFT and robertus.collidepoint(pos):
        follow = True
    
    if button == mouse.RIGHT:
        follow = False
    

pgzrun.go()