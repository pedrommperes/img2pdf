from PIL import Image
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

dir_path = os.path.dirname(os.path.realpath(__file__))

root = Tk()
root.withdraw()
filename = askopenfilename(title="Select file")
root.update()
root.destroy()

image1 = Image.open(filename)
im1 = image1.convert('RGB')

base = os.path.basename(filename)
base_ext = os.path.splitext(base)[0]

im1.save(base_ext + ".pdf")
