def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Yıldızlardan önce boşluk ekle
        print(" " * (rows - i), end="")
        
        # Şuanki satır için yıldız yazma
        print("* " * i)
        

print_pyramid(5)