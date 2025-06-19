# app.py
from flask import Flask, request, make_response
from flask_restful import Api, Resource
from extensions import db, migrate
from models import Newsletter

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletters.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(app)

    class Home(Resource):
        def get(self):
            return {"message": "Welcome to the Newsletter RESTful API"}, 200

    class Newsletters(Resource):
        def get(self):
            newsletters = [n.to_dict() for n in Newsletter.query.all()]
            return newsletters, 200

        def post(self):
            data = request.get_json()
            new_newsletter = Newsletter(
                title=data['title'],
                body=data['body']
            )
            db.session.add(new_newsletter)
            db.session.commit()
            return new_newsletter.to_dict(), 201

    class NewsletterByID(Resource):
        def get(self, id):
            newsletter = Newsletter.query.get_or_404(id)
            return newsletter.to_dict(), 200

    api.add_resource(Home, '/')
    api.add_resource(Newsletters, '/newsletters')
    api.add_resource(NewsletterByID, '/newsletters/<int:id>')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)