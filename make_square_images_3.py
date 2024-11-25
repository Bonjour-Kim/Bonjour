from PIL import Image, ExifTags
import os

# 원본 파일 경로 및 저장 경로
input_folder = r"C:\Users\Bongju Kim\OneDrive\사진\Selected"
output_folder = r"C:\Users\Bongju Kim\OneDrive\사진\Instagram"

# 저장 폴더가 없으면 생성
os.makedirs(output_folder, exist_ok=True)

# 파일 처리
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 이미지 열기
        with Image.open(input_path) as img:
            # EXIF 데이터에서 회전 정보 처리
            try:
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == 'Orientation':
                        break
                exif = img._getexif()
                if exif is not None and orientation in exif:
                    if exif[orientation] == 3:
                        img = img.rotate(180, expand=True)
                    elif exif[orientation] == 6:
                        img = img.rotate(270, expand=True)
                    elif exif[orientation] == 8:
                        img = img.rotate(90, expand=True)
            except (AttributeError, KeyError, IndexError):
                pass  # EXIF 정보가 없거나 처리 오류 발생 시 무시

            # 원본 크기
            original_width, original_height = img.size

            # 정방형 크기 결정
            square_size = max(original_width, original_height)
            new_img = Image.new("RGB", (square_size, square_size), color=(255, 255, 255))

            # 이미지 중앙에 배치
            offset = ((square_size - original_width) // 2, (square_size - original_height) // 2)
            new_img.paste(img, offset)

            # 저장
            new_img.save(output_path)

print("작업 완료! 모든 이미지가 정방형으로 저장되었습니다.")
