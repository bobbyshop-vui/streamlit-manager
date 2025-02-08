import streamlit as st
import os
import csv

# Tiêu đề
st.title('Danh sách học sinh: :flag-vn:')

# Nhập thông tin học sinh
name = st.text_input('Vui lòng nhập tên học sinh:')
age = st.text_input('Bạn mấy tuổi:')
school_name = st.text_input('Tên trường học:')
so_thich = st.text_input('Sở thích:')
teacher_name = st.text_input('Tên giáo viên:')

# Nhập điểm các môn học
st.subheader("Nhập điểm các môn học:")
math = st.number_input("Toán:", min_value=0.0, max_value=10.0, step=0.1)
english = st.number_input("Tiếng Anh:", min_value=0.0, max_value=10.0, step=0.1)
history = st.number_input("Lịch Sử:", min_value=0.0, max_value=10.0, step=0.1)
geography = st.number_input("Địa Lý:", min_value=0.0, max_value=10.0, step=0.1)
vietnamese = st.number_input("Tiếng Việt:", min_value=0.0, max_value=10.0, step=0.1)
informatics = st.number_input("Tin Học:", min_value=0.0, max_value=10.0, step=0.1)

# Hiển thị thông tin đã nhập
st.subheader("Thông tin bạn đã nhập:")
st.write(f"**Tên học sinh:** {name}")
st.write(f"**Tuổi:** {age}")
st.write(f"**Tên trường học:** {school_name}")
st.write(f"**Sở thích:** {so_thich}")
st.write(f"**Tên giáo viên:** {teacher_name}")

# Hiển thị điểm đã nhập
st.subheader("Điểm số:")
st.write(f"Toán: {math} | Tiếng Anh: {english} | Lịch Sử: {history}")
st.write(f"Địa Lý: {geography} | Tiếng Việt: {vietnamese} | Tin Học: {informatics}")

# Lưu thông tin vào file CSV
FILE_PATH = "data.csv"

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Tên", "Tuổi", "Trường", "Sở thích", "Giáo viên", "Toán", "Tiếng Anh", "Lịch Sử", "Địa Lý", "Tiếng Việt", "Tin Học"])

if st.button("Lưu thông tin"):
    if name and age and school_name and so_thich and teacher_name:
        with open(FILE_PATH, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, age, school_name, so_thich, teacher_name, math, english, history, geography, vietnamese, informatics])
        st.success("Thông tin đã được lưu thành công!")
    else:
        st.error("Vui lòng nhập đầy đủ thông tin!")

# Hiển thị danh sách đã lưu
st.subheader("Danh sách học sinh đã nhập:")
if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)

    if len(data) > 0:
        for row in data:  # Bỏ qua tiêu đề
            if len(row) >= 11:  # Kiểm tra đủ cột trước khi truy cập
                st.write(f"**Tên:** {row[0]} | **Tuổi:** {row[1]} | **Trường:** {row[2]} | **Sở thích:** {row[3]} | **Giáo viên:** {row[4]}")
                st.write(f"Toán: {row[5]} | Tiếng Anh: {row[6]} | Lịch Sử: {row[7]}")
                st.write(f"Địa Lý: {row[8]} | Tiếng Việt: {row[9]} | Tin Học: {row[10]}")
                st.write("----")
            else:
                st.warning("Dữ liệu không hợp lệ hoặc thiếu cột!")
    else:
        st.write("Chưa có dữ liệu nào.")
else:
    st.write("Chưa có dữ liệu nào.")

# Phần giới thiệu bản thân
st.title('Tôi là ai?')
st.image("profile.jpg", caption="Ảnh của tôi", use_container_width=True)
st.write('Có thể bạn chưa biết tôi là ai? Nhưng tôi là **Lê Đình Quốc Hưng**. Tôi thích nhất là các ngôn ngữ lập trình: **PHP, Python, HTML, CSS, JS, Objective-C, Swift.**')
st.write('Tôi muốn giới thiệu về dự án web server: **webserverbobby-flaskpython** của tôi và link GitHub ở: [GitHub Repository](https://github.com/bobbyshop-vui/webserverbobby-flaskpython)')
st.write('Tôi thích Flask hơn Django hay Streamlit vì:')
st.write('- Flask: Là một framework Python phổ biến, có thể xây dựng từ các dự án nhỏ đến lớn. Tuy không có sẵn nhiều tính năng như Django nhưng có thể mở rộng dễ dàng bằng các thư viện ngoài, ví dụ như Flask-SQLAlchemy cho ORM.')
st.write('- Django: Mặc dù phức tạp nhưng có nhiều tính năng mạnh mẽ mà Flask không có khi không dùng thư viện ngoài.')
st.write('- Streamlit: Không có hệ thống route, nhưng giúp tạo ứng dụng web nhanh chóng mà không cần làm việc với HTML, CSS hay JavaScript.')
st.write(':copyright: **Lê Đình Quốc Hưng**. Tất cả quyền được bảo lưu.')
