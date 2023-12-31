import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import pandas as pd
import matplotlib.patches as patches
import matplotlib
from PIL import Image, ImageChops


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


def create_scalebar(
    filename: str,
    conversion_factor: float,
    scalebar_length: int,
    unit: str = "µm",
    folder: str = "",
    save_folder: str = "",
    format: str = "tif",
    bounding_box: str = False,
    bar_color: str = "w",
    alpha: float = 1,
) -> ():
    """filename should be a string with the name you want to apply,
    conversionFactor should be a float containing the pixels for one micrometre (found in imageJ),
    minScale determines if the scale should be mm, µm, or nm as a string,
    outputs a picture with a suitable scalebar for a given microscope magnification)"""
    fig, axs = plt.subplot_mosaic([["A)"]], layout="constrained")

    test_image = Image.open(f"{folder}{filename}")

    axs["A)"].set_xticks([])
    axs["A)"].set_yticks([])
    axs["A)"].imshow(test_image)
    axs["A)"].axis("off")

    width, height = test_image.size

    width = float(width)
    height = float(height)

    bar_length = conversion_factor * scalebar_length
    bar_height = bar_length * 0.07

    if bounding_box != False:
        box_width = bar_length * 1.1
        box_height = box_width * 0.3

        box = patches.Rectangle(
            (width - box_width, height - box_height),
            box_width,
            box_height,
            linewidth=0,
            edgecolor=bounding_box,
            facecolor=bounding_box,
            alpha=alpha,
        )
        axs["A)"].add_patch(box)

    bar = patches.Rectangle(
        (
            width - bar_length * 1.05,
            height - bar_height * 3.9,
        ),
        bar_length,
        bar_height,
        linewidth=1,
        edgecolor=bar_color,
        facecolor=bar_color,
    )
    axs["A)"].add_patch(bar)

    axs["A)"].text(
        float(width - bar_length * 0.8),
        float(height - bar_height * 2.0),
        f"{scalebar_length} {unit}",
        color=bar_color,
        fontsize="12",
        verticalalignment="top",
        weight="bold",
        fontfamily="sans-serif",
    )

    fig.savefig(f"{save_folder}{filename[0:-4]}_w scalebar.jpg", dpi=800)

    # for border trimming
    im = Image.open(f"{save_folder}{filename[0:-4]}_w scalebar.jpg")
    im = trim(im)
    im.save(f"{save_folder}{filename[0:-4]}_w scalebar.{format}")

    return im
