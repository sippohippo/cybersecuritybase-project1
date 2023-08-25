CREATE TABLE users (
id SERIAL PRIMARY KEY, 
email TEXT UNIQUE, 
password TEXT, 
admin BOOLEAN,
acceptTerms BOOLEAN
);

CREATE TABLE images (
id SERIAL PRIMARY KEY,
name TEXT,
generated BOOLEAN,
data BYTEA
);

CREATE TABLE posts (
id SERIAL PRIMARY KEY,
type TEXT,
name TEXT,
handle TEXT,
content TEXT,
profilePicId INT REFERENCES images(id)
);

CREATE TABLE votes (
id SERIAL PRIMARY KEY,
isBot BOOLEAN,
postId INT REFERENCES posts(id),
userId INT REFERENCES users(id)
);

CREATE TABLE results (
id SERIAL PRIMARY KEY, 
accuracy REAL,
userId INT REFERENCES users(id)
);