import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode((1042,576))
clock = pygame.time.Clock()
bg= pygame.image.load('images/BG.png').convert()
bg= pygame.transform.scale(bg, size=(1042,576))
running = True
ninjaa = pygame.transform.scale(pygame.image.load('images/ninjarund.png').convert_alpha(), size= (75,75))
ninjad = pygame.transform.scale(pygame.image.load('images/ninjaruna.png').convert_alpha(), size= (75,75))
ninja_rect = ninjad.get_rect(center = (0,500))
ninja = ninjad
ninja_movementx = 500
suriken_surface1 = pygame.transform.scale2x(pygame.image.load('images/1.png').convert_alpha())
suriken_surface2 = pygame.transform.scale2x(pygame.image.load('images/2.png').convert_alpha())
suriken_surface3 = pygame.transform.scale2x(pygame.image.load('images/3.png').convert_alpha())
suriken_surface4 = pygame.transform.scale2x(pygame.image.load('images/4.png').convert_alpha())
suriken_list = []
def create_suriken():
    surikenx = random.randint(50,1000)
    surikeny = 0
    suriken1 = suriken_surface1.get_rect(center = (surikenx,surikeny))
    surikenx = random.randint(50,1000)
    suriken2 = suriken_surface2.get_rect(center = (surikenx,surikeny))
    surikenx = random.randint(50,1000)
    suriken3 = suriken_surface3.get_rect(center = (surikenx,surikeny))
    surikenx = random.randint(50,1000)
    suriken4 = suriken_surface4.get_rect(center = (surikenx,surikeny))    
    return suriken1, suriken2, suriken3, suriken4
def move_suriken(surikens):
    for suriken in surikens:
        suriken.centery += 5    
    return surikens
def draw_suriken(surikens):
    for suriken in surikens:        
        screen.blit(suriken_surface,suriken)
    return surikens
def check_collision(surikens):
    for suriken in surikens:
        if ninja_rect.colliderect(suriken):            
            return False
    return True
spawnsuriken = pygame.USEREVENT
pygame.time.set_timer(spawnsuriken,3000)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_RIGHT:
                ninja = ninjaa
                ninja_movementx += 50
            if event.key == pygame.K_d or event.key == pygame.K_LEFT:
                ninja = ninjad
                ninja_movementx -= 50
        if event.type == spawnsuriken:
            suriken_list.extend(create_suriken())  
            a = random.randint(1,4)
            if a == 1:
               suriken_surface = suriken_surface1
            if a == 2:
                suriken_surface = suriken_surface2
            if a == 3:
                suriken_surface = suriken_surface3
            if a == 4:
                suriken_surface = suriken_surface4
    screen.blit(bg,(0,0))
    ninja_rect.centerx = ninja_movementx
    ninja_rect.centery = 500
    suriken_list = move_suriken(suriken_list)
    draw_suriken(suriken_list)
    running = check_collision(suriken_list)
    screen.blit(ninja,ninja_rect)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()