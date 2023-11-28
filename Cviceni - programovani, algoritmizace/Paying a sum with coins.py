def rozklad( zaplatit, typy_minci ):
    def rozklady( moje_mince, zbyva_zaplatit, zaplaceno):
        if zbyva_zaplatit == 0:
            return print(zaplaceno)
        for mince in list(moje_mince):
            if mince <= zbyva_zaplatit:
                rozklady( list(moje_mince), zbyva_zaplatit - mince, zaplaceno + str(mince) + " ")
            moje_mince.remove(mince)
        return None
    rozklady(list(typy_minci), zaplatit, "")
            
pocet_minci = int(input())
typy_minci = [0]*pocet_minci
mince = input().split()
for i in range(pocet_minci):
    typy_minci[i] = int(mince[i])
zaplatit = int(input())

rozklad(zaplatit,typy_minci)