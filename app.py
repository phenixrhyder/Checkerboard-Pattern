# app.py

import gradio as gr

# --- 1. DEFINE YOUR CORE FUNCTION ---
# This is a simple placeholder function. It takes some text as input
# and returns a slightly modified version of it.
def process_text(input_text):
  """
  This function takes a string and returns a new string.
  """
  # for debugging, this will show up in the logs of your Hugging Face Space
  print(f"Processing input: {input_text}")
  
  # The actual logic of our simple app
  output_text = f"The app received your message: '{input_text}'"
  return output_text


# --- 2. CREATE THE GRADIO INTERFACE ---
# This creates the web UI that users will see and interact with.
with gr.Blocks() as demo:
  gr.Markdown("# My First Hugging Face App")
  gr.Markdown("This is a simple demo. Type something in the box and click the button.")

  # Define the input component (a textbox)
  input_component = gr.Textbox(label="Your Message")

  # Define the output component
  output_component = gr.Textbox(label="App's Response")

  # Define the button that will trigger the function
  process_button = gr.Button("Submit")

  # Link the button to your function.
  # When the button is clicked, it will run the `process_text` function.
  process_button.click(
      fn=process_text,
      inputs=input_component,
      outputs=output_component
  )


# --- 3. LAUNCH THE APP ---
# This command starts the web server when Hugging Face runs the script.
if __name__ == "__main__":
  demo.launch()
