import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=4000                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

#plt.figure(0)                             # Nova figura
#plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
#plt.xlabel('t en segons')                 # Etiqueta eix temporal
#plt.title('5 periodes de la sinusoide')   # Títol del gràfic
#plt.show()                                # Visualització de l'objecte gràfic. 

import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
#sd.play(x, fm)                # Reproducció d'àudio
#Ejercicio 2
audio, frecuencia_muestreo = sf.read('so_exemple1.wav')
#sd.play(audio, frecuencia_muestreo)
plt.figure(0)                             
plt.plot(t[0:Ls], audio[0:Ls])               
plt.xlabel('t en segons')                 
plt.title('5 periodes de la sinusoide')
plt.show()

from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(audio,abs(audio))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(audio,np.unwrap(np.angle(audio)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics


#exercici 4
x,fm = sf.read('luzbel44.wav') 
print(fm) #Freqüència de mostratge.
print(x.length())#Nombre de mostres de senyal.

temps=0.025#segment de senyal de 25ms
m=int(fm*temps)
Tm=1/fm
t=Tm*np.arange(m)
plt.figure(1)                             
plt.plot(t[0:m], audio[0:m])               
plt.xlabel('t en segons')                 
plt.title('0.025s')
plt.show()