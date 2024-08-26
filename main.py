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
    # Nội dung và chức năng cho Giải Toán
    # Ví dụ: bạn có thể tích hợp SymPy để giải toán

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
