# 🧭 KIM CHỈ NAM HỌC THUẬT: BẢN CHẤT TRI THỨC VÀ NGUYÊN LÝ "TẠI SAO" TRONG NLP
## (The Philosophy of "Why": First Principles of Natural Language Processing)

> *"Học mà không hiểu lý do tại sao giống như xây lâu đài trên cát. Biết cách làm chỉ là người thợ, hiểu lý do tại sao mới là nhà nghiên cứu làm chủ công nghệ."*

Tài liệu này được biên soạn nhằm triệt tiêu hoàn toàn hiện tượng *"học vẹt"* hay *"Vịt nghe sấm"*. Mọi khái niệm trong đề tài nghiên cứu đều được mổ xẻ qua **Mô hình 5 Tầng Tri Thức (5-Layer Knowledge Architecture)**.

---

## 🏛️ MÔ HÌNH 5 TẦNG TRI THỨC

Mỗi khi tiếp cận một bài học mới trong kho lưu trữ này, bạn sẽ luôn được dẫn dắt qua 5 câu hỏi tuần tự:

```
[1. NỖI ĐAU THỰC TẾ]     ──► Nếu không có kiến thức này, hệ thống sẽ gặp bế tắc gì?
          ↓
[2. NGUYÊN NHÂN CỐT LÕI] ──► Tại sao trực giác thông thường của con người lại thất bại trên máy tính?
          ↓
[3. Ý TƯỞNG TRỰC QUAN]   ──► Ý tưởng mộc mạc nhất để tháo gỡ bế tắc là gì?
          ↓
[4. TOÁN HỌC & GIẢI THUẬT]──► Làm thế nào để công thức hóa ý tưởng đó thành toán học khả thi?
          ↓
[5. HIỆN THỰC BẰNG CODE] ──► Từng dòng lệnh Python tương ứng với bước nào của toán?
```

---

## 🗺️ TỔNG HỢP NGUYÊN LÝ "TẠI SAO" CHO 10 KHÁI NIỆM TRỌNG YẾU

### 1. Tại sao phải phân biệt List, Dictionary, và Set?
* **Nỗi đau:** Một tập ngữ liệu có hàng trăm nghìn từ. Nếu bạn dùng danh sách thông thường (`List`) để kiểm tra xem một từ có trong từ điển không:
  - Máy tính phải dò từng từ từ đầu đến cuối danh sách: Độ phức tạp thời gian là $\mathcal{O}(N)$. Với $10,000$ từ, máy phải so sánh $10,000$ lần cho mỗi từ đơn lẻ! Quá trình tiền xử lý mất hàng giờ.
* **Bản chất tri thức:**
  - `Dictionary` và `Set` sử dụng thuật toán **Bảng băm (Hash Table)**: Băm thẳng từ vựng thành địa chỉ ô nhớ. Máy nhảy thẳng tới vị trí đó để lấy dữ liệu với độ phức tạp $\mathcal{O}(1)$ (tức thời trong vài nano-giây).
  - `Set` tự động khử trùng lặp theo quy lý thuyết tập hợp, biến hàng triệu token thô thành một tập từ điển duy nhất $|V|$ trong nháy mắt.

---

### 2. Tại sao phải chuẩn hóa Unicode NFC vs. NFD?
* **Nỗi đau:** Hai sinh viên cùng gõ chữ `"hòa"` vào form đánh giá. Một người dùng kiểu gõ Telex cũ (bỏ dấu tổ hợp NFD: `h` + `o` + `\` + `a`), một người dùng Unicode dựng sẵn NFC (`hòa` là 1 mã ký tự duy nhất).
* **Bản chất tri thức:**
  - Đối với mắt người, chúng giống hệt nhau.
  - Nhưng đối với máy tính, mã byte nhị phân của chúng hoàn toàn khác nhau:
    $$\text{NFC: } [0\text{x0068}, 0\text{x00F2}, 0\text{x0061}] \quad \neq \quad \text{NFD: } [0\text{x0068}, 0\text{x006F}, 0\text{x0300}, 0\text{x0061}]$$
  - Nếu không chuẩn hóa bằng `unicodedata.normalize('NFC')`, máy tính sẽ coi đây là hai từ hoàn toàn xa lạ, làm phân mảnh không gian từ điển và khiến mô hình dự đoán sai lệch.

---

### 3. Tại sao tiếng Việt bắt buộc phải Tách từ (Word Segmentation)?
* **Nỗi đau:** Tiếng Việt là **ngôn ngữ đơn lập (Isolating Language)**, ranh giới giữa các từ không trùng khớp với dấu cách.
* **Bản chất tri thức:**
  - Xem xét câu: `"thầy dạy rất nhiệt tình"`
  - Nếu cắt bằng khoảng trắng thuần túy: máy hiểu thành hai thực thể độc lập là `'nhiệt'` (heat/nhiệt độ) và `'tình'` (feeling/tình cảm). Cả hai từ rời này đều không mang nghĩa tích cực rõ ràng của sự "tận tụy".
  - Khi dùng `pyvi`, mô hình trường ngẫu nhiên có điều kiện (CRF) dựa trên ngữ cảnh để ghép lại thành từ phức `'nhiệt_tình'`. Đây mới là đơn vị ngữ nghĩa thực sự giúp mô hình phân loại chính xác cảm xúc.

---

### 4. Tại sao lại là TF-IDF chứ không chỉ đếm số lần xuất hiện (Word Count)?
* **Nỗi đau:** Trong văn bản, những từ xuất hiện nhiều nhất luôn là các hư từ: `và`, `thì`, `là`, `của`, `rất`, `nhưng`. Nếu chỉ đếm tần suất đơn thuần (Term Frequency - TF), các từ này sẽ áp đảo toàn bộ trọng số ma trận, làm lu mờ các từ quan trọng như `tuyệt_vời`, `tệ`, `hỏng`.
* **Bản chất tri thức:**
  - **IDF (Inverse Document Frequency)** ra đời như một chiếc "cân công lý":
    $$\text{IDF}(t) = \ln\left(\frac{N}{\text{DF}(t)}\right)$$
  - Từ nào xuất hiện ở khắp mọi câu trong trường học ($\text{DF}(t) \approx N$) $\implies \text{IDF} \to 0$ (bị tước bỏ trọng số).
  - Từ nào chỉ xuất hiện ở các câu khen/chê đặc thù $\implies \text{IDF}$ rất cao (được khuếch đại sức mạnh phân loại).

---

### 5. Tại sao phải dùng hàm Softmax ở tầng cuối cùng của mô hình?
* **Nỗi đau:** Tầng Linear cuối cùng của mạng nơ-ron xuất ra các con số thô gọi là **Logits**: ví dụ $[-2.4, 0.8, 5.1]$. Những con số này không có giới hạn, không có đơn vị đo, con người không thể biết mô hình chắc chắn bao nhiêu phần trăm.
* **Bản chất tri thức:**
  - Hàm **Softmax** thực hiện 2 việc:
    1. Lũy thừa $e^{z_i}$ để biến mọi con số âm thành dương và phóng đại sự khác biệt.
    2. Chia cho tổng các lũy thừa để chuẩn hóa tổng xác suất về đúng bằng $1.0$ ($100\%$):
       $$P(y = c | \mathbf{x}) = \frac{e^{z_c}}{\sum_{j=1}^C e^{z_j}}$$
  - Biến các tín hiệu điện toán trừu tượng thành **phân phối xác suất** có thể định lượng được.

---

### 6. Tại sao Accuracy là con số "lừa dối", và tại sao Macro-F1 là cứu cánh?
* **Nỗi đau:** Dữ liệu UIT-VSFC bị lệch lớp trầm trọng:
  - Tích cực: $51.5\%$
  - Tiêu cực: $43.7\%$
  - Trung tính: $4.8\%$
* **Bản chất tri thức:**
  - Nếu một mô hình bị mù hoàn toàn lớp Trung tính (đoán sai $100\%$ các mẫu trung tính), nhưng đoán đúng lớp Tích cực và Tiêu cực, **Accuracy vẫn đạt tới $\sim 95\%$**! Một con số lừa gạt nguy hiểm nếu dùng trong thực tế.
  - **Macro-F1** giải quyết bài toán này bằng cách lấy trung bình số học không trọng số của cả 3 lớp:
    $$\text{Macro-F1} = \frac{F1_{\text{Neg}} + F1_{\text{Neu}} + F1_{\text{Pos}}}{3}$$
  - Mỗi lớp đóng góp đúng $33.3\%$ vào điểm số chung. Nếu lớp Trung tính bị $0$ điểm, Macro-F1 lập tức rớt thảm hại. Đây là lý do vì sao mọi hội nghị khoa học uy tín (ACL, EMNLP, IEEE) đều bắt buộc dùng Macro-F1 cho bài toán mất cân bằng lớp.

---

### 7. Tại sao PhoBERT lại vượt trội hoàn toàn so với TF-IDF?
* **Nỗi đau của TF-IDF:**
  - Hai câu: `"môn này không khó tí nào"` (Tích cực) và `"môn này khó không chịu nổi"` (Tiêu cực).
  - TF-IDF biểu diễn chúng bằng túi từ (Bag-of-Words). Cả hai câu đều chứa các từ giống hệt nhau: `môn`, `này`, `không`, `khó`. TF-IDF xem hai vector này gần như trùng khớp, dẫn đến đoán sai.
* **Bản chất tri thức của PhoBERT:**
  - PhoBERT sử dụng **Cơ chế Self-Attention**:
    $$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$$
  - Khi đọc đến từ `"khó"`, vector truy vấn $\mathbf{Q}$ của nó sẽ bắn một tia chú ý cực mạnh về phía từ `"không"` đứng trước nó. Hai vector này hòa quyện vào nhau, tạo thành một biểu diễn ngữ cảnh mới: `"không_khó" \implies \text{Dễ}`.
  - Đó là lý do PhoBERT hiểu được ngữ cảnh sâu sắc và giảm được **$48.3\%$ lỗi sai** so với TF-IDF.

---

### 8. Tại sao phải chạy thực nghiệm trên nhiều Seed (Multi-Seed)?
* **Nỗi đau:** Trọng số của các tầng phân loại được khởi tạo ngẫu nhiên. Nếu chỉ chạy 1 lần duy nhất với 1 seed ngẫu nhiên, điểm số cao có thể do may mắn rơi vào vùng hội tụ thuận lợi, không có giá trị học thuật.
* **Bản chất tri thức:**
  - Để khẳng định tính ưu việt của PhoBERT là **bản chất thuật toán** chứ không phải do "may mắn", ta bắt buộc phải chạy trên ít nhất 3 seed khác nhau (ví dụ: $42, 100, 2024$).
  - Báo cáo kết quả dạng $\mu \pm \sigma$ ($94.08 \pm 0.18\%$) để chứng minh phương sai cực nhỏ, mô hình có độ bền vững (robustness) và khả năng tái lập tuyệt đối.

---

## 🧭 HƯỚNG DẪN SỬ DỤNG
Mỗi khi bước vào một bài học mới:
1. Đọc phần **"Nỗi đau thực tế"** trong bài để biết mình đang giải quyết cái gì.
2. Đọc phần **"Bản chất tri thức"** để hiểu trực giác.
3. Tự tay gõ code và đối chiếu xem dòng code nào đang thực thi công thức nào.
4. **Tuyệt đối không bước sang bài tiếp theo nếu chưa trả lời được câu hỏi "Tại sao?".**
