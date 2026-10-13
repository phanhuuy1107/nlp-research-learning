# 📖 Bài 1.1: Làm Quen Với Biến & Xử Lý Chuỗi Văn Bản (Strings)

## 🎯 Mục Tiêu Bài Học
1. Hiểu máy tính nhìn văn bản trong NLP như thế nào.
2. Nắm vững khái niệm biến và kiểu dữ liệu chuỗi (`str`).
3. Làm chủ 4 thao tác xử lý chuỗi cốt lõi: `.strip()`, `.split()`, `.replace()`, và `f-string`.

---

## 1. Khái Niệm Biến (Variable)
Trong Python, biến như một chiếc hộp dán nhãn để chứa dữ liệu. Khi làm NLP, ta thường chứa 2 thứ quan trọng nhất:
- **Văn bản (Text/String):** Được đặt trong dấu ngoặc kép `"` hoặc nháy đơn `'`.
- **Nhãn phân loại (Label/Integer):** Các con số quy ước (ví dụ: `0`: Tiêu cực, `1`: Trung tính, `2`: Tích cực).

```python
feedback = "Thầy dạy rất nhiệt tình và dễ hiểu!"
label = 2
```

---

## 2. Bốn Thao Tác Chuỗi Sống Còn Trong NLP

### 2.1. Cắt nhỏ câu thành từng từ: `.split()`
Máy tính ban đầu chỉ nhìn thấy một chuỗi dài dính liền. Để đếm từ hoặc trích xuất đặc trưng (như TF-IDF), ta phải cắt câu thành danh sách các từ:
```python
sentence = "thầy dạy nhiệt tình"
words = sentence.split(" ")
print(words)
# Kết quả: ['thầy', 'dạy', 'nhiệt', 'tình']
```

### 2.2. Dọn dẹp khoảng trắng thừa: `.strip()`
Dữ liệu người dùng gõ thường có phím cách thừa ở đầu hoặc cuối câu (`"   thầy dạy tốt   "`). Hàm `.strip()` sẽ gọt sạch chúng:
```python
raw_text = "   thầy dạy tốt   "
clean_text = raw_text.strip()
print(clean_text)
# Kết quả: "thầy dạy tốt"
```

### 2.3. Thay thế ký tự: `.replace()`
Dùng để chuẩn hóa hoặc xóa bớt ký tự không mong muốn:
```python
text = "thầy dạy tốt ."
text_no_dot = text.replace(".", "")
print(text_no_dot)
# Kết quả: "thầy dạy tốt "
```

### 2.4. In định dạng chuyên nghiệp: `f-string`
Cho phép nhét giá trị của biến trực tiếp vào chuỗi văn bản thông qua cặp ngoặc nhọn `{}`:
```python
model_name = "PhoBERT"
accuracy = 0.9408

print(f"Mô hình {model_name} đạt độ chính xác {accuracy * 100:.2f}%")
# Kết quả: Mô hình PhoBERT đạt độ chính xác 94.08%
```

---

## ✍️ Bài Tập Thực Hành (Hands-on)
Mở file `practice_1_1.py` để tự tay gõ thử và xem kết quả chạy thực tế!
