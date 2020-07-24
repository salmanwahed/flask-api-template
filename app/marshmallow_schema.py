from app import ma


class ContactSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "name", "phone")


contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)

