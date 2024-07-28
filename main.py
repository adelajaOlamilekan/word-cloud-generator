import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image, ImageOps
import pandas as pd
from os import path
import os

texts = pd.read_csv("sees22.csv")["NAMES"].to_list()

for i in range(5):
    texts.append("ALRHO")
    texts.append("DAMILOLA")

text = ' '.join(str(text) for text in texts)

dir = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

image = ImageOps.grayscale(Image.open(path.join('SEES.png')))
image = ImageOps.autocontrast(image)
image = ImageOps.invert(image)

# Binarize the image (convert to black and white)
threshold = 128
image = image.point(lambda p: p > threshold and 255)

mask_kid = np.array(image)

plt.imshow(mask_kid, cmap='gray', interpolation='bilinear')
plt.show()

wc = WordCloud(stopwords=STOPWORDS, mask=mask_kid, background_color="white", max_font_size=40, max_words=10000, random_state=42)

texts = open(file=path.join("input_text.txt"), encoding="utf-8").read()
wc.generate(text)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()