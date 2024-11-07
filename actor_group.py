class ActorGroup:
    def __init__(self):
        self.actors = []
        self.initial_positions = []

    def add(self, actor):
        self.actors.append(actor)
        self.initial_positions.append(actor.pos)

    def remove(self, actor):
        index = self.actors.index(actor)
        self.actors.remove(actor)
        self.initial_positions.pop(index)

    def draw(self):
        for actor in self.actors:
            actor.draw()

    def collidepoint(self, pos):
        for actor in self.actors:
            if actor.collidepoint(pos):
                return True
        return False


    def update(self, dt):
        for actor in self.actors:
            if hasattr(actor, 'update'):
                actor.update(dt)

    def set_position(self, new_base_pos):
        base_x, base_y = new_base_pos
        for i, actor in enumerate(self.actors):
            initial_x, initial_y = self.initial_positions[i]
            offset_x = initial_x - self.initial_positions[0][0]
            offset_y = initial_y - self.initial_positions[0][1]
            actor.pos = (base_x + offset_x, base_y + offset_y)
