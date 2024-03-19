import os

# Function to get the images from the directory
def get_images(directory):
    real_images = []
    fake_images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                if 'real' in root.lower():
                    real_images.append(os.path.join(root, file))
                elif 'fake' in root.lower() or 'ai' in root.lower():
                    fake_images.append(os.path.join(root, file))
    return real_images, fake_images

