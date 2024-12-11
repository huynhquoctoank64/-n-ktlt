import tkinter as tk

# Phương thức xử lý sự kiện khi nút được nhấn
def on_button_click():
    print("Nút đã được nhấn!")

# Tạo cửa sổ đồ họa chính
window = tk.Tk()
window.title("Cửa sổ Tkinter")  # Đặt tiêu đề cho cửa sổ
window.geometry("300x200")  # Đặt kích thước cho cửa sổ

# Thêm một nút vào cửa sổ
button = tk.Button(window, text="Nhấn vào tôi!", command=on_button_click, bg="blue", fg="white")
button.pack(pady=50)  # Sử dụng pack để đặt nút vào cửa sổ và thêm khoảng cách

# Xử lý sự kiện khi nhấn phím (ví dụ: phím "q")
def on_key_press(event):
    if event.char == 'q':
        print("Bạn đã nhấn phím 'q'!")
        window.quit()  # Đóng cửa sổ khi nhấn 'q'

# Gắn sự kiện xử lý phím cho cửa sổ
window.bind("<KeyPress>", on_key_press)

# Chạy vòng lặp chính của cửa sổ đồ họa
window.mainloop()
