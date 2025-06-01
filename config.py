# Конфигурационные параметры для игры "Змейка"

import pygame

# ============ ОСНОВНЫЕ НАСТРОЙКИ ============
class Settings:
    # Размеры окна
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_TITLE = "Змейка"
    
    # Настройки игры
    FPS = 60
    GAME_SPEED = 15  # Скорость змейки (чем больше, тем быстрее)
    BLOCK_SIZE = 20  # Размер одного блока змейки/еды
    
    # Цвета (R, G, B)
    COLORS = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "BACKGROUND": (30, 30, 30),
        "GRID": (50, 50, 50)
    }
    
    # Настройки змейки
    SNAKE_COLOR = COLORS["GREEN"]
    SNAKE_HEAD_COLOR = COLORS["BLUE"]
    
    # Настройки еды
    FOOD_COLOR = COLORS["RED"]
    FOOD_EFFECT_DURATION = 5000  # Длительность эффектов еды в мс
    
    # Настройки интерфейса
    FONT_NAME = "comicsansms"
    SCORE_FONT_SIZE = 35
    MENU_FONT_SIZE = 50
    GAME_OVER_FONT_SIZE = 45
    
    # Настройки сетки (опционально)
    GRID_VISIBLE = True
    GRID_COLOR = COLORS["GRID"]
    GRID_SPACING = BLOCK_SIZE

# ============ ИНИЦИАЛИЗАЦИЯ PYGAME ============
def init_pygame():
    pygame.init()
    pygame.display.set_caption(Settings.SCREEN_TITLE)
    screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    return screen, clock

# ============ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ ============
class GameRules:
    # Правила игры
    START_LENGTH = 3  # Начальная длина змейки
    GROW_PER_FOOD = 1  # На сколько блоков растёт змейка
    TELEPORT_BORDERS = False  # Может ли змейка телепортироваться через границы