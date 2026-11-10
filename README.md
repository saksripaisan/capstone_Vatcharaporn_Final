Serverless Image Processing Pipeline
Project Overview
This project demonstrates a serverless image processing workflow using AWS services.

The application stores images in Amazon S3. AWS Lambda uses the Pillow library to resize images. AWS Step Functions manages the workflow and Amazon API Gateway provides an endpoint for triggering the process.

The resized image is saved in a separate S3 bucket.

---

AWS Services Used

- Amazon S3
- AWS Lambda
- AWS Step Functions
- Amazon API Gateway
- Amazon CloudWatch

---

S3 Buckets
Input Bucket: original-images-vatcharaporn

Output Bucket: resized-images-vatcharaporn

---

Lambda Function
Lambda Name: image-resize-vatcharaporn

AWS Lambda was created using Python and the Pillow library.

The Lambda function downloads an image from the input S3 bucket, resizes the image into a thumbnail, and uploads the resized image to the output S3 bucket.

The function was tested successfully and generated a resized image in the output bucket.

---

Step Functions
State Machine: state-machine-vatcharaporn

Workflow:

Start > Resize Image > Check Result > Success/Fail

---

API Gateway
API Name: api_vatcharaporn

Method: POST

Stage: prod

---
