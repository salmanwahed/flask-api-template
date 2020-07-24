from app.model import Contact
from app import db
from flask_restful import Resource, abort
from flask import request
from app.marshmallow_schema import contacts_schema, contact_schema


class ContactResource(Resource):
    def get(self):
        try:
            contacts = Contact.query.all()
            return contacts_schema.dump(contacts)
        except Exception as ex:
            abort(http_status_code=500, error=ex.args[0])

    def post(self):
        try:
            new_contact = Contact(name=request.json['name'], email=request.json['email'], phone=request.json['phone'])
            db.session.add(new_contact)
            db.session.commit()
            return contact_schema.dump(new_contact)
        except Exception as ex:
            abort(http_status_code=500, error=ex.args[0])




