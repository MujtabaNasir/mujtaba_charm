import torch
from torchvision import datasets, transforms
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

def visualize_mnist_images(images, labels):
  fig, axes = plt.subplots(1, len(images), figsize=(20, 20))
  for i, (img, label) in enumerate(zip(images, labels)):
      img = img.squeeze().numpy()
      axes[i].imshow(img, cmap='gray')
      axes[i].set_title(f'Label: {label}')
      axes[i].axis('off')

      font = ImageFont.truetype(font_paths[i], 20)
      text_img = Image.new('L', (28, 28), color=0)

      draw = ImageDraw.Draw(text_img)
      text_bbox = draw.textbbox((0, 0), str(labels[i].item()), font=font)
      text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
      text_position = ((text_img.width - text_width) // 2, (text_img.height - text_height) // 4)
      draw.text(text_position, str(labels[i].item()), font=font, fill=255)

      text_images.append(text_img)

  plt.show()

def visualize_text_images(text_images,font_paths):
  fig, axes = plt.subplots(1, len(text_images), figsize=(20, 20))
  for i, text_img in enumerate(text_images):
    axes[i].imshow(text_img, cmap='gray')
    axes[i].set_title(f'Font: {font_paths[i].split("/")[-1]}')
    axes[i].axis('off')

  plt.show()

def find_overlap(mnist_img, text_img):
  fig, axes = plt.subplots(1, len(text_images), figsize=(20, 20))
  for i, text_img in enumerate(text_images):
    mnist_img_binary = (images[i].squeeze().numpy() > 0).astype(int)

    text_img_np = np.array(text_img)
    text_img_binary = (text_img_np > 0).astype(int)
    overlap = mnist_img_binary & text_img_binary

    axes[i].imshow(overlap, cmap='gray')
    axes[i].set_title(f'Overlap with {font_paths[i].split("/")[-1]}')
    axes[i].axis('off')

  plt.show()

def center_image(image):
    if not isinstance(image, Image.Image):
        image = (image * 255).astype(np.uint8)
        image = Image.fromarray(image)
    
    img_width, img_height = image.size

    background = Image.new('L', (28,28), color=0)    
    bg_width, bg_height = background.size
    position = ((bg_width - img_width) // 2, (bg_height - img_height) // 2)
        
    background.paste(image, position)

    plt.imshow(background, cmap='gray')
    plt.title("Center Image")
    plt.axis('off')
    plt.show()

def shift_image(image, x, y):
    image = np.array(image)
    shifted_image = np.roll(image, y, axis=0) 
    shifted_image = np.roll(shifted_image, x, axis=1) 
    
    plt.imshow(shifted_image, cmap='gray')
    plt.title("Shift Image")
    plt.axis('off')
    plt.show()

def scale_image(image, scale_factor):
    if not isinstance(image, Image.Image):
        image = (image * 255).astype(np.uint8)
        image = Image.fromarray(image)
    
    new_size = (int(image.width * scale_factor), int(image.height * scale_factor))
    scaled_image = image.resize(new_size, Image.LANCZOS)

    plt.imshow(scaled_image, cmap='gray')
    plt.title("Scale Image")
    plt.axis('off')
    plt.show()

def display_mnist_and_text_overlap(mnist_image, text_image):
    mnist_binary = (mnist_image.squeeze().numpy() > 0).astype(int)
    text_binary = (np.array(text_image) > 0).astype(int)

    overlap_image = np.zeros((mnist_binary.shape[0], mnist_binary.shape[1], 3), dtype=np.uint8)

    YELLOW = [255, 255, 0]  # RGB for yellow
    GREEN = [0, 255, 0]     # RGB for green
    GRAY = [128, 128, 128]  # RGB for gray

    overlap_image[mnist_binary == 1] = YELLOW

    overlap_image[text_binary == 1] = GREEN

    overlap_image[(mnist_binary == 1) & (text_binary == 1)] = GRAY
    
    plt.imshow(overlap_image)
    plt.title("Mnist & Text Image with different colored intersection")
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
  font_paths = [
      './fonts/OpenSans-Regular.ttf',
      './fonts/Roboto-Regular.ttf',
      './fonts/Ubuntu-Regular.ttf'
  ]

  text_images = []

  transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ]) 

  mnist_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
  dataloader = torch.utils.data.DataLoader(mnist_dataset, batch_size=3, shuffle=True)
  images, labels = next(iter(dataloader))

  visualize_mnist_images(images, labels)
  visualize_text_images(text_images,font_paths)
  find_overlap(images, text_images)
  center_image(images[0].squeeze().numpy())
  shift_image(images[0].squeeze().numpy(), 5, 0)
  scale_image(images[0].squeeze().numpy(), 1.2)
  display_mnist_and_text_overlap(images[1], text_images[1])
