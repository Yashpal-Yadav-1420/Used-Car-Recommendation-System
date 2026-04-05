import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_POWER = 10
PLAYER_SPEED = 5
BULLET_SPEED = 10
SHOOT_COOLDOWN = 200  # milliseconds

# Jetpack constants
MAX_JETPACK_FUEL = 100
JETPACK_CONSUMPTION_RATE = 0.5
JETPACK_REFILL_RATE = 0.2
JETPACK_FORCE = 0.7

# Weapon types
WEAPONS = {
    'pistol': {
        'damage': 10,
        'cooldown': 200,
        'bullet_speed': 10,
        'bullet_size': (10, 4),
        'bullet_color': (0, 0, 0),
        'ammo': -1  # Infinite ammo
    },
    'shotgun': {
        'damage': 8,
        'cooldown': 500,
        'bullet_speed': 8,
        'bullet_size': (8, 8),
        'bullet_color': (139, 69, 19),
        'ammo': 20,
        'bullets_per_shot': 5,
        'spread': 0.2
    },
    'machinegun': {
        'damage': 5,
        'cooldown': 100,
        'bullet_speed': 12,
        'bullet_size': (6, 3),
        'bullet_color': (178, 34, 34),
        'ammo': 50
    },
    'sniper': {
        'damage': 40,
        'cooldown': 1000,
        'bullet_speed': 20,
        'bullet_size': (15, 3),
        'bullet_color': (75, 0, 130),
        'ammo': 10
    }
}

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
BROWN = (165, 42, 42)
YELLOW = (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mini Militia Clone')
clock = pygame.time.Clock()

# Create a background
def create_background():
    background = pygame.Surface((WIDTH, HEIGHT))
    
    # Sky gradient
    for y in range(HEIGHT):
        # Gradient from light blue to darker blue
        color_value = 255 - int(y * 0.4)
        color = (100, 180, min(255, max(0, color_value)))
        pygame.draw.line(background, color, (0, y), (WIDTH, y))
    
    # Add some clouds
    for _ in range(10):
        cloud_x = random.randint(0, WIDTH)
        cloud_y = random.randint(0, HEIGHT // 2)
        cloud_size = random.randint(20, 50)
        pygame.draw.ellipse(background, (240, 240, 240), 
                           (cloud_x, cloud_y, cloud_size * 2, cloud_size))
        pygame.draw.ellipse(background, (240, 240, 240), 
                           (cloud_x + cloud_size, cloud_y - cloud_size // 2, cloud_size * 1.5, cloud_size))
    
    return background

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color, controls):
        super().__init__()
        self.image = pygame.Surface((30, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)
        self.on_ground = False
        self.health = 100
        self.score = 0
        self.controls = controls  # {'left': key, 'right': key, 'jump': key, 'shoot': key, 'jetpack': key, 'switch_weapon': key}
        self.facing_right = True
        self.last_shot_time = 0
        self.alive = True
        
        # Jetpack
        self.jetpack_fuel = MAX_JETPACK_FUEL
        self.using_jetpack = False
        
        # Weapons
        self.weapons = ['pistol', 'shotgun', 'machinegun', 'sniper']
        self.current_weapon_index = 0
        self.weapon_ammo = {weapon: WEAPONS[weapon]['ammo'] for weapon in self.weapons}
    
    @property
    def current_weapon(self):
        return self.weapons[self.current_weapon_index]
    
    def switch_weapon(self):
        self.current_weapon_index = (self.current_weapon_index + 1) % len(self.weapons)
    
    def jump(self):
        if self.on_ground:
            self.velocity.y = -JUMP_POWER
            self.on_ground = False
    
    def activate_jetpack(self, activate):
        self.using_jetpack = activate and self.jetpack_fuel > 0
    
    def move(self, dx):
        self.velocity.x = dx * PLAYER_SPEED
        if dx > 0:
            self.facing_right = True
        elif dx < 0:
            self.facing_right = False
    
    def shoot(self, bullet_group):
        weapon = WEAPONS[self.current_weapon]
        
        # Check ammo
        if weapon['ammo'] != -1 and self.weapon_ammo[self.current_weapon] <= 0:
            return False
        
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > weapon['cooldown']:
            self.last_shot_time = current_time
            
            # Consume ammo
            if weapon['ammo'] != -1:
                self.weapon_ammo[self.current_weapon] -= 1
            
            direction = 1 if self.facing_right else -1
            
            # Handle shotgun spread
            if self.current_weapon == 'shotgun' and 'bullets_per_shot' in weapon:
                for _ in range(weapon['bullets_per_shot']):
                    # Add random spread
                    spread = random.uniform(-weapon['spread'], weapon['spread'])
                    bullet = Bullet(
                        self.rect.centerx, 
                        self.rect.centery, 
                        direction,
                        weapon['bullet_speed'],
                        weapon['bullet_size'],
                        weapon['bullet_color'],
                        weapon['damage'],
                        spread_angle=spread
                    )
                    bullet_group.add(bullet)
            else:
                bullet = Bullet(
                    self.rect.centerx, 
                    self.rect.centery, 
                    direction,
                    weapon['bullet_speed'],
                    weapon['bullet_size'],
                    weapon['bullet_color'],
                    weapon['damage']
                )
                bullet_group.add(bullet)
            
            return True
        return False
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.alive = False
    
    def update(self, platforms):
        # Apply gravity
        if not self.using_jetpack:
            self.velocity.y += GRAVITY
        else:
            # Apply jetpack force
            self.velocity.y -= JETPACK_FORCE
            # Consume jetpack fuel
            self.jetpack_fuel = max(0, self.jetpack_fuel - JETPACK_CONSUMPTION_RATE)
            if self.jetpack_fuel <= 0:
                self.using_jetpack = False
        
        # Refill jetpack when on ground
        if self.on_ground and not self.using_jetpack:
            self.jetpack_fuel = min(MAX_JETPACK_FUEL, self.jetpack_fuel + JETPACK_REFILL_RATE)
        
        # Update position
        self.rect.x += self.velocity.x
        
        # Check for horizontal collisions
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity.x > 0:
                    self.rect.right = platform.rect.left
                elif self.velocity.x < 0:
                    self.rect.left = platform.rect.right
        
        self.rect.y += self.velocity.y
        self.on_ground = False
        
        # Check for vertical collisions
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity.y > 0:
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.velocity.y = 0
                elif self.velocity.y < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity.y = 0
        
        # Screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.on_ground = True
            self.velocity.y = 0
    
    def draw(self, surface):
        # Draw player
        pygame.draw.rect(surface, BLUE if self.facing_right else RED, self.rect)
        
        # Draw jetpack flame when active
        if self.using_jetpack:
            flame_height = random.randint(10, 20)
            flame_width = 10
            flame_x = self.rect.x - flame_width if self.facing_right else self.rect.right
            flame_y = self.rect.centery
            flame_rect = pygame.Rect(flame_x, flame_y, flame_width, flame_height)
            pygame.draw.rect(surface, YELLOW, flame_rect)
        
        # Draw weapon
        weapon_length = 20
        weapon_height = 6
        weapon_x = self.rect.right if self.facing_right else self.rect.left - weapon_length
        weapon_y = self.rect.centery - weapon_height // 2
        weapon_rect = pygame.Rect(weapon_x, weapon_y, weapon_length, weapon_height)
        pygame.draw.rect(surface, BLACK, weapon_rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed=10, size=(10, 4), color=BLACK, damage=10, spread_angle=0):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = speed
        self.damage = damage
        self.spread_angle = spread_angle
    
    def update(self):
        # Apply spread angle
        dx = self.speed * self.direction * math.cos(self.spread_angle)
        dy = self.speed * math.sin(self.spread_angle)
        
        self.rect.x += dx
        self.rect.y += dy
        
        # Remove if off screen
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.kill()

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        
        # Create texture for platform
        self.image.fill(BROWN)
        # Add top grass line
        pygame.draw.line(self.image, GREEN, (0, 0), (width, 0), 3)
        
        # Add some random dots for texture
        for _ in range(width // 5):
            dot_x = random.randint(0, width - 3)
            dot_y = random.randint(4, height - 3)
            dot_size = random.randint(1, 3)
            pygame.draw.rect(self.image, (139, 69, 19), (dot_x, dot_y, dot_size, dot_size))
        
        self.rect = self.image.get_rect(topleft=(x, y))

class WeaponPickup(pygame.sprite.Sprite):
    def __init__(self, x, y, weapon_type):
        super().__init__()
        self.image = pygame.Surface((25, 15))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=(x, y))
        self.weapon_type = weapon_type
        
        # Add pulsing effect
        self.pulse_timer = 0
        self.pulse_direction = 1
    
    def update(self):
        # Make the pickup pulse
        self.pulse_timer += 0.05 * self.pulse_direction
        if self.pulse_timer > 1:
            self.pulse_timer = 1
            self.pulse_direction = -1
        elif self.pulse_timer < 0:
            self.pulse_timer = 0
            self.pulse_direction = 1
            
        scale = 0.8 + 0.2 * self.pulse_timer
        new_width = int(25 * scale)
        new_height = int(15 * scale)
        
        center = self.rect.center
        self.image = pygame.Surface((new_width, new_height))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=center)

def create_level():
    platforms = pygame.sprite.Group()
    
    # Ground
    platforms.add(Platform(0, HEIGHT - 20, WIDTH, 20))
    
    # Platforms
    platforms.add(Platform(100, HEIGHT - 150, 200, 20))
    platforms.add(Platform(500, HEIGHT - 150, 200, 20))
    platforms.add(Platform(300, HEIGHT - 250, 200, 20))
    platforms.add(Platform(150, HEIGHT - 350, 150, 20))
    platforms.add(Platform(500, HEIGHT - 350, 150, 20))
    
    return platforms

def create_weapon_pickups():
    pickups = pygame.sprite.Group()
    
    # Add some weapon pickups
    pickups.add(WeaponPickup(200, HEIGHT - 180, 'shotgun'))
    pickups.add(WeaponPickup(400, HEIGHT - 280, 'machinegun'))
    pickups.add(WeaponPickup(600, HEIGHT - 380, 'sniper'))
    
    return pickups

def draw_health_bar(surface, x, y, health):
    BAR_WIDTH = 100
    BAR_HEIGHT = 10
    fill_width = (health / 100) * BAR_WIDTH
    outline_rect = pygame.Rect(x, y, BAR_WIDTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill_width, BAR_HEIGHT)
    
    pygame.draw.rect(surface, RED, fill_rect)
    pygame.draw.rect(surface, WHITE, outline_rect, 2)

def draw_jetpack_bar(surface, x, y, fuel):
    BAR_WIDTH = 100
    BAR_HEIGHT = 5
    fill_width = (fuel / MAX_JETPACK_FUEL) * BAR_WIDTH
    outline_rect = pygame.Rect(x, y, BAR_WIDTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill_width, BAR_HEIGHT)
    
    pygame.draw.rect(surface, YELLOW, fill_rect)
    pygame.draw.rect(surface, WHITE, outline_rect, 1)

def show_game_over(surface, winner):
    font = pygame.font.SysFont('Arial', 48)
    if winner:
        text = font.render(f'Player {winner} Wins!', True, BLACK)
    else:
        text = font.render('Game Over - Draw!', True, BLACK)
    
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
    surface.blit(text, text_rect)
    
    font_small = pygame.font.SysFont('Arial', 24)
    restart_text = font_small.render('Press R to restart or Q to quit', True, BLACK)
    restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
    surface.blit(restart_text, restart_rect)

def main():
    # Create background
    background = create_background()
    
    # Create players
    player1 = Player(100, HEIGHT - 100, BLUE, {
        'left': pygame.K_a,
        'right': pygame.K_d,
        'jump': pygame.K_w,
        'shoot': pygame.K_SPACE,
        'jetpack': pygame.K_LSHIFT,
        'switch_weapon': pygame.K_e
    })
    
    player2 = Player(WIDTH - 100, HEIGHT - 100, RED, {
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT,
        'jump': pygame.K_UP,
        'shoot': pygame.K_RCTRL,
        'jetpack': pygame.K_RSHIFT,
        'switch_weapon': pygame.K_RETURN
    })
    
    players = pygame.sprite.Group(player1, player2)
    
    # Create level
    platforms = create_level()
    
    # Create weapon pickups
    weapon_pickups = create_weapon_pickups()
    
    # Create bullets
    bullets = pygame.sprite.Group()
    
    # Game loop
    running = True
    game_over = False
    winner = None
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Restart the game
                        main()
                        return
                    elif event.key == pygame.K_q:
                        running = False
            else:
                # Handle weapon switching
                if event.type == pygame.KEYDOWN:
                    if event.key == player1.controls['switch_weapon']:
                        player1.switch_weapon()
                    if event.key == player2.controls['switch_weapon']:
                        player2.switch_weapon()
            
        # Player controls (when game is not over)
        if not game_over:
            keys = pygame.key.get_pressed()
            
            # Player 1 controls
            if player1.alive:
                dx1 = 0
                if keys[player1.controls['left']]:
                    dx1 = -1
                if keys[player1.controls['right']]:
                    dx1 = 1
                player1.move(dx1)
                
                if keys[player1.controls['jump']]:
                    player1.jump()
                
                player1.activate_jetpack(keys[player1.controls['jetpack']])
                
                if keys[player1.controls['shoot']]:
                    player1.shoot(bullets)
            
            # Player 2 controls
            if player2.alive:
                dx2 = 0
                if keys[player2.controls['left']]:
                    dx2 = -1
                if keys[player2.controls['right']]:
                    dx2 = 1
                player2.move(dx2)
                
                if keys[player2.controls['jump']]:
                    player2.jump()
                
                player2.activate_jetpack(keys[player2.controls['jetpack']])
                
                if keys[player2.controls['shoot']]:
                    player2.shoot(bullets)
            
            # Update
            players.update(platforms)
            bullets.update()
            weapon_pickups.update()
            
            # Check for weapon pickups
            for player in players:
                pickup_collision = pygame.sprite.spritecollide(player, weapon_pickups, True)
                for pickup in pickup_collision:
                    # Refill ammo for the picked up weapon
                    player.weapon_ammo[pickup.weapon_type] = WEAPONS[pickup.weapon_type]['ammo']
                    player.score += 5
            
            # Collision detection (bullets hitting players)
            for bullet in bullets:
                player_hit = pygame.sprite.spritecollideany(bullet, players)
                if player_hit:
                    # Only damage if bullet doesn't belong to this player
                    is_player1_bullet = bullet.rect.x < WIDTH / 2 and player1.facing_right or bullet.rect.x > WIDTH / 2 and not player1.facing_right
                    is_player2_bullet = bullet.rect.x > WIDTH / 2 and player2.facing_right or bullet.rect.x < WIDTH / 2 and not player2.facing_right
                    
                    if player_hit == player1 and not is_player1_bullet:
                        player1.take_damage(bullet.damage)
                        bullet.kill()
                        if not player1.alive and player2.alive:
                            winner = "2"
                            game_over = True
                            player2.score += 50
                    
                    elif player_hit == player2 and not is_player2_bullet:
                        player2.take_damage(bullet.damage)
                        bullet.kill()
                        if not player2.alive and player1.alive:
                            winner = "1"
                            game_over = True
                            player1.score += 50
            
            # Check if both players are dead (draw)
            if not player1.alive and not player2.alive:
                game_over = True
            
            # Periodically spawn new weapon pickups
            if random.random() < 0.005:  # 0.5% chance per frame
                x = random.randint(50, WIDTH - 50)
                y = random.randint(50, HEIGHT - 100)
                weapon_type = random.choice(['shotgun', 'machinegun', 'sniper'])
                weapon_pickups.add(WeaponPickup(x, y, weapon_type))
        
        # Draw everything
        screen.blit(background, (0, 0))
        
        # Draw platforms
        platforms.draw(screen)
        
        # Draw weapon pickups
        weapon_pickups.draw(screen)
        
        # Draw players (custom draw method)
        for player in players:
            if player.alive:
                player.draw(screen)
        
        # Draw bullets
        bullets.draw(screen)
        
        # Draw health bars and weapon info
        # Player 1
        draw_health_bar(screen, 10, 10, player1.health)
        draw_jetpack_bar(screen, 10, 25, player1.jetpack_fuel)
        
        # Player 2
        draw_health_bar(screen, WIDTH - 110, 10, player2.health)
        draw_jetpack_bar(screen, WIDTH - 110, 25, player2.jetpack_fuel)
        
        # Show score and weapon info
        font = pygame.font.SysFont('Arial', 18)
        
        # Player 1 info
        score1_text = font.render(f'P1: {player1.score}', True, BLACK)
        weapon1_text = font.render(f'Weapon: {player1.current_weapon}', True, BLACK)
        ammo1_text = font.render(f'Ammo: {"∞" if player1.weapon_ammo[player1.current_weapon] == -1 else player1.weapon_ammo[player1.current_weapon]}', True, BLACK)
        
        screen.blit(score1_text, (15, 35))
        screen.blit(weapon1_text, (15, 55))
        screen.blit(ammo1_text, (15, 75))
        
        # Player 2 info
        score2_text = font.render(f'P2: {player2.score}', True, BLACK)
        weapon2_text = font.render(f'Weapon: {player2.current_weapon}', True, BLACK)
        ammo2_text = font.render(f'Ammo: {"∞" if player2.weapon_ammo[player2.current_weapon] == -1 else player2.weapon_ammo[player2.current_weapon]}', True, BLACK)
        
        screen.blit(score2_text, (WIDTH - 100, 35))
        screen.blit(weapon2_text, (WIDTH - 150, 55))
        screen.blit(ammo2_text, (WIDTH - 100, 75))
        
        # Controls info
        if not game_over:
            controls_text = font.render('P1: WASD + SPACE + SHIFT + E | P2: Arrows + RCTRL + RSHIFT + RETURN', True, BLACK)
            screen.blit(controls_text, (WIDTH // 2 - 250, HEIGHT - 20))
        
        if game_over:
            show_game_over(screen, winner)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 

