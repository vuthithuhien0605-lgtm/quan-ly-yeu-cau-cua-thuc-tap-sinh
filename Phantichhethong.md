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
- Đăng nhập hệ thống
- Tạo yêu cầu (với loại và mức độ ưu tiên)
- Xem trạng thái yêu cầu
- Tìm kiếm yêu cầu
- Quản lý yêu cầu (Admin)
- Cập nhật trạng thái xử lý (Admin)
- Lọc yêu cầu theo trạng thái/ưu tiên/loại (Admin)
- Xem lịch sử thay đổi trạng thái
- Quản lý người dùng (Admin)
- Xem báo cáo thống kê (Admin)
- Phân trang danh sách yêu cầu

---

## Hình 4.1. Sơ đồ Use Case hệ thống
<img width="795" height="557" alt="sodousecase" src="https://github.com/user-attachments/assets/41a1e7a1-ce7c-41e8-91c0-1543919a741e" />


```text
                 +--------------------------------------+
                 | HỆ THỐNG QUẢN LÝ YÊU CẦU            |
                 | THỰC TẬP SINH                       |
                 +--------------------------------------+

      +--------------------+             +--------------------+
      |  Thực tập sinh     |             |       Admin        |
      +--------------------+             +--------------------+
                |                                     |
                |                                     |
      +--------------------+             +------------------------+
      | Đăng nhập          |             | Đăng nhập              |
      +--------------------+             +------------------------+
                |                                     |
      +--------------------+             +------------------------+
      | Tạo yêu cầu        |             | Quản lý yêu cầu        |
      +--------------------+             +------------------------+
                |                                     |
      +--------------------+             +------------------------+
      | Xem trạng thái     |             | Cập nhật trạng thái    |
      | yêu cầu            |             +------------------------+
      +--------------------+                        |
                                                    |
                                         +------------------------+
                                         | Quản lý người dùng     |
                                         +------------------------+
                                                    |
                                         +------------------------+
                                         | Xem báo cáo thống kê   |
                                         +------------------------+
```

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

---
<img width="434" height="186" alt="UseCaseThuctapsinhtaoyeucau" src="https://github.com/user-attachments/assets/f9548d3d-fad6-41ac-acb8-962fedda2197" />

---
## UC03 – Theo dõi tiến trình yêu cầu
| Thành phần        | Nội dung                                          |
| ----------------- | ------------------------------------------------- |
| Tên Use Case      | Theo dõi tiến trình yêu cầu                       |
| Actor             | Thực tập sinh                                     |
| Mô tả             | Theo dõi trạng thái xử lý các yêu cầu đã gửi      |
| Điều kiện         | Đã đăng nhập                                      |
| Luồng xử lý chính | Chọn yêu cầu → Hệ thống hiển thị tiến trình xử lý |
| Kết quả           | Người dùng xem được tiến độ xử lý                 |

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
## UC06 – Quản lý hồ sơ cá nhân
| Thành phần        | Nội dung                             |
| ----------------- | ------------------------------------ |
| Tên Use Case      | Quản lý hồ sơ cá nhân                |
| Actor             | Thực tập sinh                        |
| Mô tả             | Xem và cập nhật thông tin cá nhân    |
| Điều kiện         | Đã đăng nhập                         |
| Luồng xử lý chính | Mở hồ sơ → Chỉnh sửa → Lưu thông tin |
| Kết quả           | Thông tin được cập nhật              |

---
## UC07 – Duyệt yêu cầu
| Thành phần        | Nội dung                           |
| ----------------- | ---------------------------------- |
| Tên Use Case      | Quản lý thực tập sinh              |
| Actor             | Admin                              |
| Mô tả             | Quản lý danh sách thực tập sinh    |
| Điều kiện         | Admin đăng nhập                    |
| Luồng xử lý chính | Xem danh sách → Cập nhật thông tin |
| Kết quả           | Dữ liệu được cập nhật              |

---
## UC08 – Quản lý thực tập sinh
| Thành phần        | Nội dung                           |
| ----------------- | ---------------------------------- |
| Tên Use Case      | Quản lý thực tập sinh              |
| Actor             | Admin                              |
| Mô tả             | Quản lý danh sách thực tập sinh    |
| Điều kiện         | Admin đăng nhập                    |
| Luồng xử lý chính | Xem danh sách → Cập nhật thông tin |
| Kết quả           | Dữ liệu được cập nhật              |

---
## UC09 – Quản lý tài khoản người dùng
| Thành phần        | Nội dung                       |
| ----------------- | ------------------------------ |
| Tên Use Case      | Quản lý tài khoản              |
| Actor             | Admin                          |
| Mô tả             | Tạo, khóa, cấp quyền tài khoản |
| Điều kiện         | Admin đăng nhập                |
| Luồng xử lý chính | Tạo tài khoản → Phân quyền     |
| Kết quả           | Tài khoản được cập nhật        |

---
## UC010 – Xem Dashboard thống kê
| Thành phần        | Nội dung                                 |
| ----------------- | ---------------------------------------- |
| Tên Use Case      | Xem Dashboard                            |
| Actor             | Admin                                    |
| Mô tả             | Xem số liệu tổng quan hệ thống           |
| Điều kiện         | Admin đăng nhập                          |
| Luồng xử lý chính | Mở Dashboard → Hệ thống tổng hợp dữ liệu |
| Kết quả           | Hiển thị thống kê                        |

---
# 4.3. Sơ đồ Hoạt động (Activity Diagram)

Activity Diagram mô tả luồng hoạt động chính của hệ thống từ lúc người dùng thực hiện thao tác cho đến khi hệ thống xử lý và trả kết quả.

Các luồng nghiệp vụ chính gồm:
- Quy trình đăng nhập
- Quy trình tạo yêu cầu (với ghi log lịch sử)
- Quy trình xử lý yêu cầu
- Quy trình cập nhật trạng thái xử lý (với ghi log lịch sử)
- Quy trình tìm kiếm và lọc yêu cầu
- Quy trình phân trang

### Bao gồm:
- Đăng nhập hệ thống
- Nhập thông tin yêu cầu (tiêu đề, nội dung, loại, ưu tiên)
- Gửi yêu cầu
- Kiểm tra dữ liệu (validation)
- Lưu dữ liệu vào Database (MySQL)
- Ghi log vào bảng nhat_ky_trang_thai
- Cập nhật trạng thái xử lý
- Tìm kiếm và lọc yêu cầu
- Phân trang kết quả
- Hiển thị kết quả

---

## Hình 4.3.1. Activity Diagram – Quy trình thực tập tạo yêu cầu
---
<img width="871" height="749" alt="image" src="https://github.com/user-attachments/assets/10667897-446b-4b37-ad16-3f4a0e85aec8" />





## Hình 4.3.3. Activity Diagram – Quy trình Admin xử lý yêu cầu
---
<img width="904" height="783" alt="image" src="https://github.com/user-attachments/assets/79387666-c9be-4a27-9b8a-ac2845dcb6c0" />




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
## Hình 4.4.1. Sequence Diagram – Tạo yêu cầu
---
<img width="614" height="522" alt="SequenceUI" src="https://github.com/user-attachments/assets/aae7158d-8e6c-47c8-8559-559de7f2b31f" />


## Hình 4.4.2. Sequence Diagram – Admin xử lý yêu cầu
---
<img width="648" height="533" alt="SequenceAdmin" src="https://github.com/user-attachments/assets/b2f67bca-4ced-471f-92f3-c2a245bf237d" />



# 4.5. Thiết kế cơ sở dữ liệu

Hệ thống sử dụng MySQL để lưu trữ dữ liệu, kết nối qua PyMySQL và quản lý bằng Flask-SQLAlchemy ORM.

Các bảng dữ liệu chính gồm:
- **nguoi_dung** - Quản lý tài khoản người dùng
- **yeu_cau_thuc_tap** - Lưu thông tin yêu cầu
- **nhat_ky_trang_thai** - Theo dõi lịch sử thay đổi trạng thái

Trong đó:
- Bảng **nguoi_dung** lưu thông tin tài khoản (email, mật khẩu hash, họ tên, vai trò, trạng thái)
- Bảng **yeu_cau_thuc_tap** lưu thông tin yêu cầu (tiêu đề, nội dung, loại, ưu tiên, trạng thái, ghi chú admin)
- Bảng **nhat_ky_trang_thai** lưu lịch sử cập nhật trạng thái (trạng thái cũ, trạng thái mới, người cập nhật, thời gian, ghi chú)

**Quan hệ:**
- `yeu_cau_thuc_tap.nguoi_dung_id` → `nguoi_dung.id` (Many-to-One)
- `nhat_ky_trang_thai.yeu_cau_id` → `yeu_cau_thuc_tap.id` (Many-to-One)
- `nhat_ky_trang_thai.nguoi_cap_nhat_id` → `nguoi_dung.id` (Many-to-One)

---

## Hình 4.5. ERD Database Diagram
---
<img width="472" height="413" alt="ERD Database Diagram" src="https://github.com/user-attachments/assets/80440370-0da2-4c7e-ae49-716601c6ee75" />



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


