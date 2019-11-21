# BY : MOHAMED ASHRAF GABER
# THIS IS A GAME WHICH CALLED "KILL THE ZOMBIES"
# IT'S MADE PY PYGAME
# YOU SHOULD KILL ALL ZOMBIES TO WIN
# WHEN YOU TOUCH THE ZOMBIES YOUR SCORE LESS 5 POINTS

# the imports that i will need it in this game
import pygame

# this line to initialization by game to start work
pygame.init()
pygame.display.set_caption('KILL ZOMBIES')

# ALL VARIABLES WILL BE HERE
run = True
# all source we need
# the background and all sounds are here
bg = pygame.image.load('images/Simple View.png')  # the background image
bgMusic = pygame.mixer.music.load('images/RGA-GT - Being Cool Doesn`t Make Me Fool.mp3')  # background music
pygame.mixer.music.play(-1)  # to make background music play auto
bulletSound = pygame.mixer.Sound('images/laserfire02.ogg')  # the sound of bullet
hitSound = pygame.mixer.Sound('images/laserfire01.ogg')  # the sound of hit
clock = pygame.time.Clock()  # this clock make fps to the game


# this is the surface that we will use and all things will display here
win = pygame.display.set_mode((1024, 575))


# this class will include all things to the player (images, animation, properties)
class Player:
    # this variables for the player's animation
    walkRight = [pygame.image.load('images/Player/Asset 7R.png'), pygame.image.load('images/Player/Asset 8R.png'),
                 pygame.image.load('images/Player/Asset 9R.png'), pygame.image.load('images/Player/Asset 10R.png'),
                 pygame.image.load('images/Player/Asset 11R.png'), pygame.image.load('images/Player/Asset 12R.png')]

    walkLeft = [pygame.image.load('images/Player/Asset 1L.png'), pygame.image.load('images/Player/Asset 2L.png'),
                pygame.image.load('images/Player/Asset 3L.png'), pygame.image.load('images/Player/Asset 4L.png'),
                pygame.image.load('images/Player/Asset 5L.png'), pygame.image.load('images/Player/Asset 6L.png')]

    standRight = [pygame.image.load('images/Player/Asset 46R.png'), pygame.image.load('images/Player/Asset 47R.png'),
                  pygame.image.load('images/Player/Asset 46R.png'), pygame.image.load('images/Player/Asset 48R.png'), ]

    standLeft = [pygame.image.load('images/Player/Asset 43L.png'), pygame.image.load('images/Player/Asset 44L.png'),
                 pygame.image.load('images/Player/Asset 43L.png'), pygame.image.load('images/Player/Asset 45L.png'), ]

    shootRight = [pygame.image.load('images/Player/Asset 1SR.png'), pygame.image.load('images/Player/Asset 2SR.png'),
                  pygame.image.load('images/Player/Asset 3SR.png'), pygame.image.load('images/Player/Asset 4SR.png'),
                  pygame.image.load('images/Player/Asset 5SR.png'), pygame.image.load('images/Player/Asset 6SR.png'), ]

    def __init__(self, x, y, width, height):
        # this variables for the information about the player
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fast = 11
        self.walk_count = 0
        self.right = False
        self.left = False
        self.stand = True
        self.stand_count = 0
        self.isJump = False
        self.jump_count = 10
        self.hitBox = (self.x, self.y, self.width, self.height)
        self.health = 5
        self.visible = True
        self.died = False

    # this function to draw the player and make it in the screen
    def draw(self, wins):
        if self.walk_count > 17:
            self.walk_count = 0

        if not self.stand:
            if self.left:
                wins.blit(self.walkLeft[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1

            elif self.right:
                wins.blit(self.walkRight[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1

        else:
            if self.stand_count > 12:
                self.stand_count = 0

            if self.left:
                wins.blit(self.standLeft[self.stand_count // 4], (self.x, self.y))
                self.walk_count = 0
                self.stand_count += 1
            else:
                wins.blit(self.standRight[self.stand_count // 4], (self.x, self.y))
                self.walk_count = 0
                self.stand_count += 1
        self.hitBox = (self.x, self.y, self.width + 20, self.height + 22)
        pygame.draw.rect(wins, (255, 0, 0), (self.hitBox[0] - 8, self.hitBox[1] - 20, 100, 15))
        pygame.draw.rect(wins, (0, 180, 0), (self.hitBox[0] - 8, self.hitBox[1] - 20,
                                             100 - (25 * (5 - self.health)), 17))

    def hit_by_touch(self):
        self.x = 500
        zombie.x = 0
        font2 = pygame.font.SysFont('Arial', 100, True)
        text2 = font2.render('-3', 1, (255, 0, 0))
        win.blit(text2, (1024 / 2, 575/2))

        if self.health > 1:
            self.health -= 1
            bulletSound.play()

        else:
            self.visible = False
            self.died = True

        pygame.display.update()
        i = 0
        while i < 15:
            pygame.time.delay(10)
            i += 1

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

    def hit_by_fire(self):

        if self.health > 1:
            self.health -= 1
            bulletSound.play()

        else:
            self.visible = False
            self.died = True

    @staticmethod
    def dead():
        global run
        font0 = pygame.font.SysFont('Arial', 100, True)
        text10 = font0.render('YOU DIED', 1, (255, 0, 0))
        win.blit(text10, (300, 175))
        for i in range(10000000):
            pass
        run = False


# this class for the enemy
class Enemy:
    walkRight = [pygame.image.load('images/Enemy/Asset 48RE.png'), pygame.image.load('images/Enemy/Asset 49RE.png'),
                 pygame.image.load('images/Enemy/Asset 50RE.png'), pygame.image.load('images/Enemy/Asset 51RE.png'),
                 pygame.image.load('images/Enemy/Asset 52RE.png'), pygame.image.load('images/Enemy/Asset 53RE.png'),
                 pygame.image.load('images/Enemy/Asset 54RE.png'), pygame.image.load('images/Enemy/Asset 55RE.png'),
                 pygame.image.load('images/Enemy/Asset 56RE.png'), ]

    walkLeft = [pygame.image.load('images/Enemy/Asset 39LE.png'), pygame.image.load('images/Enemy/Asset 40LE.png'),
                pygame.image.load('images/Enemy/Asset 41LE.png'), pygame.image.load('images/Enemy/Asset 42LE.png'),
                pygame.image.load('images/Enemy/Asset 43LE.png'), pygame.image.load('images/Enemy/Asset 44LE.png'),
                pygame.image.load('images/Enemy/Asset 45LE.png'), pygame.image.load('images/Enemy/Asset 46LE.png'),
                pygame.image.load('images/Enemy/Asset 47LE.png'), ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.fast = 5
        self.walk_count = 0
        self.hitBox = (self.x + 20, self.y + 15, 80, 100)
        self.heath = 4
        self.visible = True
        self.died = False
        self.isJump = False
        self.jump_count = 10

    # to draw the enemy and his animation
    def draw(self, wins):
        self.move()

        if self.walk_count > 26:
            self.walk_count = 0

        if self.fast < 0:
            wins.blit(self.walkLeft[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        else:
            wins.blit(self.walkRight[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        self.hitBox = (self.x + 20, self.y + 15, 80, 100)
        pygame.draw.rect(win, (255, 0, 0), (self.hitBox[0] - 15, self.hitBox[1] - 20, 100, 15))
        pygame.draw.rect(win, (0, 180, 0),
                         (self.hitBox[0] - 15, self.hitBox[1] - 20, 100 - (25 * (4 - self.heath)), 15))

    # to move the enemy automatically
    def move(self):
        if self.fast > 0:
            if self.x + self.width + self.fast < self.path[1]:
                self.x += self.fast

            else:
                self.fast *= -1
                self.walk_count = 0

        else:
            if self.x - self.fast > self.path[0]:
                self.x += self.fast

            else:
                self.fast *= -1
                self.walk_count = 0

    def hit(self):
        if self.heath > 0:
            self.heath -= 1

        else:
            self.visible = False
            self.died = True

    @staticmethod
    def dead():
        global run
        font0 = pygame.font.SysFont('Arial', 100, True)
        text10 = font0.render('YOU WON', 1, (0, 255, 0))
        win.blit(text10, (300, 175))
        for i in range(10000000):
            pass
        run = False


# this class for the fire
class Projectiles:
    def __init__(self, x, y, color, radius, face):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.face = face
        self.fast = 8 * self.face

    def draw(self, wins):
        pygame.draw.circle(wins, self.color, (self.x, self.y), self.radius)


class ProjectilesForEnemy:
    def __init__(self, x, y, color, radius, face):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.face = face
        self.fast = 8 * self.face

    def draw(self, wins):
        pygame.draw.circle(wins, self.color, (self.x, self.y), self.radius)


# here will be the objects and other variables
man = Player(500, 425, 51, 114)
zombie = Enemy(0, 445, 122, 124, 990)
shot = 0
bullets = []
bulletEnemy = []
score = 0  # The score of the game
tim = 0
p = 1


# This function check if the player touch the zombie and hurt him
def man_heart():
    global score

    if zombie.visible and man.visible:
        if man.hitBox[1] < zombie.hitBox[1] + zombie.hitBox[3] and (man.hitBox[1] + man.hitBox[3] > zombie.hitBox[1]):
            if man.hitBox[0] + man.hitBox[2] > zombie.hitBox[0] and \
                    (man.hitBox[0] < zombie.hitBox[0] + zombie.hitBox[2]):
                score -= 3
                man.hit_by_touch()


# this is simple timer to make time between each bullet
def simple_timer():
    global shot

    if shot > 0:
        shot += 1
    if shot > 5:
        shot = 0


# to check if the player close the game
def check_close():
    global run

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


# this function tell where is the fire and if the fire hit the zombie or not
# if the fire hit the zombie the score will be increased
# if the zombie was hit five times he will be removed
def where_fire_player():
    global score

    for bullet in bullets:
        # check if the bullet touch the zombie
        if zombie.visible and man.visible:
            if bullet.y + bullet.radius > zombie.hitBox[1] and bullet.y - bullet.radius < \
                            zombie.hitBox[1] + zombie.hitBox[3]:
                if bullet.x + bullet.radius > zombie.hitBox[0] and bullet.x - bullet.radius < \
                                zombie.hitBox[0] + zombie.hitBox[2]:

                    bulletSound.play()
                    score += 1
                    bullets.pop(bullets.index(bullet))
                    zombie.hit()

        # if the bullet inside the screen it will move directly
        if bullet.x < 1024 and (bullet.x > 0):
            bullet.x += bullet.fast

        # delete the bullet if it's out of screen
        else:
            bullets.pop(bullets.index(bullet))


def where_fire_enemy():
    for bullet in bulletEnemy:

        # check if the bullet touch the zombie
        if zombie.visible and man.visible:
            if bullet.y + bullet.radius > man.hitBox[1] and bullet.y - bullet.radius < \
                            man.hitBox[1] + man.hitBox[3]:
                if bullet.x + bullet.radius > man.hitBox[0] and bullet.x - bullet.radius < \
                                man.hitBox[0] + man.hitBox[2]:
                    bulletSound.play()
                    bulletEnemy.pop(bulletEnemy.index(bullet))
                    man.hit_by_fire()

        for fire in bullets:
            if bullet.y + bullet.radius > fire.y and (bullet.y - bullet.radius < fire.y + 15):
                if bullet.x + bullet.radius > fire.x and (bullet.x - bullet.radius < fire.x):
                    bulletSound.play()
                    bulletEnemy.pop(bulletEnemy.index(bullet))
                    bullets.pop(bullets.index(fire))

        if bullet.x < 1024 and (bullet.x > 0):
            bullet.x += bullet.fast

        else:
            bulletEnemy.pop(bulletEnemy.index(bullet))


def enemy_jump():
    t = 0
    if t > 0:
        t += 1
    if t > 80000000000:
        t = 0
    if not zombie.isJump:
        if t == 0 and zombie.visible:
            zombie.isJump = True
            t += 1

    else:
        if zombie.jump_count >= -10:
            neg = 1
            if zombie.jump_count < 0:
                neg = -1

            zombie.y -= (zombie.jump_count ** 2) / 2 * neg
            zombie.jump_count -= 1
        else:
            zombie.jump_count = 10
            zombie.isJump = False


def fire_player():
    global tim

    if tim > 0:
        tim += 1
    if tim > 80:
        tim = 0

    if tim == 0 and man.visible:
        # this if statement made to check if the player is looking for right or left
        # and make the direction of the bullet right or left
        if zombie.fast < 0:
            facing = -1

        else:
            facing = 1

        # make sure that five bullets only appear on the screen
        if len(bulletEnemy) < 5:
            hitSound.play()

            bulletEnemy.append(Projectiles(zombie.x + (round(zombie.width // 2)), round(zombie.y + zombie.height // 2),
                                           (0, 0, 255), 15, facing))
            tim = 1
    where_fire_enemy()


def space():
    global shot

    if keys[pygame.K_SPACE] and shot == 0 and man.visible:
        # this if statement made to check if the player is looking for right or left
        # and make the direction of the bullet right or left
        if man.left:
            facing = -1

        else:
            facing = 1

        # make sure that five bullets only appear on the screen
        if len(bullets) < 5:
            hitSound.play()

            bullets.append(Projectiles(man.x + (round(man.width // 2)), round(man.y + man.height // 2), (255, 0, 0), 15,
                                       facing))
        shot = 1


# this is about the directions of the player (right or left)
def directions():

    # this about the player in right position
    if keys[pygame.K_RIGHT] and man.x < 1000 - man.width:
        man.x += man.fast
        man.right = True
        man.left = False
        man.stand = False

    # this about the player in left position
    elif keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.fast
        man.left = True
        man.right = False
        man.stand = False

    else:
        man.walk_count = 0
        man.stand = True


# here when the player jump
def up():
    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True

    else:
        if man.jump_count >= -10:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count ** 2) / 2 * neg
            man.jump_count -= 1
        else:
            man.jump_count = 10
            man.isJump = False

    return


# this contain all keys
def press_key():
    # enemy_jump()
    space()
    directions()
    up()


# to print the score on the screen
def print_score():
    font = pygame.font.SysFont('Arial', 30, True)  # The settings of the font
    text = font.render('SCORE: ' + str(score), 1, (0, 0, 255))  # make the text able to be on the screen
    win.blit(text, (860, 30))


# this function will put in it all things to appear in the screen
def draw_game():
    global p

    win.blit(bg, (0, 0))  # to make the background as image

    fire_player()
    # to check if tha man is still alive to draw it
    if man.visible:
        man.draw(win)

    if man.died:
        man.dead()

    elif score == 20:
        zombie.dead()
    # to print the score on the screen
    print_score()

    # to check if tha zombie is still alive to draw it
    if zombie.visible:
        zombie.draw(win)

    else:

        zombie.visible = True
        zombie.draw(win)

        if p % 2 == 0:
            zombie.x = -60
            zombie.fast = 5
            p += 1
        else:
            zombie.x = 1024
            zombie.fast = -5
            p += 1
        zombie.heath = 4
        if man.health < 5:
            man.health += 1

    for f in bulletEnemy:
        f.draw(win)
    # Draw the bullets on the screen
    for fire in bullets:
        fire.draw(win)

    pygame.display.update()  # This very important to appear all things without any glitches


# this is tha main function
def main():

    man_heart()
    # this is simple timer to make time between each bullet
    simple_timer()

    # checking if the user close the game
    check_close()

    # to check if the bullet in side the screen
    where_fire_player()

    # all keys in this function
    press_key()

    draw_game()


# This the mainloop that make things display until the game end
while run:
    clock.tick(27)  # this make 27 fps to the game
    # that include all pressed the user do
    keys = pygame.key.get_pressed()

    main()


# quit the game
pygame.quit()
