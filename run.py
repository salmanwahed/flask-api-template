from app import app, views
from app.model import db

if __name__ == '__main__':
    db.create_all()
    app.run()
