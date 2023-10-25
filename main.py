import random

sayı=int(input("sayı girin"))

dogruCevap = random.randint(0,10)


if sayı==dogruCevap:
    print("tebrikler tek seferde bildiz")

else:
    if sayı>dogruCevap:
        print("aşağı")
        sayı=int(input("sayı girin"))
        if sayı==dogruCevap:
            print("doğru bildiniz")
        else :
            print("yanlış bildiniz " + format(dogruCevap))    
    elif sayı<dogruCevap:
        print("yukarı")
        sayı=int(input("yeniden sayıyı girin"))
        if sayı==dogruCevap:
            print("doğru bildin")
        else:
            print ("yanlış bildin"+ format (dogruCevap))  
