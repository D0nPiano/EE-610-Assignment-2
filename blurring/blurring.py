from pyblur.PsfBlur import PsfBlur_random
from PIL import Image

#im = Image.open("Black_footed_Albatross_0005_2755588934.jpg")
im = Image.open("Frigatebird_0011_331410800.jpg")

im.show()

blurred, psf = PsfBlur_random(im)
blurred.show()