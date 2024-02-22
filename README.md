# OCR based Medical Data Extraction Project

## Problem statement

Health insurance companies must adhere to government regulations when processing claims, often outsourcing manual extraction of patient and prescription data from scanned images. This manual process is prone to errors, especially with large image sets during crises like pandemics. Meeting the 24-hour data extraction deadline is challenging.

## Solution approach

We're developing an automated program to extract data from images, aiming to address the challenges faced by manual extraction methods. While machines can't completely replace humans, our program significantly reduces the time and effort spent on manual data entry. We're leveraging Python and the pytesseract library for extraction, with Regex for refining the output. This approach saves valuable resources and ensures accurate data extraction

## Technologies used

- Python
- oops
- Pdf2image module
- Opencv
- pytesseract
- Regular expression
- pytest
- Postman
- FastApi

## Workflow
<img src="https://github.com/TrivikramR/Data_Extraction_Healthcare_Project/blob/main/backend/notebook/ocr.png" class="center">

### PDF to Image
For converting PDF to image, we have used pdf2image library.

### Without preprocessing extracting data
Tried extracting data from source files without any processing, as they are not in proper format to be extracted, the extracted data was not as expected.

<img src="https://github.com/TrivikramR/Data_Extraction_Healthcare_Project/blob/main/backend/notebook/ocr6.png" class="center">

### Extracted data from the above image

<img src="https://github.com/TrivikramR/Data_Extraction_Healthcare_Project/blob/main/backend/notebook/ocr1.png" class="center">

### Image processing
we decided to preprocess the image using opencv module, before extracting data from them. For that we have first used normal thresholding and checked, which resulted in below image

<img src="https://github.com/TrivikramR/Data_Extraction_Healthcare_Project/blob/main/backend/notebook/ocr2.png" class="center">
So, if there is any shadow or some noise, the normal thresholding fade out the area. which will result in loss of data.

In the search of better approach of this problem, we have decided to use adaptive thresholding technique. In this technique, the image will be divided into sub image and the thresholding value will be different for all sub regions. And the end result of adaptive thresholding is much better compared to normal thresholding.

<img src="https://github.com/TrivikramR/Data_Extraction_Healthcare_Project/blob/main/backend/notebook/ocr3.png" class="center">

### After preprocessing the image data extraction
<img src="https://github.com/TrivikramR/Data_Extraction_Healthcare_Project/blob/main/backend/notebook/ocr4.png" class="center">

### Notebook
The code was written in using OOPs concepts for extracting the medical data from prescription and patient details documents.

### OOPS design

By using this report, decisions can be taken based on the data. Further it will help in answering n number of why questions based on the situations.

### Regular expression

using regular expression module we can match the patterns and extract the data we want from the files. For this project, analyst the medical files and as fact all the medical documents will follow same pattern, we wrote patterns that match only the required data. Before writing the python code, It is advisable to practise and match the patterns in regex 101 website.

### Test Driven Development

In this project test driven development methodology was used to develop the code. For testing pytest module was used. For all the methods and final result the test cases was designed and checked simultaneously while developing the code.

### FastApi

Used FastAPI for hosting the server of the project. FastApi, as name suggest is help us to develop fast and some other advantages are,

-In build Data validation
-In build Documentation
-Fast running and performance

### Postman

As it is a backend project, not developed frontend part. For checking how the server responds for http requests, used postman to trigger http requests and tested the outcome.

<img src="https://github.com/TrivikramR/Data_Extraction_Healthcare_Project/blob/main/backend/notebook/ocr5.png" class="center">


