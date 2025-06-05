from PIL import Image
import os

input_folder = "./images/input_folder"
output_folder = "./images/output_folder"
output_pdf_path = os.path.join(output_folder, "택배비_지원_정책자금2.pdf")

os.makedirs(output_folder, exist_ok=True)

# 이미지 수집 및 정렬
image_files = sorted([
    f for f in os.listdir(input_folder)
    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
])

# 이미지 열기 및 RGB 변환
image_list = []
for file in image_files:
    img_path = os.path.join(input_folder, file)
    img = Image.open(img_path)
    img = img.convert("RGB")  # PDF는 RGB 포맷만 지원
    image_list.append(img)

# 첫 이미지 기준으로 PDF 생성, 나머지는 append
if image_list:
    image_list[0].save(output_pdf_path, save_all=True, append_images=image_list[1:])
    print(f"병합 완료: {output_pdf_path}")
else:
    print("변환할 이미지가 없습니다.")