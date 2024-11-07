from pgzero.actor import Actor

class AnimatedActor(Actor):
    def __init__(self, images, pos):
        super().__init__(images[0], pos)
        self.images = images
        self.current_frame = 0
        self.frame_count = len(images)
        self.animation_speed = 0.1  # Adjust this for faster/slower animation
        self.time_elapsed = 0

    def update(self, dt):
        self.time_elapsed += dt
        if self.time_elapsed >= self.animation_speed:
            self.time_elapsed = 0
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.image = self.images[self.current_frame]
