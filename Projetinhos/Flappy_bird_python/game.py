import pygame
import os
import random
import time


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('Projetos','Projetinhos','Flappy_bird_python','imgs','pipe.png')))
GORUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('Projetos','Projetinhos','Flappy_bird_python','imgs','base.png')))
BACKGROUND_IMAGE =pygame.transform.scale2x(pygame.image.load(os.path.join('Projetos','Projetinhos','Flappy_bird_python','imgs','bg.png')))

if (random.randint(1,25)) == 1:
    BIRD_IMAGES = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('Projetos','Projetinhos','Flappy_bird_python','imgs','birdS1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('Projetos','Projetinhos','Flappy_bird_python','imgs','birdS2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('Projetos','Projetinhos','Flappy_bird_python','imgs','birdS3.png')))
]
else:
    BIRD_IMAGES = [
        pygame.transform.scale2x(pygame.image.load(os.path.join('Projetos','Projetinhos','Flappy_bird_python','imgs','bird1.png'))),
        pygame.transform.scale2x(pygame.image.load(os.path.join('Projetos','Projetinhos','Flappy_bird_python','imgs','bird2.png'))),
        pygame.transform.scale2x(pygame.image.load(os.path.join('Projetos','Projetinhos','Flappy_bird_python','imgs','bird3.png')))
    ]

pygame.font.init()
SCORE_FONT = pygame.font.SysFont('arial', 50)

FAIL_FONT = pygame.font.SysFont('arial', 40)


class Bird:
    IMGS = BIRD_IMAGES
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.velocity = 0
        self.height = self.y
        
        self.time = 0
        self.image_score = 0
        self.image   = self.IMGS[0]
        
    def jump(self):
        self.velocity = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
        self.time += 1
        displacement = 1.5 * (self.time**2) + self.velocity * self.time
        
        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2
            
        self.y += displacement
        
        if displacement < 0 or self.y < (self.height + 50):
            if self.angle < self.MAX_ROTATION:
                self.angle = self.MAX_ROTATION
        else:
             if self.angle > -90:
                 self.angle -= self.ROTATION_VELOCITY       
        
    def draw(self, screen):
        self.image_score += 1
        
        if self.image_score < self.ANIMATION_TIME:
            self.image = self.IMGS[0]
        elif self.image_score < self.ANIMATION_TIME * 2:
            self.image = self.IMGS[1]
        elif self.image_score < self.ANIMATION_TIME * 3:
            self.image = self.IMGS[2]
        elif self.image_score < self.ANIMATION_TIME * 4:
            self.image = self.IMGS[1]
        elif self.image_score >= self.ANIMATION_TIME * 4 + 1:
            self.image = self.IMGS[0]
            self.image_score = 0
            
        if self.angle <= -80:
            self.image = self.IMGS[1]
            self.image_score = self.ANIMATION_TIME * 2
            
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        center_image = self.image.get_rect(topleft = (self.x, self.y)).center
        rectangle = rotated_image.get_rect(center = center_image)
        screen.blit(rotated_image, rectangle.topleft)
        
    def get_mask(self):
        return pygame.mask.from_surface(self.image)


class Pipe:
    DISTANCE = 200
    VELOCITY = 5
    
    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top_pos = 0
        self.base_pos = 0
        self.TOP_PIPE = pygame.transform.flip(PIPE_IMAGE, False, True)
        self.BASE_PIPE = PIPE_IMAGE
        self.passed = False
        self.def_height()
        
    def def_height(self):
        self.height = random.randrange(50, 450)
        self.top_pos = self.height - self.TOP_PIPE.get_height()
        self.base_pos = self.height + self.DISTANCE
        
    def move(self):
        self.x -= self.VELOCITY
        
    def draw(self, screen):
        screen.blit(self.TOP_PIPE, (self.x, self.top_pos))
        screen.blit(self.BASE_PIPE, (self.x, self.base_pos))
           
    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.TOP_PIPE)
        base_mask = pygame.mask.from_surface(self.BASE_PIPE)
        
        top_distance = (self.x - bird.x, self.top_pos - round(bird.y))
        base_distance = (self.x - bird.x, self.base_pos - round(bird.y))
        
        top_point = bird_mask.overlap(top_mask, top_distance)
        base_point = bird_mask.overlap(base_mask, base_distance)
        
        if base_point or top_point:
            return True
        else:
            return False
        

class Ground:
    VELOCITY = 5
    WIDTH = GORUND_IMAGE.get_width()
    IMAGE = GORUND_IMAGE
    
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        
    def move(self):
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY
        
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH
            
    def draw(self, screen):
        screen.blit(self.IMAGE, (self.x1, self.y))
        screen.blit(self.IMAGE, (self.x2, self.y))
        
def draw_mainScreen(screen, birds, pipes, ground, score):
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    for bird in birds:
        bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)
        
    text = SCORE_FONT.render(f"{score}", 1, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))
    ground.draw(screen)
    pygame.display.update()
    
def lose(screen, score):
    text = FAIL_FONT.render(f"You failed, you've got {score} points", 1, (255 , 255, 255))
    screen.blit(text, (SCREEN_WIDTH - 40 - text.get_width(), 250))
    pygame.display.update()
    
def main():
    birds = [Bird(230, 350)]
    ground = Ground(730)
    pipes = [Pipe(700)]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = 0
    clock = pygame.time.Clock()
    
    running = True
    while running:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    quit()
                if (event.key == pygame.K_SPACE) or (event.key == pygame.K_w):
                    for bird in birds:
                        bird.jump()
                        
        for bird in birds:
            bird.move()
        ground.move()   
        
        add_pipe = False
        remove_pipes = []
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.collide(bird):
                    birds.pop(i)
                    if birds == []:
                        running = False
                        time.sleep(1)
                        lose(screen, score)
                        time.sleep(2)
                        pygame.quit()
                        quit()
                    
                if not pipe.passed and bird.x > pipe.x:
                    pipe.passed =  True
                    add_pipe = True
                    
            pipe.move()
            if pipe.x + pipe.TOP_PIPE.get_width() < 0:
                remove_pipes.append(pipe)

        if add_pipe:
            score += 1
            pipes.append(Pipe(600))
        for pipe in remove_pipes:
            pipes.remove(pipe)    
        
        for i, bird in enumerate(birds):
            if (bird.y + bird.image.get_height()) > ground.y or bird.y < 0:
                birds.pop(i)
                if birds == []:
                    running = False
                    time.sleep(1)
                    lose(screen, score)
                    time.sleep(2)
                    pygame.quit()
                    quit()
      
        draw_mainScreen(screen, birds, pipes, ground, score)
        
if __name__ == '__main__':
    main()
    
    
    
    
    
#add modo de ganhar o jogo
    #se pontuação for X, jogo vence
#add outros assets para fazer o jogo se parecer mais com pokemon
#melhorar tela de morte
#melhorar jogo quando o jogador perder o jogo
#add um try again no jogo
    #um sistema de score máximo entre as tentativas
