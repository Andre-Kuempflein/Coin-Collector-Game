import pygame
from .models import LevelConfig

class CoinCollectorGame:
    def __init__(self, config: LevelConfig, fps: int, debug: bool):
        pygame.init()
        self.config = config
        self.fps = fps
        self.debug = debug
        
        # Fenster initialisieren
        self.screen = pygame.display.set_mode((config.width, config.height))
        pygame.display.set_caption("Coin Collector")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)

        # Spieler-Rechteck erstellen
        self.player_size = 30
        self.player_rect = pygame.Rect(
            config.player_start[0], 
            config.player_start[1], 
            self.player_size, 
            self.player_size
        )
        self.player_speed = 5
        self.score = 0
        
        # Hindernisse und Münzen laden
        self.walls = [pygame.Rect(w.x, w.y, w.w, w.h) for w in config.walls]
        self.coins = config.coins.copy()

    def run(self):
        running = True
        while running:
            self.clock.tick(self.fps)
            
            # Events abfragen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # Bewegung und Kollision
            self.handle_movement()
            self.handle_coin_collection()

            # Zeichnen
            self.draw()

            # Siegbedingung
            if not self.coins:
                pygame.display.set_caption("Alle Muenzen gesammelt! Druecke ESC zum Beenden.")

        pygame.quit()

    def handle_movement(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        
        # Eingabe prüfen
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]: dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy += 1

        # Diagonalgeschwindigkeit normalisieren
        # Wir nutzen den Faktor 1/Wurzel(2), damit man diagonal nicht schneller ist.
        if dx != 0 and dy != 0:
            factor = 0.7071
            dx *= factor
            dy *= factor

        # X-Bewegung mit Wand-Check
        if dx != 0:
            self.player_rect.x += dx * self.player_speed
            for wall in self.walls:
                if self.player_rect.colliderect(wall):
                    if dx > 0: self.player_rect.right = wall.left
                    else: self.player_rect.left = wall.right

        # Y-Bewegung mit Wand-Check
        if dy != 0:
            self.player_rect.y += dy * self.player_speed
            for wall in self.walls:
                if self.player_rect.colliderect(wall):
                    if dy > 0: self.player_rect.bottom = wall.top
                    else: self.player_rect.top = wall.bottom

    def handle_coin_collection(self):
        for coin in self.coins[:]:
            # Kollision: Wenn der Mittelpunkt der Münze im Spieler-Rechteck liegt
            if self.player_rect.collidepoint(coin.x, coin.y):
                self.coins.remove(coin)
                self.score += 1

    def draw(self):
        self.screen.fill((30, 30, 30))

        # Hindernisse zeichnen
        for wall in self.walls:
            pygame.draw.rect(self.screen, (100, 100, 100), wall)
            if self.debug:
                pygame.draw.rect(self.screen, (255, 0, 0), wall, 2)

        # Münzen zeichnen (Kreise)
        for coin in self.coins:
            pygame.draw.circle(
                self.screen, (255, 215, 0), (int(coin.x), int(coin.y)), int(coin.r)
            )

        # Spieler zeichnen (blaues Rechteck)
        pygame.draw.rect(self.screen, (0, 200, 255), self.player_rect)
        if self.debug:
            pygame.draw.rect(self.screen, (0, 255, 0), self.player_rect, 2)

        # HUD oben anzeigen
        hud_text = f"Punkte: {self.score} | Verbleibend: {len(self.coins)}"
        text_surface = self.font.render(hud_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (10, 10))

        pygame.display.flip()