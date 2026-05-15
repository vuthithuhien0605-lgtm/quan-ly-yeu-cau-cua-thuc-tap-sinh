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

## UC05 – Cập nhật trạng thái xử lý

| Thành phần         | Nội dung                                                           |
|--------------------|--------------------------------------------------------------------|
| Tên Use Case       | Cập nhật trạng thái xử lý                                          |
| Actor              | Admin                                                              |
| Mô tả              | Admin cập nhật trạng thái xử lý yêu cầu                            |
| Điều kiện          | Admin đã đăng nhập                                                 |
| Luồng xử lý chính  | Chọn yêu cầu → Cập nhật trạng thái → Hệ thống lưu lịch sử xử lý    |
| Kết quả            | Trạng thái yêu cầu được cập nhật                                   |

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

```text
+------------------------------+
| Thực tập sinh đăng nhập      |
+------------------------------+
               |
               v
+------------------------------+
| Nhập thông tin yêu cầu       |
+------------------------------+
               |
               v
+------------------------------+
| Gửi yêu cầu                  |
+------------------------------+
               |
               v
+------------------------------+
| Hệ thống kiểm tra dữ liệu    |
+------------------------------+
               |
               v
+------------------------------+
| Lưu dữ liệu vào Database     |
+------------------------------+
               |
               v
+------------------------------+
| Thông báo tạo thành công     |
+------------------------------+
```
## Hình 4.3.2. Activity Diagram – Quy trình tạo yêu cầu

```text
                          ●
                          |
                          v
            +---------------------------+
            | Đăng nhập hệ thống        |
            +---------------------------+
                          |
                          v
            +---------------------------+
            | Chọn tạo yêu cầu mới      |
            +---------------------------+
                          |
                          v
            +---------------------------+
+----------+| Nhập thông tin yêu cầu    |
|           +---------------------------+
|                         |
|                         v
|           +---------------------------+
|           | Kiểm tra dữ liệu          |
|           +---------------------------+
|                         |
|                         v
|                   /----------------\
|                  /  Dữ liệu hợp lệ? \
|                 /--------------------\
|                   |              |
|                  Không           Có
|                   |              |
|                   v              v
|      +-------------------+   +----------------------+
+-----+| Hiển thị lỗi      |   | Lưu vào Database     |
       +-------------------+   +----------------------+
                                   |
                                   v
                        +-----------------------------+
                        | Hiển thị thông báo thành công|
                        +-----------------------------+
                                   |
                                   |
                                   |
                                   v
                                   ◎
```
---

## Hình 4.3.3. Activity Diagram – Quy trình Admin xử lý yêu cầu

```text
                          ●
                          |
                          v
            +---------------------------+
            | Admin đăng nhập hệ thống  |
            +---------------------------+
                          |
                          v
            +---------------------------+
            | Xem danh sách yêu cầu     |
            +---------------------------+
                          |
                          v
            +---------------------------+
            | Chọn yêu cầu cần xử lý    |
            +---------------------------+
                          |
                          v
            +---------------------------+
            | Cập nhật trạng thái       |
            +---------------------------+
                          |
                          v
            +---------------------------+
            | Lưu lịch sử xử lý         |
            +---------------------------+
                          |
                          v
            +---------------------------+
            | Hiển thị kết quả cập nhật |
            +---------------------------+
                          |
                          v
                          ◎
```

---

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

```text
+----------------+   +----------------+   +----------------+   +----------------+
| Thực tập sinh  |   |  Giao diện UI  |   | PHP Controller |   | MySQL Database |
+----------------+   +----------------+   +----------------+   +----------------+
        |                     |                    |                     |
        | Đăng nhập           |                    |                     |
        |-------------------->|                    |                     |
        |                     | Gửi request        |                     |
        |                     |------------------->|                     |
        |                     |                    | Kiểm tra tài khoản  |
        |                     |                    |-------------------->|
        |                     |   Trả kết quả      |                     |
        |                     |<-------------------|---------------------|                     
        |                     |                    |                     |
        | Tạo yêu cầu         |                    |                     |
        |-------------------->|                    |                     |
        |                     | Gửi dữ liệu        |                     |
        |                     |------------------->|                     |
        |                     |                    | Kiểm tra dữ liệu    |
        |                     |                    |-------------------->|
        |                     |                    | Lưu yêu cầu         |
        |                     |                    |-------------------->|
        |                     |                    | Trả kết quả         |
        |                     |                    |<--------------------|                     
        |                     |Hiển thị thông báo  |                     |                  
                              |<-------------------|                     |                     
```

## Hình 4.4.2. Sequence Diagram – Admin xử lý yêu cầu

```text
+-------------+   +----------------+   +----------------+   +----------------+
|    Admin    |   |  Giao diện AD  |   | PHP Controller |   |    Database    |
+-------------+   +----------------+   +----------------+   +----------------+
       |                    |                    |                     |
       | Chọn yêu cầu       |                    |                     |
       |------------------->|                    |                     |
       |                    | Gửi request        |                     |
       |                    |------------------->|                     |
       |                    |                    | Kiểm tra dữ liệu    |
       |                    |                    |-------------------->|
       |                    |                    | Cập nhật trạng thái |
       |                    |                    |-------------------->|
       |                    |                    | Lưu lịch sử xử lý   |
       |                    |                    |-------------------->|
       |                    |                    | Trả kết quả         |
       |                    |                    |<--------------------|
       |                    |   Hiển thị kết quả |                     |
       |                    |<-------------------|                     |
```

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

```text
+----------------------+
|     người_dùng       |
+----------------------+
| mã_người_dùng        |
| họ_tên               |
| email                |
| mật_khẩu             |
| vai_trò              |
| ngày_tạo             |
+----------------------+
           |
           | 1
           |
           | N
+------------------------------+
|    yêu_cầu_thực_tập          |
+------------------------------+
| mã_yêu_cầu                   |
| mã_người_dùng                |
| tiêu_đề                      |
| mô_tả                        |
| loại_yêu_cầu                 |
| trạng_thái_hiện_tại          |
| ngày_tạo                     |
+------------------------------+
           |
           | 1
           |
           | N
+----------------------+
|   nhật_ký_trạng_thái |
+----------------------+
| mã_nhật_ký           |
| mã_yêu_cầu           |
| trạng_thái_cũ        |
| trạng_thái_mới       |
| người_cập_nhật       |
| ngày_tạo             |
|                      |
+----------------------+
```

---

# 4.6. Kết luận chương

Trong chương này, hệ thống đã được phân tích dựa trên các chức năng nghiệp vụ chính.

Các sơ đồ Use Case, Activity Diagram, Sequence Diagram và ERD giúp mô tả rõ:
- Luồng hoạt động của hệ thống
- Chức năng của từng đối tượng sử dụng
- Mối quan hệ dữ liệu giữa các thành phần


