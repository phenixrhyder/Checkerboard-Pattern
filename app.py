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
        color1 (str): The name of the first color.
        color2 (str): The name of the second color.

    Returns:
        (PIL.Image.Image, str): A tuple containing the generated image 
                                and the path to a temporary file for download.
    """
    # Calculate the total size of the image
    image_size = board_size * square_size
    
    # Create a new blank image in RGBA mode to support transparency
    # The background is now transparent (0,0,0,0)
    image = Image.new("RGBA", (image_size, image_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Loop through each square position
    for row in range(board_size):
        for col in range(board_size):
            # Determine which color string to use for the current square
            if (row + col) % 2 == 0:
                color_name = color1
            else:
                color_name = color2
            
            # Use a transparent tuple if "Transparent" is selected, otherwise use the color name
            if color_name == "Transparent":
                square_color = (0, 0, 0, 0)
            else:
                square_color = color_name

            # Calculate the coordinates of the square
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            
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
    gr.Markdown("Use the sliders and dropdowns to customize your pattern, then click Generate.")

    with gr.Row():
        # Input sliders for customization
        board_size_slider = gr.Slider(minimum=2, maximum=20, value=8, step=1, label="Board Size (e.g., 8x8)")
        square_size_slider = gr.Slider(minimum=10, maximum=100, value=50, step=5, label="Square Size (pixels)")

    # Define a list of standard colors, now including Transparent
    color_choices = ["Transparent", "White", "Black", "Gray", "Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Cyan", "Magenta"]

    with gr.Row():
        # Dropdowns now include and default to Transparent
        dropdown_1 = gr.Dropdown(choices=color_choices, value="Transparent", label="Color 1")
        dropdown_2 = gr.Dropdown(choices=color_choices, value="Black", label="Color 2")

    # The button to trigger the image generation
    generate_button = gr.Button("Generate Image")

    # The output component to display the generated image
    output_image = gr.Image(label="Generated Checkerboard")
    
    # The file component for the download button
    download_button = gr.File(label="Download Image as PNG")

    # Link the button to the function
    generate_button.click(
        fn=create_checkerboard,
        inputs=[board_size_slider, square_size_slider, dropdown_1, dropdown_2],
        outputs=[output_image, download_button]
    )

# --- Launch the App ---
if __name__ == "__main__":
    demo.launch()
