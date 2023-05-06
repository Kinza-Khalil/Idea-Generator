# IdeaGenerator

**Set up a virtual environment and install dependencies**

- Open VS Code and open your project folder.
- Open the terminal in VS Code (View > Terminal).
- Create a virtual environment: python -m venv venv
- Activate the virtual environment:
  Windows: venv\Scripts\activate
  macOS/Linux: source venv/bin/activate
- Install dependencies: pip install -r requirements.txt

**Test the application**

- Set your OpenAI API key in the terminal: export OPENAI_API_KEY=your_api_key (macOS/Linux) or set OPENAI_API_KEY=your_api_key (Windows).
- Run the Flask application: flask run
- Open your web browser and go to http://127.0.0.1:5000.
