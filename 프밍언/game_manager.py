# game_manager.py

import pygame
import random
import os
import time

# --- 1. 게임 상수 설정 ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# 색상 및 FPS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 150, 0) 
FPS = 60

# 리소스 관련 상수
ASSETS_PATH = 'assets'
GROUND_HEIGHT = 30 
DOG_WIDTH, DOG_HEIGHT = 80, 80 
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50 

# 이미지 로드 변수는 함수 내에서 초기화될 예정입니다.
DOG_IMAGE = None
OBSTACLE_IMAGES = []
IMAGE_LOADED = False
FONT = None
SCREEN = None # 화면 객체도 함수 내에서 초기화될 예정입니다.

def load_game_assets():
    """ 필요한 모든 이미지와 폰트를 로드하고 전역 변수에 할당합니다. """
    global DOG_IMAGE, OBSTACLE_IMAGES, IMAGE_LOADED, FONT
    
    try:
        # 폰트 로드
        FONT = pygame.font.Font(None, 30)
        
        # 🐕 강아지 이미지 로드
        DOG_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'dog.png'))
        DOG_IMAGE = pygame.transform.scale(DOG_IMAGE, (DOG_WIDTH, DOG_HEIGHT))
        
        # 🚧 장애물 이미지 로드 및 리스트 생성
        OBSTACLE_IMAGES.clear() # 혹시 모를 중복 로드 방지
        
        # 1. 웅덩이
        img_puddle = pygame.image.load(os.path.join(ASSETS_PATH, 'obstacle_1.png'))
        
        # 2. 쓰레기
        img_trash = pygame.image.load(os.path.join(ASSETS_PATH, 'obstacle_2.png'))
        
        OBSTACLE_IMAGES.append(pygame.transform.scale(img_puddle, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT)))
        OBSTACLE_IMAGES.append(pygame.transform.scale(img_trash, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT)))
        
        IMAGE_LOADED = True
    except pygame.error as e:
        print(f"🚨 이미지 로드 오류: {e}. Placeholder를 사용합니다. PNG 파일이 assets 폴더에 있는지 확인하세요.")
        IMAGE_LOADED = False

# --- 3. 클래스 정의 --- 

class Dog:
    """ 플레이어 (강아지) 클래스 """
    def __init__(self):
        self.image = DOG_IMAGE if IMAGE_LOADED else None
        self.rect = pygame.Rect(50, SCREEN_HEIGHT - GROUND_HEIGHT - DOG_HEIGHT, DOG_WIDTH, DOG_HEIGHT)
        self.is_jumping = False
        self.jump_vel = 0
        self.gravity = 1
        self.jump_power = 18 

    def update(self):
        if self.is_jumping:
            self.rect.y -= self.jump_vel
            self.jump_vel -= self.gravity
            if self.rect.y >= SCREEN_HEIGHT - GROUND_HEIGHT - DOG_HEIGHT:
                self.rect.y = SCREEN_HEIGHT - GROUND_HEIGHT - DOG_HEIGHT
                self.is_jumping = False
                self.jump_vel = 0

    def draw(self, screen):
        if IMAGE_LOADED: screen.blit(self.image, self.rect)
        else: pygame.draw.rect(screen, (255, 255, 0), self.rect)

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_vel = self.jump_power

class Obstacle:
    """ 장애물 클래스 """
    def __init__(self, speed):
        self.type = random.randint(0, len(OBSTACLE_IMAGES) - 1) if IMAGE_LOADED else 0
        self.image = OBSTACLE_IMAGES[self.type] if IMAGE_LOADED else None
        self.rect = pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT - OBSTACLE_HEIGHT, 
                                OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        if IMAGE_LOADED: screen.blit(self.image, self.rect)
        else: pygame.draw.rect(screen, (255, 0, 0), self.rect)

# --- 4. 게임 함수 ---

def run_mini_game():
    """ 챗봇의 '4. 미니게임' 기능 실행 함수 """
    
    # 🌟 1. 함수 시작 시 Pygame 초기화 및 화면 설정 🌟
    pygame.init() 
    global SCREEN, FONT # 전역 변수 사용을 선언
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("반려견 산책 게임")
    load_game_assets() # 이미지 및 폰트 로드
    
    running = True
    clock = pygame.time.Clock()
    
    dog = Dog()
    obstacles = []
    game_speed = 0 
    score = 0
    game_started = False
    
    def generate_obstacle():
        # 장애물 생성 빈도 조절
        if random.randint(0, 100) < 5: 
            obstacles.append(Obstacle(game_speed))

    def draw_ground(screen):
        pygame.draw.line(screen, GREEN, (0, SCREEN_HEIGHT - GROUND_HEIGHT), 
                         (SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT), GROUND_HEIGHT)

    def draw_score(screen):
        if FONT:
            score_text = FONT.render(f"Score: {score // 10}", True, BLACK) 
            screen.blit(score_text, (SCREEN_WIDTH - 150, 10))
        
    def draw_start_message(screen):
        if FONT:
            start_text = FONT.render("Press SPACE to START", True, (50, 50, 50))
            screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))

    # 게임 루프
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    
                    if not game_started:
                        game_started = True
                        game_speed = 7 
                        dog.jump() 
                    else:
                        dog.jump()
                        
                if event.key == pygame.K_ESCAPE:
                    running = False 

        # --- 업데이트 ---
        if game_started:
            score += 1
            if score % 200 == 0:
                game_speed += 0.5 

            dog.update()
            
            # 장애물 생성 및 업데이트 (오류 처리 및 빈도 조절 적용)
            if random.randint(0, int(FPS * 0.8)) < game_speed: 
                generate_obstacle()

            for obstacle in list(obstacles):
                obstacle.update()
                
                if obstacle.rect.right < 0:
                    obstacles.remove(obstacle)
                
                # 충돌 감지
                if dog.rect.colliderect(obstacle.rect):
                    running = False 

        # --- 그리기 ---
        SCREEN.fill(WHITE)
        draw_ground(SCREEN)
        dog.draw(SCREEN)

        for obstacle in obstacles:
            obstacle.draw(SCREEN)

        draw_score(SCREEN)
        
        if not game_started:
            draw_start_message(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    # --- 게임 오버 및 복귀 처리 ---
    final_score = score // 10
    
    # 1. 게임 오버 메시지 출력
    if FONT:
        SCREEN.fill(WHITE)
        game_over_text = FONT.render("GAME OVER (Press ENTER to return)", True, BLACK)
        score_final_text = FONT.render(f"Final Score: {final_score}", True, BLACK)
        
        SCREEN.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
        SCREEN.blit(score_final_text, (SCREEN_WIDTH // 2 - score_final_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))
        pygame.display.flip()
    
    # 2. 콘솔에 최종 점수 출력
    print(f"\n==============================================")
    print(f"✨ 미니게임 종료! 최종 산책 점수: {final_score}점 ✨")
    print("==============================================")
    
    # 3. 사용자 입력 대기 및 창 닫기
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                waiting = False
        time.sleep(0.1) 
    
    # 🌟 4. Pygame 시스템 완전히 종료 🌟
    pygame.quit() 
    # 함수 종료. main.py의 while True 루프로 복귀함.