from matplotlib import pyplot as plt
from matplotlib import font_manager as fm
import numpy as np

def find_sys_fonts():
    # find installed system fonts
    fonts = fm.findSystemFonts(fontpaths=None, fontext='ttf')
    fonts.sort()
    print(' \n'.join(fonts))
    
def show_avl_fonts():
    fonts = fm.fontManager.ttflist
    fonts = sorted(fonts, key=lambda f: f.name)
    for font in fonts:
        print('NAME: {0:<10} STYLE: {1:<8} FILE: {2:<8}'.format(font.name, font.style, font.fname.split('/')[-1]))

#%% 
#find_sys_fonts()
#show_avl_fonts()
#fm._rebuild()
plt.rcParams['font.family'] = 'Libertinus Serif'
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Libertinus Serif'
plt.rcParams['mathtext.it'] = 'Libertinus Serif:italic'
plt.rcParams['mathtext.bf'] = 'Libertinus Serif:bold'
#%%
x = np.linspace(0, 7, 1000)
plt.plot(x, np.sin(x), label=r'$\frac{ab}{cd\pi} \sum_{i=0}\log(1)$')
plt.xlabel(r'$x_\mathrm{y}$')
plt.legend()
plt.show()