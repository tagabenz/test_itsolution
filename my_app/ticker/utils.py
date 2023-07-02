import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import ArtistAnimation
import os


def anim_create(text):
    matplotlib.use('agg')
    plt.rcParams['animation.ffmpeg_path'] = f'{os.getcwd()}/ffmpeg'
    plt.style.use('dark_background')
    fig=plt.figure()

    frames=[]

    for i in text:
        line=plt.figtext(0,0.5, s=text, size=64)
        frames.append([line])
        text=text[1:]

    anim=ArtistAnimation(fig,frames,interval=100)
    FFwriter = animation.FFMpegWriter(fps=10)

    anim.save('animate.mp4', writer = FFwriter)
