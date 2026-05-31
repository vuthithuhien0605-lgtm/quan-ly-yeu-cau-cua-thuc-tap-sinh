# 4. PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG

hệ thống được phân tích dựa trên các chức năng nghiệp vụ chính của bài toán quản lý yêu cầu thực tập sinh.

Nội dung tập trung vào:
- Phân tích Use Case
- Mô tả luồng hoạt động hệ thống
- Thiết kế cơ sở dữ liệu
- Thiết kế luồng xử lý dữ liệu

Hệ thống được xây dựng nhằm:
- Hỗ trợ thực tập sinh tạo và theo dõi yêu cầu
- Hỗ trợ Admin quản lý và xử lý yêu cầu
- Theo dõi trạng thái xử lý theo thời gian thực
- Ghi lại lịch sử thay đổi trạng thái
- Tìm kiếm và lọc yêu cầu nâng cao
- Phân trang để tối ưu hiệu suất
- Quản lý dữ liệu tập trung và trực quan hơn

**Công nghệ sử dụng:**
- Backend: Python Flask 3.0.0
- ORM: Flask-SQLAlchemy 3.1.1
- Database: MySQL (PyMySQL)
- Frontend: HTML5, CSS3, Bootstrap 5
- Security: Werkzeug Password Hashing

---

# 4.1. Sơ đồ Use Case (Use Case Diagram)

Use Case Diagram mô tả các chức năng chính của hệ thống và mối quan hệ giữa người dùng với hệ thống.

Hệ thống gồm 2 đối tượng sử dụng chính:
- Thực tập sinh
- Admin

Trong đó:
- Thực tập sinh có thể tạo yêu cầu và theo dõi trạng thái xử lý
- Admin có thể quản lý yêu cầu, cập nhật trạng thái và xem thống kê hệ thống
### Bao gồm:

#### Thực tập sinh
- Đăng nhập hệ thống
- Tạo yêu cầu
- Xem trạng thái yêu cầu
- Xem thông báo
- Quản lý hồ sơ cá nhân
- Sử dụng trợ lý AI

#### Admin
- Đăng nhập hệ thống
- Quản lý yêu cầu
- Cập nhật trạng thái xử lý
- Quản lý người dùng
- Xem báo cáo thống kê
- Quản lý trợ lý AI
---

## Hình 4.1. Sơ đồ Use Case hệ thống
<img width="871" height="364" alt="image" src="https://github.com/user-attachments/assets/c1f3f1e4-55f1-441c-b527-fb86871b41e7" />
---

# 4.2. Đặc tả Use Case

## UC01 – Đăng nhập hệ thống

| Thành phần         | Nội dung                                                          |
|--------------------|-------------------------------------------------------------------|
| Tên Use Case       | Đăng nhập hệ thống                                                |
| Actor              | Admin, Thực tập sinh                                              |
| Mô tả              | Người dùng đăng nhập vào hệ thống bằng tài khoản được cấp         |
| Điều kiện          | Người dùng đã có tài khoản                                        |
| Luồng xử lý chính  | Nhập email và mật khẩu → Hệ thống kiểm tra → Đăng nhập thành công |
| Kết quả            | Người dùng truy cập vào hệ thống                                  |

---
<img width="555" height="220" alt="UseCaseDangnhaphethong " src="https://github.com/user-attachments/assets/ce96b554-8b8c-4a6c-93a3-26af074cbd85" />

---
## UC02 – Tạo yêu cầu

| Thành phần         | Nội dung                                                         |
|--------------------|------------------------------------------------------------------|
| Tên Use Case       | Tạo yêu cầu                                                      |
| Actor              | Thực tập sinh                                                    |
| Mô tả              | Thực tập sinh tạo yêu cầu gửi tới Admin                          |
| Điều kiện          | Người dùng đã đăng nhập                                          |
| Luồng xử lý chính  | Nhập thông tin yêu cầu (tiêu đề, nội dung, loại, ưu tiên) → Gửi yêu cầu → Hệ thống lưu dữ liệu → Ghi log lịch sử trạng thái |
| Kết quả            | Yêu cầu được lưu vào hệ thống với trạng thái "Mới"               |

---<img width="488" height="149" alt="image" src="https://github.com/user-attachments/assets/cc57c487-5103-42bd-a3b2-7d1b8133ef6e" />


---
### UC03 – Theo dõi tiến trình yêu cầu

| Thành phần       | Nội dung                                            |
| ---------------- | --------------------------------------------------- |
| Tên Use Case     | Theo dõi tiến trình yêu cầu                         |
| Actor            | Thực tập sinh                                       |
| Mô tả            | Theo dõi trạng thái xử lý các yêu cầu đã gửi        |
| Điều kiện        | Thực tập sinh đã đăng nhập hệ thống                 |
| Luồng xử lý chính| Chọn yêu cầu → Xem tiến trình → Xem lịch sử xử lý   |
| Kết quả          | Tiến trình xử lý được hiển thị                      |

<img width="587" height="248" alt="image" src="https://github.com/user-attachments/assets/b0f5c298-0b34-44d3-b24b-06cc31007ee1" />

---
## UC04 – Xem thông báo
| Thành phần        | Nội dung                                     |
| ----------------- | -------------------------------------------- |
| Tên Use Case      | Xem thông báo                                |
| Actor             | Thực tập sinh                                |
| Mô tả             | Xem các thông báo từ hệ thống                |
| Điều kiện         | Đã đăng nhập                                 |
| Luồng xử lý chính | Mở màn hình thông báo → Hệ thống tải dữ liệu |
| Kết quả           | Danh sách thông báo được hiển thị            |

<img width="540" height="148" alt="image" src="https://github.com/user-attachments/assets/a4c98d9e-bbbd-4196-a703-c50b7487bd8c" />

---
## UC05 – Cập nhật trạng thái xử lý

| Thành phần         | Nội dung                                                           |
|--------------------|--------------------------------------------------------------------|
| Tên Use Case       | Cập nhật trạng thái xử lý                                          |
| Actor              | Admin                                                              |
| Mô tả              | Admin cập nhật trạng thái xử lý yêu cầu                            |
| Điều kiện          | Admin đã đăng nhập                                                 |
| Luồng xử lý chính  | Chọn yêu cầu → Cập nhật trạng thái và ghi chú → Hệ thống lưu lịch sử thay đổi vào bảng nhat_ky_trang_thai → Cập nhật timestamp |
| Kết quả            | Trạng thái yêu cầu được cập nhật và lịch sử được ghi lại          |
---
<img width="547" height="334" alt="UseCaseAdmincapnhattrangthai" src="https://github.com/user-attachments/assets/672f45c9-3912-4c6e-b987-fd31111fd0d8" />

---
### UC06 – Quản lý hồ sơ cá nhân

| Thành phần       | Nội dung                                            |
| ---------------- | --------------------------------------------------- |
| Tên Use Case     | Quản lý hồ sơ cá nhân                               |
| Actor            | Thực tập sinh                                       |
| Mô tả            | Xem và cập nhật thông tin cá nhân                   |
| Điều kiện        | Thực tập sinh đã đăng nhập hệ thống                 |
| Luồng xử lý chính| Mở hồ sơ → Chỉnh sửa thông tin → Lưu thay đổi       |
| Kết quả          | Thông tin cá nhân được cập nhật                     |

<img width="691" height="168" alt="image" src="https://github.com/user-attachments/assets/a7dc1ab2-60a0-4af4-9690-445569daf00d" />

---
### UC07 – Duyệt yêu cầu

| Thành phần       | Nội dung                                                   |
| ---------------- | ---------------------------------------------------------- |
| Tên Use Case     | Duyệt yêu cầu                                               |
| Actor            | Admin                                                      |
| Mô tả            | Tiếp nhận và xử lý các yêu cầu từ thực tập sinh            |
| Điều kiện        | Admin đã đăng nhập hệ thống                                |
| Luồng xử lý chính| Chọn yêu cầu → Xem chi tiết → Phê duyệt/Từ chối → Ghi chú  |
| Kết quả          | Trạng thái yêu cầu được cập nhật                           |

<img width="432" height="176" alt="image" src="https://github.com/user-attachments/assets/93483c55-82c1-463f-a802-aa03243a5d1e" />


---
### UC08 – Quản lý thực tập sinh

| Thành phần       | Nội dung                                            |
| ---------------- | --------------------------------------------------- |
| Tên Use Case     | Quản lý thực tập sinh                               |
| Actor            | Admin                                               |
| Mô tả            | Quản lý thông tin và tiến trình thực tập sinh       |
| Điều kiện        | Admin đã đăng nhập hệ thống                         |
| Luồng xử lý chính| Xem danh sách → Cập nhật thông tin                  |
| Kết quả          | Dữ liệu thực tập sinh được cập nhật                 |

<img width="527" height="157" alt="image" src="https://github.com/user-attachments/assets/c525deba-c685-4497-a3b4-24335f28c207" />

---
### UC09 – Quản lý tài khoản người dùng

| Thành phần       | Nội dung                                            |
| ---------------- | --------------------------------------------------- |
| Tên Use Case     | Quản lý tài khoản người dùng                        |
| Actor            | Admin                                               |
| Mô tả            | Tạo mới, khóa và phân quyền tài khoản               |
| Điều kiện        | Admin đã đăng nhập hệ thống                         |
| Luồng xử lý chính| Tạo tài khoản → Phân quyền → Lưu dữ liệu            |
| Kết quả          | Tài khoản được cập nhật                             |

<img width="520" height="148" alt="image" src="https://github.com/user-attachments/assets/e73cc395-b362-4ab7-aa8b-0f6e22d5e4b8" />

---
### UC10 – Xem báo cáo thống kê

| Thành phần       | Nội dung                                            |
| ---------------- | --------------------------------------------------- |
| Tên Use Case     | Xem báo cáo thống kê                                |
| Actor            | Admin                                               |
| Mô tả            | Theo dõi số liệu tổng quan của hệ thống             |
| Điều kiện        | Admin đã đăng nhập hệ thống                         |
| Luồng xử lý chính| Mở Dashboard → Hệ thống tổng hợp dữ liệu            |
| Kết quả          | Báo cáo và biểu đồ thống kê được hiển thị           |

<img width="501" height="152" alt="image" src="https://github.com/user-attachments/assets/7df7c7a3-1286-4e2a-863d-98d1bae57ebb" />

---
### UC11 – Quản lý trợ lý AI

| Thành phần       | Nội dung                                            |
| ---------------- | --------------------------------------------------- |
| Tên Use Case     | Quản lý trợ lý AI                                   |
| Actor            | Admin                                               |
| Mô tả            | Cấu hình và theo dõi hoạt động của trợ lý AI        |
| Điều kiện        | Admin đã đăng nhập hệ thống                         |
| Luồng xử lý chính| Truy cập AI → Cập nhật cấu hình → Lưu thay đổi      |
| Kết quả          | Cấu hình trợ lý AI được cập nhật                    |

<img width="394" height="129" alt="image" src="https://github.com/user-attachments/assets/d5223a70-4ed0-4a1a-a757-8ca2e7be8eee" />

---
### UC12 – Sử dụng trợ lý AI

| Thành phần       | Nội dung                                            |
| ---------------- | --------------------------------------------------- |
| Tên Use Case     | Sử dụng trợ lý AI                                   |
| Actor            | Thực tập sinh                                       |
| Mô tả            | Đặt câu hỏi và nhận hỗ trợ từ trợ lý AI             |
| Điều kiện        | Thực tập sinh đã đăng nhập hệ thống                 |
| Luồng xử lý chính| Nhập câu hỏi → AI xử lý → Trả kết quả               |
| Kết quả          | Người dùng nhận được câu trả lời từ AI              |

<img width="386" height="129" alt="image" src="https://github.com/user-attachments/assets/f2009d4c-c5d8-44be-8e91-48caa4a89d26" />

---
# 4.3. Sơ đồ Hoạt động (Activity Diagram)

# 4.3. Sơ đồ Hoạt động (Activity Diagram)

Activity Diagram mô tả luồng hoạt động của hệ thống từ khi người dùng thực hiện thao tác cho đến khi hệ thống xử lý và trả kết quả.

Các sơ đồ hoạt động được xây dựng dựa trên các chức năng nghiệp vụ chính của hệ thống quản lý yêu cầu thực tập sinh, giúp mô tả rõ trình tự xử lý dữ liệu, điều kiện rẽ nhánh và sự tương tác giữa người dùng với hệ thống.

Các luồng nghiệp vụ chính bao gồm:

* Quy trình đăng nhập hệ thống
* Quy trình tạo yêu cầu thực tập
* Quy trình theo dõi tiến trình xử lý yêu cầu
* Quy trình xem thông báo
* Quy trình xử lý yêu cầu của Admin
* Quy trình xem Dashboard thống kê

### Nội dung mô tả

Các Activity Diagram thể hiện:

* Người dùng thực hiện thao tác trên giao diện hệ thống
* Hệ thống tiếp nhận và kiểm tra dữ liệu đầu vào
* Xử lý nghiệp vụ theo từng chức năng
* Lưu trữ và cập nhật dữ liệu trong cơ sở dữ liệu MySQL
* Cập nhật trạng thái yêu cầu khi có thay đổi
* Hiển thị kết quả xử lý cho người dùng
* Hỗ trợ Admin quản lý và theo dõi toàn bộ quá trình xử lý yêu cầu

Thông qua các sơ đồ hoạt động, có thể thấy được toàn bộ luồng xử lý nghiệp vụ của hệ thống từ phía Thực tập sinh đến Admin, đảm bảo việc quản lý yêu cầu được thực hiện một cách rõ ràng, nhất quán và dễ theo dõi.


---

Hình 4.3.1. Activity Diagram – Đăng nhập hệ thống
                    ┌─────────────┐
                    │   Bắt đầu   │
                    └──────┬──────┘
                           │
                           ▼
              ┌────────────────────────┐
              │ Mở màn hình đăng nhập  │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Nhập Email và Mật khẩu │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Nhấn nút Đăng nhập     │
              └───────────┬────────────┘
                          │
                          ▼
                     ◇ Hợp lệ ?
                     /        \
                  Không        Có
                   /            \
                  ▼              ▼
      ┌──────────────────┐  ┌──────────────────┐
      │ Thông báo lỗi    │  │ Xác định vai trò │
      └────────┬─────────┘  └────────┬─────────┘
               │                     │
               └──────────┬──────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Chuyển tới Dashboard   │
              └───────────┬────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │  Kết thúc   │
                    └─────────────┘
Hình 4.3.2. Activity Diagram – Tạo yêu cầu
                    ┌─────────────┐
                    │   Bắt đầu   │
                    └──────┬──────┘
                           │
                           ▼
              ┌────────────────────────┐
              │ Mở màn hình yêu cầu    │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Nhập tiêu đề yêu cầu   │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Nhập nội dung yêu cầu  │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Chọn loại yêu cầu      │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Chọn mức độ ưu tiên    │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Nhấn nút Gửi yêu cầu   │
              └───────────┬────────────┘
                          │
                          ▼
                     ◇ Hợp lệ ?
                     /        \
                  Không        Có
                   /            \
                  ▼              ▼
      ┌──────────────────┐  ┌──────────────────┐
      │ Hiển thị lỗi     │  │ Lưu yêu cầu      │
      └────────┬─────────┘  └────────┬─────────┘
               │                     │
               │                     ▼
               │         ┌─────────────────────┐
               │         │ Cập nhật trạng thái │
               │         │ "Mới tạo"           │
               │         └─────────┬───────────┘
               │                   │
               └─────────┬─────────┘
                         │
                         ▼
             ┌─────────────────────────┐
             │ Thông báo thành công    │
             └───────────┬─────────────┘
                         │
                         ▼
                   ┌─────────────┐
                   │  Kết thúc   │
                   └─────────────┘
Hình 4.3.3. Activity Diagram – Theo dõi tiến trình yêu cầu
                    ┌─────────────┐
                    │   Bắt đầu   │
                    └──────┬──────┘
                           │
                           ▼
              ┌────────────────────────┐
              │ Mở màn hình tiến trình │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Chọn yêu cầu cần xem   │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Tải dữ liệu tiến trình │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Hiển thị trạng thái    │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Hiển thị ghi chú xử lý │
              └───────────┬────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │  Kết thúc   │
                    └─────────────┘
Hình 4.3.4. Activity Diagram – Xem thông báo
                    ┌─────────────┐
                    │   Bắt đầu   │
                    └──────┬──────┘
                           │
                           ▼
              ┌────────────────────────┐
              │ Mở màn hình thông báo  │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Tải danh sách thông báo│
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Hiển thị danh sách     │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Xem chi tiết thông báo │
              └───────────┬────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │  Kết thúc   │
                    └─────────────┘
Hình 4.3.5. Activity Diagram – Admin xử lý yêu cầu
                    ┌─────────────┐
                    │   Bắt đầu   │
                    └──────┬──────┘
                           │
                           ▼
             ┌──────────────────────────┐
             │ Mở quản lý yêu cầu       │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │ Chọn yêu cầu cần xử lý   │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │ Xem chi tiết yêu cầu     │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │ Chọn trạng thái mới      │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │ Nhập ghi chú xử lý       │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │ Nhấn nút Cập nhật        │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │ Lưu thay đổi             │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │ Thông báo thành công     │
             └────────────┬─────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │  Kết thúc   │
                    └─────────────┘
Hình 4.3.6. Activity Diagram – Dashboard thống kê
                    ┌─────────────┐
                    │   Bắt đầu   │
                    └──────┬──────┘
                           │
                           ▼
               ┌───────────────────────┐
               │ Mở Dashboard          │
               └──────────┬────────────┘
                          │
                          ▼
               ┌───────────────────────┐
               │ Tổng hợp dữ liệu      │
               └──────────┬────────────┘
                          │
                          ▼
               ┌───────────────────────┐
               │ Thống kê yêu cầu      │
               └──────────┬────────────┘
                          │
                          ▼
               ┌───────────────────────┐
               │ Hiển thị biểu đồ      │
               └──────────┬────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │  Kết thúc   │
                    └─────────────┘


# 4.4. Sơ đồ Trình tự (Sequence Diagram)

Sequence Diagram mô tả quá trình tương tác giữa người dùng, giao diện hệ thống, Flask Backend và cơ sở dữ liệu trong quá trình xử lý yêu cầu.

Trong hệ thống gồm 2 luồng xử lý chính:
- Thực tập sinh tạo yêu cầu (với ghi log lịch sử)
- Admin xử lý và cập nhật trạng thái yêu cầu (với ghi log lịch sử)

Các sơ đồ trình tự giúp mô tả:
- Luồng gửi và nhận dữ liệu
- Quá trình xử lý của Flask Backend
- Quá trình lưu dữ liệu vào MySQL Database
- Quá trình ghi log vào bảng nhat_ky_trang_thai
- Quá trình phản hồi kết quả cho người dùng

### Bao gồm:
- Người dùng gửi request (submit form)
- Giao diện gửi dữ liệu đến Flask
- Flask Backend xử lý và validate dữ liệu
- SQLAlchemy ORM tương tác với Database
- Database lưu dữ liệu vào bảng yeu_cau_thuc_tap
- Database lưu log vào bảng nhat_ky_trang_thai
- Admin cập nhật trạng thái
- Hệ thống trả kết quả cho người dùng
---

Hình 4.4.x. Sequence Diagram – Đăng nhập hệ thống
---
<img width="651" height="520" alt="image" src="https://github.com/user-attachments/assets/3ce02113-97bf-468b-b9c3-ed9b9cc53de6" />

---


## Hình 4.4.1. Sequence Diagram – Tạo yêu cầu
---
<img width="698" height="521" alt="image" src="https://github.com/user-attachments/assets/2ff90091-5233-44ee-a1e7-4f348dc1ef5a" />



## Hình 4.4.2. Sequence Diagram – Admin xử lý yêu cầu
---
<img width="639" height="552" alt="image" src="https://github.com/user-attachments/assets/fb651073-c74b-4067-bc91-3ac302f412ae" />




# 4.5. Thiết kế cơ sở dữ liệu

Cơ sở dữ liệu được xây dựng nhằm lưu trữ tập trung toàn bộ thông tin của hệ thống quản lý yêu cầu thực tập sinh, bao gồm dữ liệu người dùng, yêu cầu thực tập và lịch sử xử lý yêu cầu.

Hệ thống sử dụng **MySQL** làm hệ quản trị cơ sở dữ liệu, kết nối thông qua thư viện **PyMySQL** và được quản lý bằng **Flask-SQLAlchemy ORM**. Việc sử dụng ORM giúp đơn giản hóa quá trình thao tác dữ liệu, tăng khả năng bảo trì và mở rộng hệ thống.

### Các bảng dữ liệu chính

#### Bảng nguoi_dung

Bảng này dùng để lưu thông tin tài khoản đăng nhập của người dùng trong hệ thống.

Thông tin lưu trữ bao gồm:

* Mã người dùng (ID)
* Họ và tên
* Email đăng nhập
* Mật khẩu đã mã hóa
* Vai trò người dùng (Admin hoặc Thực tập sinh)
* Trạng thái tài khoản
* Thời gian tạo tài khoản

#### Bảng yeu_cau_thuc_tap

Bảng này dùng để lưu toàn bộ yêu cầu được tạo bởi thực tập sinh.

Thông tin lưu trữ bao gồm:

* Mã yêu cầu
* Người tạo yêu cầu
* Tiêu đề yêu cầu
* Nội dung yêu cầu
* Loại yêu cầu
* Mức độ ưu tiên
* Trạng thái hiện tại
* Ghi chú xử lý của Admin
* Thời gian tạo và cập nhật

#### Bảng nhat_ky_trang_thai

Bảng này dùng để ghi nhận lịch sử thay đổi trạng thái của từng yêu cầu trong suốt quá trình xử lý.

Thông tin lưu trữ bao gồm:

* Mã nhật ký
* Mã yêu cầu
* Trạng thái cũ
* Trạng thái mới
* Người cập nhật
* Ghi chú xử lý
* Thời gian cập nhật

### Quan hệ giữa các bảng

Hệ thống được thiết kế theo mô hình quan hệ với các liên kết chính như sau:

* Một người dùng có thể tạo nhiều yêu cầu thực tập.
* Mỗi yêu cầu chỉ thuộc về một người dùng.
* Một yêu cầu có thể phát sinh nhiều bản ghi lịch sử trạng thái.
* Mỗi bản ghi lịch sử trạng thái thuộc về một yêu cầu cụ thể.
* Một người dùng (Admin) có thể thực hiện nhiều lần cập nhật trạng thái.

Các khóa ngoại được sử dụng nhằm đảm bảo tính toàn vẹn dữ liệu và hỗ trợ truy xuất thông tin một cách hiệu quả.

### Mô hình ERD

Sơ đồ ERD (Entity Relationship Diagram) thể hiện cấu trúc dữ liệu và mối quan hệ giữa các bảng trong hệ thống.

Thông qua sơ đồ ERD, có thể dễ dàng nhận thấy:

* Quan hệ giữa người dùng và yêu cầu thực tập.
* Quan hệ giữa yêu cầu thực tập và nhật ký trạng thái.
* Luồng dữ liệu phục vụ việc theo dõi và xử lý yêu cầu trong toàn bộ hệ thống.

## Hình 4.5. ERD Database Diagram
+----------------------+
|      NGUOI_DUNG      |
+----------------------+
| PK id               |
| ho_ten              |
| email               |
| mat_khau            |
| vai_tro             |
| trang_thai          |
| created_at          |
+----------------------+
           |
           | 1
           |
           | N
           ▼
+------------------------------+
|     YEU_CAU_THUC_TAP         |
+------------------------------+
| PK id                        |
| FK nguoi_dung_id             |
| tieu_de                      |
| noi_dung                     |
| loai_yeu_cau                 |
| muc_do_uu_tien               |
| trang_thai                   |
| ghi_chu_admin                |
| created_at                   |
| updated_at                   |
+------------------------------+
           |
           | 1
           |
           | N
           ▼
+------------------------------+
|    NHAT_KY_TRANG_THAI        |
+------------------------------+
| PK id                        |
| FK yeu_cau_id                |
| FK nguoi_cap_nhat_id         |
| trang_thai_cu                |
| trang_thai_moi               |
| ghi_chu                      |
| thoi_gian_cap_nhat           |
+------------------------------+


# 4.6. Kết luận chương

Trong chương này, hệ thống đã được phân tích dựa trên các chức năng nghiệp vụ chính.

Các sơ đồ Use Case, Activity Diagram, Sequence Diagram và ERD giúp mô tả rõ:
- Luồng hoạt động của hệ thống
- Chức năng của từng đối tượng sử dụng
- Mối quan hệ dữ liệu giữa các thành phần

**Công nghệ triển khai:**
- Backend: Python Flask 3.0.0 với SQLAlchemy ORM
- Database: MySQL với PyMySQL connector
- Frontend: HTML5, CSS3, Bootstrap 5
- Security: Werkzeug password hashing, Session-based authentication

**Tính năng đã triển khai:**
- ✅ Đăng nhập/đăng xuất với phân quyền
- ✅ Tạo và quản lý yêu cầu
- ✅ Cập nhật trạng thái với ghi log lịch sử
- ✅ Tìm kiếm và lọc nâng cao
- ✅ Phân trang danh sách yêu cầu
- ✅ Timeline lịch sử thay đổi trạng thái
- ✅ Dashboard thống kê cho admin và student


