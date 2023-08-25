# Cyber Security Base 2023 Project 1

## What is this?

This is a basic app with five security flaws intentionally left in the source code. This repository is my submissions in the University of Helsinki course Cyber Security Base 2023 Project I. You can find the course materials [here](https://cybersecuritybase.mooc.fi/module-3.1). The file [EssayCyberSecurityMooc.txt](https://github.com/sippohippo/cybersecuritybase-project1/blob/main/EssayCyberSecurityMooc.txt) contains the descriptions of the flaws.


## Short description of the app

This flask app is a small browser experiment / game where participants are shown a simulated social media feed and asked to label the profiles they see as humans or bots. This is used to demonstrate how distinguishing profile pictures and posts generated with deep learning from genuine posts and pictures is very difficult. A full description of the project is given in the bottom of the page.


## Installation, setup and running the app

This app and guide assumes you have access to a terminal/console which has bash. 

1. Install PostgreSQL if you do not have it already: https://www.postgresql.org/download/

2. Clone this repository and go to the newly created directory

```bash
git clone https://github.com/sippohippo/cybersecuritybase-project1
```

```bash
cd cybersecuritybase-project1
```

3. This step is *optional*. If you are not using the default postgres database_url postgresql://localhost then change it to the correct one by opening the .env file.

4. Activate a virtual environment and install dependencies

```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r ./requirements.txt
```

5. Setup the database and populate it with the data. Note, you need to change the image file addresses to your local ones in lines 5-10 in the test data! 

```bash
psql < schema.sql
```
```bash
psql < data.sql
```

6. Start the app

```bash
flask run
```

7. Open the app by going to http://127.0.0.1:5000 in your browser


## User guide

1. Create a new account
2. Start the experiment
3. Vote for each profile and press submit
4. See the results
5. Return to main menu and quit or do the experiment again

## Admin account

The data contains a default profile with the username admin and password admin. 

## App description

The purpose of this app is two-fold. First, it works as a game that demonstrates how difficult it is to detect bot profiles on a social media feed. Second, from the admins point of view it allows running experiments and collecting data on how well people playing the game can distinguish real and fake profiles. 

For the user, the app is a game where they can log in and play. When they begin to play, they are presented a simulated social media feed (e.g. like on Twitter), with multiple posts visible at once. These posts will be drawn randomly from a large sample of genuine and fake ones. Thus, each game will be unique and each user will see a different instance of the simulated social media feed. The user can then vote for each of these posts if they believe it is written by a bot or a real human. Once they are done labeling each post, they see how many accounts they labeled correctly and what their score is.

For the administrator, the app allows viewing statistics on how well the users of the app have performed in the game and removing users. 

The fake profiles and general setup of this type of an experiment is described in more detail and demonstrated in the paper *Are Deep Learning-Generated Social Media Profiles Indistinguishable from Real Profiles?* [[1]](#1). This previous implementation was done with a Qualtrics survey, and the goal of this project is to allow hosting the experiment on a webpage in the future.

### Main features

* The user can log in and out or create a new profile 
* After logging in the user sees the main menu where the options are to play the game or log out
* When choosing to play the game, the app takes the user to a new page which consists of a simulated social media feed with 3 visible posts. Each post contains text as well as the name and profile picture of the profile that posted it. The user can mark each profile as a human or a bot. 
* After completing the task the user sees how many profiles they labeled accurately and then can play again or go to the main menu.
* The administrator can remove participants
* The administrator can view statistics on how well the users have performed

### Database tables

* users (contains credentials for users and admins)
* posts (contains the posts and profile information of the creator of the post. The data of real profiles has been collected earlier via the Twitter API and generated data produced with GPT-3)
* images (profile images created with StyleGAN as well as real profile images)
* votes (contains data on how each user voted on a given experiment)
* results (contains the statistics from each experiment that was conducted)


### Note on data and GDPR compliance

The "real" test profiles in the test data of this public Github repository do not contain genuine names or post content and are generated with a similar method as the fake profiles. All data in this repository is purely for demonstrating that the app works. In production, the real profiles would contain data collected via Twitter's API. 


## References
<a id="1">[1]</a> 
Rossi, S., Kwon, Y., Auglend, O., Mukkamala, R., Rossi, M., & Thatcher, J. (2023). 
Are Deep Learning-Generated Social Media Profiles Indistinguishable from Real Profiles?
Proceedings of the 56th Hawaii International Conference on System Sciences. https://hdl.handle.net/10125/102645.
