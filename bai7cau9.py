print("Huynh Quoc Toan MSV:235752021610081")
import shutil

def copy_file(vunhom,vudong):
    shutil.copy(vunhom, vudong)

# Gọi hàm để sao chép tệp
copy_file('vunhom.txt', 'vudong.txt')

#Hàm shutil.copy() sao chép tệp từ vị trí nguồn sang vị trí đích.
# Đây là cách đơn giản và nhanh chóng để sao chép tệp mà không cần phải mở và đọc nội dung của tệp.
#Hàm này sao chép cả nội dung và quyền truy cập (permissions) của tệp.
