# Web-Scrapper-using-LLMs
A Flask-based web scraper app that extracts content from URLs or search topics using BeautifulSoup or LlamaIndex, then summarizes it using local LLMs via Ollama. Includes a user-friendly HTML/CSS frontend for input and output display.

## 🚀 Features

- 🌐 Scrape content from public web pages using BeautifulSoup.
- 🤖 Use LLaMA3 or Gemma (via Ollama) to summarize and interact with the text.
- 🎨 Gradient-styled HTML/CSS interface for input and output.
- ⚡ Flask backend with multithreading for better performance.

- ## 🛠️ Setup Instructions

# 1. Install Python packages
pip install -r requirements.txt

# 2. Install Ollama and run a model
# Download from: https://ollama.com/download
ollama run llama3
# or
ollama run gemma

# 3. Run the Flask app
python app.py

# 4. Open in your browser
# Visit: http://127.0.0.1:5000
