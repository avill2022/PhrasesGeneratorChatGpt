import openai #pip install openai
import os

import customtkinter as ctk


def openaiChat(prompt):
    # Set OpenAI API key
	openai.api_key = os.getenv("OPENAI_API_KEY")
	# Define prompt and parameters
	model = "text-davinci-002"
	#max_tokens = 50

	# Generate text using GPT-3 API
	response = openai.Completion.create(
		engine=model,
		prompt=prompt,
		#max_tokens=max_tokens,
	)
	# Print generated text
	print(response.choices[0].text.strip())

prompt = ""
openaiChat(prompt=prompt)