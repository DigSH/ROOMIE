from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

# Almacén de conversaciones
conversations = []

# Ruta principal para el chat
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and request.form['question']:
        question = 'Yo: ' + request.form['question']

        # Solicitud a OpenAI
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=question,
            temperature=0.5,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )

        answer = 'AI: ' + response.choices[0].text.strip()

        # Añadir pregunta y respuesta al historial
        conversations.append(question)
        conversations.append(answer)

    return render_template('index.html', chat=conversations)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
