from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', bio='demo makes music', alias='Demorgan', profile_image="asdfgasddfg", first_name='dem', last_name='ooo', style_id=1)
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password', bio='demo makes bad music', alias='Demorgan2', profile_image="asdfgasddfgyyy", first_name='marn', last_name='eee', style_id=2)
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', bio='demo makes good music', alias='Demorgan3', profile_image="asdfgasddfguuu", first_name='bobb', last_name='eee', style_id=3)

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()