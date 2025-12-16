# health_manager.py

# ==============================================================================
# 2. 강아지 사람 나이 변환 로직
# ==============================================================================

def get_dog_size_multiplier(size):
    """ 강아지 크기에 따른 연간 나이 증가 곱수를 반환합니다. """
    if size == '소형':  
        return 4
    elif size == '중형': 
        return 5
    elif size == '대형': 
        return 6
    else:
        return 5 

def calculate_human_age(dog_age, dog_size):
    """ 강아지 나이와 크기를 입력받아 사람 나이로 환산합니다. """
    
    if dog_age < 1:
        return "강아지 나이는 최소 1살 이상이어야 합니다."

    if dog_age == 1:
        human_age = 15 
    elif dog_age == 2:
        human_age = 24 
    else:
        multiplier = get_dog_size_multiplier(dog_size)
        human_age = 24 + (dog_age - 2) * multiplier

    return f"🐶 {dog_size} 강아지의 실제 나이 {dog_age}세는 사람 나이로 약 {human_age}세 입니다."

def handle_age_conversion():
    """ 나이 계산 기능을 실행하고 결과를 출력합니다. (main.py에서 호출) """
    print("\n[2. 강아지 사람 나이 계산]")
    try:
        age_input = int(input("강아지의 실제 나이(만 나이, 정수)를 입력하세요: "))
        size_input = input("강아지의 크기(소형/중형/대형)를 입력하세요: ").strip()

        if size_input not in ['소형', '중형', '대형']:
            print("❌ 오류: 크기는 '소형', '중형', '대형' 중 하나로 입력해 주세요.")
            return

        result = calculate_human_age(age_input, size_input)
        print(f"\n{result}")
        
    except ValueError:
        print("\n❌ 오류: 나이는 정수(숫자)로 입력해 주세요.")
    except Exception as e:
        print(f"\n❌ 오류가 발생했습니다: {e}")

# ==============================================================================
# 3. 소중대형견 별 비만 여부 로직
# ==============================================================================

# 크기별 표준 체중 범위 정의 (정상 범위)
STANDARD_WEIGHTS = {
    '소형': {'min': 4.0, 'max': 9.0},  
    '중형': {'min': 10.0, 'max': 24.0}, 
    '대형': {'min': 25.0, 'max': 50.0} 
}
OVERWEIGHT_THRESHOLD = 0.10 # 정상 최대치에서 10% 초과 시 '비만'으로 판정

def check_obesity(current_weight, dog_size):
    """ 강아지의 크기와 현재 체중을 비교하여 비만 여부를 판단합니다. """
    
    if dog_size not in STANDARD_WEIGHTS:
        return "오류: 알 수 없는 강아지 크기입니다."

    standard = STANDARD_WEIGHTS[dog_size]
    min_w = standard['min']
    max_w = standard['max']

    if current_weight < min_w:
        verdict = "저체중"
        advice = f"적정 체중({min_w}kg)보다 낮습니다. 영양 상태와 활동량을 점검해 보세요."
    elif min_w <= current_weight <= max_w:
        verdict = "정상"
        advice = "아주 좋습니다! 현재 체중을 잘 유지하고 계시네요."
    else:
        over_percentage = (current_weight - max_w) / max_w
        
        if over_percentage > OVERWEIGHT_THRESHOLD:
            verdict = "비만"
            advice = f"체중이 정상 범위({max_w}kg)를 {over_percentage:.1%} 초과했습니다. 식단 조절과 산책 시간을 늘려야 합니다."
        else:
            verdict = "과체중"
            advice = f"체중이 정상 범위({max_w}kg)를 약간 초과했습니다. 간식량을 줄이고 꾸준히 활동해 주세요."
            
    return f"🩺 비만도 판정: **{verdict}**\n- 적정 체중 범위: {min_w}kg ~ {max_w}kg\n- 현재 체중: {current_weight}kg\n- 조언: {advice}"

def handle_obesity_check():
    """ 비만도 측정 기능을 실행하고 결과를 출력합니다. (main.py에서 호출) """
    print("\n[3. 소중대형견 별 비만 여부 측정]")
    try:
        weight_input = float(input("강아지의 현재 체중(kg, 소수점 가능)을 입력하세요: "))
        size_input = input("강아지의 크기(소형/중형/대형)를 입력하세요: ").strip()

        if size_input not in STANDARD_WEIGHTS:
            print("❌ 오류: 크기는 '소형', '중형', '대형' 중 하나로 입력해 주세요.")
            return

        result = check_obesity(weight_input, size_input)
        print(f"\n{result}")

    except ValueError:
        print("\n❌ 오류: 체중은 숫자로 입력해 주세요.")
    except Exception as e:
        print(f"\n❌ 오류가 발생했습니다: {e}")