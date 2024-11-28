import os
import re
from collections import Counter

# 단어 빈도 분석 함수
def analyze_word_frequency(directory):
    # 제외할 단어 목록
    exclude_words = {"이모티콘", "사진", "샵검색", "삭제된", "메시지입니다"}
    word_pattern = re.compile(r"[가-힣]{2,}")  # 2자 이상 한글 단어 패턴
    word_counter = Counter()

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    # 메시지 내용만 추출
                    if ", " in line and " : " in line:
                        try:
                            message = line.strip().split(" : ", 1)[1]
                            words = word_pattern.findall(message)
                            # 제외 단어를 필터링하며 카운팅
                            filtered_words = [word for word in words if word not in exclude_words]
                            word_counter.update(filtered_words)
                        except IndexError:
                            continue

    # 특정 단어 집계
    specific_words = {"축구", "야구"}
    specific_counts = {word: word_counter.get(word, 0) for word in specific_words}

    return word_counter.most_common(), specific_counts

# 결과 출력
if __name__ == "__main__":
    chat_dir = r"C:\Users\Bongju Kim\OneDrive\Coding\Kakaotalk_Chat_고려대 축구방"
    
    # 단어 빈도 분석
    top_words, specific_counts = analyze_word_frequency(chat_dir)

    print("\n가장 많이 사용된 단어와 빈도")
    for rank, (word, count) in enumerate(top_words[:10], 1):
        print(f"{rank}. {word}: {count}회")

    print("\n'축구'와 '야구' 단어 사용 횟수:")
    for word, count in specific_counts.items():
        print(f"{word}: {count}회")
