# -*- coding: utf-8 -*-
# ==============================================================================
# BÀI TẬP THỰC HÀNH 1.2: CẤU TRÚC DỮ LIỆU NLP (LIST, DICT, SET & COMPREHENSION)
# ==============================================================================
import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

print("=" * 65)
print(">>> BÀI THỰC HÀNH 1.2: QUẢN LÝ NGỮ LIỆU BẰNG CẤU TRÚC DỮ LIỆU")
print("=" * 65)

# 1. TẬP NGỮ LIỆU MẪU (CORPUS)
raw_feedbacks = [
    "   giảng viên rất tận tâm   ",
    "bài tập quá dài và khó",
    "phòng học máy lạnh bị hỏng",
    "thầy giảng bài rất dễ hiểu",
    "   nội dung bình thường không có gì đặc sắc   "
]
raw_labels = ["Tích cực", "Tiêu cực", "Tiêu cực", "Tích cực", "Trung tính"]

# 2. LÀM SẠCH VĂN BẢN BẰNG LIST COMPREHENSION
# Duyệt qua từng câu và áp dụng .strip()
clean_feedbacks = [text.strip() for text in raw_feedbacks]
print("\n1. KẾT QUẢ SAU KHI LÀM SẠCH (List Comprehension):")
for i, (sent, lbl) in enumerate(zip(clean_feedbacks, raw_labels), 1):
    print(f"  Câu {i}: '{sent}' -> Nhãn: {lbl}")

# 3. ÁNH XẠ NHÃN BẰNG DICTIONARY (LABEL ENCODING)
label_map = {
    "Tiêu cực": 0,
    "Trung tính": 1,
    "Tích cực": 2
}
# Chuyển đổi toàn bộ nhãn chữ sang số
encoded_labels = [label_map[lbl] for lbl in raw_labels]
print("\n2. NHÃN ĐÃ MÃ HÓA SANG DẠNG SỐ HỌC (Categorical to Numerical):")
print(f"  Chữ : {raw_labels}")
print(f"  Số  : {encoded_labels}")

# 4. TRÍCH XUẤT KHÔNG GIAN TỪ VỰNG (VOCABULARY SIZE |V|) BẰNG SET
all_words = []
for sent in clean_feedbacks:
    all_words.extend(sent.split(" "))

total_tokens = len(all_words)
unique_vocab = set(all_words)
vocab_size = len(unique_vocab)

print("\n3. THỐNG KÊ TỪ VỰNG (VOCABULARY PROFILE):")
print(f"  • Tổng số từ (Tokens count)           : {total_tokens}")
print(f"  • Kích thước từ điển duy nhất (|V|)    : {vocab_size} từ")
print(f"  • Danh sách các từ duy nhất trong Set : {sorted(list(unique_vocab))}")

print("\n" + "=" * 65)
print(">>> Hoàn thành thực nghiệm 1.2 thành công!")
print("=" * 65)
