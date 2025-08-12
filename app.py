# app.py

import gradio as gr
from PIL import Image, ImageDraw

def create_checkerboard(board_size=8, square_size=50):
    """
    Generates a checkerboard image using the Pillow library.

    Args:
        board_size (int): The number of squares per side (e.g., 8 for an 8x8 board).
        square_size (int): The size of each square in pixels.

    Returns:
        PIL.Image.Image: The generated checkerboard image.
    """
    # Calculate the total size of the image
    image_size = board_size * square_size
    
    # Create a new blank image in RGB mode with a white background
    image = Image.new("RGB", (image_size, image_size), "white")
    draw = ImageDraw.Draw(image)

    # Define the colors for the checkerboard
    color1 = (255, 255, 255)  # White
    color2 = (0, 0, 0)      # Black

    # Loop through each square position
    for row in range(board_size):
        for col in range(board_size):
            # Calculate the top-left and bottom-right coordinates of the square
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size

            # Determine the color of the square
            if (row + col) % 2 == 0:
                square_color = color1
            else:
                square_color = color2
            
            # Draw the rectangle on the image
            draw.rectangle([x1, y1, x2, y2], fill=square_color)

    return image

# --- Create the Gradio Interface ---
with gr.Blocks() as demo:
    gr.Markdown("# Checkerboard Pattern Generator")
    gr.Markdown("Use the sliders to change the size of the board and the squares, then click Generate.")

    with gr.Row():
        # Input sliders for customization
        board_size_slider = gr.Slider(minimum=2, maximum=20, value=8, step=1, label="Board Size (e.g., 8x8)")
        square_size_slider = gr.Slider(minimum=10, maximum=100, value=50, step=5, label="Square Size (pixels)")

    # The button to trigger the image generation
    generate_button = gr.Button("Generate Image")

    # The output component to display the generated image
    output_image = gr.Image(label="Generated Checkerboard")

    # Link the button to the function
    generate_button.click(
        fn=create_checkerboard,
        inputs=[board_size_slider, square_size_slider],
        outputs=output_image
    )

# --- Launch the App ---
if __name__ == "__main__":
    demo.launch()
