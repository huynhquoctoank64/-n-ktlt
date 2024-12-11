import tkinter as tk

# Phương thức xử lý khi người dùng nhấn vào một indicator
def on_indicator_click(value):
    # Cập nhật màu sắc của tất cả indicator về mặc định (xám)
    indicator1.config(bg="gray")
    indicator2.config(bg="gray")
    indicator3.config(bg="gray")

    # Đổi màu của indicator được chọn (ví dụ: màu xanh lá)
    if value == "Option 1":
        indicator1.config(bg="green")
    elif value == "Option 2":
        indicator2.config(bg="green")
    elif value == "Option 3":
        indicator3.config(bg="green")

    # Cập nhật nhãn để hiển thị lựa chọn
    label.config(text=f"Lựa chọn của bạn là: {value}")

# Tạo cửa sổ đồ họa chính
window = tk.Tk()
window.title("Indicator Example")  # Đặt tiêu đề cho cửa sổ
window.geometry("300x300")  # Đặt kích thước cho cửa sổ

# Tạo các indicator (hình tròn) bằng canvas hoặc label
indicator1 = tk.Label(window, text="●", font=("Arial", 40), bg="gray", width=5, height=2)
indicator1.pack(pady=10)
indicator1.bind("<Button-1>", lambda e: on_indicator_click("Option 1"))

indicator2 = tk.Label(window, text="●", font=("Arial", 40), bg="gray", width=5, height=2)
indicator2.pack(pady=10)
indicator2.bind("<Button-1>", lambda e: on_indicator_click("Option 2"))

indicator3 = tk.Label(window, text="●", font=("Arial", 40), bg="gray", width=5, height=2)
indicator3.pack(pady=10)
indicator3.bind("<Button-1>", lambda e: on_indicator_click("Option 3"))

# Thêm một nhãn để hiển thị lựa chọn
label = tk.Label(window, text="Lựa chọn của bạn là: None")
label.pack(pady=20)

# Chạy vòng lặp chính của cửa sổ đồ họa
window.mainloop()
