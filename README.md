# AutoTyper
A free and open-source tool designed to automate typing tasks, with built in AI for advanced users. 


---

## 📦 Features

### 🖱️ AutoTyper Mode
- Simulates human typing behavior by typing out text with customizable speed and randomness.
- Trigger typing with a simple hotkey.
- Perfect for demonstrations, testing, or automation.

### 🤖 AutoTyper + AI Mode
- Adds natural language generation capabilities using [Ollama](https://ollama.com/) and the `qwen2.5:0.5b` model.
- AI processes your input and transforms it into structured revision-friendly content.
- Displays AI output in a built-in console text box for immediate feedback.

### ⚙️ Settings Panel
- **Typing Speed**: Set how fast the text should be typed.
- **Randomness**: Introduce a more human-like variability in typing speed.
- All values are configurable through a sleek popup UI.

### 🌗 Dark Mode UI
- Fully built with **CustomTkinter**, the app includes a responsive, dark-themed GUI.
- Dynamic layout with resizing and intuitive button placement.

---

## 🛠️ Requirements

- Python 3.9 or newer
- [Ollama](https://ollama.com/) installed (for AI mode only)
- The following Python packages:
  - `customtkinter`
  - `keyboard`
  - `pyautogui`
  - `ollama`
  - `tkinter` (standard with Python)

You can install dependencies with:

```bash
pip install customtkinter keyboard pyautogui ollama
