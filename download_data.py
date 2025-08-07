import nltk
import os

# Define the download directory
DOWNLOAD_DIR = os.path.join(os.getcwd(), "nltk_data")

# Create the directory if it doesn't exist
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# Add the custom path to NLTK's data path
nltk.data.path.append(DOWNLOAD_DIR)

# Download the required packages to the specified directory
print(f"Downloading NLTK data to: {DOWNLOAD_DIR}")
nltk.download('punkt', download_dir=DOWNLOAD_DIR)
nltk.download('stopwords', download_dir=DOWNLOAD_DIR)
print("Download complete.")