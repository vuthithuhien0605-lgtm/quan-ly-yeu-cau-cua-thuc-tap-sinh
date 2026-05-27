# KẾ HOẠCH THỰC HIỆN ĐỀ TÀI

## Tên đề tài
Xây dựng hệ thống quản lý yêu cầu thực tập sinh (theo dõi và xử lý)

---

## Thông tin sinh viên thực hiện
- Họ và tên: Vũ Thị Thu Hiền 
- Vai trò: Sinh viên năm 3
- Đơn vị thực hiện: Công ty Unikom

---

## Giới thiệu đề tài
Hiện nay nhiều doanh nghiệp và đơn vị thực tập vẫn quản lý các yêu cầu của thực tập sinh thông qua tin nhắn hoặc các công cụ đơn giản, gây khó khăn trong việc theo dõi và xử lý yêu cầu.

Đề tài “Xây dựng hệ thống quản lý yêu cầu thực tập sinh” được thực hiện nhằm xây dựng một hệ thống web hỗ trợ quản lý, theo dõi và xử lý các yêu cầu của thực tập sinh một cách hiệu quả hơn. Hệ thống giúp mentor/admin dễ dàng tiếp nhận yêu cầu, theo dõi tiến độ xử lý và quản lý thông tin liên quan.

---

## Mục tiêu đề tài
- Quản lý yêu cầu của thực tập sinh
- Theo dõi trạng thái xử lý yêu cầu
- Hỗ trợ mentor/admin xử lý yêu cầu hiệu quả
- Xây dựng giao diện hiện đại và dễ sử dụng

---

## Công nghệ sử dụng
- **Backend:** Python Flask 3.0.0
- **Database:** MySQL (qua PyMySQL)
- **ORM:** Flask-SQLAlchemy 3.1.1
- **Frontend:** HTML5, CSS3, JavaScript
- **UI Framework:** Bootstrap 5
- **Icons:** Bootstrap Icons
- **Security:** Werkzeug (Password Hashing)
- **Environment:** Python 3.13.7, XAMPP (MySQL)
- **Version Control:** Git/GitHub
- **IDE:** VS Code

---

## Chức năng dự kiến

### Đối với thực tập sinh
- Đăng nhập hệ thống
- Tạo yêu cầu mới (với loại và mức độ ưu tiên)
- Theo dõi trạng thái yêu cầu
- Xem thông báo phản hồi từ Admin
- Tìm kiếm yêu cầu của mình
- Xem lịch sử thay đổi trạng thái

### Cho Admin 
- Quản lý tài khoản người dùng
- Xem và xử lý yêu cầu
- Cập nhật trạng thái yêu cầu
- Theo dõi tiến độ xử lý
- Tìm kiếm và lọc yêu cầu (theo trạng thái, ưu tiên, loại)
- Xem lịch sử thay đổi trạng thái
- Xem thống kê dashboard

---
QUY TRÌNH THỰC HIỆN ĐỀ TÀI
-  Xây dựng kế hoạch thực hiện đề tài
-  Xác định mục tiêu và phạm vi hệ thống
- Xác định các chức năng chính của hệ thống
- Phân chia thời gian thực hiện theo từng giai đoạn
## Người thực hiện chính
 - Sinh viên xác định định hướng đề tài
 -  Sinh viên lựa chọn chức năng phù hợp với thời gian thực hiện
 - Sinh viên xây dựng kế hoạch phát triển hệ thống
## AI hỗ trợ chính
- Gợi ý cấu trúc PLAN
- Gợi ý timeline thực hiện
- Gợi ý quy trình phát triển phần mềm
- Hỗ trợ trình bày nội dung tài liệu
### Khảo sát và Phân tích yêu cầu
- Tìm hiểu quy trình quản lý yêu cầu thực tập sinh
- Xác định nhu cầu sử dụng của Admin và Thực tập sinh
- Phân tích các chức năng của hệ thống
- Xây dựng Use Case cho hệ thống
- Phân tích luồng xử lý dữ liệu
## Người thực hiện chính
- Sinh viên phân tích nghiệp vụ thực tế
- Sinh viên xác định chức năng cần xây dựng
- Sinh viên xây dựng quy trình hoạt động hệ thống
## AI hỗ trợ chính
- Gợi ý Use Case
- Gợi ý Activity Diagram và Sequence Diagram
- Hỗ trợ mô tả chức năng hệ thống
- Hỗ trợ trình bày nội dung phân tích
### Thiết kế Database, UI và Backend
# Thiết kế Database
- Thiết kế bảng người dùng (nguoi_dung)
- Thiết kế bảng yêu cầu (yeu_cau_thuc_tap)
- Thiết kế bảng nhật ký trạng thái (nhat_ky_trang_thai)
- Thiết kế quan hệ dữ liệu (Foreign Keys, Relationships)
- Viết SQL script tạo bảng với PyMySQL
# Thiết kế UI
- Thiết kế giao diện đăng nhập
- Thiết kế giao diện Admin Dashboard
- Thiết kế giao diện Student Dashboard
- Thiết kế giao diện quản lý yêu cầu
- Thiết kế form tạo yêu cầu với validation
- Thiết kế timeline lịch sử trạng thái
# Thiết kế Backend Flask
- Thiết kế cấu trúc thư mục dự án Flask
- Thiết kế Models với SQLAlchemy ORM
- Thiết kế Routes và Views
- Thiết kế Authentication với Session
- Thiết kế Decorators (@login_required, @admin_required)
- Thiết kế Pagination và Search/Filter
## Người thực hiện chính
- Sinh viên thiết kế cấu trúc database
- Sinh viên thiết kế giao diện hệ thống
- Sinh viên xác định luồng xử lý dữ liệu
## AI hỗ trợ chính
- Gợi ý Database Schema với SQLAlchemy
- Gợi ý bố cục UI/UX với Bootstrap 5
- Hỗ trợ viết code mẫu Flask/Python
- Gợi ý cấu trúc thư mục dự án Flask
- Gợi ý tối ưu queries và xử lý form
- Hỗ trợ implement Pagination và Search
### Lập trình
- Xây dựng giao diện bằng HTML/CSS/JavaScript/Bootstrap 5
- Xây dựng Models với Flask-SQLAlchemy
- Xây dựng chức năng đăng ký và đăng nhập (Session-based)
- Xây dựng chức năng tạo yêu cầu với validation
- Xây dựng chức năng quản lý và xử lý yêu cầu
- Xây dựng chức năng tìm kiếm và lọc nâng cao
- Xây dựng chức năng phân trang (Pagination)
- Xây dựng chức năng ghi lịch sử trạng thái
- Kết nối Flask với MySQL qua PyMySQL
- Hiển thị dữ liệu từ database với Jinja2 Templates
- Xử lý phân quyền người dùng (Decorators)
## Người thực hiện chính
- Sinh viên lập trình hệ thống
- Sinh viên xử lý logic chức năng
- Sinh viên kết nối frontend và backend
- Sinh viên kiểm soát source code
## AI hỗ trợ chính
- Hỗ trợ viết code Flask/Python
- Hỗ trợ debug và sửa lỗi
- Gợi ý xử lý chức năng
- Gợi ý tối ưu giao diện và source code
- Hỗ trợ implement tính năng mới
### Kiểm thử
- Kiểm tra chức năng đăng nhập
- Kiểm tra chức năng tạo và xử lý yêu cầu
- Kiểm tra chức năng tìm kiếm và lọc
- Kiểm tra chức năng phân trang
- Kiểm tra lịch sử trạng thái
- Kiểm tra dữ liệu hệ thống
- Kiểm tra giao diện người dùng (responsive)
- Kiểm tra phân quyền admin/student
- Sửa lỗi phát sinh
## Người thực hiện chính
- Sinh viên kiểm thử chức năng thực tế
- Sinh viên đánh giá hoạt động hệ thống
- Sinh viên chỉnh sửa lỗi
## AI hỗ trợ chính
- Gợi ý test case
- Hỗ trợ tìm lỗi hệ thống
- Gợi ý cải thiện hiệu năng và giao diện
### Release
- Hoàn thiện hệ thống
- Tối ưu source code
- Upload source code lên GitHub
- Hoàn thiện báo cáo thực tập
- Chuẩn bị slide và demo hệ thống
## Người thực hiện chính
- Sinh viên hoàn thiện sản phẩm
- Sinh viên viết báo cáo
- Sinh viên chuẩn bị demo và thuyết trình
## AI hỗ trợ chính
- Hỗ trợ trình bày báo cáo
- Gợi ý nội dung slide
- Hỗ trợ mô tả dự án và hệ thống
- Hỗ trợ format tài liệu
  
-----

## Kế hoạch thực hiện
KẾ HOẠCH THỰC HIỆN THEO TUẦN
## Tuần 1: PLAN + Phân tích hệ thống
- Xây dựng kế hoạch thực hiện đề tài
- Khảo sát và phân tích yêu cầu hệ thống
- Xây dựng Use Case
- Thiết kế Database sơ bộ
- Thiết kế giao diện UI cơ bản
- Vẽ Use Case Diagram và ERD
## AI hỗ trợ chính
- Gợi ý Use Case
- Gợi ý Database Schema
- Gợi ý UI cơ bản
- Hỗ trợ trình bày tài liệu
## Sinh viên thực hiện chính
- Phân tích nghiệp vụ hệ thống
- Xác định chức năng cần xây dựng
 Hoàn thiện nội dung phân tích
## Tuần 2: Thiết kế và Lập trình hệ thống
- Xây dựng chức năng đăng ký/đăng nhập
- Xây dựng chức năng quản lý yêu cầu
- Xây dựng chức năng cập nhật trạng thái xử lý
- Kết nối PHP với MySQL
- Hoàn thiện giao diện Admin và Thực tập sinh
- Hoàn thiện API xử lý dữ liệu
## AI hỗ trợ chính
- Hỗ trợ viết code mẫu PHP
- Hỗ trợ debug
- Gợi ý xử lý form và session
- Gợi ý xử lý dữ liệu với MySQL
## Sinh viên thực hiện chính
- Lập trình chức năng hệ thống
- Kết nối frontend và backend
- Kiểm soát logic xử lý
## Tuần 3: Kiểm thử và Hoàn thiện hệ thống
- Kiểm thử chức năng hệ thống
- Sửa lỗi và tối ưu giao diện
- Hoàn thiện source code
- Upload source code lên GitHub
- Hoàn thiện báo cáo thực tập
- Chuẩn bị slide và demo hệ thống
## AI hỗ trợ chính
- Gợi ý test case
- Hỗ trợ tìm lỗi
- Hỗ trợ trình bày báo cáo và slide
## Sinh viên thực hiện chính
- Kiểm thử thực tế
- Tối ưu hệ thống
- Hoàn thiện báo cáo và demo hệ thống


