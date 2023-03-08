from PIL import Image

obr = Image.new("RGB", (400,400,), 'cyan')
pixels = obr.load()
K = input("Napis suradnice (x,y) prveho bodu a oddel ich ciarkou: ")
L = input("Napis suradnice (x,y) bodu ktory chces spojit a oddel ich ciarkou: ")
K = K.split(",")
L = L.split(",")
Kx = int(K[0])
Ky = int(K[1])
Lx = int(L[0])
Ly = int(L[1])

if Kx < Lx:
    a = (Ly-Ky)/(Lx-Kx)
    b = Ky-a*Kx
    for x in range(Kx,Lx):
        y = int(a*x+b)
        pixels[x,y] = (30,50,0)
elif Kx == Lx:
    if Ky < Ly:
        for y in range(Ky,Ly):
            x = Kx
            pixels[x,y] = (30,50,0)
    elif Ky == Ly:
        x = Kx
        y = Ky
        pixels[x,y] = (30,50,0)
    else:
        for y in range(Ly,Ky):
            x = Kx
            pixels [x,y] = (30,50,0)
else:
    a = (Ky-Ky) / (Kx-Lx)
    b = Ly-a*Lx
    for x in range(Lx,Kx):
        y = int(a*x+b)
        pixels[x,y] = (30,50,0)

obr.show()