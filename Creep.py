class Creep():
    def __init__(
        self, screen, filename, pos, dir, speed):
        self.filename = "fishdish/" + filename[0]
        '''
        Creep Object
        Screen: A pygame screen (pygame.display)
        filename (image for the creep)
        init_pos: A tuple containing (x,y)
        init_dir: A 2d vector of the creep
        speed: creep speed in pixel/millisecond
        '''
    def update(self):
        displace = vec2d(
