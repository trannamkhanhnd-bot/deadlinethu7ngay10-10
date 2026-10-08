import random
so_bi_mat = random.randint(1, 100)
print("TRÒ CHƠI ĐOÁN SỐ BÍ MẬT")
print("Máy tính đã chọn một số trong khoảng từ 1 đến 100. Hãy đoán xem là số nào!")
while True:
    so_doan = int(input("Nhập số bạn đoán:"))
    if so_doan == so_bi_mat:
        print("Chúc mừng! Bạn đã đoán đúng số bí mật.")
        break
    elif so_doan < so_bi_mat:
        print("Số bạn đoán nhỏ hơn số bí mật. Try again.")
    else:
        print("Số bạn đoán lớn hơn số bí mật. Try again.")
    