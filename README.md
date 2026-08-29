# C-Flask-String-Reverser

A lightweight full-stack web application that demonstrates inter-process communication between a **Python Flask** web backend and a compiled **C program** via system subprocess pipes.

---

## 📌 How It Works

1. **Frontend:** The user enters text into an HTML form served by Flask.
2. **Backend (Python):** Flask captures the form input and pipes it directly into the standard input (`stdin`) of an executable C program using `subprocess.run()`.
3. **Execution Engine (C):** The compiled C program reads the input from `stdin`, reverses the characters, flushes the output buffer, and sends it back via standard output (`stdout`).
4. **Response:** Flask captures `stdout` from the binary and renders the reversed string on the webpage.

---

## 📁 Project Structure

```text
.
├── app.py              # Flask server handling requests & subprocess execution
├── main.c              # C program logic for string reversal
├── main.exe            # Compiled executable (Windows) / 'main' on Linux/macOS
└── templates/
    └── index.html      # HTML form and result display UI
