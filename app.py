import streamlit as st
import random
from transformers import pipeline, set_seed

info_text = """
### Prompt Engineer, Special Topics,  Fall 2023


### Project: prompt generator [Github](https://github.com/fwangboulder/prompt_generator_ai_art)

### Fang Wang(fwangboulder@gmail.com)

### Lecturer:
### Shalini gopalkrishnan (shalinisgopal@gmail.com)

California Science and Technology University
https://www.cstu.edu/

"""
with st.sidebar:
    st.markdown(info_text)
# Create a text generation pipeline with a GPT-2 model
generator = pipeline("text-generation", model='Gustavosta/MagicPrompt-Stable-Diffusion')

def generate(prompt):
    # Set a random seed for text generation
    seed = random.randint(100, 1000000)
    set_seed(seed)

    # Generate text based on the provided prompt
    generated_text = generator(prompt, max_length=(len(prompt) + random.randint(50, 100)), num_return_sequences=3)

    # Store the generated text in a list
    results = [text['generated_text'] for text in generated_text]
    return results

# Set the title and description for your Streamlit app
st.title("AI Art Prompt Generator App")
st.markdown("This web application is designed for generating AI art prompts using the Stable Diffusion model developed by Gustavosta. Input your start text.")

# Create a text input box for the user to provide their prompt
starting_text = st.text_area("Enter text:", "Three little pigs")

# Create a button to trigger text generation
if st.button("Generate"):
    # Generate text based on the user's input
    generated_texts = generate(starting_text)

    # Display the generated text sequences
    for i, text in enumerate(generated_texts):
        st.write(f"Sequence {i+1}:\n{text}")
