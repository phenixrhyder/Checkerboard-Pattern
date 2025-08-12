# app.py

import gradio as gr
from PIL import Image, ImageDraw
import tempfile # Needed to create a temporary file for downloading

def create_checkerboard(board_size, square_size, color1, color2):
    """
    Generates a checkerboard image using the Pillow library with custom colors.

    Args:
        board_size (int): The number of squares per side.
        square_size (int): The size of each square in pixels.
        color1 (str): The hex code for the first color.
        color2 (str): The hex code for the second color.

    Returns:
        (PIL.Image.Image, str): A tuple containing the generated image 
                                and the path to a temporary file for download.
    """
    # Calculate the total size of the image
    image_size = board_size * square_size
    
    # Create a new blank image
    image = Image.new("RGB", (image_size, image_size), "white")
    draw = ImageDraw.Draw(image)

    # Loop through each square position
    for row in range(board_size):
        for col in range(board_size):
            # Calculate the coordinates of the square
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size

            # Determine the color of the square
            if (row + col) % 2 == 0:
                square_color = color1
            else:
                square_color = color2
            
            # Draw the rectangle
            draw.rectangle([x1, y1, x2, y2], fill=square_color)

    # Save the image to a temporary file to make it downloadable
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        image.save(temp_file.name)
        download_path = temp_file.name

    return image, download_path

# --- Create the Gradio Interface ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Checkerboard Pattern Generator")
    gr.Markdown("Use the sliders and color pickers to customize your pattern, then click Generate.")

    with gr.Row():
        # Input sliders for customization
        board_size_slider = gr.Slider(minimum=2, maximum=20, value=8, step=1, label="Board Size (e.g., 8x8)")
        square_size_slider = gr.Slider(minimum=10, maximum=100, value=50, step=5, label="Square Size (pixels)")

    with gr.Row():
        # NEW: Color pickers for the two board colors
        color_picker_1 = gr.ColorPicker(value="#FFFFFF", label="Color 1 (Light)")
        color_picker_2 = gr.ColorPicker(value="#000000", label="Color 2 (Dark)")

    # The button to trigger the image generation
    generate_button = gr.Button("Generate Image")

    # The output component to display the generated image
    output_image = gr.Image(label="Generated Checkerboard")
    
    # NEW: The file component for the download button
    download_button = gr.File(label="Download Image as PNG")

    # Link the button to the function
    generate_button.click(
        fn=create_checkerboard,
        inputs=[board_size_slider, square_size_slider, color_picker_1, color_picker_2],
        outputs=[output_image, download_button] # We now have two outputs
    )

# --- Launch the App ---
if __name__ == "__main__":
    demo.launch()
