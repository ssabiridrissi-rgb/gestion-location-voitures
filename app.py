# Application principale - Gestion Location Voitures

from flask import Flask, render_template

app = Flask(__name__)

# Liste des voitures disponibles
voitures = []

@app.route('/')
def index():
    # HOTFIX : afficher un message si aucune voiture disponible
    if not voitures:
        message = "Aucune voiture disponible pour le moment."
    else:
        message = None
    return render_template('index.html', voitures=voitures, message=message)

if __name__ == '__main__':
    app.run(debug=True)