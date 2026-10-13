# 🎓 CHƯƠNG TRÌNH ĐÀO TẠO NLP TOÀN DIỆN: TỪ NỀN TẢNG ĐẾN CHUYÊN SÂU
## (Comprehensive Natural Language Processing: From Zero to Research Mastery)

Kho lưu trữ tài liệu học thuật, giải thích bản chất toán học và hệ thống bài tập thực hành được thiết kế chuẩn mực theo 4 giai đoạn tiến trình.

---

## 🗺️ BẢN ĐỒ LỘ TRÌNH 4 GIAI ĐOẠN

```
[GIAI ĐOẠN I] ───► [GIAI ĐOẠN II] ───► [GIAI ĐOẠN III] ───► [GIAI ĐOẠN IV]
Python & Cấu trúc    Đại số & Tiền       Classical ML đến      Thực nghiệm Nâng cao
Dữ liệu Văn bản     xử lý Tiếng Việt      Transformers/PhoBERT   & Phản biện Nghiên cứu
```

---

## 📚 CHI TIẾT TỪNG GIAI ĐOẠN

### 🟢 GIAI ĐOẠN I: NỀN TẢNG PYTHON VÀ CẤU TRÚC DỮ LIỆU CHO NLP
*Mục tiêu: Xóa bỏ hoàn toàn sự lúng túng khi đọc và viết mã nguồn Python.*
- **Module 1.1:** Biến, Kiểu dữ liệu, Thao tác Chuỗi (String Manipulation) và Định dạng `f-string`.
  - [Bài giảng 1.1](phase_1_python_nlp/lesson_1_1_strings_variables.md) | [Thực hành 1.1](phase_1_python_nlp/practice_1_1.py)
- **Module 1.2:** Cấu trúc Dữ liệu Sống còn: `List`, `Dictionary`, `Set` và Kỹ thuật List Comprehension.
  - [Bài giảng 1.2](phase_1_python_nlp/lesson_1_2_data_structures.md) | [Thực hành 1.2](phase_1_python_nlp/practice_1_2.py)
- **Module 1.3:** Regular Expressions (Biểu thức chính quy - Regex) trong Dọn dẹp Ngữ liệu.
- **Module 1.4:** Tư duy Thiết kế Hàm (`def`), Module Hóa và Xử lý Ngoại lệ (`try-except`).

---

### 🟡 GIAI ĐOẠN II: ĐẠI SỐ TUYẾN TÍNH & TIỀN XỬ LÝ TIẾNG VIỆT CHUYÊN SÂU
*Mục tiêu: Hiểu bản chất các phép biến đổi ma trận và đặc thù ngôn ngữ học tiếng Việt.*
- **Module 2.1:** Đại số Tuyến tính Thực chiến với `NumPy`: Vector, Ma trận, Phép nhân vô hướng (Dot Product).
- **Module 2.2:** Ngôn ngữ học Tính toán Tiếng Việt:
  - Bản chất ngôn ngữ đơn lập (Isolating Language).
  - Tách từ (Word Segmentation) bằng mô hình CRF trong `pyvi`.
  - Chuẩn hóa Bảng mã Unicode (NFC vs. NFD).
- **Module 2.3:** Xây dựng Pipeline Tiền xử lý Hoàn chỉnh và Phân tích Thống kê Dữ liệu (EDA).
  - [Chuyên đề: Từ Ngôn ngữ học đến Tensor Đại số](deep_dive_01_linguistics_to_tensors.md)

---

### 🟠 GIAI ĐOẠN III: TỪ MACHINE LEARNING CỔ ĐIỂN ĐẾN TRANSFORMERS
*Mục tiêu: Mổ xẻ không gian vector, hàm mất mát và cơ chế Attention bên trong mô hình.*
- **Module 3.1:** Không gian Vector Thưa (Sparse Space):
  - Thuật toán TF-IDF, N-gram và Mô hình Phân loại Hồi quy Logistic.
  - Tự tay tính ma trận TF-IDF trên giấy và cài đặt thuần túy bằng Python.
- **Module 3.2:** Lý thuyết Tối ưu & Đo lường Đánh giá:
  - Hàm mất mát Cross-Entropy Loss, Gradient Descent.
  - Ma trận Nhầm lẫn (Confusion Matrix), Nghịch lý Accuracy và Bản chất Macro-F1.
- **Module 3.3:** Kiến trúc Transformer & Cơ chế Self-Attention:
  - Scaled Dot-Product Attention: Query, Key, Value.
  - Multi-Head Attention, Residual Connection, Layer Normalization.
- **Module 3.4:** Pre-trained Language Models & PhoBERT:
  - Kiến trúc RoBERTa, Kỹ thuật Byte-Pair Encoding (BPE) Subword.
  - Fine-tuning PhoBERT trên tập ngữ liệu phân loại cảm xúc UIT-VSFC.

---

### 🔴 GIAI ĐOẠN IV: THỰC NGHIỆM CHUẨN TÁI LẬP & PHẢN BIỆN BẢO VỆ
*Mục tiêu: Đạt chuẩn mực nghiên cứu khoa học quốc tế, làm chủ hoàn toàn đề tài.*
- **Module 4.1:** Phương pháp luận Nghiên cứu Thực nghiệm:
  - Thiết kế đa seed ngẫu nhiên (Seeds 42, 100, 2024), Đảm bảo tính Bất biến dữ liệu (SHA-256 Data Hashing).
  - Kiểm định ý nghĩa thống kê (Statistical Significance Testing).
- **Module 4.2:** Nghiên cứu Triệt tiêu (Ablation Study) & Phân tích Lỗi Định tính (Qualitative Error Analysis):
  - 5 nhóm lỗi cơ bản trong phân loại văn bản tiếng Việt.
- **Module 4.3:** Diễn tập Bảo vệ & Phản biện Nghiên cứu (Mock Defense):
  - Bộ 10 câu hỏi cốt lõi từ hội đồng phản biện và cách giải thích học thuật chuẩn mực.
