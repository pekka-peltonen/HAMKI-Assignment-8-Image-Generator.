HAMK Assignment #8 – Image Generator CLI

Author: Pekka Peltonen
Course: AI APIs and Standalone AI Applications
Model: OpenAI GPT Image 2 (gpt-image-2)

Description

A Python command-line application that generates images using the OpenAI Image API and saves them locally.

Features

Generates images from text prompts

Supports aspect ratio, image count, output folder and quality settings

Validates command-line arguments

Handles API errors

Saves images with unique filenames

Prints the saved filenames

Requirements

Python 3.13

OpenAI Python package

An OpenAI API key stored in the OPENAI_API_KEY environment variable

Install the package:

pip install openai

Usage

python generate.py --prompt "A red wooden cottage beside a Finnish lake" --aspect-ratio 3:2 --count 1 --output images --quality low

Generate two images:

python generate.py --prompt "A Finnish lakeside sauna at sunset" --aspect-ratio 3:2 --count 2 --output images --quality low

Show available options:

python generate.py --help

Testing

The application was tested successfully by generating three images and saving them locally.

Invalid input was also tested using --count 0. The application correctly rejected the value.

Notes

The API key is not included in the source code. Image generation requires API access and may incur charges.
