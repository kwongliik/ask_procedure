# Atur cara mengira isipadu kon

pi = 3.142

def kira_kon(jejari,tinggi): 
    isipadu_kon=(1/3) * pi * (jejari**2) * (tinggi)
    return isipadu_kon

def kon(isipadu):
    print(f"Isipadu kon = {isipadu:.2f}")

# Atur cara utama
r = float(input("Masukkan jejari:"))
h = float(input("Masukkan tinggi:"))
v = kira_kon(r, h)
kon(v)


