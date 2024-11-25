from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

# 원본 파일 경로 및 저장 경로
input_folder = r"C:\Users\Bongju Kim\OneDrive\사진\Selected"
output_folder = r"C:\Users\Bongju Kim\OneDrive\사진\Instagram"

# 저장 폴더가 없으면 생성
os.makedirs(output_folder, exist_ok=True)

def add_watermark(image, text="Bonjour"):
    # 워터마크 위치 후보들 (좌상단, 중앙상단, 우상단, 좌하단, 중앙하단, 우하단)
    positions = [
        (0, 0),  # 좌상단
        (image.width // 2, 0),  # 중앙상단
        (image.width, 0),  # 우상단
        (0, image.height),  # 좌하단
        (image.width // 2, image.height),  # 중앙하단
        (image.width, image.height),  # 우하단
    ]

    # 이미지를 흑백으로 변환하고 밝기 분석
    grayscale = image.convert("L")
    brightness_scores = []

    for x, y in positions:
        # 분석할 영역 크기 (이미지 크기에 비례)
        region_size = min(image.width, image.height) // 10
        x_start = max(x - region_size // 2, 0)
        y_start = max(y - region_size // 2, 0)
        x_end = min(x + region_size // 2, image.width)
        y_end = min(y + region_size // 2, image.height)
        region = grayscale.crop((x_start, y_start, x_end, y_end))
        brightness_scores.append(sum(region.getdata()) / len(region.getdata()))

    # 밝기가 가장 높은 위치 선택
    best_position = positions[brightness_scores.index(max(brightness_scores))]

    # 워터마크 글씨체와 크기
    font_size = max(image.width, image.height) // 20
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # 워터마크 색상 결정 (배경 밝기에 따라 검정 또는 흰색)
    watermark_color = (0, 0, 0) if max(brightness_scores) > 128 else (255, 255, 255)

    # 워터마크 추가
    draw = ImageDraw.Draw(image)

    # textbbox를 이용해 텍스트 크기 계산
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    
    # 텍스트 위치 계산
    if best_position == (0, 0):  # 좌상단
        text_position = (best_position[0], best_position[1])
        alignment = "left"
    elif best_position == (image.width // 2, 0):  # 중앙상단
        text_position = (best_position[0] - text_width // 2, best_position[1])
        alignment = "center"
    elif best_position == (image.width, 0):  # 우상단
        text_position = (best_position[0] - text_width, best_position[1])
        alignment = "right"
    elif best_position == (0, image.height):  # 좌하단
        text_position = (best_position[0], best_position[1] - text_height)
        alignment = "left"
    elif best_position == (image.width // 2, image.height):  # 중앙하단
        text_position = (best_position[0] - text_width // 2, best_position[1] - text_height)
        alignment = "center"
    elif best_position == (image.width, image.height):  # 우하단
        text_position = (best_position[0] - text_width, best_position[1] - text_height)
        alignment = "right"

    draw.text(text_position, text, font=font, fill=watermark_color)
    return image

# 파일 처리
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 이미지 열기
        with Image.open(input_path) as img:
            # EXIF 회전 처리: EXIF 데이터를 무시하고 올바르게 회전된 이미지를 만듦
            img = ImageOps.exif_transpose(img)
            
            # 원본 크기
            original_width, original_height = img.size

            # 정방형 크기 결정
            if original_width > original_height:
                # 가로로 긴 경우: 위아래 흰 배경 추가
                square_size = original_width
                new_img = Image.new("RGB", (square_size, square_size), color=(255, 255, 255))
                offset = (0, (square_size - original_height) // 2)
            else:
                # 세로로 긴 경우: 좌우 흰 배경 추가 (세로 방향 유지)
                square_size = original_height
                new_img = Image.new("RGB", (square_size, square_size), color=(255, 255, 255))
                offset = ((square_size - original_width) // 2, 0)

            # 기존 이미지를 새 배경에 붙이기
            new_img.paste(img, offset)

            # 워터마크 추가 (원본 사진에 추가 후 흰 배경 처리)
            watermarked_img = add_watermark(img.copy())  # 원본 이미지에 워터마크 추가
            # 워터마크가 추가된 이미지를 새 배경 위에 붙임
            new_img.paste(watermarked_img, offset)

            # 저장
            new_img.save(output_path)

print("작업 완료! 모든 이미지가 정방형으로 저장되고 워터마크가 추가되었습니다.")
