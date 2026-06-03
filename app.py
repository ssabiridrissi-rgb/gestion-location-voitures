import os
import json
from datetime import date
from flask import Flask, flash, jsonify, redirect, render_template, request, url_for
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

voitures = [
    {"id": 1, "marque": "Renault",    "modele": "Clio",     "type": "citadine",   "places": 5, "prix_jour": 30,  "transmission": "manuelle",    "carburant": "essence"},
    {"id": 2, "marque": "Peugeot",    "modele": "308",      "type": "berline",    "places": 5, "prix_jour": 45,  "transmission": "automatique", "carburant": "diesel"},
    {"id": 3, "marque": "Dacia",      "modele": "Duster",   "type": "suv",        "places": 5, "prix_jour": 55,  "transmission": "manuelle",    "carburant": "diesel"},
    {"id": 4, "marque": "Ford",       "modele": "Transit",  "type": "utilitaire", "places": 3, "prix_jour": 80,  "transmission": "manuelle",    "carburant": "diesel"},
    {"id": 5, "marque": "Mercedes",   "modele": "Classe A", "type": "berline",    "places": 5, "prix_jour": 90,  "transmission": "automatique", "carburant": "essence"},
    {"id": 6, "marque": "BMW",        "modele": "Serie 3",  "type": "berline",    "places": 5, "prix_jour": 110, "transmission": "automatique", "carburant": "essence"},
    {"id": 7, "marque": "Toyota",     "modele": "Yaris",    "type": "citadine",   "places": 5, "prix_jour": 35,  "transmission": "automatique", "carburant": "hybride"},
    {"id": 8, "marque": "Volkswagen", "modele": "Touareg",  "type": "suv",        "places": 7, "prix_jour": 95,  "transmission": "automatique", "carburant": "diesel"},
]

reservations = []

@app.route('/')
def index():
    message = "Aucune voiture disponible pour le moment." if not voitures else None
    return render_template(
        'index.html',
        voitures=voitures,
        message=message,
        reservations_count=len(reservations),
    )

def get_next_reservation_id():
    return max((reservation["id"] for reservation in reservations), default=0) + 1

def get_next_car_id():
    return max((voiture["id"] for voiture in voitures), default=0) + 1

def get_car_by_id(voiture_id):
    return next((voiture for voiture in voitures if voiture["id"] == voiture_id), None)

def get_reservations_by_car():
    grouped_reservations = {voiture["id"]: [] for voiture in voitures}
    for reservation in reservations:
        grouped_reservations.setdefault(reservation["voiture_id"], []).append(reservation)
    return grouped_reservations

def build_car_from_form(voiture_id):
    return {
        "id": voiture_id,
        "marque": request.form["marque"].strip(),
        "modele": request.form["modele"].strip(),
        "type": request.form["type"],
        "places": int(request.form["places"]),
        "prix_jour": int(request.form["prix_jour"]),
        "transmission": request.form["transmission"],
        "carburant": request.form["carburant"],
    }

def build_reservation_from_form(voiture):
    date_debut = date.fromisoformat(request.form["date_debut"])
    date_fin = date.fromisoformat(request.form["date_fin"])
    duree = (date_fin - date_debut).days + 1

    return {
        "id": get_next_reservation_id(),
        "voiture_id": voiture["id"],
        "client_nom": request.form["client_nom"].strip(),
        "client_email": request.form["client_email"].strip(),
        "client_telephone": request.form["client_telephone"].strip(),
        "date_debut": date_debut.isoformat(),
        "date_fin": date_fin.isoformat(),
        "duree": duree,
        "total": duree * voiture["prix_jour"],
    }

@app.route('/voitures/<int:voiture_id>/reserve', methods=['POST'])
def reserve_car(voiture_id):
    voiture = get_car_by_id(voiture_id)
    if voiture is None:
        flash("Voiture introuvable.", "error")
        return redirect(url_for('index'))

    try:
        reservation = build_reservation_from_form(voiture)
    except ValueError:
        flash("Les dates de reservation sont invalides.", "error")
        return redirect(url_for('index', _anchor='catalogue'))

    if not reservation["client_nom"] or not reservation["client_email"] or not reservation["client_telephone"]:
        flash("Veuillez remplir toutes les informations client.", "error")
        return redirect(url_for('index', _anchor='catalogue'))

    if reservation["duree"] <= 0:
        flash("La date de fin doit etre apres la date de debut.", "error")
        return redirect(url_for('index', _anchor='catalogue'))

    reservations.append(reservation)
    flash(
        f"Reservation confirmee pour {voiture['marque']} {voiture['modele']} - total {reservation['total']} DH.",
        "success",
    )
    return redirect(url_for('index', _anchor='catalogue'))

@app.route('/admin')
def admin_cars():
    return render_template(
        'admin.html',
        voitures=voitures,
        reservations=reservations,
        reservations_by_car=get_reservations_by_car(),
    )

@app.route('/admin/voitures/add', methods=['POST'])
def add_car():
    voitures.append(build_car_from_form(get_next_car_id()))
    flash("Voiture ajoutee avec succes.", "success")
    return redirect(url_for('admin_cars'))

@app.route('/admin/voitures/<int:voiture_id>/update', methods=['POST'])
def update_car(voiture_id):
    voiture = get_car_by_id(voiture_id)
    if voiture is None:
        flash("Voiture introuvable.", "error")
        return redirect(url_for('admin_cars'))

    voiture.update(build_car_from_form(voiture_id))
    flash("Voiture modifiee avec succes.", "success")
    return redirect(url_for('admin_cars'))

@app.route('/admin/voitures/<int:voiture_id>/delete', methods=['POST'])
def delete_car(voiture_id):
    voiture = get_car_by_id(voiture_id)
    if voiture is None:
        flash("Voiture introuvable.", "error")
        return redirect(url_for('admin_cars'))

    voitures.remove(voiture)
    reservations[:] = [
        reservation for reservation in reservations
        if reservation["voiture_id"] != voiture_id
    ]
    flash("Voiture supprimee avec succes.", "success")
    return redirect(url_for('admin_cars'))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data.get('messages', [])

    api_key = os.environ.get('GROQ_API_KEY')
    if not api_key:
        return jsonify({"error": "GROQ_API_KEY non configurée. Ajoutez-la dans le fichier .env"}), 500

    catalogue = json.dumps(
        [{"marque": v["marque"], "modele": v["modele"], "type": v["type"],
          "places": v["places"], "prix_jour": v["prix_jour"] + 10,
          "transmission": v["transmission"], "carburant": v["carburant"]}
         for v in voitures],
        ensure_ascii=False, indent=2
    )

    system_prompt = f"""Tu es Alex, un conseiller sympathique de l'agence AutoLoc. Tu aides les clients à trouver la voiture idéale.

Catalogue disponible:
{catalogue}

Instructions:
- Accueille chaleureusement le client dès le premier message.
- Pose des questions une par une (pas toutes en même temps) pour cerner ses besoins:
  1. Budget journalier approximatif
  2. Nombre de passagers
  3. Type de trajet (ville / vacances / longue route / déménagement)
  4. Préférence transmission (automatique / manuelle / peu importe)
- Après 3 à 4 échanges, recommande LA voiture la plus adaptée, cite son nom complet (marque + modèle), son prix, et explique en 2 phrases pourquoi c'est le bon choix.
- Si le budget est trop bas pour toutes les voitures, propose la moins chère et mentionne la différence.
- Réponds TOUJOURS en français. Sois concis (max 3 phrases par réponse). Sois chaleureux."""

    groq_messages = [{"role": "system", "content": system_prompt}]
    for msg in messages:
        role = "assistant" if msg["role"] == "assistant" else "user"
        groq_messages.append({"role": role, "content": msg["content"]})

    try:
        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=groq_messages,
            max_tokens=400,
        )
        reply = completion.choices[0].message.content
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": f"Erreur Groq : {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
