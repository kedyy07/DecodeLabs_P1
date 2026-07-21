# Rule-Based AI Chatbot 🤖

## Description
This is **Project 1** for the Artificial Intelligence track at **DecodeLabs**. It is a foundational Rule-Based AI Chatbot built using Python. This project focuses on the "Logic Engine" (System 2) of AI, emphasizing control flow, deterministic responses, and O(1) algorithmic efficiency using Hash Maps (Dictionaries) instead of standard if-elif ladders. 

## Key Features & Architecture
* **Infinite Loop Architecture**: Runs continuously in a `while True` loop until a kill command is received.
* **Input Sanitization**: Normalizes raw user input by converting it to lowercase and stripping excess whitespace.
* **O(1) Intent Matching**: Utilizes Python dictionaries for instant O(1) key-value lookups, making it highly efficient.
* **Graceful Fallback**: Uses the `.get()` method to handle unknown queries seamlessly without crashing.
* **Exit Strategy**: Built-in safe termination using the `exit` command.

## Knowledge Base (Intents)
The chatbot currently recognizes and responds to exact matches for the following inputs:
* `hello` / `hi`
* `how are you`
* `what is your name`
* `what is ai`
* `who created you`
* `help`
* `bye`
* `exit` (Kill Command)

## How to Run
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Open your terminal or command prompt.
4. Navigate to the directory containing the file.
5. Run the script using:
   ```bash
   python chatbot.py