# seed.py
from app import create_app
from extensions import db
from models import Newsletter
from faker import Faker

def seed_database():
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        db.session.query(Newsletter).delete()
        
        # Create fake data
        fake = Faker()
        newsletters = []
        for _ in range(20):
            newsletter = Newsletter(
                title=fake.sentence(),
                body=fake.paragraph(nb_sentences=5)
            )
            newsletters.append(newsletter)
        
        db.session.add_all(newsletters)
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()