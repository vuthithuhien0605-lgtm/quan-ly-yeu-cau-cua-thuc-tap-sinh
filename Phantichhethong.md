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
- Quản lý dữ liệu tập trung và trực quan hơn

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
- Tạo yêu cầu
- Xem trạng thái yêu cầu
- Quản lý yêu cầu
- Cập nhật trạng thái xử lý
- Quản lý người dùng
- Xem báo cáo thống kê

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
| Luồng xử lý chính  | Nhập nội dung yêu cầu → Gửi yêu cầu → Hệ thống lưu dữ liệu       |
| Kết quả            | Yêu cầu được lưu vào hệ thống                                    |

---
<img width="434" height="186" alt="UseCaseThuctapsinhtaoyeucau" src="https://github.com/user-attachments/assets/f9548d3d-fad6-41ac-acb8-962fedda2197" />

---
## UC05 – Cập nhật trạng thái xử lý

| Thành phần         | Nội dung                                                           |
|--------------------|--------------------------------------------------------------------|
| Tên Use Case       | Cập nhật trạng thái xử lý                                          |
| Actor              | Admin                                                              |
| Mô tả              | Admin cập nhật trạng thái xử lý yêu cầu                            |
| Điều kiện          | Admin đã đăng nhập                                                 |
| Luồng xử lý chính  | Chọn yêu cầu → Cập nhật trạng thái → Hệ thống lưu lịch sử xử lý    |
| Kết quả            | Trạng thái yêu cầu được cập nhật                                   |
---
<img width="547" height="334" alt="UseCaseAdmincapnhattrangthai" src="https://github.com/user-attachments/assets/672f45c9-3912-4c6e-b987-fd31111fd0d8" />

---

# 4.3. Sơ đồ Hoạt động (Activity Diagram)

Activity Diagram mô tả luồng hoạt động chính của hệ thống từ lúc người dùng thực hiện thao tác cho đến khi hệ thống xử lý và trả kết quả.

Các luồng nghiệp vụ chính gồm:
- Quy trình đăng nhập
- Quy trình tạo yêu cầu
- Quy trình xử lý yêu cầu
- Quy trình cập nhật trạng thái xử lý

### Bao gồm:
- Đăng nhập hệ thống
- Nhập thông tin yêu cầu
- Gửi yêu cầu
- Kiểm tra dữ liệu
- Lưu dữ liệu vào Database
- Cập nhật trạng thái xử lý
- Hiển thị kết quả

---

## Hình 4.3.1. Activity Diagram – Quy trình thực tập tạo yêu cầu
---
<img width="269" height="508" alt="ActivityThuctapsinhtaoyeucau" src="https://github.com/user-attachments/assets/91d318d5-613d-466d-8784-93794e2e1652" />


## Hình 4.3.2. Activity Diagram – Quy trình tạo yêu cầu
---
<img width="513" height="666" alt="Activitytaoyeucau" src="https://github.com/user-attachments/assets/37f72ff0-4235-4d03-a057-8fb3236ad992" />



## Hình 4.3.3. Activity Diagram – Quy trình Admin xử lý yêu cầu
---
<img width="275" height="464" alt="ActivityAdminxulyyeucau" src="https://github.com/user-attachments/assets/6f13ab1d-90ab-4f9a-ac67-e535c2005753" />



# 4.4. Sơ đồ Trình tự (Sequence Diagram)

Sequence Diagram mô tả quá trình tương tác giữa người dùng, giao diện hệ thống, PHP Controller và cơ sở dữ liệu trong quá trình xử lý yêu cầu.

Trong hệ thống gồm 2 luồng xử lý chính:
- Thực tập sinh tạo yêu cầu
- Admin xử lý và cập nhật trạng thái yêu cầu

Các sơ đồ trình tự giúp mô tả:
- Luồng gửi và nhận dữ liệu
- Quá trình xử lý của hệ thống
- Quá trình lưu dữ liệu vào Database
- Quá trình phản hồi kết quả cho người dùng

### Bao gồm:
- Người dùng gửi request
- Giao diện gửi dữ liệu
- PHP Controller xử lý
- Database lưu dữ liệu
- Admin cập nhật trạng thái
- Hệ thống trả kết quả

---
## Hình 4.4.1. Sequence Diagram – Tạo yêu cầu
---
<img width="614" height="522" alt="SequenceUI" src="https://github.com/user-attachments/assets/aae7158d-8e6c-47c8-8559-559de7f2b31f" />


## Hình 4.4.2. Sequence Diagram – Admin xử lý yêu cầu
---
<img width="648" height="533" alt="SequenceAdmin" src="https://github.com/user-attachments/assets/b2f67bca-4ced-471f-92f3-c2a245bf237d" />



# 4.5. Thiết kế cơ sở dữ liệu

Hệ thống sử dụng MySQL để lưu trữ dữ liệu.

Các bảng dữ liệu chính gồm:
- người_dùng
- yêu_cầu_thực_tập
- nhật_ký_trạng_thái

Trong đó:
- Bảng người_dùng lưu thông tin tài khoản người dùng
- Bảng yêu_cầu_thực_tập lưu thông tin yêu cầu thực tập sinh
- Bảng nhật_ký_trạng_thái lưu lịch sử cập nhật trạng thái yêu cầu

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


