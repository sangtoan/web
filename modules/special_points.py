import streamlit as st
from sympy import symbols, sqrt, Eq, solve, latex, simplify, Point, Matrix

def special_points_calculator():
    st.header("Tính toán các điểm đặc biệt trong tam giác")

    # Checkbox cho lựa chọn 2D hoặc 3D
    is_2d = st.checkbox("2D", value=True)
    is_3d = st.checkbox("3D", value=False)

    if is_2d:
        is_3d = False
    elif is_3d:
        is_2d = False

    # Tạo các input cho các điểm A, B, C
    Ax, Ay = st.text_input("Điểm A (x, y):", "0, 0").split(',')
    Bx, By = st.text_input("Điểm B (x, y):", "0, 0").split(',')
    Cx, Cy = st.text_input("Điểm C (x, y):", "0, 0").split(',')

    Az = Bz = Cz = "0"  # Khởi tạo giá trị mặc định cho z
    if is_3d:
        Az = st.text_input("Điểm A (z):", "0")
        Bz = st.text_input("Điểm B (z):", "0")
        Cz = st.text_input("Điểm C (z):", "0")

    # Các nút tính toán
    if st.button("Trực Tâm"):
        if is_2d:
            result = calculate_orthocenter(float(Ax), float(Ay), float(Bx), float(By), float(Cx), float(Cy))
        else:
            result = calculate_orthocenter_3d(float(Ax), float(Ay), float(Az), float(Bx), float(By), float(Bz), float(Cx), float(Cy), float(Cz))
        st.latex(result)
    
    if st.button("Tâm Nội Tiếp"):
        if is_2d:
            result = calculate_incenter(float(Ax), float(Ay), float(Bx), float(By), float(Cx), float(Cy))
        else:
            result = calculate_incenter_3d(float(Ax), float(Ay), float(Az), float(Bx), float(By), float(Bz), float(Cx), float(Cy), float(Cz))
        st.latex(result)

    if st.button("Chân Đường Cao Đỉnh A"):
        if is_2d:
            result = calculate_altitude_foot(float(Ax), float(Ay), float(Bx), float(By), float(Cx), float(Cy))
        else:
            result = calculate_altitude_foot_3d(float(Ax), float(Ay), float(Az), float(Bx), float(By), float(Bz), float(Cx), float(Cy), float(Cz))
        st.latex(result)

    # Thêm các nút tính toán khác
    if st.button("Tâm Ngoại Tiếp"):
        if is_2d:
            result = calculate_circumcenter(float(Ax), float(Ay), float(Bx), float(By), float(Cx), float(Cy))
        else:
            result = calculate_circumcenter_3d(float(Ax), float(Ay), float(Az), float(Bx), float(By), float(Bz), float(Cx), float(Cy), float(Cz))
        st.latex(result)

    if st.button("Phân Giác Ngoài A"):
        if is_2d:
            result = calculate_exterior_bisector(float(Ax), float(Ay), float(Bx), float(By), float(Cx), float(Cy))
        else:
            result = calculate_exterior_bisector_3d(float(Ax), float(Ay), float(Az), float(Bx), float(By), float(Bz), float(Cx), float(Cy), float(Cz))
        st.latex(result)

def calculate_orthocenter(Ax, Ay, Bx, By, Cx, Cy):
    Hx, Hy = symbols('Hx Hy')
    equation1 = Eq((Hx - Ax) * (Cx - Bx) + (Hy - Ay) * (Cy - By), 0)
    equation2 = Eq((Hx - Bx) * (Ax - Cx) + (Hy - By) * (Ay - Cy), 0)
    solutions = solve((equation1, equation2), (Hx, Hy))
    if isinstance(solutions, dict):
        Hx_sol = solutions[Hx]
        Hy_sol = solutions[Hy]
        return f"Trực tâm: \\(\\left({latex(Hx_sol)}, {latex(Hy_sol)}\\right)\\)"
    else:
        return "Không tìm thấy trực tâm."

def calculate_orthocenter_3d(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz):
    Hx, Hy, Hz = symbols('Hx Hy Hz')
    AH = Matrix([Hx - Ax, Hy - Ay, Hz - Az])
    BH = Matrix([Hx - Bx, Hy - By, Hz - Bz])
    BC = Matrix([Cx - Bx, Cy - By, Cz - Bz])
    AC = Matrix([Cx - Ax, Cy - Ay, Cz - Az])
    AB = Matrix([Bx - Ax, By - Ay, Bz - Az])
    
    eq1 = Eq(AH.dot(BC), 0)
    eq2 = Eq(BH.dot(AC), 0)
    eq3 = Eq(AB.cross(AC).dot(AH), 0)
    
    solution = solve((eq1, eq2, eq3), (Hx, Hy, Hz))
    if solution:
        Hx_sol = solution[Hx]
        Hy_sol = solution[Hy]
        Hz_sol = solution[Hz]
        return f"Trực tâm: \\(\\left({latex(Hx_sol)}, {latex(Hy_sol)}, {latex(Hz_sol)}\\right)\\)"
    else:
        return "Không tìm thấy trực tâm."

def calculate_incenter(Ax, Ay, Bx, By, Cx, Cy):
    A = Point(Ax, Ay)
    B = Point(Bx, By)
    C = Point(Cx, Cy)

    a = B.distance(C)
    b = C.distance(A)
    c = A.distance(B)

    Ix = (a * Ax + b * Bx + c * Cx) / (a + b + c)
    Iy = (a * Ay + b * By + c * Cy) / (a + b + c)

    return f"Tâm nội tiếp: \\(\\left({latex(simplify(Ix))}, {latex(simplify(Iy))}\\right)\\)"

def calculate_incenter_3d(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz):
    A = Point(Ax, Ay, Az)
    B = Point(Bx, By, Bz)
    C = Point(Cx, Cy, Cz)

    a = B.distance(C)
    b = C.distance(A)
    c = A.distance(B)

    Ix = (a * Ax + b * Bx + c * Cx) / (a + b + c)
    Iy = (a * Ay + b * By + c * Cy) / (a + b + c)
    Iz = (a * Az + b * Bz + c * Cz) / (a + b + c)

    return f"Tâm nội tiếp: \\(\\left({latex(simplify(Ix))}, {latex(simplify(Iy))}, {latex(simplify(Iz))}\\right)\\)"

def calculate_altitude_foot(Ax, Ay, Bx, By, Cx, Cy):
    Hx, Hy = symbols('Hx Hy')
    equation1 = Eq((Hx - Ax) * (Cx - Bx) + (Hy - Ay) * (Cy - By), 0)
    equation2 = Eq((Hx - Bx) * (Ax - Cx) + (Hy - By) * (Ay - Cy), 0)
    solutions = solve((equation1, equation2), (Hx, Hy))
    if isinstance(solutions, dict):
        Hx_sol = solutions[Hx]
        Hy_sol = solutions[Hy]
        return f"Chân đường cao: \\(\\left({latex(Hx_sol)}, {latex(Hy_sol)}\\right)\\)"
    else:
        return "Không tìm thấy chân đường cao."

def calculate_altitude_foot_3d(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz):
    Hx, Hy, Hz, t = symbols('Hx Hy Hz t')
    equation1 = Eq((Hx - Ax) * (Cx - Bx) + (Hy - Ay) * (Cy - By) + (Hz - Az) * (Cz - Bz), 0)
    equation2 = Eq((Hx - Bx), t * (Bx - Cx))
    equation3 = Eq((Hy - By), t * (By - Cy))
    equation4 = Eq((Hz - Bz), t * (Bz - Cz))

    solutions = solve((equation1, equation2, equation3, equation4), (Hx, Hy, Hz, t))
    if isinstance(solutions, dict):
        Hx_sol = solutions[Hx]
        Hy_sol = solutions[Hy]
        Hz_sol = solutions[Hz]
        return f"Chân đường cao: \\(\\left({latex(Hx_sol)}, {latex(Hy_sol)}, {latex(Hz_sol)}\\right)\\)"
    else:
        return "Không tìm thấy chân đường cao."

def calculate_circumcenter(Ax, Ay, Bx, By, Cx, Cy):
    x, y = symbols('x y')
    equation1 = Eq(sqrt((x - Ax) ** 2 + (y - Ay) ** 2), sqrt((x - Bx) ** 2 + (y - By) ** 2))
    equation2 = Eq(sqrt((x - Bx) ** 2 + (y - By) ** 2), sqrt((x - Cx) ** 2 + (y - Cy) ** 2))
    solution = solve((equation1, equation2), (x, y))
    if solution:
        x_sol = solution[0][0]
        y_sol = solution[0][1]
        return f"Tâm ngoại tiếp: \\(\\left({latex(x_sol)}, {latex(y_sol)}\\right)\\)"
    else:
        return "Không tìm thấy tâm ngoại tiếp."

def calculate_circumcenter_3d(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz):
    Hx, Hy, Hz = symbols('Hx Hy Hz')
    AH = Matrix([Hx - Ax, Hy - Ay, Hz - Az])
    AC = Matrix([Cx - Ax, Cy - Ay, Cz - Az])
    AB = Matrix([Bx - Ax, By - Ay, Bz - Az])

    mixed_product = AB.cross(AC).dot(AH)
    eq3 = Eq(mixed_product, 0)

    equation1 = Eq(sqrt((Hx - Ax) ** 2 + (Hy - Ay) ** 2 + (Hz - Az) ** 2), sqrt((Hx - Bx) ** 2 + (Hy - By) ** 2 + (Hz - Bz) ** 2))
    equation2 = Eq(sqrt((Hx - Bx) ** 2 + (Hy - By) ** 2 + (Hz - Bz) ** 2), sqrt((Hx - Cx) ** 2 + (Hy - Cy) ** 2 + (Hz - Cz) ** 2))

    solution = solve((equation1, equation2, eq3), (Hx, Hy, Hz))
    if solution:
        Hx_sol = solution[0][0]
        Hy_sol = solution[0][1]
        Hz_sol = solution[0][2]
        return f"Tâm ngoại tiếp: \\(\\left({latex(Hx_sol)}, {latex(Hy_sol)}, {latex(Hz_sol)}\\right)\\)"
    else:
        return "Không tìm thấy tâm ngoại tiếp."

def calculate_exterior_bisector(Ax, Ay, Bx, By, Cx, Cy):
    k = symbols('k')
    Hx = (Bx - k * Cx) / (1 - k)
    Hy = (By - k * Cy) / (1 - k)
    equation = Eq((Ax - Hx)**2 + (Ay - Hy)**2, (Ax - Bx)**2 + (Ay - By)**2)
    solution = solve(equation, k)
    if solution:
        Hx_sol = (Bx - solution[0] * Cx) / (1 - solution[0])
        Hy_sol = (By - solution[0] * Cy) / (1 - solution[0])
        return f"Chân phân giác ngoài: \\(\\left({latex(simplify(Hx_sol))}, {latex(simplify(Hy_sol))}\\right)\\)"
    else:
        return "Không tìm thấy chân phân giác ngoài."

def calculate_exterior_bisector_3d(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz):
    k = symbols('k')
    Hx = (Bx - k * Cx) / (1 - k)
    Hy = (By - k * Cy) / (1 - k)
    Hz = (Bz - k * Cz) / (1 - k)
    equation = Eq((Ax - Hx)**2 + (Ay - Hy)**2 + (Az - Hz)**2, (Ax - Bx)**2 + (Ay - By)**2 + (Az - Bz)**2)
    solution = solve(equation, k)
    if solution:
        Hx_sol = (Bx - solution[0] * Cx) / (1 - solution[0])
        Hy_sol = (By - solution[0] * Cy) / (1 - solution[0])
        Hz_sol = (Bz - solution[0] * Cz) / (1 - solution[0])
        return f"Chân phân giác ngoài: \\(\\left({latex(simplify(Hx_sol))}, {latex(simplify(Hy_sol))}, {latex(simplify(Hz_sol))}\\right)\\)"
    else:
        return "Không tìm thấy chân phân giác ngoài."

# Chạy ứng dụng Streamlit
if __name__ == "__main__":
    special_points_calculator()
