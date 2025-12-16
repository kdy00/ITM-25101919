# ITM-25101919
🐶 PetDogManager-Chatbot: 반려견 종합 관리 챗봇  
📌 프로젝트 개요 (Project Overview)  
본 프로젝트는 반려견의 건강 및 안전 관리, 그리고 사용자에게 재미있는 경험을 제공하기 위해 설계된 Python 콘솔 기반의 통합 챗봇 솔루션입니다. 시스템은 main.py를 중심으로 모듈화되어 있으며, 특히 Pygame을 활용하여 산책 환경을 시뮬레이션한 미니게임 기능을 성공적으로 통합하여 인터랙티브한 경험을 제공합니다.

✨ 주요 기능 (Key Features)  
1. 실시간 산책 적합성 분석,	weather.py, 외부 기상청 API 연동을 가정하여 현재 기온과 날씨(비, 눈, 강풍 등)를 분석합니다. 반려견에게 위험한 환경(고온, 저온, 악천후)일 경우 산책 부적합 판정을 내리고 안전 조언을 제공합니다.
2. 강아지 나이 환산, health_manager.py, 강아지의 크기(소형/중형/대형)별 성장 속도 차이를 반영하여 사람 나이로 환산하는 알고리즘을 구현했습니다
3. 비만도 측정 및 조언,	health_manager.py,	크기별 표준 체중을 기준으로 현재 체중의 정상, 과체중, 비만 여부를 정밀 판정합니다. 적절한 식단 및 활동량 조언을 출력합니다.
4. Pygame 미니게임 (장애물 회피),	game_manager.py, 구글 공룡 게임을 모티브로 한 산책 시뮬레이션 게임입니다.

🛠️ 개발 환경 및 기술 스택 (Tech Stack)    
언어: Python 3.x  
GUI/게임 라이브러리: pygame  
모듈 구성: 모듈화 기반의 OOP (Object-Oriented Programming) 설계 적용.  
버전 관리: Git & GitHub  

📂 프로젝트 구조 (Project Structure)  
```
PetDogManager/
├── main.py              # 챗봇 메뉴, 루프 제어
├── health_manager.py    # 건강(나이, 비만도) 로직
├── weather.py           # 날씨 및 산책 적합성 로직
├── game_manager.py      # Pygame 게임 로직 (가장 복잡한 모듈)
└── assets/              # 게임 이미지 리소스
    ├── dog.png
    ├── obstacle_1.png 
    └── obstacle_2.png
```

🚀 설치 및 실행 방법 (Getting Started)  
1. 필수 라이브러리 설치  
터미널에서 pygame을 설치합니다.  
pip install pygame  

2. 저장소 복제 (Clone Repository)  
Git을 사용하여 프로젝트 파일을 로컬 환경으로 복제합니다.  
git clone [GitHub 저장소 URL]  
cd PetDogManager-Chatbot  

3. 챗봇 실행  
프로젝트 루트 디렉터리에서 main.py 파일을 실행합니다.  
python main.py  

🕹️ 미니게임 조작법  
게임을 시작하기 전에 스페이스바를 눌러야 합니다.  
키,동작  
Spacebar 또는 ↑,게임 시작 / 점프  
Enter,게임 오버 화면에서 메인 메뉴로 복귀  
Esc,게임 강제 종료 및 메인 메뉴 복귀  

💻 개발 노트 및 트러블슈팅 (Developer Notes)  
Pygame 안전 종료: game_manager.py는 run_mini_game() 함수 내에서 pygame.init()으로 시작하고 pygame.quit()으로 종료함으로써, 메인 main.py 콘솔 프로그램에 영향을 주지 않고 게임 기능만 독립적으로 실행 및 종료할 수 있도록 설계되었습니다.
장애물 난이도: random.randint(0, int(FPS * 0.8)) 공식을 사용하여 게임 속도(game_speed)에 따라 장애물 생성 빈도가 동적으로 증가하도록 구현했습니다.

👨‍💻 개발자 정보 (Author)  
이름: 김동연
