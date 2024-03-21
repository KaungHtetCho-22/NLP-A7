from flask import Flask, render_template, request, send_file
from utils import load_conversational_chain, perform_inference

app = Flask(__name__)

# Path to the saved conversational chain pickle file
chain_path = '../models/conversational_chain.pkl'

# Path to the single PDF document
pdf_path = '../docs/ait_paragraphs.pdf'

# Load the conversational chain
chain = load_conversational_chain(chain_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    global chat_history
    
    if request.method == 'GET':
        # Render the initial template if no question has been submitted yet
        return render_template('index.html', question='', answer='', chat_history='', pdf_link=pdf_path)
    
    if request.method == 'POST':
        # Get the user's question from the form
        user_question = request.form['user_question']
        
        # Get the chatbot response
        response = perform_inference(chain, user_question)
        
        # Extract relevant information
        question = response['question']
        answer = response['answer']
        chat_history = response['chat_history']
        
        # Render the template with the response data
        return render_template('index.html', question=question, answer=answer, chat_history=chat_history, pdf_link=pdf_path)

@app.route('/docs/ait_paragraphs.pdf')
def download_pdf():
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
