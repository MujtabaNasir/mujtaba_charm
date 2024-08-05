import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from PIL import Image, ImageDraw, ImageFont


def fetch_mnist() -> tuple[np.ndarray, np.ndarray]:
    """
    Fetches the MNIST dataset and saves it to a compressed file.

    Returns:
        tuple: A tuple containing the training images and labels.
    """
    mnist = tf.keras.datasets.mnist.load_data()
    (train_images, train_labels), _ = mnist
    np.savez_compressed("mnist.npz", images=train_images, labels=train_labels)
    return train_images, train_labels


def create_digit_image(digit: int, font_path: str, image_size: tuple[int, int] = (28, 28)) -> Image.Image:
    """
    Creates an image of a digit using a specified font.

    Args:
        digit (int): The digit to draw.
        font_path (str): Path to the font file.
        image_size (tuple[int, int], optional): Size of the output image. Defaults to (28, 28).

    Returns:
        Image.Image: An image of the digit.
    """
    font = ImageFont.truetype(font_path, 24)
    image = Image.new("L", image_size, color=255)
    draw = ImageDraw.Draw(image)
    text_bbox = draw.textbbox((0, 0), str(digit), font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    text_x = (image_size[0] - text_width) / 2
    text_y = (image_size[1] - text_height) / 2
    draw.text((text_x, text_y), str(digit), font=font, fill=0)
    return image


def get_image_overlapping(img1: np.ndarray, img2: np.ndarray) -> np.ndarray:
    """
    Finds the overlapping areas between two images.

    Args:
        img1 (np.ndarray): The first image.
        img2 (np.ndarray): The second image.

    Returns:
        np.ndarray: A binary image showing the overlapping areas.
    """
    mnist_array = np.array(img1)
    font_array = np.array(img2)
    overlap = np.logical_and(mnist_array < 128, font_array < 128)
    return overlap


def show_images(img1: np.ndarray, img2: np.ndarray, overlap_image: np.ndarray) -> None:
    """
    Displays three images: MNIST image, font image, and overlap image.

    Args:
        img1 (np.ndarray): The MNIST image.
        img2 (np.ndarray): The font image.
        overlap_image (np.ndarray): The overlap image.
    """
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    axes[0].imshow(img1, cmap="gray")
    axes[0].set_title("MNIST Image")
    axes[0].axis("off")

    axes[1].imshow(img2, cmap="gray")
    axes[1].set_title("Font Image")
    axes[1].axis("off")

    axes[2].imshow(overlap_image, cmap="gray")
    axes[2].set_title("Overlap Image")
    axes[2].axis("off")

    plt.show()
