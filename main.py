import json
import requests

# Replace 'your_api_key' with your actual API key
api_key = 'helloworld'

# URL for the OCR.Space API endpoint
api_url = 'https://api.ocr.space/parse/image'

# Path to the local image file
image_path = 'Input_Data/Data_Sheet_1.jpg'

# Open the image file and prepare it for upload
with open(image_path, 'rb') as image_file:
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

        # Save the extracted text to a text file
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(parsed_text)

        print(f"Extracted text saved to 'output.txt'")
    else:
        print(f"Error: {response.status_code}")

# Print the OCR results
print(response.json())
