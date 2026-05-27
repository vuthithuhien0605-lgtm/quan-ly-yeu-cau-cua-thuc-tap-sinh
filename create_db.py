from app import app, db
from werkzeug.security import generate_password_hash

# Tạo context
with app.app_context():
    # Xóa bảng cũ (nếu có)
    db.drop_all()
    
    # Tạo bảng mới
    db.create_all()
    print("✅ Đã tạo bảng thành công!")
    
    # Thêm dữ liệu mẫu
    from app import NguoiDung, YeuCauThucTap, NhatKyTrangThai
    
    admin = NguoiDung(
        email='admin@unikom.com',
        mat_khau=generate_password_hash('admin123'),
        ho_ten='Quản trị viên',
        vai_tro='admin',
        trang_thai='hoat_dong'
    )
    
    student1 = NguoiDung(
        email='hien.vu@student.com',
        mat_khau=generate_password_hash('student123'),
        ho_ten='Vũ Thị Thu Hiền',
        vai_tro='thuc_tap_sinh',
        so_dien_thoai='0123456789',
        trang_thai='hoat_dong'
    )
    
    student2 = NguoiDung(
        email='student1@unikom.com',
        mat_khau=generate_password_hash('student123'),
        ho_ten='Nguyễn Văn A',
        vai_tro='thuc_tap_sinh',
        so_dien_thoai='0987654321',
        trang_thai='hoat_dong'
    )
    
    db.session.add(admin)
    db.session.add(student1)
    db.session.add(student2)
    db.session.commit()
    
    print("✅ Đã thêm dữ liệu mẫu thành công!")
    print("\n📋 Tài khoản demo:")
    print("   Admin: admin@unikom.com / admin123")
    print("   Sinh viên: hien.vu@student.com / student123")
    print("   Sinh viên: student1@unikom.com / student123")
