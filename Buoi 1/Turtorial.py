#bai 1---------------------------------------------------------------------
# print("nhap n1 = ")
# giatri1 = input()
# print("nhap n2 = ")
# giatri2 = input()
#
# def tinh():
#     n1 = int(giatri1)
#     n2 = int(giatri2)
#     tong = n1 + n2
#     hieu = n1 - n2
#     thuong = n1 / n2
#     tich  = n1 * n2
#     thuongdu = n1 % n2
#     mu = n1**n2
#     print("tong la: ", tong)
#     print("hieu la: ", hieu)
#     print("thuong la: ", thuong)
#     print("tich la: ", tich)
#     print("thuong du la: ", thuongdu)
#     print("mu la: ", mu)
#
# tinh()

#bai 2----------------------------------------------------------------------
# giatri1 = input('Nhap Diem: ')
#
# def chuyendiem():
#     diem = float(giatri1)
#     if(diem < 4.0):
#         print("F")
#     elif(4.0 <= diem <= 5.5):
#         print("D")
#     elif(5.5 <= diem <= 7.0):
#         print("C")
#     elif(7.0 <= diem <= 8.5):
#         print("B")
#     elif(8.5 <= diem <= 10):
#         print("A")
#
# chuyendiem()

#bai 3---------------------------------------------------------------------
# n = int(input('Nhap n = '))
#
# def uocso():
#     print("Uoc so cua ", n, "la: ")
#     for i in range(1, n + 1):
#         if(n%i == 0):
#             print(i)
# uocso()
#bai 4---------------------------------------------------------------------
# n = int(input('Nhap n = '))
# if(n == 1):
#     print( n,"La so nguyen to")
# elif(n % n and n % 1):
#     print(n,"La so nguyen to")
# else:
#     print(n,"Khong la so nguyen to")

#bai 5--------------------------------------------------------------------
# n = int(input('Nhap n = '))
# count = 0
# if(n==0):
#     print(1)
# else:
#     while(n != 0):
#         count += 1
#         n = n//10 #chia lay phan nguyen
# print(count)

#bai 6--------------------------------------------------------------------
n = int(input('Nhap n = '))
while (n != 0):
    print(n % 10, end="")
    n = n // 10  # Chia lấy phần nguyên











