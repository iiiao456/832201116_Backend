from config import get_db_connection

def add_contact(name, phone, location):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO contacts (name, phone, location) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, phone, location))
    connection.commit()
    cursor.close()
    connection.close()

def get_contacts():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    cursor.close()
    connection.close()
    return contacts

def update_contact(contact_id, name, phone, location):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "UPDATE contacts SET name=%s, phone=%s, location=%s WHERE id=%s"
    cursor.execute(query, (name, phone, location, contact_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_contact(contact_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM contacts WHERE id=%s"
    cursor.execute(query, (contact_id,))
    connection.commit()
    cursor.close()
    connection.close()