import pygame
import sys

# 初始化 Pygame
pygame.init()

# 游戏常量
WINDOW_SIZE = 800
BOARD_SIZE = 15
GRID_SIZE = WINDOW_SIZE // (BOARD_SIZE + 1)
PIECE_RADIUS = GRID_SIZE // 2 - 2

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (205, 133, 63)

# 创建窗口
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("五子棋")

class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = 'black'
        self.game_over = False
    
    def draw_board(self):
        screen.fill(BROWN)
        # 绘制棋盘线
        for i in range(BOARD_SIZE):
            # 横线
            pygame.draw.line(screen, BLACK,
                           (GRID_SIZE, (i + 1) * GRID_SIZE),
                           (WINDOW_SIZE - GRID_SIZE, (i + 1) * GRID_SIZE))
            # 竖线
            pygame.draw.line(screen, BLACK,
                           ((i + 1) * GRID_SIZE, GRID_SIZE),
                           ((i + 1) * GRID_SIZE, WINDOW_SIZE - GRID_SIZE))
        
        # 绘制棋子
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] == 'black':
                    pygame.draw.circle(screen, BLACK,
                                     ((j + 1) * GRID_SIZE, (i + 1) * GRID_SIZE),
                                     PIECE_RADIUS)
                elif self.board[i][j] == 'white':
                    pygame.draw.circle(screen, WHITE,
                                     ((j + 1) * GRID_SIZE, (i + 1) * GRID_SIZE),
                                     PIECE_RADIUS)
    
    def place_piece(self, row, col):
        if self.board[row][col] is None and not self.game_over:
            self.board[row][col] = self.current_player
            if self.check_win(row, col):
                self.game_over = True
                return f"{self.current_player} 赢了！"
            self.current_player = 'white' if self.current_player == 'black' else 'black'
            return None
        return "此位置已有棋子"

    def check_win(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            # 正向检查
            for i in range(1, 5):
                new_row, new_col = row + dx * i, col + dy * i
                if not (0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE):
                    break
                if self.board[new_row][new_col] != self.current_player:
                    break
                count += 1
            # 反向检查
            for i in range(1, 5):
                new_row, new_col = row - dx * i, col - dy * i
                if not (0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE):
                    break
                if self.board[new_row][new_col] != self.current_player:
                    break
                count += 1
            if count >= 5:
                return True
        return False

def main():
    game = GomokuGame()
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                x, y = event.pos
                col = round((x - GRID_SIZE) / GRID_SIZE)
                row = round((y - GRID_SIZE) / GRID_SIZE)
                
                if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                    result = game.place_piece(row, col)
                    if result:
                        print(result)

        game.draw_board()
        
        if game.game_over:
            text = font.render(f"{('白方' if game.current_player == 'white' else '黑方')}获胜！", True, BLACK)
            screen.blit(text, (WINDOW_SIZE // 2 - 100, 20))
        else:
            text = font.render(f"当前玩家：{('白方' if game.current_player == 'white' else '黑方')}", True, BLACK)
            screen.blit(text, (WINDOW_SIZE // 2 - 100, 20))

        pygame.display.flip()

if __name__ == "__main__":
    main() 