import sqlite3
import os
from werkzeug.security import generate_password_hash

# Kết nối SQLite
db_path = 'app.db'
connection = sqlite3.connect(db_path)

try:
    with connection:
        cursor = connection.cursor()
        print("🔄 Đang tạo bảng...")
        
        # Tạo bảng nguoi_dung
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS nguoi_dung (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                mat_khau TEXT NOT NULL,
                ho_ten TEXT NOT NULL,
                vai_tro TEXT NOT NULL DEFAULT 'thuc_tap_sinh',
                so_dien_thoai TEXT,
                trang_thai TEXT DEFAULT 'hoat_dong',
                ngay_tao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ngay_cap_nhat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Tạo bảng yeu_cau_thuc_tap
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS yeu_cau_thuc_tap (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nguoi_dung_id INTEGER NOT NULL,
                tieu_de TEXT NOT NULL,
                noi_dung TEXT NOT NULL,
                loai_yeu_cau TEXT DEFAULT 'khac',
                muc_do_uu_tien TEXT DEFAULT 'trung_binh',
                trang_thai TEXT DEFAULT 'moi',
                ghi_chu_admin TEXT,
                ngay_tao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ngay_cap_nhat TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (nguoi_dung_id) REFERENCES nguoi_dung(id) ON DELETE CASCADE
            )
        """)
        
        # Tạo bảng nhat_ky_trang_thai
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS nhat_ky_trang_thai (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                yeu_cau_id INTEGER NOT NULL,
                trang_thai_cu TEXT,
                trang_thai_moi TEXT NOT NULL,
                ghi_chu TEXT,
                nguoi_cap_nhat_id INTEGER,
                ngay_cap_nhat TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (yeu_cau_id) REFERENCES yeu_cau_thuc_tap(id) ON DELETE CASCADE,
                FOREIGN KEY (nguoi_cap_nhat_id) REFERENCES nguoi_dung(id) ON DELETE SET NULL
            )
        """)
        
        print("✅ Đã tạo bảng thành công!")
        
        # Kiểm tra xem đã có dữ liệu chưa
        cursor.execute("SELECT COUNT(*) FROM nguoi_dung")
        count = cursor.fetchone()[0]
        
        if count == 0:
            print("🔄 Đang thêm dữ liệu mẫu...")
            
            # Tạo hash mật khẩu
            admin_pass = generate_password_hash('admin123')
            student_pass = generate_password_hash('student123')
            
            # Thêm tài khoản
            cursor.execute("""
                INSERT INTO nguoi_dung (email, mat_khau, ho_ten, vai_tro) 
                VALUES (?, ?, ?, ?)
            """, ('admin@unikom.com', admin_pass, 'Quản trị viên', 'admin'))
            
            cursor.execute("""
                INSERT INTO nguoi_dung (email, mat_khau, ho_ten, vai_tro, so_dien_thoai) 
                VALUES (?, ?, ?, ?, ?)
            """, ('hien.vu@student.com', student_pass, 'Vũ Thị Thu Hiền', 'thuc_tap_sinh', '0123456789'))
            
            cursor.execute("""
                INSERT INTO nguoi_dung (email, mat_khau, ho_ten, vai_tro, so_dien_thoai) 
                VALUES (?, ?, ?, ?, ?)
            """, ('student1@unikom.com', student_pass, 'Nguyễn Văn A', 'thuc_tap_sinh', '0987654321'))
            
            connection.commit()
            
            print("✅ Đã thêm dữ liệu mẫu thành công!")
            print("\n📋 Tài khoản demo:")
            print("   Admin: admin@unikom.com / admin123")
            print("   Sinh viên: hien.vu@student.com / student123")
        else:
            print("ℹ️  Dữ liệu đã tồn tại, bỏ qua việc thêm mẫu")
            
finally:
    connection.close()
    print("\n✅ Hoàn tất khởi tạo database!")
