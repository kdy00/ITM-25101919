# weather.py

import urllib.request
import re

SEOUL_ZONE_CODE = "1100000000"
SEOUL_LOCATION_NAME = "서울특별시"

def get_current_weather(zone_code=SEOUL_ZONE_CODE):
    """실시간 날씨 정보를 가져옵니다."""
    try:
        url = f"https://www.weather.go.kr/w/rss/dfs/hr1-forecast.do?zone={zone_code}"
        xml = urllib.request.urlopen(url, timeout=5).read().decode("utf-8")
    except Exception:
        return None, SEOUL_LOCATION_NAME

    temp_match = re.search(r"<temp>(.*?)</temp>", xml)
    wf_match = re.search(r"<wfKor>(.*?)</wfKor>", xml)
    
    current_temp = int(float(temp_match.group(1))) if temp_match else 20
    current_wf = wf_match.group(1).strip() if wf_match else "맑음"
    
    current_data = {
        'temp': current_temp,
        'wf': current_wf,
    }
            
    return current_data, SEOUL_LOCATION_NAME

# 산책 부적합 판단 기준 (수정 가능)
TEMP_TOO_HOT = 28.0 
TEMP_TOO_COLD = 5.0
BAD_WEATHER = ['비', '눈', '호우', '강풍', '태풍'] 

def check_walk_suitability(weather_data, location_name):
    """ 날씨 데이터를 분석하여 산책 가능 여부를 판단합니다. """
    
    if weather_data is None:
        return f"현재 {location_name}의 날씨 정보를 가져올 수 없습니다. 안전에 유의하세요."

    temp = weather_data['temp']
    wf = weather_data['wf'] 
    reason = []

    # 1. 온도 체크
    if temp >= TEMP_TOO_HOT:
        reason.append(f"온도가 {temp}°C로 너무 높습니다. 열사병에 주의하세요.")
    elif temp <= TEMP_TOO_COLD:
        reason.append(f"온도가 {temp}°C로 너무 낮습니다. 동상에 주의하세요.")

    # 2. 날씨 상태 체크
    for bad in BAD_WEATHER:
        if bad in wf:
            reason.append(f"날씨 상태가 '{wf}'입니다. 실내 놀이를 추천합니다.")
            break
            
    # 3. 최종 판단
    if reason:
        result = f"🚨 **산책 부적합** 🚨\n({location_name} 현재 기온: {temp}°C, 날씨: {wf})"
        result += "\n\n❌ 부적합 이유:\n" + "\n".join(f"- {r}" for r in reason)
        result += "\n\n대신 실내에서 할 수 있는 활동을 찾아보세요!"
    else:
        result = f"✅ **산책 적합** ✅\n({location_name} 현재 기온: {temp}°C, 날씨: {wf})"
        result += "\n\n오늘도 즐거운 산책 되세요! 산책 시간을 조정하여 더 안전하게 즐기세요."

    return result