import pygame
import config
from game_manager import GameManger
from utils.draw_test import draw_text
pygame.init()  # 是 Pygame 库中用于初始化所有导入的 Pygame 模块的函数
pygame.mixer.init()#初始化声音
pygame.font.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

ico=pygame.image.load("static/images/maze.png").convert()
pygame.display.set_icon(ico)
pygame.display.set_caption("汽车迷宫")


pygame.mixer.music.load("static/sounds/bgm.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

game_manager = GameManger(screen)

running = True
success_time=-1#-1没有获胜否则表示获胜的时刻
success_finished=False
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        elif success_finished and evect.type == pygame.KEYDOWN:#如果已经通关了则按任意键结束
            running=False
    if success_finished:
        screen.fill("black")
        draw_text(screen,"Win!",200,config.SCREEN_WIDTH/2,config.SCREEN_HEIGHT/2)
    else:
        if success_time >=0:
            if pygame.time.get_ticks()-success_time>2000:
                has_next=game_manager.next_level()
                if not has_next:#没有下一关
                    success_finished=True
                    continue
                success_time=-1
        screen.fill("black")
        if game_manager.update():
            success_time=pygame.time.get_ticks()
    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
