import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image, ImageOps
import pandas as pd
from os import path
import os
# from cairosvg import svg2png
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

PRIORITY_NAME = "MUJEEB"
DEPARTMENT = "SEES"
texts = pd.read_csv("sees22.csv")["NAMES"].to_list()

for _ in range(5):
    texts.append(PRIORITY_NAME)

text = ' '.join(str(text) for text in texts)

dir = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

image = ImageOps.grayscale(Image.open(path.join('SEES.png')))
image = ImageOps.autocontrast(image)
image = ImageOps.invert(image)

# Binarize the image (convert to black and white)
threshold = 128
image = image.point(lambda p: p > threshold and 255)

mask_kid = np.array(image)

fig = plt.figure( figsize=(20,10))

plt.imshow(mask_kid, cmap='gray', interpolation='bilinear')
plt.show()

wc = WordCloud(stopwords=STOPWORDS, mask=mask_kid, background_color="white", max_font_size=500, max_words=10000, random_state=42)

wc.generate(text)

plt.tight_layout(pad=0)

with open(f"{PRIORITY_NAME}_{DEPARTMENT}.svg", "w") as text_file:
    text_file.write(wc.to_svg())

# Convert SVG to PNG
# svg2png(url=f"{PRIORITY_NAME}_{DEPARTMENT}.svg", write_to=f"{PRIORITY_NAME}_{DEPARTMENT}.png")

# # Paths to input SVG and output PNG
# input_svg = f'{PRIORITY_NAME}_{DEPARTMENT}.svg'
# output_png = f'{PRIORITY_NAME}_{DEPARTMENT}.png'

# # Convert SVG to ReportLab graphics object
# drawing = svg2rlg(input_svg)

# # Render the graphics object to PNG
# renderPM.drawToFile(drawing, 'temp.png', fmt='PNG')

# # Open the temporary PNG file and save it with Pillow
# with Image.open('temp.png') as img:
#     img.save(output_png, 'PNG')

print(f"Converted {input_svg} to {output_png}")