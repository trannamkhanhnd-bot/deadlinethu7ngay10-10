tong =0
so_luong = 0
so_chia_het_cho_3_va_5 = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        tong += i
        so_luong += 1
        print("Tổng các stn chia hết cho 3 hoặc 5 là:", tong)
        print("Số lượng các stn chia hết cho 3 hoặc 5 là:", so_luong)
        if i % 3 == 0 and i % 5 == 0:
            so_chia_het_cho_3_va_5 += 1
            print("Số lượng các stn chia hết cho 3 và 5 là:", so_chia_het_cho_3_va_5)