from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class NguoiDung(db.Model):
    __tablename__ = 'nguoi_dung'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mat_khau = db.Column(db.String(255), nullable=False)
    ho_ten = db.Column(db.String(100), nullable=False)
    vai_tro = db.Column(db.Enum('admin', 'thuc_tap_sinh'), nullable=False)
    so_dien_thoai = db.Column(db.String(15))
    trang_thai = db.Column(db.Enum('hoat_dong', 'khoa'), default='hoat_dong')
    ngay_tao = db.Column(db.DateTime, default=datetime.utcnow)

class YeuCauThucTap(db.Model):
    __tablename__ = 'yeu_cau_thuc_tap'
    id = db.Column(db.Integer, primary_key=True)
    nguoi_dung_id = db.Column(db.Integer, db.ForeignKey('nguoi_dung.id'), nullable=False)
    tieu_de = db.Column(db.String(200), nullable=False)
    noi_dung = db.Column(db.Text, nullable=False)
    loai_yeu_cau = db.Column(db.Enum('ho_tro_ky_thuat', 'xin_nghi', 'thac_mac', 'khac'), default='khac')
    muc_do_uu_tien = db.Column(db.Enum('thap', 'trung_binh', 'cao', 'khan_cap'), default='trung_binh')
    trang_thai = db.Column(db.Enum('moi', 'dang_xu_ly', 'hoan_thanh', 'tu_choi'), default='moi')
    ghi_chu_admin = db.Column(db.Text)
    ngay_tao = db.Column(db.DateTime, default=datetime.utcnow)
    ngay_cap_nhat = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    nguoi_dung = db.relationship('NguoiDung', backref='yeu_cau')

class NhatKyTrangThai(db.Model):
    __tablename__ = 'nhat_ky_trang_thai'
    id = db.Column(db.Integer, primary_key=True)
    yeu_cau_id = db.Column(db.Integer, db.ForeignKey('yeu_cau_thuc_tap.id'), nullable=False)
    trang_thai_cu = db.Column(db.String(50))
    trang_thai_moi = db.Column(db.String(50), nullable=False)
    ghi_chu = db.Column(db.Text)
    nguoi_cap_nhat_id = db.Column(db.Integer, db.ForeignKey('nguoi_dung.id'))
    ngay_cap_nhat = db.Column(db.DateTime, default=datetime.utcnow)
    
    yeu_cau = db.relationship('YeuCauThucTap', backref='lich_su')
    nguoi_cap_nhat = db.relationship('NguoiDung')

# Decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Vui lòng đăng nhập', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        if session.get('vai_tro') != 'admin':
            flash('Bạn không có quyền truy cập', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    if 'user_id' in session:
        if session.get('vai_tro') == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('student_dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = NguoiDung.query.filter_by(email=email, trang_thai='hoat_dong').first()
        
        if user and check_password_hash(user.mat_khau, password):
            session['user_id'] = user.id
            session['email'] = user.email
            session['ho_ten'] = user.ho_ten
            session['vai_tro'] = user.vai_tro
            
            flash(f'Chào mừng {user.ho_ten}!', 'success')
            
            if user.vai_tro == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('student_dashboard'))
        else:
            flash('Email hoặc mật khẩu không đúng', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Đã đăng xuất', 'info')
    return redirect(url_for('login'))

@app.route('/student/dashboard')
@login_required
def student_dashboard():
    user_id = session.get('user_id')
    
    total = YeuCauThucTap.query.filter_by(nguoi_dung_id=user_id).count()
    new = YeuCauThucTap.query.filter_by(nguoi_dung_id=user_id, trang_thai='moi').count()
    processing = YeuCauThucTap.query.filter_by(nguoi_dung_id=user_id, trang_thai='dang_xu_ly').count()
    completed = YeuCauThucTap.query.filter_by(nguoi_dung_id=user_id, trang_thai='hoan_thanh').count()
    
    recent = YeuCauThucTap.query.filter_by(nguoi_dung_id=user_id).order_by(YeuCauThucTap.ngay_tao.desc()).limit(5).all()
    
    return render_template('student/dashboard.html', 
                         total=total, new=new, processing=processing, 
                         completed=completed, recent=recent)

@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    total = YeuCauThucTap.query.count()
    new = YeuCauThucTap.query.filter_by(trang_thai='moi').count()
    processing = YeuCauThucTap.query.filter_by(trang_thai='dang_xu_ly').count()
    completed = YeuCauThucTap.query.filter_by(trang_thai='hoan_thanh').count()
    urgent = YeuCauThucTap.query.filter_by(muc_do_uu_tien='khan_cap').filter(YeuCauThucTap.trang_thai != 'hoan_thanh').count()
    students = NguoiDung.query.filter_by(vai_tro='thuc_tap_sinh').count()
    
    recent = YeuCauThucTap.query.join(NguoiDung).order_by(YeuCauThucTap.ngay_tao.desc()).limit(10).all()
    
    return render_template('admin/dashboard.html',
                         total=total, new=new, processing=processing,
                         completed=completed, urgent=urgent, students=students,
                         recent=recent)

# Student routes
@app.route('/student/create', methods=['GET', 'POST'])
@login_required
def student_create():
    if request.method == 'POST':
        tieu_de = request.form.get('tieu_de')
        noi_dung = request.form.get('noi_dung')
        loai_yeu_cau = request.form.get('loai_yeu_cau')
        muc_do_uu_tien = request.form.get('muc_do_uu_tien')
        
        yeu_cau = YeuCauThucTap(
            nguoi_dung_id=session.get('user_id'),
            tieu_de=tieu_de,
            noi_dung=noi_dung,
            loai_yeu_cau=loai_yeu_cau,
            muc_do_uu_tien=muc_do_uu_tien
        )
        
        db.session.add(yeu_cau)
        db.session.flush()  # Get ID before commit
        
        # Ghi lịch sử trạng thái ban đầu
        lich_su = NhatKyTrangThai(
            yeu_cau_id=yeu_cau.id,
            trang_thai_cu=None,
            trang_thai_moi='moi',
            ghi_chu='Yêu cầu được tạo',
            nguoi_cap_nhat_id=session.get('user_id')
        )
        db.session.add(lich_su)
        db.session.commit()
        
        flash('Tạo yêu cầu thành công!', 'success')
        return redirect(url_for('student_requests'))
    
    return render_template('student/create.html')

@app.route('/student/requests')
@login_required
def student_requests():
    user_id = session.get('user_id')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # Tìm kiếm
    search = request.args.get('search', '').strip()
    query = YeuCauThucTap.query.filter_by(nguoi_dung_id=user_id)
    
    if search:
        query = query.filter(
            db.or_(
                YeuCauThucTap.tieu_de.contains(search),
                YeuCauThucTap.noi_dung.contains(search)
            )
        )
    
    # Phân trang
    pagination = query.order_by(YeuCauThucTap.ngay_tao.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('student/requests.html', 
                         requests=pagination.items,
                         pagination=pagination,
                         search=search)

@app.route('/student/request/<int:id>')
@login_required
def student_view_request(id):
    yeu_cau = YeuCauThucTap.query.get_or_404(id)
    if yeu_cau.nguoi_dung_id != session.get('user_id'):
        flash('Bạn không có quyền xem yêu cầu này', 'danger')
        return redirect(url_for('student_dashboard'))
    
    # Lấy lịch sử trạng thái
    lich_su = NhatKyTrangThai.query.filter_by(yeu_cau_id=id).order_by(NhatKyTrangThai.ngay_cap_nhat.desc()).all()
    
    return render_template('student/view.html', yeu_cau=yeu_cau, lich_su=lich_su)

# Admin routes
@app.route('/admin/requests')
@admin_required
def admin_requests():
    page = request.args.get('page', 1, type=int)
    per_page = 15
    
    # Lọc
    status_filter = request.args.get('status')
    priority_filter = request.args.get('priority')
    loai_filter = request.args.get('loai')
    
    # Tìm kiếm
    search = request.args.get('search', '').strip()
    
    query = YeuCauThucTap.query.join(NguoiDung)
    
    if status_filter:
        query = query.filter(YeuCauThucTap.trang_thai == status_filter)
    
    if priority_filter:
        query = query.filter(YeuCauThucTap.muc_do_uu_tien == priority_filter)
    
    if loai_filter:
        query = query.filter(YeuCauThucTap.loai_yeu_cau == loai_filter)
    
    if search:
        query = query.filter(
            db.or_(
                YeuCauThucTap.tieu_de.contains(search),
                YeuCauThucTap.noi_dung.contains(search),
                NguoiDung.ho_ten.contains(search),
                NguoiDung.email.contains(search)
            )
        )
    
    # Phân trang
    pagination = query.order_by(YeuCauThucTap.ngay_tao.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('admin/requests.html', 
                         requests=pagination.items,
                         pagination=pagination,
                         status_filter=status_filter, 
                         priority_filter=priority_filter,
                         loai_filter=loai_filter,
                         search=search)

@app.route('/admin/request/<int:id>', methods=['GET', 'POST'])
@admin_required
def admin_view_request(id):
    yeu_cau = YeuCauThucTap.query.get_or_404(id)
    
    if request.method == 'POST':
        trang_thai_moi = request.form.get('trang_thai')
        ghi_chu = request.form.get('ghi_chu_admin')
        
        # Lưu trạng thái cũ
        trang_thai_cu = yeu_cau.trang_thai
        
        # Cập nhật yêu cầu
        yeu_cau.trang_thai = trang_thai_moi
        yeu_cau.ghi_chu_admin = ghi_chu
        
        # Ghi lịch sử nếu trạng thái thay đổi
        if trang_thai_cu != trang_thai_moi:
            lich_su = NhatKyTrangThai(
                yeu_cau_id=id,
                trang_thai_cu=trang_thai_cu,
                trang_thai_moi=trang_thai_moi,
                ghi_chu=ghi_chu,
                nguoi_cap_nhat_id=session.get('user_id')
            )
            db.session.add(lich_su)
        
        db.session.commit()
        
        flash('Cập nhật trạng thái thành công!', 'success')
        return redirect(url_for('admin_view_request', id=id))
    
    # Lấy lịch sử trạng thái
    lich_su = NhatKyTrangThai.query.filter_by(yeu_cau_id=id).order_by(NhatKyTrangThai.ngay_cap_nhat.desc()).all()
    
    return render_template('admin/view.html', yeu_cau=yeu_cau, lich_su=lich_su)

@app.route('/admin/users')
@admin_required
def admin_users():
    users = NguoiDung.query.order_by(NguoiDung.ngay_tao.desc()).all()
    return render_template('admin/users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
