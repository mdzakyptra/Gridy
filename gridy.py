import os 

def coin_change(targetCoin, coin_list):
   
    
    result = {}
    
    while targetCoin > 0 and coin_list != []:
        
        coinTerbesar = max(coin_list)
        
        
        if coinTerbesar <= targetCoin:
            hitungCoin = targetCoin // coinTerbesar  
            targetCoin -= coinTerbesar * hitungCoin  
            result[coinTerbesar] = hitungCoin
        else:
            
            coin_list.remove(coinTerbesar)
    
    
    if targetCoin != 0:
        print("Tidak bisa memberikan kembalian yang tepat.")
    else:
    
        print("\nHasil kembalian:")
        for coin, hitungCoin in result.items():
            print(f"Coin {coin}: {hitungCoin} keping")


def menu():
    
    while True:
        try:
            targetCoin = int(input("Masukkan jumlah target coin: "))
            if targetCoin <= 0:
                raise ValueError("Jumlah target coin harus lebih dari 0")
            break
        except ValueError: 
            print("Input yang integer integer aja dan spasinya hanya sekali")

    while True:
        try:
            coin_list = list(map(int, input("Masukkan daftar coin yang tersedia (pisahkan dengan spasi): ").split()))
            if any(c <= 0 for c in coin_list):
                raise ValueError("Nilai koin harus lebih besar dari 0.")
            break
        except ValueError:
            print("Nilai Error")

    print(f"\nDaftar coin yang tersedia: {coin_list}")
    print(f"Target coin: {targetCoin}")
    
    
    coin_change(targetCoin, coin_list)

    
    while True:
        ulangi = input("\nApakah Anda ingin mencoba lagi? (y/n): ").lower() 
        if ulangi == 'y':
            os.system("cls") 
            menu()
        elif ulangi == 'n':
            os.system("cls") 
            print("Terima kasih dan assalamualaikum")
            exit() 
        else:
            os.system("cls") 
            print("Masukkan y atau n")
menu()
