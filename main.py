from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Saya suka tidur", 
              "Saya kurang suka menonton film", 
              "Saya tidak suka makan pedas"]

list = ['Mandaffection','Christyzer','Liamelior',
'ZeeMotion','Callistaverse','Onielity',
'Oracle','Fenidelity','Symfiony',
'FloRisen','Freyanation','Ellatheria',
'Gitroops','Gracieluv','Degrees',
'Helismiley','Interindah','Indiraise',
'Jessination','Lynear','KATH, Inc',
'Lunarian','MarshaOshi','Muffin',
'Raishanrise','Adellion','Inshanity',
'Gracias','Wargavi48'	]

@app.route("/") # Ini halaman home
def index():
    return f'<h1>Hai! di halaman ini, kamu dapat mempelajari beberapa fakta menarik tentang diriku!</h1><a href="/random_fact">View a random fact!</a><h4>Kumpulan akun akun X orang keren</h4> <a href="/akun_keren">Buka aja</a>'

@app.route("/random_fact") #Ini adalah halaman random fakta
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/akun_keren")
def X():
    return f'<p>{random.choice(list)}</p>'

app.run(debug=True)