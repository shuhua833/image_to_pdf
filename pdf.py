from PIL import Image
im1 = Image.open(r'e:\first.jpg')
im2 = Image.open(r'e:\second.jpg')
im3 = Image.open(r'e:\third.jpg')
im_list = [im2,im3]

im1.save(r"e:\myimage.pdf" ,save_all=True, append_images=im_list)
