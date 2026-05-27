# 🧠 Adlytix Intent Engine (Lite Bot Architecture)

> A modular, intent-based NLP chatbot engine utilizing Python Lists and Dictionaries for fast keyword-to-answer mapping.

## 🚀 Overview
The **Adlytix Intent Engine** demonstrates a professional "Separation of Concerns" architecture. Instead of hardcoding responses within the execution logic, the system decouples the **Knowledge Base** (`adlytix_brain.py`) from the **Execution Engine** (`lite_engine.py`). This allows non-technical team members to update business plans, pricing, and FAQs without touching the core Python logic.

## 🏗️ System Architecture
This project uses the **List of Dictionaries** pattern (similar to JSON structure) to group keywords into "Intents." 

* **`adlytix_brain.py` (The Data Layer):** Contains structured dictionaries. Each dictionary acts as an intent block with a list of target `keywords` and a specific `answer`.
* **`lite_engine.py` (The Logic Layer):** Imports the data layer. It tokenizes user input and utilizes nested iterations to match keywords against the intent blocks.

## ✨ Core Features
* **Modular Design:** Data and logic are in completely separate files.
* **Intent Matching:** Groups multiple keyword variations (utterances) to a single response.
* **Infinite Loop Control:** Type `exit` or `quit` for a safe system shutdown.
* **O(N) Scanning:** Iterates through groups sequentially and breaks execution instantly upon finding a match to save memory.

## 💻 How to Run
1. Clone this repository:
   ```bash
   git clone [https://github.com/zeeshan-aibuilder/Adlytix-Intent-Engine.git](https://github.com/zeeshan-aibuilder/Adlytix-Intent-Engine.git)
