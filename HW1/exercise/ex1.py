import cv2 
import matplotlib.pyplot as plt

# Load an image from file as function
def load_image(image_path):
    img = cv2.imread(image_path)
    return img

# Display an image as function
def display_image(image, title="Image"):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis(False)
    plt.show()

# grayscale an image as function
def grayscale_image(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray_img

# Save an image as function
def save_image(image, output_path):
    cv2.imwrite(output_path, image)

# flip an image as function 
def flip_image(image):
    flipped_img = cv2.flip(image, 1)
    return flipped_img

# rotate an image as function
def rotate_image(image, angle):
    (width, height) = image.shape[1::-1]
    image_center = (width/2, height/2) 

    rotate_matrix = cv2.getRotationMatrix2D(center=image_center, angle=angle, scale=1)
    rotate_img = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))
    return rotate_img

if __name__ == "__main__":
    # Load an image from file
    img = load_image("./uet.png")

    # Display the image
    display_image(img, "Original Image")

    # Convert the image to grayscale
    img_gray = grayscale_image(img)

    # Display the grayscale image
    display_image(img_gray, "Grayscale Image")

    # Save the grayscale image
    save_image(img_gray, "./lena_gray.jpg")

    # Flip the grayscale image
    img_gray_flipped = flip_image(img_gray)

    # Display the flipped grayscale image
    display_image(img_gray_flipped, "Flipped Grayscale Image")

    # Rotate the grayscale image
    img_gray_rotated = rotate_image(img_gray, 45)

    # Display the rotated grayscale image
    display_image(img_gray_rotated, "Rotated Grayscale Image")

    # Save the rotated grayscale image
    save_image(img_gray_rotated, "./lena_gray_rotated.jpg")

    img_flipped = flip_image(img)
    img_rotated = rotate_image(img, 45)
    save_image(img_flipped, "./uet_flipped.jpg")
    save_image(img_rotated, "./uet_rotated.jpg")

    # Show the images
    plt.show() 
