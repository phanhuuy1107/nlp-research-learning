# -*- coding: utf-8 -*-
# ==============================================================================
# BÀI TẬP THỰC HÀNH 1.1: BIẾN VÀ THAO TÁC VỚI CHUỖI VĂN BẢN
# ==============================================================================
import sys
# Đảm bảo terminal Windows hiển thị chuẩn tiếng Việt UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# 1. Ví dụ mẫu:
sample_text = "   Thầy dạy rất nhiệt tình và tận tâm !   "
print("--- [VÍ DỤ MẪU] ---")
print("Câu gốc chưa xử lý   :", repr(sample_text))

cleaned = sample_text.strip()
print("Sau khi dùng .strip() :", repr(cleaned))

words = cleaned.split(" ")
print("Sau khi dùng .split() :", words)
print("Số lượng phần tử từ  :", len(words))
print("--------------------------------------------------\n")


# 2. PHẦN BÀI TẬP CỦA BẠN:
# Cho câu phản hồi sau của sinh viên:
raw_feedback = "   Bài tập môn này quá khó và dài !   "

# Yêu cầu:
# a) Dùng .strip() để làm sạch khoảng trắng 2 đầu và gán vào biến 'clean_feedback'
clean_feedback = raw_feedback.strip()

# b) Dùng .split(" ") để tách câu trên thành danh sách các từ và gán vào 'word_list'
word_list = clean_feedback.split(" ")

# c) Dùng len() để đếm xem có bao nhiêu từ trong 'word_list'
num_words = len(word_list)

# In kết quả kiểm tra:
print("--- [KẾT QUẢ BÀI TẬP CỦA BẠN] ---")
print(f"Câu sau khi làm sạch: '{clean_feedback}'")
print(f"Danh sách các từ    : {word_list}")
print(f"Tổng số từ đếm được : {num_words}")
