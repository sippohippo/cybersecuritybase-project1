from secrets import token_hex
#from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from flask import session
from database import db

def login(email, password):
    query = text("""
            SELECT id, email, password, admin
            FROM users
            WHERE email=:email
            """)
    result = db.session.execute(query, {"email":email})

    user = result.fetchone()

    if email_exists(email):
        #if check_password_hash(user.password, password):
        if user.password == password:
            session["user_id"] = user.id
            session["email"] = email
            session["csrf_token"] = token_hex(16)
            session["admin"] = False
            if user.admin:
                session["admin"] = True
            return True
        return False
    return False


def newuser(email, password):
    #password = generate_password_hash(password)
    if email_exists(email):
        return False

    query = f"INSERT INTO users (admin,acceptTerms,password,email) VALUES (FALSE,FALSE,'{password}','{email}')"
          
    db.session.execute(text(query))
    db.session.commit()

    # query = text("""
    #         INSERT INTO users (email,password,admin,acceptTerms)
    #         VALUES (:email,:password,FALSE,FALSE)
    #         """)
    # db.session.execute(query, {"email":email, "password":password})
    # db.session.commit()

    return login(email, password)


def email_exists(email):
    query = text("""
            SELECT email
            FROM users
            WHERE email=:email
            """)
    result = db.session.execute(query, {"email":email})
    if not result.fetchone():
        return False
    return True


def accept_terms(email):
    query = text("""
            UPDATE users 
            SET acceptTerms = TRUE 
            WHERE email=:email
            """)
    db.session.execute(query, {"email":email})
    db.session.commit()


def terms_accepted(email):
    query = text("""
            SELECT acceptTerms
            FROM users
            WHERE email=:email
            """)
    result = db.session.execute(query, {"email":email})
    response = result.fetchone()[0]
    if response:
        return True
    return False


def is_admin(email):
    query = text("""
            SELECT admin
            FROM users
            WHERE email=:email
            """)
    result = db.session.execute(query, {"email":email})
    response = result.fetchone()[0]
    if response:
        return True
    return False
