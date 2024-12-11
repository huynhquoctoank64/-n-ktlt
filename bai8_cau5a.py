import tkinter as tk

# Phương thức xử lý khi người dùng chọn một lựa chọn
def on_radio_select():
    selection = radio_var.get()  # Lấy giá trị của lựa chọn hiện tại
    label.config(text=f"Lựa chọn của bạn là: {selection}")

# Tạo cửa sổ đồ họa chính
window = tk.Tk()
window.title("Radio Button Example")  # Đặt tiêu đề cho cửa sổ
window.geometry("300x200")  # Đặt kích thước cho cửa sổ

# Tạo một biến để lưu giá trị của lựa chọn radio button
radio_var = tk.StringVar(value="Option 1")  # Giá trị mặc định là "Option 1"

# Tạo các radio button cho các lựa chọn
radio1 = tk.Radiobutton(window, text="Lựa chọn 1", variable=radio_var, value="Option 1", command=on_radio_select)
radio1.pack()

radio2 = tk.Radiobutton(window, text="Lựa chọn 2", variable=radio_var, value="Option 2", command=on_radio_select)
radio2.pack()

radio3 = tk.Radiobutton(window, text="Lựa chọn 3", variable=radio_var, value="Option 3", command=on_radio_select)
radio3.pack()

# Thêm một nhãn để hiển thị lựa chọn
label = tk.Label(window, text="Lựa chọn của bạn là: Option 1")
label.pack(pady=20)

# Chạy vòng lặp chính của cửa sổ đồ họa
window.mainloop()
