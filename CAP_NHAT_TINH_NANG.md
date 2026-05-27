# CẬP NHẬT TÍNH NĂNG MỚI

**Ngày cập nhật:** 20/05/2026  
**Phiên bản:** 1.1.0

---

## 🎉 TÍNH NĂNG MỚI ĐÃ BỔ SUNG

### 1. ✅ Lịch sử trạng thái (Status History)

**Mô tả:** Hệ thống giờ đây tự động ghi lại mọi thay đổi trạng thái của yêu cầu.

**Chi tiết:**
- ✅ Tự động ghi log khi tạo yêu cầu mới
- ✅ Tự động ghi log khi admin cập nhật trạng thái
- ✅ Lưu thông tin: trạng thái cũ → trạng thái mới, người cập nhật, thời gian, ghi chú
- ✅ Hiển thị timeline đẹp mắt với icon và màu sắc phân biệt
- ✅ Cả admin và student đều có thể xem lịch sử

**Cách sử dụng:**
1. Vào trang chi tiết yêu cầu (admin hoặc student)
2. Cuộn xuống phần "Lịch sử trạng thái"
3. Xem timeline các thay đổi từ mới nhất đến cũ nhất

**Database:**
- Sử dụng bảng `nhat_ky_trang_thai` đã có sẵn
- Model `NhatKyTrangThai` đã được thêm vào `app.py`

---

### 2. ✅ Phân trang (Pagination)

**Mô tả:** Danh sách yêu cầu giờ được chia thành nhiều trang để tải nhanh hơn.

**Chi tiết:**
- ✅ Admin: 15 yêu cầu/trang
- ✅ Student: 10 yêu cầu/trang
- ✅ Nút điều hướng: Trước, Sau, số trang
- ✅ Hiển thị thông tin: "Trang X / Y (Z yêu cầu)"
- ✅ Giữ nguyên bộ lọc và tìm kiếm khi chuyển trang

**Cách sử dụng:**
1. Vào trang "Quản lý yêu cầu" (admin) hoặc "Yêu cầu của tôi" (student)
2. Nếu có nhiều hơn 15/10 yêu cầu, sẽ xuất hiện phân trang ở cuối bảng
3. Click số trang hoặc nút Trước/Sau để chuyển trang

**Lợi ích:**
- ⚡ Tải trang nhanh hơn khi có nhiều yêu cầu
- 📱 Dễ dàng điều hướng trên mobile
- 🎯 Tìm kiếm và lọc vẫn hoạt động tốt

---

### 3. ✅ Tìm kiếm và lọc nâng cao (Advanced Search & Filter)

**Mô tả:** Tìm kiếm thông minh và lọc đa điều kiện giúp tìm yêu cầu nhanh chóng.

#### Cho Admin:
**Tìm kiếm theo:**
- ✅ Tiêu đề yêu cầu
- ✅ Nội dung yêu cầu
- ✅ Tên người tạo
- ✅ Email người tạo

**Lọc theo:**
- ✅ Trạng thái: Mới, Đang xử lý, Hoàn thành, Từ chối
- ✅ Mức độ ưu tiên: Thấp, Trung bình, Cao, Khẩn cấp
- ✅ Loại yêu cầu: Hỗ trợ kỹ thuật, Xin nghỉ, Thắc mắc, Khác

**Cách sử dụng:**
1. Vào "Quản lý yêu cầu"
2. Nhập từ khóa vào ô "Tìm kiếm"
3. Chọn các bộ lọc (có thể kết hợp nhiều bộ lọc)
4. Click nút "Lọc"
5. Click nút X để xóa bộ lọc

#### Cho Student:
**Tìm kiếm theo:**
- ✅ Tiêu đề yêu cầu
- ✅ Nội dung yêu cầu

**Cách sử dụng:**
1. Vào "Yêu cầu của tôi"
2. Nhập từ khóa vào ô "Tìm kiếm yêu cầu"
3. Click nút "Tìm"
4. Click nút X để xóa tìm kiếm

**Lợi ích:**
- 🔍 Tìm yêu cầu cụ thể trong vài giây
- 🎯 Lọc theo nhiều tiêu chí cùng lúc
- 💡 Hiển thị badge "Đang lọc" khi có bộ lọc active
- 📊 Hiển thị số lượng kết quả tìm được

---

## 🔧 THAY ĐỔI KỸ THUẬT

### Models (app.py)
```python
# Thêm model mới
class NhatKyTrangThai(db.Model):
    __tablename__ = 'nhat_ky_trang_thai'
    id = db.Column(db.Integer, primary_key=True)
    yeu_cau_id = db.Column(db.Integer, db.ForeignKey('yeu_cau_thuc_tap.id'))
    trang_thai_cu = db.Column(db.String(50))
    trang_thai_moi = db.Column(db.String(50), nullable=False)
    ghi_chu = db.Column(db.Text)
    nguoi_cap_nhat_id = db.Column(db.Integer, db.ForeignKey('nguoi_dung.id'))
    ngay_cap_nhat = db.Column(db.DateTime, default=datetime.utcnow)
```

### Routes đã cập nhật:
1. **`student_create()`** - Ghi log khi tạo yêu cầu
2. **`student_requests()`** - Thêm tìm kiếm và phân trang
3. **`student_view_request()`** - Lấy lịch sử trạng thái
4. **`admin_requests()`** - Thêm tìm kiếm, lọc nâng cao và phân trang
5. **`admin_view_request()`** - Ghi log khi cập nhật trạng thái, lấy lịch sử

### Templates đã cập nhật:
1. **`templates/admin/requests.html`** - Form tìm kiếm/lọc + phân trang
2. **`templates/student/requests.html`** - Form tìm kiếm + phân trang
3. **`templates/admin/view.html`** - Timeline lịch sử trạng thái
4. **`templates/student/view.html`** - Timeline lịch sử trạng thái

---

## 📋 HƯỚNG DẪN CÀI ĐẶT

### Bước 1: Cập nhật code
Code đã được cập nhật trong các file:
- ✅ `app.py`
- ✅ `templates/admin/requests.html`
- ✅ `templates/admin/view.html`
- ✅ `templates/student/requests.html`
- ✅ `templates/student/view.html`

### Bước 2: Database đã sẵn sàng
Bảng `nhat_ky_trang_thai` đã được tạo từ trước bởi `init_db.py`, không cần chạy lại.

### Bước 3: Khởi động lại server
```bash
# Dừng server hiện tại (Ctrl+C)
# Khởi động lại
python app.py
```

### Bước 4: Kiểm tra
1. Đăng nhập với tài khoản admin hoặc student
2. Thử tạo yêu cầu mới → Kiểm tra lịch sử
3. Thử tìm kiếm và lọc → Kiểm tra kết quả
4. Thử phân trang → Kiểm tra điều hướng
5. Admin cập nhật trạng thái → Kiểm tra log mới

---

## 🎨 GIAO DIỆN MỚI

### Trang quản lý yêu cầu (Admin)
```
┌─────────────────────────────────────────────────────┐
│ 🔍 Tìm kiếm và lọc                                  │
│ [Tìm kiếm...] [Trạng thái▼] [Ưu tiên▼] [Loại▼] [Lọc]│
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ 📋 Tìm thấy 25 yêu cầu                    [Đang lọc]│
│ ┌─────────────────────────────────────────────────┐ │
│ │ ID │ Người tạo │ Tiêu đề │ ... │ Thao tác      │ │
│ ├─────────────────────────────────────────────────┤ │
│ │ #1 │ Hiền      │ ...     │ ... │ [👁 Xem]      │ │
│ └─────────────────────────────────────────────────┘ │
│                                                       │
│ [◀ Trước] [1] [2] [3] ... [Sau ▶]                   │
│ Trang 1 / 3 (25 yêu cầu)                            │
└─────────────────────────────────────────────────────┘
```

### Chi tiết yêu cầu (Timeline)
```
┌─────────────────────────────────────────────────────┐
│ 🕐 Lịch sử trạng thái                               │
│                                                       │
│ ⚪ Mới → Đang xử lý          20/05/2026 14:30       │
│    bởi Admin                                         │
│    ┌─────────────────────────────────────────────┐  │
│    │ Đã tiếp nhận, đang xử lý...                 │  │
│    └─────────────────────────────────────────────┘  │
│                                                       │
│ ⚪ Yêu cầu được tạo          20/05/2026 10:00       │
│    bởi Vũ Thị Thu Hiền                              │
│    ┌─────────────────────────────────────────────┐  │
│    │ Yêu cầu được tạo                            │  │
│    └─────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## 📊 SO SÁNH TRƯỚC VÀ SAU

| Tính năng | Trước | Sau |
|-----------|-------|-----|
| **Lịch sử trạng thái** | ❌ Không có | ✅ Timeline đầy đủ |
| **Phân trang** | ❌ Load tất cả | ✅ 10-15 items/trang |
| **Tìm kiếm** | ❌ Không có | ✅ Tìm đa trường |
| **Lọc admin** | ⚠️ Chỉ 2 bộ lọc | ✅ 3 bộ lọc + tìm kiếm |
| **Lọc student** | ❌ Không có | ✅ Tìm kiếm |
| **Performance** | ⚠️ Chậm khi nhiều data | ✅ Nhanh với pagination |

---

## 🐛 LƯU Ý VÀ TROUBLESHOOTING

### Lưu ý:
1. ✅ Lịch sử chỉ ghi khi trạng thái **thay đổi**, không ghi nếu chỉ sửa ghi chú
2. ✅ Yêu cầu cũ (tạo trước khi cập nhật) sẽ không có log "Yêu cầu được tạo"
3. ✅ Phân trang giữ nguyên bộ lọc khi chuyển trang
4. ✅ Tìm kiếm không phân biệt hoa thường

### Nếu gặp lỗi:
**Lỗi: "NhatKyTrangThai is not defined"**
- Kiểm tra đã thêm model vào `app.py` chưa
- Restart server

**Lỗi: "pagination object has no attribute 'items'"**
- Kiểm tra đã cập nhật route đúng chưa
- Đảm bảo dùng `.paginate()` thay vì `.all()`

**Không thấy lịch sử:**
- Tạo yêu cầu mới để test
- Hoặc admin cập nhật trạng thái yêu cầu cũ

---

## 🚀 TÍNH NĂNG TIẾP THEO (Đề xuất)

Sau khi hoàn thành 3 tính năng này, có thể bổ sung thêm:

1. **Notification system** - Thông báo khi có cập nhật
2. **Export Excel/PDF** - Xuất báo cáo
3. **Dashboard charts** - Biểu đồ thống kê
4. **Profile management** - Quản lý thông tin cá nhân
5. **User CRUD** - Admin tạo/sửa/xóa user
6. **Upload files** - Đính kèm file vào yêu cầu

---

**Người thực hiện:** AI Assistant (Kiro)  
**Ngày:** 20/05/2026  
**Phiên bản:** 1.1.0
