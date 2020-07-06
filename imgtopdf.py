
# Import modules

from fpdf import FPDF
from PIL import Image
import os
import time

# Get target folder and output file name

print('\n')
target = input(str('Enter location of folder containing images : '))
print('\n')
outname = input(str('Enter output pdf file name : '))
print('\n')

if outname == '':
 print('Output name can\'t be empty')
 exit()

if '.pdf' not in outname:
 outname = f"{outname}.pdf"
 print('.pdf added to output pdf file name\n')

# Check provided path

try:
 os.listdir(target)
except FileNotFoundError:
 print('\nInvalid path\n')
 exit()
except NotADirectoryError:
 print('\nPath provided is not a directory\n')
 exit()

# Store image names in a dict from target folder

dict = []

for name in os.listdir(target):
 if name.endswith(('.jpg', '.jpeg', '.png')):
  loc = str(os.path.join(target, name))
  dict.append(loc)

if len(dict) == 0:
 if target.endswith('/'):
  tar = target[:-1]
  print(f"\nNo image files found in {str(os.path.basename(tar))}")
  exit()
 else:
  print(f"\nNo image files found in {str(os.path.basename(target))}")
  exit()

# Print detected images

for index in range(0, len(dict)):
 print(os.path.basename(dict[index]))
 time.sleep(1)

print(f"\n{str(len(dict))} image files found\n\nConverting..\n")

time.sleep(5)

# Rotate landscape images if present

for index in range(0, len(dict)):
 img = Image.open(dict[index])

 width, height = img.size

 if width > height:

  img2 = img.transpose(Image.ROTATE_270) # Rotating landscape image

  os.remove(dict[index]) # Delete original

  img2.save(dict[index]) # Save rotated

# Add images from dict to a pdf file

pdf = FPDF()

for img in dict:
 pdf.add_page()
 pdf.image(img, 0, 0, 210, 297)  # 0, 0, 210, 297 is equivalent to an A4 page

# Save pdf in current directory

current = str(os.getcwd())
final_path = str(os.path.join(current, outname))
pdf.output(final_path, "F")
print(f"PDF with {str(len(dict))} image files generated!")

