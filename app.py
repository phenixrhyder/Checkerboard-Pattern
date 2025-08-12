# app.py

import gradio as gr
from PIL import Image, ImageDraw
import tempfile

# Define a dictionary of preset canvas sizes (width, height)
PRESET_SIZES = {
    "Square (1:1)": (1080, 1080),
    "Classic TV (4:3)": (1200, 900),
    "Widescreen (16:9)": (1920, 1080),
    "Tumblr Header": (3000, 1055),
}

def create_checkerboard(preset_name, square_size, color1, color2):
    """
    Generates a checkerboard image by filling a preset canvas with perfect squares.

    Args:
        preset_name (str): The key for the PRESET_SIZES dictionary.
        square_size (int): The width and height of each perfect square in pixels.
        color1 (str): The name of the first color.
        color2 (str): The name of the second color.

    Returns:
        (PIL.Image.Image, str): A tuple containing the generated image 
                                and the path to a temporary file for download.
    """
    # Get the image dimensions from the selected preset
    image_width, image_height = PRESET_SIZES[preset_name]

    # Calculate how many squares will fit in the canvas
    board_size_w = int(image_width / square_size) + 1
    board_size_h = int(image_height / square_size) + 1

    # Create a new blank image in RGBA mode to support transparency
    image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Loop through each square position
    for row in range(board_size_h):
        for col in range(board_size_w):
            # Determine which color string to use for the current square
            if (row + col) % 2 == 0:
                color_name = color1
            else:
                color_name = color2
            
            # Use a transparent tuple if "Transparent" is selected
            square_color = (0, 0, 0, 0) if color_name == "Transparent" else color_name

            # Calculate the coordinates of the square
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            
            # Draw the rectangle (which is now always a square)
            draw.rectangle([x1, y1, x2, y2], fill=square_color)

    # Save the image to a temporary file to make it downloadable
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        image.save(temp_file.name)
        download_path = temp_file.name

    return image, download_path

# --- Create the Gradio Interface ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Checkerboard Pattern Generator")
    gr.Markdown("Select a preset canvas size, the size of the squares, and colors, then click Generate.")

    with gr.Row():
        # Dropdown for preset sizes
        preset_dropdown = gr.Dropdown(
            choices=list(PRESET_SIZES.keys()), 
            value="Square (1:1)", 
            label="Canvas Size Preset"
        )
        # CHANGED: Slider now controls the size of each square
        square_size_slider = gr.Slider(
            minimum=10, 
            maximum=200, 
            value=50, 
            step=1, 
            label="Square Size (pixels)"
        )

    # Define a list of standard colors, including Transparent
    color_choices = ["Transparent", "White", "Black", "Gray", "Red", "Green", "Blue", "Yellow", "Purple", "Orange"]

    with gr.Row():
        # Color dropdowns remain the same
        dropdown_1 = gr.Dropdown(choices=color_choices, value="Transparent", label="Color 1")
        dropdown_2 = gr.Dropdown(choices=color_choices, value="Black", label="Color 2")

    generate_button = gr.Button("Generate Image")
    output_image = gr.Image(label="Generated Checkerboard")
    download_button = gr.File(label="Download Image as PNG")

    # Link the button to the function with the new inputs
    generate_button.click(
        fn=create_checkerboard,
        inputs=[preset_dropdown, square_size_slider, dropdown_1, dropdown_2],
        outputs=[output_image, download_button]
    )

if __name__ == "__main__":
    demo.launch()
