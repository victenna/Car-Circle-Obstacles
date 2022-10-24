import pygame,math,time
pygame.init()
clock=pygame.time.Clock()
start = time.time()
screen= pygame.display.set_mode((1200,900))
#car_img1=pygame.image.load('car_1.png')
bground=pygame.image.load('bground.png')
font_name = pygame.font.match_font('arial')
images=[pygame.image.load('car_1.png'),pygame.image.load('car_2.png')]
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, 'white')
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Car(pygame.sprite.Sprite):
    def __init__(self,scale):
        super().__init__()
        self.image=images[0]
        self.image=pygame.transform.scale(self.image,(scale,scale))
        self.car_x=920
        self.car_y=430
        
        

    def update(self):
        button=pygame.key.get_pressed()
        if button[pygame.K_LEFT]:
            self.image=images[1]
            
            if self.car_x>150:
                self.car_x-=10
            else:
                self.car_x+=0
                
        if button[pygame.K_RIGHT]:
            self.image=images[0]
            if self.car_x<1050:
                self.car_x+=10
            else:
                self.car_x+=0
                
        self.rect=self.image.get_rect(center=(self.car_x,self.car_y))
        
            
    def draw(self):
        screen.blit(self.image,self.rect)

car1=Car(50)#,0)
#angle=0

class Obstacle():
    def __init__(self):
        super().__init__()
        self.obstacle_image=pygame.image.load('obstacle1.png')
        self.image=self.obstacle_image
        self.rect = self.image.get_rect(center=(600, 450))
        self.angle = 0
    def rot(self,d_angle):#,angle):
        self.image = pygame.transform.rotate(self.obstacle_image, self.angle)
        self.angle += d_angle
        self.rect = self.image.get_rect(center=self.rect.center)
    def draw(self):
        screen.blit(self.image,self.rect)
obstacle=Obstacle()
penalty=0
col,col1=0,0
s=0
while True:
    Time=time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(bground,(0,0))
    car1.update()
    car1.draw()
    obstacle.rot(-3)
    obstacle.draw()
    collision=pygame.sprite.collide_mask(obstacle,car1)
    
    if collision==None:
        col,col1=0,0
    if collision!=None:
        col1=1
        delta=col1-col
        col=col1
        if delta==1:
            penalty+=1
        
    #print('col=',col,'col1=',col1)
    draw_text(screen, 'Penalty  =', 38, 150, 600)
    draw_text(screen, str(penalty), 38, 250, 600)
    draw_text(screen, 'Time in sec  =', 38, 490, 10)
    counter=round(Time - start)
    if counter>=60:
        s=s+1
        draw_text(screen, 'Game Over', 72, 700, 700)
        if s>1:
            break
        
    draw_text(screen, str(counter), 38, 670, 10)
    pygame.display.update()
    clock.tick(60)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

    

    
    
        
        
    
