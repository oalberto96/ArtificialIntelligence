# Conway's Game of life

## Instalacion

### Pygame

```bash
sudo apt-get install python-pygame
```

Descargar el codigo fuente

```bash
sudo apt-get install mercurial
hg clone https://bitbucket.org/pygame/pygame
cd pygame
```

Instalar las dependencias
```bash
sudo apt-get install python3-dev python3-setuptools python3-numpy libsdl-dev libsdl-image1.2-dev \
  libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev \
  libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev
```

Compilar e instalar pygame
```bash
python3 setup.py build
sudo python3 setup.py install
```
## Reglas

1. Cualquier celula viva con menos de 2 vecinos muere por baja poblacion
1. Cualquier celula con mas de 3 vecinos vivos muere como causa de sobrepoblacion
1. Cualquier celula con 2 o 3 vecinos vive hasta la siguiente generacion
1. Cualquier celula muerta con exactamente 3 vecinos vivos, revive



#### Referencias
https://askubuntu.com/questions/401342/how-to-download-pygame-in-python3-3
http://web.stanford.edu/~cdebs/GameOfLife/
