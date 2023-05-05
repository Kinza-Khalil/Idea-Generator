from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_ideas():
    category = request.json['category']
    prompt = f"Generate 3 unique ideas for {category}:"
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    ideas = response.choices[0].text.strip().split("\n")
    return jsonify({"ideas": ideas})

if __name__ == '__main__':
    app.run(debug=True)
