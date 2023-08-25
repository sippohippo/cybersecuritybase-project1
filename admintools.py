from sqlalchemy.sql import text
from database import db


def get_participants():
    query = text("""
            SELECT DISTINCT email
            FROM users
            WHERE id IN (
                SELECT DISTINCT userId
                FROM results
                )
            """)
    result = db.session.execute(query)
    participants = result.fetchall()
    return participants


def total_responses():
    query = text("""
            SELECT COUNT(id)
            FROM results
            """)
    result = db.session.execute(query)
    count = result.fetchone()[0]
    return count


def average_accuracy():
    query = text("""
            SELECT AVG(accuracy)
            FROM results
            """)
    result = db.session.execute(query)
    accuracy = result.fetchone()[0]
    return accuracy


def remove_user(user_id):
    query = text("""
            DELETE FROM votes
            WHERE userId=:userId
            """)
    db.session.execute(query, {"userId":user_id})

    query = text("""
            DELETE FROM results
            WHERE userId=:userId
            """)
    db.session.execute(query, {"userId":user_id})

    query = text("""
            DELETE FROM users
            WHERE id=:userId
            """)
    db.session.execute(query, {"userId":user_id})

    db.session.commit()


def get_id(email):
    query = text("""
            SELECT id
            FROM users
            WHERE email=:email
            """)
    result = db.session.execute(query, {"email":email})
    user_id = result.fetchone()
    return user_id
