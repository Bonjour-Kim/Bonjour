import os
import re
from collections import defaultdict

# 카카오톡 대화 분석 함수
def analyze_kakao_chat(directory):
    # 파일 읽기 및 데이터 구조 초기화
    message_pattern = re.compile(r"^(\d{4}\. \d{1,2}\. \d{1,2}\. \d{2}:\d{2}), (.*?): (.+)$")
    user_data = defaultdict(lambda: {"messages": [], "long_messages": 0, "build_ups": 0})
    
    # 파일 순회
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                previous_user = None
                consecutive_count = 0

                for line in file:
                    match = message_pattern.match(line.strip())
                    if match:
                        timestamp, user, message = match.groups()
                        user_data[user]["messages"].append(message)
                        
                        # 1. 빌드업 계산
                        if user == previous_user:
                            consecutive_count += 1
                        else:
                            if consecutive_count >= 3:
                                user_data[previous_user]["build_ups"] += 1
                            consecutive_count = 1
                        previous_user = user
                        
                        # 2. 메시지 길이 (롱패스) 계산
                        if len(message) < 100:
                            user_data[user]["long_messages"] += len(message)
                
                # 마지막 사용자 빌드업 체크
                if consecutive_count >= 3:
                    user_data[previous_user]["build_ups"] += 1

    # 결과 계산
    build_up_ranking = []
    long_pass_ranking = []

    for user, data in user_data.items():
        total_messages = len(data["messages"])
        if total_messages > 0:
            build_up_ratio = data["build_ups"] / total_messages
            build_up_ranking.append((user, build_up_ratio))
        
        if data["long_messages"] > 0:
            average_length = data["long_messages"] / total_messages
            long_pass_ranking.append((user, average_length))
    
    # 정렬
    build_up_ranking.sort(key=lambda x: x[1], reverse=True)
    long_pass_ranking.sort(key=lambda x: x[1], reverse=True)

    return build_up_ranking, long_pass_ranking

# 결과 출력
if __name__ == "__main__":
    chat_dir = r"C:\Users\Bongju Kim\OneDrive\Coding\Kakaotalk_Chat_고려대 축구방"
    build_up_ranking, long_pass_ranking = analyze_kakao_chat(chat_dir)
    
    print("1. 빌드업 비율 순위")
    for rank, (user, ratio) in enumerate(build_up_ranking, 1):
        print(f"{rank}. {user}: {ratio:.2%}")

    print("\n2. 평균 메시지 길이 순위 (100글자 미만)")
    for rank, (user, avg_length) in enumerate(long_pass_ranking, 1):
        print(f"{rank}. {user}: {avg_length:.2f}자")