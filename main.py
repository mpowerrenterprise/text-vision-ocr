import os
import json
import requests

# Replace 'your_api_key' with your actual API key
api_key = 'helloworld'

# Input and output folder paths
input_folder = 'input'
output_folder = 'output'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# URL for the OCR.Space API endpoint
api_url = 'https://api.ocr.space/parse/image'

# Loop through all image files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        # Path to the input image file
        input_image_path = os.path.join(input_folder, filename)

        # Open the image file and prepare it for upload
        with open(input_image_path, 'rb') as image_file:
            # Set up the API request parameters
            payload = {
                'apikey': api_key,
            }

            # Prepare the image file to be included in the request
            files = {'image': ('image.jpg', image_file, 'image/jpeg')}

            # Send the POST request to the OCR.Space API
            response = requests.post(api_url, data=payload, files=files)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract JSON content from the response
                data = response.json()

                # Extract ParsedText
                parsed_text = data['ParsedResults'][0]['ParsedText']

                # Save the extracted text to a text file in the output folder
                output_text_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
                with open(output_text_path, 'w', encoding='utf-8') as file:
                    file.write(parsed_text)

                print(f"Text extracted from {filename} and saved to {output_text_path}")
            else:
                print(f"Error processing {filename}. Status Code: {response.status_code}")

