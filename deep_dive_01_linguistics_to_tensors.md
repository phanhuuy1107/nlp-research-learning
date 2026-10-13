# 🎓 CHUYÊN ĐỀ HỌC THUẬT SỐ 1: TỪ NGÔN NGỮ HỌC ĐẾN TENSOR ĐẠI SỐ
## (From Computational Linguistics to Mathematical Tensors)

> **Mục tiêu chuyên đề:** Cung cấp góc nhìn toán học và bản chất ngôn ngữ học tính toán đằng sau toàn bộ pipeline nghiên cứu của bài báo UIT-VSFC. Không coi code là hộp đen.

---

## 1. NGUYÊN LÝ NGÔN NGỮ HỌC TÍNH TOÁN CHO TIẾNG VIỆT

### 1.1. Tiếng Việt - Ngôn ngữ đơn lập (Isolating Language)
Trong tiếng Anh (ngôn ngữ biến hình):
$$\text{Boundary}(\text{Word}) \equiv \text{Whitespace}$$
Ví dụ: `"student"`, `"understands"`, `"understood"` có ranh giới từ trùng khớp với khoảng trắng.

Trong **tiếng Việt**:
- Đơn vị cơ sở của chữ viết là **Âm tiết (Syllable)**, được ngăn cách bởi dấu cách.
- Đơn vị mang nghĩa của ngữ pháp là **Từ (Word)**, bao gồm:
  - *Từ đơn (Single syllable):* `sách`, `bút`, `thầy`.
  - *Từ phức / từ ghép (Compound words):* `học_sinh`, `nhiệt_tình`, `giáo_trình`.
  - *Từ láy (Reduplicative words):* `khó_khăn`, `dễ_dàng`.

### 1.2. Hậu quả toán học nếu không Tách từ (Word Segmentation)
Nếu áp dụng trực tiếp phép cắt theo khoảng trắng:
$$\text{"bài tập quá khó"} \xrightarrow{\text{split(' ')}} \{\text{'bài'}, \text{'tập'}, \text{'quá'}, \text{'khó'}\}$$

- $\text{'bài'}$ và $\text{'tập'}$ bị xem là hai chiều độc lập (orthogonal dimensions) trong không gian vector:
  $$\vec{v}_{\text{bài}} \perp \vec{v}_{\text{tập}}$$
- Máy tính mất đi khái niệm toàn vẹn `bài_tập` (assignment/exercise).
- Thư viện `pyvi` giải quyết bài toán này bằng mô hình chuỗi **CRF (Conditional Random Fields)** hoặc **MaxEnt** để nối các âm tiết thành từ ghép:
  $$\text{"bài tập quá khó"} \xrightarrow{\text{pyvi}} \{\text{'bài\_tập'}, \text{'quá'}, \text{'khó'}\}$$

---

## 2. CHUYỂN HÓA DỮ LIỆU: TỪ VĂN BẢN ĐẾN MA TRẬN SỐ

### 2.1. Không gian vector rời rạc (Sparse Vector Space) - TF-IDF
Giả sử ta có tập từ điển gồm $|V|$ từ duy nhất: $\mathcal{V} = \{w_1, w_2, \dots, w_{|V|}\}$.
Mỗi câu văn bản $d$ được biểu diễn thành một vector:
$$\mathbf{x}_d = [s(w_1, d), s(w_2, d), \dots, s(w_{|V|}, d)]^T \in \mathbb{R}^{|V|}$$

Trong đó, trọng số TF-IDF của từ $t$ trong văn bản $d$ thuộc tập ngữ liệu $\mathcal{D}$:
$$\text{TF-IDF}(t, d, \mathcal{D}) = \text{TF}(t, d) \times \text{IDF}(t, \mathcal{D})$$

1. **Term Frequency (Tần suất từ):**
   $$\text{TF}(t, d) = \frac{f_{t, d}}{\sum_{t' \in d} f_{t', d}}$$
2. **Inverse Document Frequency (Nghịch đảo tần suất văn bản):**
   $$\text{IDF}(t, \mathcal{D}) = \ln \left( \frac{1 + |\mathcal{D}|}{1 + |\{d \in \mathcal{D} : t \in d\}|} \right) + 1$$
   *Ý nghĩa toán học:* Nếu từ $t$ xuất hiện ở hầu hết mọi câu (ví dụ: `và`, `thì`, `là`), mẫu số lớn $\implies \text{IDF} \to 0$. Từ đó bị triệt tiêu sức nặng phân loại.

**Nhược điểm chí tử của TF-IDF:**
- Chiều không gian cực lớn ($|V| = 10,000$ chiều trong bài báo của bạn), nhưng ma trận chứa hơn $99\%$ số $0$ (Sparse Matrix).
- Giả thuyết **Bag-of-Words** giả định các từ độc lập thống kê với nhau:
  $$\text{Sim}(\text{"không tốt"}, \text{"rất tốt"}) \approx \text{bị nhiễu bởi sự xuất hiện của từ 'tốt'}$$

---

### 2.2. Không gian phân bố ngữ cảnh (Dense Contextual Space) - PhoBERT
Mô hình **PhoBERT** (dựa trên kiến trúc RoBERTa) từ bỏ biểu diễn rời rạc. Nó ánh xạ mỗi token vào không gian vector liên tục:
$$\mathbf{e}_t \in \mathbb{R}^{768}$$

Mỗi tầng ẩn (Hidden layer) biến đổi vector thông qua cơ chế **Scaled Dot-Product Self-Attention**:
$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$$

* **Query ($\mathbf{Q}$):** Đại diện cho từ hiện tại đang truy vấn ngữ cảnh.
* **Key ($\mathbf{K}$):** Đại diện cho các từ khác trong câu để đo độ tương đồng.
* **Value ($\mathbf{V}$):** Lượng thông tin ngữ nghĩa thực sự được tổng hợp lại.
* Ma trận Attention $\mathbf{A} = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)$ cho phép từ `"không"` truyền trọng số mạnh mẽ sang từ `"tốt"` kế bên để đảo ngược vector ngữ nghĩa của toàn câu.

---

## 3. TẠI SAO PHẢI LÀ MACRO-F1 TRÊN TẬP UIT-VSFC?

### 3.1. Nghịch lý của Độ chính xác (Accuracy Paradox)
Phân phối nhãn thực tế trên tập UIT-VSFC ($16,175$ mẫu):
- **Tích cực (Positive):** $\sim 51.5\%$
- **Tiêu cực (Negative):** $\sim 43.7\%$
- **Trung tính (Neutral):** $\sim 4.8\%$ (Chỉ có $167$ mẫu trong tập Test $3,166$ mẫu!)

Nếu một mô hình "ngu ngơ" dự đoán $100\%$ các câu là Tích cực hoặc Tiêu cực và bỏ qua hoàn toàn lớp Trung tính:
$$\text{Accuracy} = \frac{1409 + 1590}{3166} = \frac{2999}{3166} \approx \mathbf{94.72\%}$$
$\implies$ Độ chính xác cao một cách giả tạo trong khi mô hình hoàn toàn hỏng trên lớp Trung tính!

### 3.2. Cơ chế bù trừ công bằng của Macro-F1
$$\text{Macro-F1} = \frac{1}{3} \left( F1_{\text{Negative}} + F1_{\text{Neutral}} + F1_{\text{Positive}} \right)$$

Trong đó:
$$F1_c = 2 \times \frac{\text{Precision}_c \times \text{Recall}_c}{\text{Precision}_c + \text{Recall}_c}$$

Bởi vì mỗi lớp đều có trọng số đóng góp là $\frac{1}{3}$ (không quan tâm lớp đó nhiều hay ít mẫu):
- Nếu $F1_{\text{Neutral}} = 0$, thì $\text{Macro-F1}$ ngay lập tức bị kéo tụt xuống tối đa chỉ còn $\frac{2}{3} \approx 66.6\%$.
- Đó là lý do khi **TF-IDF chỉ đạt $F1_{\text{Neutral}} = 13.04\%$**, điểm tổng Macro-F1 bị kéo tụt xuống **$65.06\%$**.
- Trong khi **PhoBERT kéo được $F1_{\text{Neutral}}$ lên $59.64\%$**, đưa Macro-F1 tổng thể lên **$82.95\%$** ($+17.89\text{ pp}$).

---

## 4. TỔNG KẾT BẢN ĐỒ KIẾN THỨC CỦA BẠN

Khi ai đó (hoặc người hướng dẫn) hỏi:
1. *"Tại sao em phải chạy PyVi trước khi đưa vào PhoBERT?"*
   $\to$ Trả lời: Do đặc thù tiếng Việt là ngôn ngữ đơn lập, âm tiết không đồng nhất với từ vựng. Tokenizer của PhoBERT được huấn luyện sẵn trên văn bản đã phân đoạn từ cấp từ vựng (Word-level BPE), nếu không tách từ bằng `pyvi`, mô hình sẽ bị vỡ token thành các sub-syllable làm suy giảm $-5.46\text{ pp}$ Macro-F1 (đã chứng minh ở phần Ablation Study).
2. *"Tại sao TF-IDF thất bại trước PhoBERT?"*
   $\to$ Trả lời: TF-IDF dựa trên giả thuyết Bag-of-Words trong không gian thưa, triệt tiêu thông tin thứ tự từ và bất lực trước cấu trúc đảo ngữ/phủ định ngữ cảnh. PhoBERT học biểu diễn ngữ nghĩa dày đặc 768 chiều với cơ chế Self-Attention nắm bắt phụ thuộc xa giữa các từ.
