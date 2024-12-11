print ("sinh vien:Huynh Quoc Toan MSV:235752021610081")
ds = input('Danh sách: ')
'''Sử dụng hàm split() để chia chuỗi thành danh sách
với các phần tử cách nhau bởi dấu trống hoặc tab'''
elements = ds.split()
# In ra danh sách theo thứ tự ngược lại
print("Dãy theo thứ tự ngược lại là:", ' '.join(elements[::-1]))


