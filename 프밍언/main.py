# main.py

import time
# Pygame 관련 함수가 포함된 모듈을 불러옵니다.
from game_manager import run_mini_game 
# 다른 기능 모듈을 불러옵니다.
from health_manager import handle_age_conversion, handle_obesity_check
from weather import get_current_weather, check_walk_suitability 

def display_menu():
    """ 메인 메뉴를 출력합니다. """
    print("\n==============================================")
    print("        🐶 반려견 매니저 챗봇 🐶")
    print("==============================================")
    print("1. 실시간 날씨 및 산책 가능 여부 확인")
    print("2. 강아지 사람 나이 계산")
    print("3. 소/중/대형견 별 비만 여부 측정")
    print("4. 미니게임 - 산책 장애물 회피 게임 시작")
    print("5. 종료")
    print("----------------------------------------------")


def handle_weather_and_walk():
    """ 날씨 데이터를 가져와 산책 적합성을 확인합니다. """
    print("\n[1. 실시간 날씨 및 산책 가능 여부 확인]")
    
    weather_data, location_name = get_current_weather() 
    
    print(check_walk_suitability(weather_data, location_name))
    


def main():
    """ 챗봇의 메인 루프를 실행합니다. """
    while True:
        display_menu()
        choice = input("원하는 기능의 번호를 입력하세요: ").strip()

        if choice == '1':
            handle_weather_and_walk()
        elif choice == '2':
            handle_age_conversion()
        elif choice == '3':
            handle_obesity_check()
        elif choice == '4':
            # Pygame 게임 실행: run_mini_game 내부에서 init/quit을 책임집니다.
            run_mini_game() 
            print("\n(게임을 종료하고 메인 메뉴로 돌아왔습니다.)")

        elif choice == '5':
            print("\n매니저를 종료합니다. 오늘도 행복한 하루 되세요!")
            break
        else:
            print("\n❌ 잘못된 번호입니다. 1부터 5 사이의 숫자를 입력해 주세요.")
        
        # 게임을 제외한 기능 수행 후 잠시 대기
        if choice in ['1', '2', '3']:
            input("\n(엔터를 눌러 메인 메뉴로 돌아갑니다...)")
        
if __name__ == "__main__":
    # main.py에서는 pygame.init()을 호출하지 않아, 게임 종료 후 안전하게 복귀합니다.
    main()