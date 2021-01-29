'''
Name: matplotlib_tutorial.py
Author: Patrick Walsh
Date: 1/28/2021
Purpose: Program shows basics of matplotlib, how
to create line plots, bar graphs, and show images.


Comment: Run following command to generate pylintrc file in directory
where pylint command is being run:
pylint --generate-rcfile | out-file -encoding utf8 .pylintrc
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# t = np.arange(0, 5, 0.2)  # arange(start, stop, step(optional))

# plt.plot([1, 2, 3, 4])  # single list presumes just y values

# plt.plot([1, 2, 3, 4], ["a", "b", "c", "d"])  # ([x values], [y values])

# plt.plot([1, 2, 3, 4], [5, 4, 6, 1], 'b--')  # optional third argument for color and type of plot
# 'b-' default value, solid blue line
# 'g-' solid green line
# 'b--' dashed blue line
# 'ro' red circles for plot
# 'bo' blue circles for plot
# 'go' green circles for plot
# Complete documentation:
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

# plt.axis([0, 10, 0, 80])  # axis([xmin, xmax, ymin, ymax]) for limits of graph
#
# plt.title("MATPLOTLIB is awesome")  # title above graph
# plt.text(x=0.5, y=5.5, s="Start!")  # text labels (x=coord, y=coord, s="string")
# plt.text(x=3.5, y=0.5, s="Finish!")  # text labels (x=coord, y=coord, s="string")
#
# plt.ylabel("Y values")  # text along y axis
# plt.xlabel("X values")  # text along x axis

# plt.plot(t, t, 'r-')  # plot(x, y, 'argument')
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')  # making multiple plots at once

# bar graph
# labels = ["Python", "Java", "SQL"]
# values = [230, 431, 364]
# plt.bar(labels, values)
# plt.suptitle("Most Popular Languages")

# show images
# https://matplotlib.org/tutorials/introductory/images.html#sphx-glr-tutorials-introductory-images-py
# first, import matplotlib.image
img = mpimg.imread(r"C:\\Users\\pwalsh\\Desktop\\School\\UMGC\\SDEV300\\Week 3\\Cafeteria-sharedassets0.assets-217.png")
# print(img)  # see values of image as numpy array
plt.imshow(img)  # display image in plot window

plt.show()  # show plot
