from vpython import *
from math import*
from numpy import*

scene = canvas()



#tekst

scene.append_to_caption("\n")
Naslov = wtext(text="Harmonijski oscilator s prigušenjem", align="center", color=color.black) 
scene.append_to_caption("\n")


#widgeti svi, mijenjanje parametara, pokretanje itd



scene.append_to_caption("\n")



#postavljanje konstnanti

delta_t=0.0005 #rezultati ce bit tocniji sto je manji vremenski razmak
t=0
k=0.5
Lo=0.9 
m=0.02
b=0.05
v0 = 0



scene.append_to_caption("\n")

#Slider za konstantu opruge

wtext(text="Konstanta opruge", align="center", color=color.black, height=0.25)
scene.append_to_caption("\n")

def konstanta(s):
    global k, m, w0, beta, b
    k = s.value
    
    w0 = sqrt(k / m)
    beta = a * w0
    b = 2 * m * beta
    
    opis_konstanta.text = 'k = '+'{:1.2f}'.format(ks.value)+"N/m"+"\n\n"
ks = slider(bind=konstanta,min=0.1,max=10,value=0.5)
opis_konstanta = wtext(text='k = '+'{:1.2f}'.format(ks.value)+"N/m"+"\n\n")

scene.append_to_caption("\n")
wtext(text="Masa tijela", align="center", color=color.black, height=0.25)
scene.append_to_caption("\n")

#Slider za masu tijela

def masa(d):
    global m, w0, beta, b, k
    m = d.value
    
    w0 = sqrt(k / m)
    beta = a * w0
    b = 2 * m * beta
    
    opis_masa.text = ' m = '+'{:1.2f}'.format(ms.value)+"kg"+"\n\n"
ms = slider(bind=masa,min=0.02,max=0.5,value=0.02)
opis_masa = wtext(text=' m = '+'{:1.2f}'.format(ms.value)+"kg"+"\n\n")

scene.append_to_caption("\n")
wtext(text="Početni položaj", align="center", color=color.black, height=0.25)
scene.append_to_caption("\n")

poc_pozicija=0.25


#Slider za početni položaj tijela --> udaljenost od zida

def pocetni_polozaj(iznos_polozaja):
    global poc_pozicija
    
    poc_pozicija = Lo+iznos_polozaja.value
    
    opis_poc_polozaja.text = ' x0 = '+'{:1.2f}'.format(polozajs.value)+"m"+"  "
polozajs = slider(bind=pocetni_polozaj,min=-0.7,max=0.7,value=-0.65)
opis_poc_polozaja = wtext(text=' x0 = '+'{:1.2f}'.format(polozajs.value)+"m"+"  ")

#Slider za početnu brzinu tijela

scene.append_to_caption("\n\n\n")
wtext(text="Početna brzina", align="center", color=color.black, height=0.25)
scene.append_to_caption("\n")

def pocetna_brzina(iznos_brzine):
    global v0, v
    
    v0 = iznos_brzine.value
    
    opis_brzina.text = ' v0 = '+'{:1.2f}'.format(brzinas.value)+"m/s"+"  "
brzinas = slider(bind=pocetna_brzina,min=-1,max=1,value=0)
opis_brzina = wtext(text=' v0 = '+'{:1.2f}'.format(brzinas.value)+"m/s"+"  ")



v=v0


#gumb za novi početni polozaj tijela

scene.append_to_caption("\n\n")

def novi_x0_v0(b): 
    global tijelo, opruga, Lhat, x, ptijela, stol,v
    
    v=v0
    
    
    #brišem staro i crtam novo sve
    
    tijelo.visible=False
    del tijelo
    opruga.visible=False
    del opruga
    
    ptijela=m*vector(v,0,0)#za brzinu 
    tijelo=box(pos=vector(poc_pozicija,0,0), size=vector(0.1,0.1,0.1), color=color.blue, make_trail=False)
    stol=box(pos=vector(0,-0.05,0), size=vector(5,0.01,2), color=color.white, make_trail=False)
    zid=box(pos=vector(0,0.01,0), size=vector(0.01,0.5,0.5), color=color.white, make_trail=False)
    opruga=helix(pos=vector(0,0,0), axis=tijelo.pos-zid.pos, radius=0.05)
    L=tijelo.pos
    Lhat=hat(L) #smjer
    x=mag(L)-Lo #produljenje
        
    return

button(text="Potvrdi x0 i v0", bind=novi_x0_v0)
scene.append_to_caption("\n\n")




a=0 #prvo stavljam oscilator bez prigušenja
b=0
beta=0
w0=0
#Slider za koeficijent prigušenja tijela

scene.append_to_caption("\n")
wtext(text="Konstanta o kojoj ovisi prigušenje", align="center", color=color.black, height=0.25)
scene.append_to_caption("\n")


koja_je_vrsta=""


def iznos_konst(slide):
    global a, w0, beta, b, m, vrstaprigusenja, koja_je_vrsta
    a = slide.value
    
    w0 = sqrt(k / m)
    beta = a * w0
    b = 2 * m * beta
    
    #za printanje vrste prigusenja
    
    vrstaprigusenja=""
    koja_je_vrsta=""
    
    prigusenja=[", bez prigušenja", ", podkritično prigušeno", ", kritično prigušeno", ", nadkritično prigušeno"]
    
    if a==0:
        indeks=0    
    elif round(a,1)>0 and round(a,1)<1:
        indeks=1
    elif round(a,1)==1:
        indeks=2 
    elif round(a,1)>1:
        indeks=3
        
    vrstaprigusenja=prigusenja[indeks]
    koja_je_vrsta= str(round(a,1)) + str(vrstaprigusenja)
    
    opis_koeficijenta.text = ' a ≈ '+koja_je_vrsta+" "+"\n\n"
koef_s = slider(bind=iznos_konst,min=0,max=1.5,value=0)
opis_koeficijenta = wtext(text=" a = 0, bez prigušenja "+"\n\n")




scene.append_to_caption("\n\n\n\n")



w0 = sqrt(k / m)
beta = a * w0 #ovaj a mi govori kakvo je prigusenje
b = 2 * m * beta






#crtaje stola, tijela, zida, opruge

ptijela=m*vector(0,0,0)#za brzinu 
tijelo=box(pos=vector(poc_pozicija,0,0), size=vector(0.1,0.1,0.1), color=color.blue, make_trail=False)
stol=box(pos=vector(0,-0.05,0), size=vector(5,0.01,2), color=color.white, make_trail=False)
zid=box(pos=vector(0,0.01,0), size=vector(0.01,0.5,0.5), color=color.white, make_trail=False)
opruga=helix(pos=vector(0,0,0), axis=tijelo.pos-zid.pos, radius=0.05)
L=tijelo.pos
Lhat=hat(L) #smjer
x=mag(L)-Lo #produljenje

#x-t graf
g1 = graph(xtitle="t/s", ytitle="x/m", width=500, height=300)
fc = gcurve(color=color.red, graph=g1)

#E-t graf
# #energije mehanička, potencijalna, kinetička

g2 = graph(xtitle="t/s", ytitle="E/J", width=500, height=300)

Emechblock=gcurve(color=color.green, label="mehanička energija",graph=g2)
Peblock=gcurve(color=color.blue, label="potencijalna energija",graph=g2)
Keblock=gcurve(color=color.red, label="kinetička energija",graph=g2)


#v-t graf

g3 = graph(xtitle="t/s", ytitle="v/ m/s", width=500, height=300)
vc = gcurve(color=color.black, graph=g3)

#a-t graf
g4 = graph(xtitle="t/s", ytitle="a/ m/s2", width=500, height=300)
ac = gcurve(color=color.blue, graph=g4)


#pauziranje i pokretanje

running = True
def Run(b): # b = button
    global running, remember_dt, delta_t, L, Lhat, x, pamti_poc_poziciju
    running = not running
    if running:
        b.text = "Pause"
        delta_t = remember_dt
    else: 
        b.text = "Run"
        remember_dt = delta_t
        delta_t = 0
        
    return

button(text="Pause", pos=scene.title_anchor, bind=Run)

while True:
    rate (200)
        
            
    Ke=0.5/m*mag(ptijela)**2
    Pe=0.5*k*x**2
    Emech=Pe+Ke
    Keblock.plot( pos=(t,Ke) )
    Peblock.plot( pos=(t,Pe) )
    Emechblock.plot(pos=(t,Emech))
    
    Fopruge=-k*x*Lhat
    Fotpora=b*(-ptijela/m)
    ptijela=ptijela+(Fopruge+Fotpora)*delta_t
    tijelo.pos=tijelo.pos+ptijela*delta_t/m
    opruga.axis=tijelo.pos-zid.pos
    L=tijelo.pos
    Lhat=hat(L)
    x=mag(L)-Lo
    
    #za pomak, brzinu i akceleraciju graf
    akc = -b * v / m - k * x / m #prema formuli
    v = v + akc * delta_t
    
    t = t + delta_t
    fc.plot(t, x)
    vc.plot(t,v)
    ac.plot(t,akc)

    
    






