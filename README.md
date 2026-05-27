# Hệ thống Quản lý Yêu cầu Thực tập sinh

Hệ thống web hỗ trợ quản lý, theo dõi và xử lý các yêu cầu của thực tập sinh tại công ty Unikom.

## 📋 Mô tả dự án

Hệ thống giúp:
- Thực tập sinh tạo và theo dõi yêu cầu
- Admin quản lý và xử lý yêu cầu hiệu quả
- Theo dõi trạng thái xử lý theo thời gian thực
- Quản lý dữ liệu tập trung và trực quan

## 🛠️ Công nghệ sử dụng

- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend:** PHP
- **Database:** MySQL
- **Server:** XAMPP/WAMP
- **Version Control:** Git/GitHub

## 📁 Cấu trúc thư mục

```
project/
├── admin/                  # Trang quản trị
│   ├── dashboard.php
│   ├── manage_requests.php
│   ├── manage_users.php
│   └── view_request.php
├── assets/                 # Tài nguyên tĩnh
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── auth/                   # Xác thực
│   ├── login.php
│   └── logout.php
├── config/                 # Cấu hình
│   ├── database.php
│   └── session.php
├── database/               # Database
│   └── schema.sql
├── includes/               # Template
│   ├── header.php
│   └── footer.php
├── student/                # Trang thực tập sinh
│   ├── dashboard.php
│   ├── create_request.php
│   ├── my_requests.php
│   └── view_request.php
└── index.php               # Trang chủ
```

## 🚀 Hướng dẫn cài đặt

### Yêu cầu hệ thống
- XAMPP/WAMP (PHP 7.4+, MySQL 5.7+)
- Trình duyệt web hiện đại (Chrome, Firefox, Edge)

### Các bước cài đặt

1. **Clone repository**
```bash
git clone https://github.com/your-username/quan-ly-yeu-cau-thuc-tap-sinh.git
```

2. **Copy project vào thư mục htdocs**
```
C:\xampp\htdocs\quan-ly-yeu-cau-thuc-tap-sinh\
```

3. **Khởi động XAMPP**
- Mở XAMPP Control Panel
- Start Apache và MySQL

4. **Tạo database**
- Truy cập: http://localhost/phpmyadmin
- Tạo database mới tên: `quan_ly_thuc_tap_sinh`
- Import file: `database/schema.sql`

5. **Cấu hình kết nối database** (nếu cần)
- Mở file: `config/database.php`
- Chỉnh sửa thông tin kết nối:
```php
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'quan_ly_thuc_tap_sinh');
```

6. **Truy cập hệ thống**
```
http://localhost/quan-ly-yeu-cau-thuc-tap-sinh
```

## 👤 Tài khoản demo

### Admin
- Email: `admin@unikom.com`
- Mật khẩu: `admin123`

### Thực tập sinh
- Email: `hien.vu@student.com`
- Mật khẩu: `student123`

## ✨ Chức năng chính

### Đối với Thực tập sinh
- ✅ Đăng nhập hệ thống
- ✅ Tạo yêu cầu mới
- ✅ Theo dõi trạng thái yêu cầu
- ✅ Xem lịch sử yêu cầu
- ✅ Xem thông báo phản hồi từ Admin

### Đối với Admin
- ✅ Quản lý tài khoản người dùng
- ✅ Xem danh sách yêu cầu
- ✅ Cập nhật trạng thái yêu cầu
- ✅ Theo dõi tiến độ xử lý
- ✅ Tìm kiếm và lọc yêu cầu
- ✅ Xem thống kê hệ thống

## 📊 Database Schema

### Bảng: nguoi_dung
Lưu thông tin tài khoản người dùng (Admin và Thực tập sinh)

### Bảng: yeu_cau_thuc_tap
Lưu thông tin các yêu cầu của thực tập sinh

### Bảng: nhat_ky_trang_thai
Lưu lịch sử thay đổi trạng thái yêu cầu

## 🐛 Xử lý lỗi thường gặp

### Lỗi kết nối database
- Kiểm tra MySQL đã chạy chưa
- Kiểm tra thông tin kết nối trong `config/database.php`
- Đảm bảo database đã được import

### Lỗi 404 Not Found
- Kiểm tra đường dẫn project trong htdocs
- Đảm bảo Apache đã chạy

### Lỗi session
- Xóa cache trình duyệt
- Kiểm tra quyền ghi file trong thư mục project

## 👨‍💻 Tác giả

**Vũ Thị Thu Hiền**
- Sinh viên năm 3
- Công ty: Unikom
- Email: hien.vu@student.com

## 📝 License

Dự án này được phát triển cho mục đích học tập và thực tập tại công ty Unikom.

## 🙏 Lời cảm ơn

Cảm ơn công ty Unikom và các mentor đã hỗ trợ trong quá trình thực hiện đề tài.

---

**Phiên bản:** 1.0.0  
**Ngày cập nhật:** 20/05/2026
