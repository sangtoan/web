import streamlit as st

# Tiêu đề chính của ứng dụng
st.title("STex - Phần Mềm Hỗ Trợ Sử Dụng Latex")

# Tạo menu chính trong sidebar
main_menu = st.sidebar.selectbox("Chọn Menu Chính", [
    "Trộn Đề", "Giải Toán", "Tạo Bài Đồng Loạt", "Soát Lỗi", "Beamer",
    "Đề Tương Tự Theo Ma Trận", "MathPix2Tex-Đề Tự Luận", "Game Logic",
    "Phiếu Tô", "Tiện ích", "Trộn Đề 2025", "Thông tin tác giả"
])

# Hiển thị nội dung tương ứng với menu chính đã chọn
if main_menu == "Trộn Đề":
    st.header("Trộn Đề")
    # Nội dung và chức năng cho Trộn Đề
    # Ví dụ: thêm các input hoặc button liên quan đến chức năng trộn đề

elif main_menu == "Giải Toán":
    st.header("Giải Toán")
    # Tạo các nút cho từng chức năng
if st.button("Điều kiện đếm số"):
    # Gọi hàm hoặc mở dialog tương ứng với điều kiện đếm số
    st.write("Bạn đã chọn chức năng Điều kiện đếm số")
    # Điều hướng đến chức năng trong ConditionDialog()
    ConditionDialog()

if st.button("Điểm trong tam giác"):
    st.write("Bạn đã chọn chức năng Điểm trong tam giác")
    SpecialPointsTab()

if st.button("Tích vô hướng có hướng"):
    st.write("Bạn đã chọn chức năng Tích vô hướng có hướng")
    VectorCalculatorDialog()

if st.button("Tìm hình chiếu"):
    st.write("Bạn đã chọn chức năng Tìm hình chiếu")
    ProjectionCalculatorDialog()

if st.button("Tính diện tích và thể tích"):
    st.write("Bạn đã chọn chức năng Tính diện tích và thể tích")
    GeometryCalculatorDialog()

if st.button("Tính giới hạn hàm số"):
    st.write("Bạn đã chọn chức năng Tính giới hạn hàm số")
    LimitCalculatorDialog()

if st.button("Giải hệ phương trình"):
    st.write("Bạn đã chọn chức năng Giải hệ phương trình")
    SystemOfEquationsSolverDialog()

if st.button("Giải phương trình bậc cao"):
    st.write("Bạn đã chọn chức năng Giải phương trình bậc cao")
    AdvancedEquationSolverDialog()

if st.button("Tính khoảng cách điểm tới mặt phẳng"):
    st.write("Bạn đã chọn chức năng Tính khoảng cách điểm tới mặt phẳng")
    PlaneDistanceCalculatorDialog()

if st.button("Máy tính cơ bản"):
    st.write("Bạn đã chọn chức năng Máy tính cơ bản")
    Calculator()

if st.button("Phân tích đa thức"):
    st.write("Bạn đã chọn chức năng Phân tích đa thức")
    PolynomialOperationsDialog()

if st.button("Tính tổng hữu hạn"):
    st.write("Bạn đã chọn chức năng Tính tổng hữu hạn")
    FiniteSumCalculatorDialog()

# Các chức năng từ các module khác
if st.button("Tính tích phân"):
    st.write("Bạn đã chọn chức năng Tính tích phân")
    # Tích hợp các hàm từ tich_phan.py

if st.button("Nguyên hàm"):
    st.write("Bạn đã chọn chức năng Nguyên hàm")
    # Tích hợp các hàm từ nguyenham.py

if st.button("Đạo hàm"):
    st.write("Bạn đã chọn chức năng Đạo hàm")
    # Tích hợp các hàm từ dao_ham.py

if st.button("Khoảng cách giữa hai điểm"):
    st.write("Bạn đã chọn chức năng Khoảng cách giữa hai điểm")
    # Tích hợp các hàm từ khoang_cach_2diem.py

if st.button("Khoảng cách điểm tới đường"):
    st.write("Bạn đã chọn chức năng Khoảng cách điểm tới đường")
    # Tích hợp các hàm từ khoang_cach_diem_to_duong.py

if st.button("Khoảng cách giữa hai đường thẳng"):
    st.write("Bạn đã chọn chức năng Khoảng cách giữa hai đường thẳng")
    # Tích hợp các hàm từ khoang_cach_dt_to_dt.py

if st.button("Tổ hợp và xác suất"):
    st.write("Bạn đã chọn chức năng Tổ hợp và xác suất")
    CombinatoricsCalculatorDialog()

if st.button("Giải toán thống kê"):
    st.write("Bạn đã chọn chức năng Giải toán thống kê")
    # Tích hợp các hàm từ giai_toan_thong_ke.py

elif main_menu == "Tạo Bài Đồng Loạt":
    st.header("Tạo Bài Đồng Loạt")
    # Nội dung và chức năng cho Tạo Bài Đồng Loạt

elif main_menu == "Soát Lỗi":
    st.header("Soát Lỗi")
    # Nội dung và chức năng cho Soát Lỗi

elif main_menu == "Beamer":
    st.header("Beamer")
    # Nội dung và chức năng cho Beamer

elif main_menu == "Đề Tương Tự Theo Ma Trận":
    st.header("Đề Tương Tự Theo Ma Trận")
    # Nội dung và chức năng cho Đề Tương Tự Theo Ma Trận

elif main_menu == "MathPix2Tex-Đề Tự Luận":
    st.header("MathPix2Tex-Đề Tự Luận")
    # Nội dung và chức năng cho MathPix2Tex-Đề Tự Luận

elif main_menu == "Game Logic":
    st.header("Game Logic")
    # Nội dung và chức năng cho Game Logic

elif main_menu == "Phiếu Tô":
    st.header("Phiếu Tô")
    # Nội dung và chức năng cho Phiếu Tô

elif main_menu == "Tiện ích":
    st.header("Tiện ích")
    # Nội dung và chức năng cho Tiện ích

elif main_menu == "Trộn Đề 2025":
    st.header("Trộn Đề 2025")
    # Nội dung và chức năng cho Trộn Đề 2025

elif main_menu == "Thông tin tác giả":
    st.header("Thông tin tác giả")
    # Thông tin về tác giả hoặc các liên hệ liên quan
