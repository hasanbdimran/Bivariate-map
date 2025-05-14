import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import xycmap

x = 'std'
y = 'pct_flood'

corner_colors = ("white", "yellow", "cyan", "indigo")
n = (5, 5)  # x, y
cmap = xycmap.custom_xycmap(corner_colors=corner_colors, n=n)

colors = xycmap.bivariate_color(sx=test_shp[x], 
                                sy=test_shp[y], cmap=cmap)

fig, ax = plt.subplots(figsize=(10,10))
test_shp.plot(ax=ax, color=colors, ec='k')
cax = fig.add_axes([0.75, 0.25, 0.12, .12])
cax = xycmap.bivariate_legend(ax=cax, 
                              sx=test_shp[x], 
                              sy=test_shp[y], 
                              cmap=cmap)

legend_xticklabels = [np.round(float(i.get_text()), 1) for i in cax.get_xticklabels()]
legend_yticklabels = [np.round(float(i.get_text()), 1) for i in cax.get_yticklabels()]

cax.set_xticklabels(legend_xticklabels)
cax.set_yticklabels(legend_yticklabels)
cax.set_xlabel('Standard Deviation', fontsize=9)
cax.set_ylabel("Percent Flood (%)", fontsize=9)
cax.tick_params(axis='both', which='major', labelsize=8)
cax.tick_params(axis='x', which='major', labelrotation=90)

ax.set_xticks([])
ax.set_yticks([])
