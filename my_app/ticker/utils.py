import os,datetime

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import ArtistAnimation


def anim_create(text):
    name=text
    matplotlib.use('agg')
    plt.rcParams['animation.ffmpeg_path'] = f'{os.getcwd()}/ffmpeg_linux'
    plt.style.use('dark_background')
    fig=plt.figure(figsize=(1, 1), dpi=(100)) # Размер клипа
    
    
    frames=[]

    for i in text:
        line=plt.figtext(-1,0.5, s=text, size=12)
        frames.append([line])
        text=text[1:]

    anim=ArtistAnimation(fig,frames,interval=100)
    FFwriter = animation.FFMpegWriter(fps=10)
    # FFwriter.frame_size(100,100)
    anim.save(f'media/{name}.mp4', writer = FFwriter)
