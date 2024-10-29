from flask import Flask, render_template, request, redirect, url_for, jsonify
from model import add_contact, get_contacts, update_contact, delete_contact
import os

app = Flask(__name__)
app.config['TEMPLATES_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')

print(app.config['TEMPLATES_FOLDER'] )
@app.route('/')
def index():
    contacts = get_contacts()
    return render_template('index.html', contacts=contacts)

@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.form
    add_contact(data['name'], data['phone'], data['location'])
    return redirect(url_for('index'))

@app.route('/contacts/<int:contact_id>', methods=['POST'])
def edit_contact(contact_id):
    data = request.form
    update_contact(contact_id, data['name'], data['phone'], data['location'])
    return redirect(url_for('index'))

@app.route('/contacts/<int:contact_id>/delete', methods=['POST'])
def remove_contact(contact_id):
    delete_contact(contact_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)