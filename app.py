from flask import Flask, render_template, request, jsonify
from scraper import scrape_website
import ollama
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=4)  
scraped_text_global = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    global scraped_text_global
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    future = executor.submit(scrape_website, url)  
    scraped_text = future.result()

    if "Error" in scraped_text:
        return jsonify({"error": scraped_text}), 400

    scraped_text_global = " ".join(scraped_text.split()) 
    return jsonify({"scraped_text": scraped_text_global})

@app.route('/ask', methods=['POST'])
def ask():
    global scraped_text_global
    data = request.json
    question = data.get("question")
    model = data.get("model", "llama3:latest")  
    if not question:
        return jsonify({"error": "Question is required"}), 400

    if not scraped_text_global:
        return jsonify({"error": "No scraped text available. Please scrape a website first."}), 400

    prompt = f"Based on the following text, answer the question:\n\n{scraped_text_global[:3000]}\n\nQuestion: {question}"

    future = executor.submit(query_llm, model, prompt)  
    answer = future.result()

    return jsonify({"answer": answer})

def query_llm(model, prompt):
    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"] if "message" in response else "Error in generating answer."
    except Exception as e:
        return f"Ollama error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, threaded=True)  