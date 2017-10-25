## Instalacion

### Pygame

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

#### Referencias
https://askubuntu.com/questions/401342/how-to-download-pygame-in-python3-3

