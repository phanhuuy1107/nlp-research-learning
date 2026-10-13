# 📖 Module 1.2: Cấu Trúc Dữ Liệu Lõi (List, Dictionary, Set) & Xử Lý Ngữ Liệu

## 🎯 Mục Tiêu Học Thuật
1. Nắm bản chất cách bộ nhớ máy tính lưu trữ tập ngữ liệu văn bản (Corpus).
2. Phân biệt rõ sự khác nhau giữa `List` (thứ tự), `Dictionary` (bảng tra cứu O(1)) và `Set` (tập hợp từ vựng duy nhất).
3. Làm chủ kỹ thuật **List Comprehension** — công cụ mạnh mẽ xuất hiện ở mọi script huấn luyện NLP hiện đại.

---

## 1. Ba Cấu Trúc Dữ Liệu Trọng Yếu Trong NLP

### 1.1. `List` (Danh sách tuần tự) — Biểu diễn Tập Ngữ liệu & Chuỗi Token
`List` lưu trữ các phần tử có thứ tự, cho phép trùng lặp. Trong NLP:
- Tập câu huấn luyện (Sentences) là một `List[str]`.
- Nhãn đi kèm (Labels) là một `List[int]`.

```python
sentences = [
    "thầy dạy rất nhiệt tình",
    "bài tập quá dài và khó",
    "phòng học máy lạnh bị hỏng"
]
labels = [2, 0, 0]  # 2: Tích cực, 0: Tiêu cực
```

### 1.2. `Dictionary` (Từ điển / Bảng ánh xạ băm - Hash Map) — Ánh xạ Từ và Nhãn
`Dictionary` lưu trữ theo cặp `Key: Value`. Thời gian tìm kiếm là $\mathcal{O}(1)$ (tức thời):
- Ánh xạ giữa chữ và số: `LABEL2ID` và `ID2LABEL`.
- Xây dựng bảng từ vựng (Vocabulary): Gán mỗi từ duy nhất với một mã số ID nguyên.

```python
label2id = {"Tiêu cực": 0, "Trung tính": 1, "Tích cực": 2}
id2label = {0: "Tiêu cực", 1: "Trung tính", 2: "Tích cực"}

# Tra cứu tức thì:
print(label2id["Tích cực"])  # Kết quả: 2
```

### 1.3. `Set` (Tập hợp không trùng lặp) — Trích xuất Không Gian Từ Vựng (Vocabulary $|V|$)
`Set` chỉ giữ lại các phần tử duy nhất, tự động loại bỏ từ trùng lặp:
```python
words = ["thầy", "dạy", "rất", "hay", "và", "thầy", "rất", "nhiệt", "tình"]
unique_words = set(words)
print(unique_words)
# Kết quả: {'thầy', 'dạy', 'rất', 'hay', 'và', 'nhiệt', 'tình'}
print(f"Kích thước từ điển: {len(unique_words)} từ")
```

---

## 2. Kỹ Thuật Viết Code Đẳng Cấp: List Comprehension

Trong các file của đồ án (như `train_baseline.py` và `data_pipeline.py`), bạn bắt gặp dòng:
```python
train_texts = [ViTokenizer.tokenize(t) for t in dataset['train']['sentence']]
```

Đây chính là **List Comprehension** — cú pháp rút gọn giúp duyệt qua toàn bộ văn bản và biến đổi chỉ trong 1 dòng duy nhất, tốc độ thực thi nhanh hơn vòng lặp `for` thông thường.

### Cú pháp so sánh:
*Cách viết truyền thống (4 dòng):*
```python
cleaned_sentences = []
for s in sentences:
    cleaned_sentences.append(s.strip())
```

*Cách viết List Comprehension (1 dòng chuẩn Pythonic):*
```python
cleaned_sentences = [s.strip() for s in sentences]
```

---

## ✍️ Thực Hành
Mở file `phase_1_python_nlp/practice_1_2.py` để tự tay chạy và quan sát cách dữ liệu chuyển hóa!
