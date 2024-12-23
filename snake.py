import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 游戏常量
WINDOW_SIZE = 800
GRID_SIZE = 20
GRID_COUNT = WINDOW_SIZE // GRID_SIZE

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 方向定义
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("贪吃蛇")
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        # 蛇的初始位置和方向
        self.snake = [(GRID_COUNT//2, GRID_COUNT//2)]
        self.direction = RIGHT
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        self.speed = 10

    def generate_food(self):
        while True:
            food = (random.randint(0, GRID_COUNT-1), random.randint(0, GRID_COUNT-1))
            if food not in self.snake:
                return food

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()

    def update(self):
        if self.game_over:
            return

        # 移动蛇
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        # 检查碰撞
        if (new_head in self.snake or 
            new_head[0] < 0 or new_head[0] >= GRID_COUNT or 
            new_head[1] < 0 or new_head[1] >= GRID_COUNT):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # 检查是否吃到食物
        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
            self.speed = min(20, 10 + self.score // 5)  # 随着分数增加速度
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill(BLACK)

        # 画蛇
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN,
                           (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE,
                            GRID_SIZE-1, GRID_SIZE-1))

        # 画食物
        pygame.draw.rect(self.screen, RED,
                        (self.food[0]*GRID_SIZE, self.food[1]*GRID_SIZE,
                         GRID_SIZE-1, GRID_SIZE-1))

        # 修改显示文字的部分，使用系统默认中文字体
        try:
            font = pygame.font.Font("simhei.ttf", 36)  # 使用黑体
        except:
            font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 36)  # 备选方案：微软雅黑
        
        score_text = font.render(f'分数: {self.score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            game_over_text = font.render('游戏结束! 按R重新开始', True, WHITE)
            text_rect = game_over_text.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2))
            self.screen.blit(game_over_text, text_rect)

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(self.speed)

if __name__ == "__main__":
    game = SnakeGame()
    game.run() 