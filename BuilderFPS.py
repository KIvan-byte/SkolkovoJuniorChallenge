from PIL import Image

def transparency(filename1, filename2):
    images = [Image.open(x) for x in [filename1, filename2]]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save('twoFPS.jpg')

if __name__ == '__main__':
    transparency('csgo.jpg','analytics.jpg')