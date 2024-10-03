import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import sqlite3
from datetime import datetime
from rag_functions import rag


# Initialize the Dash app
app = dash.Dash(__name__)
    
# Set up SQLite database
def init_db():
    conn = sqlite3.connect('rag_interactions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS interactions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  question TEXT,
                  answer TEXT)''')
    conn.commit()
    conn.close()

def save_interaction(question, answer):
    conn = sqlite3.connect('rag_interactions.db')
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO interactions (timestamp, question, answer) VALUES (?, ?, ?)",
              (timestamp, question, answer))
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Define the layout
app.layout = html.Div([
    html.H1("Sitema RAG sobre reglamento de Transito CDMX"),
    dcc.Input(id="question-input", type="text", placeholder="Hola, realiza tu pregunta dentro de este apartado...", style={'width': '100%'}),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='answer-output', style={'whiteSpace': 'pre-line', 'marginTop': '20px'}),
    html.Div(id='db-status', style={'marginTop': '10px', 'color': 'green'})
])

# Define the callback to update the output and save to database
@app.callback(
    [Output('answer-output', 'children'),
     Output('db-status', 'children')],
    Input('submit-button', 'n_clicks'),
    State('question-input', 'value')
)
def update_output_and_save(n_clicks, question):
    if n_clicks > 0 and question:
        answer = rag(question)
        save_interaction(question, answer)
        return (
            f"Question: {question}\n\nAnswer: {answer}",
            "Interaction saved to database."
        )
    return "Aquí aparecerá tu respuesta :)", ""

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')