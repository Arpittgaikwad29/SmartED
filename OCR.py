import boto3
from pdf2image import convert_from_path
import os

# Initialize AWS Textract client
textract = boto3.client('textract', region_name='us-east-1')  # Change region if needed

# Convert PDF to images
pdf_path = "CSA_sam_assig_for_practice.pdf"  # Replace with your PDF file
output_folder = "pdf"  # Folder to save images temporarily

os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist
images = convert_from_path(pdf_path, dpi=300)  # Convert PDF to high-resolution images

extracted_text = ""  # Variable to store extracted text

# Process each image
for i, image in enumerate(images):
    image_path = os.path.join(output_folder, f"page_{i+1}.png")
    image.save(image_path, "PNG")  # Save image temporarily

    # Read image bytes
    with open(image_path, "rb") as img_file:
        image_bytes = img_file.read()

    # Extract text using Textract
    response = textract.detect_document_text(Document={'Bytes': image_bytes})

    # Store extracted text
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            extracted_text += item["Text"] + "\n"

    # Delete the image immediately after processing
    os.remove(image_path)

print(extracted_text)

# Remove the empty folder after all images are deleted
if not os.listdir(output_folder):
    os.rmdir(output_folder)
