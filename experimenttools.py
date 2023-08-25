from random import sample, shuffle
from sqlalchemy.sql import text
from flask import session
from database import db


def select_posts(n_posts):
    query = text("""
            SELECT p.name, p.handle, p.content, p.type, i.id, p.id
            FROM posts p, images i
            WHERE p.profilePicId = i.id
            """)
    result = db.session.execute(query).fetchall()
    posts = sample(result, n_posts)
    shuffle(posts)
    return posts


def select_image(id):
    query = text("""
            SELECT data
            FROM images
            WHERE id=:id
            """)
    result = db.session.execute(query, {"id":id})
    data = result.fetchone()[0]
    return data


def record_votes(profiles, votes):
    profile_ids = []
    profile_labels = []
    total_correct = 0

    for i in profiles:
        profile_ids.append(i[5])
        label = i[3]
        if label == "bot":
            profile_labels.append("TRUE")
        else:
            profile_labels.append("FALSE")

    for i in range(0, len(votes)):
        vote = votes[i]
        post = profile_ids[i]
        true_label = profile_labels[i]
        if vote == true_label:
            total_correct += 1

        user = session["user_id"]
        query = text("""
                INSERT INTO votes (isBot, postId, userId)
                VALUES (:isBot, :postId, :userId)
                """)
        db.session.execute(query, {"isBot":vote, "postId":post, "userId":user})
    db.session.commit()
    return round(total_correct/len(profiles), 2)*100


def record_accuracy(accuracy):
    user = session["user_id"]
    query = text("""
            INSERT INTO results (accuracy, userId)
            VALUES (:accuracy, :userId)
            """)
    db.session.execute(query, {"accuracy":accuracy, "userId":user})
    db.session.commit()
