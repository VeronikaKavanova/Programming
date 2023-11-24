def vyres_dve_rovnice_o_dvou_neznamych(a,b,c,d,e,f,g,h):
    """rovnice jsou ve tvaru:
        a + bx = c + dy
        e + fx = g + hy"""
    
    matice = [
    [b,-d,c-a],
    [f,-h,g-e]
    ]
    print(matice)

    nasobek = -(f//b)
    print(nasobek)
    for i in range(len(matice[1])-1):
        matice[1][i] += matice[0][i]*nasobek
    
    print(matice)

    y = matice[1][2]//matice[1][1]
    x = (matice[0][2]-matice[0][1])//matice[0][0]

    print(x,y)

vyres_dve_rovnice_o_dvou_neznamych(1,1,1,1,2,3,4,5)