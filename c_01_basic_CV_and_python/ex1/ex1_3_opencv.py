# %% [markdown]
# # EX 1.3- Opencv: forest pyramid
# ## Prep
# This code is just to load everything... no need to read it
#%%
# to run in google colab
import sys
if 'google.colab' in sys.modules:
    ! apt-get install subversion
    ! svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_01_basic_CV_and_python/ex1/forest.jpg
    ! svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_01_basic_CV_and_python/ex1/pyramids.png

# to run interactively with vscode
import os
if os.getcwd().endswith("AI_is_Math"):
    os.chdir("c_01_basic_CV_and_python/ex1")

#%%
import numpy as np
import matplotlib.pyplot as plt
import cv2
#%%

forest_img = cv2.imread("forest.jpg")
pyramid_img = cv2.imread("pyramids.png")
pyramid_img = cv2.cvtColor(pyramid_img,cv2.COLOR_BGR2GRAY)
forest_img = cv2.cvtColor(forest_img,cv2.COLOR_BGR2GRAY)

#%%
# TODO: your goal is to build the pyramids in the forest!
#  Hints to think about:
#  - are the images the same size?
#  - How to mask/overlay the pixels from pyramids image to forest image
#
#  TODO: this section can be done in 3-5 lines of nice looking code, try not to write more then 10 lines here.
res_im = []

#%%
plt.figure()
plt.imshow(res_im, cmap='gray', vmin=0, vmax=255)
plt.show()
#%%