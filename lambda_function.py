import boto3
from PIL import Image

s3 = boto3.client('s3')

INPUT_BUCKET = 'original-images-vatcharaporn'
OUTPUT_BUCKET = 'resized-images-vatcharaporn'

def lambda_handler(event, context):

    input_file = 'japanese-maple-autumn-medium.jpg'

    input_path = f'/tmp/{input_file}'
    output_path = f'/tmp/resized-{input_file}'

    # Download image from input bucket
    s3.download_file(
        INPUT_BUCKET,
        input_file,
        input_path
    )

    # Open image using Pillow
    image = Image.open(input_path)

    # Resize image to thumbnail
    image.thumbnail((200, 200))

    # Save resized image
    image.save(output_path)

    # Upload resized image to output bucket
    s3.upload_file(
        output_path,
        OUTPUT_BUCKET,
        f'resized-{input_file}'
    )

    return {
        'statusCode': 200,
        'success': True,
        'message': 'Image resized successfully',
        'output_file': f'resized-{input_file}'
    }