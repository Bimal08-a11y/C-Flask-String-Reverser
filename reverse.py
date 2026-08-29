from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    
    if request.method == "POST":
        # 1. Grab inputs from the HTML form
        text = request.form.get("text")
        
        # 2. Run your compiled C program
        proc = subprocess.run(
            ["main.exe"],
            input=f"{text}",
            text=True,
            capture_output=True
        )
        
        # 3. Capture the output
        result = proc.stdout.strip()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
