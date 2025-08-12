---
title: Checkerboard Pattern Generator
sdk: gradio
app_file: app.py
---
Welcome to the Checkerboard Pattern Generator! This is a simple and interactive Hugging Face Space that allows you to create custom checkerboard images directly in your browser.
🚀 How to Use
Using the app is straightforward:
 * Board Size: Use the first slider to select the number of squares on the board (e.g., a value of 8 creates an 8x8 board).
 * Square Size: Use the second slider to control the size of each individual square in pixels.
 * Generate: Click the "Generate Image" button to create your checkerboard based on your settings. The resulting image will appear below.
Feel free to experiment with different values to create patterns of all sizes!
🛠️ Technical Details
This application is built using the following open-source libraries:
 * Gradio: Provides the fast and easy-to-use web interface with sliders, buttons, and image display components.
 * Pillow (PIL): The core image processing library used to draw the checkerboard pattern on a blank canvas.
The entire application is contained within the app.py file and runs on the Hugging Face Spaces infrastructure.
