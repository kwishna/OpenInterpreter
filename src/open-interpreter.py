# https://github.com/KillianLucas/open-interpreter

import interpreter

# -------- ------------- you will need to set the model manually:
interpreter.model = "gpt-3.5-turbo"
interpreter.api_key = "your_openai_api_key"
interpreter.auto_run = True

# ------------ ------------ ------------ ------------ ------------ ------------ ------------
interpreter.chat("Plot AAPL and META's normalized stock prices") # Executes a single command
interpreter.chat() # Starts an interactive chat

# ------------ ------------ ------------ ------------ ------------ ------------ ------------
interpreter.chat("Add subtitles to all videos in /videos.") # ... Streams output to your terminal, completes task ...
interpreter.chat("These look great but can you make the subtitles bigger?")

# ------------ ------------ ------------ ------------ ------------ ------------ ------------
interpreter.reset() # start new chat

# ------------ ------------ ------------ ------------ ------------ ------------ ------------
# interpreter.chat() returns a List of messages when return_messages=True, which can be used to resume a conversation with interpreter.load(messages):
messages = interpreter.chat("My name is Killian.", return_messages=True) # Save messages to 'messages'
interpreter.reset() # Reset interpreter ("Killian" will be forgotten)
interpreter.load(messages) # Resume chat from 'messages' ("Killian" will be remembered)