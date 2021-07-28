# coding_challenge

This is a simple backeend server which uses Flask.

## Prerequisites

Make sure you have docker if you want to run in a container and python3 if you want to run locally.

### Run locally

1. Create a virtual env: `virtualenv venv`
2. Activate it: `source venv/bin/activate`
3. Install dependencies: `pip3 install -r requirements.txt`
4. Running the app:`python3 server.py`

### Ruin with Docker

1. Build image with docker-compose : `docker-compose build`.
2. Run the app on fly:`docker-compose up`

### Further explanations

- This application has 3 files : `server.py`, `database.py` and `key.json`
- `server.py` is the server handling all traffict from browser to the database.
- `database.py` handles database queries.
- `key.json` store symetric key for encryption and decryption.

### Security risks/assumptions

- `symetric key`: we store the symetric in the project because the app lacks infrastructure for keeping the key secret.
- `suggestion`: key should be keep in secret secure places like aws-secret-manager.
- The application checks input and performs `input sanitization` to prevent `XSS Attack`.
- Encrpytion is considered for all message and url stored in the in-memroy database, becuase incase an attacker hacks into database he/she can not see the data in plaintext.
- Data stored in the database automatically delete themselves after 7 days, we compare the day of today and going back 7 days if any data matches the date it is deleted. This is achieved by a cron in `server,py`.
- For `randomization URL` application use `uuid` which has low chance of collision and infeasable to guess.

### Database

1. App use in-memory database. However, sometimes you have to make several request for database to save the data so you can access the data through url.
2. Once the database save the data , onwards the application runs smooth hence no need of multiple request to save the data

### Routes
1. `server.py`:
    - `@app.route("/",methods=['POST'])` : post message to the server
    - `@app.route("/message/<url>",methods=["GET"])` : with right url it bring the message stored in the database.
    - `@app.route('/delete',methods=['POST'])` : delete all messages which have expired.

### Database functions

- `connect` : create the in-memory database and create a table , furthermore inserting data to the table
- `access_db` : Retrieve data from database when quired
- `delete_data` :  Delete all the data which matches the quiry.

### Pytest

- I managed to run 3 test with score 100%
- I could not test some other function since, I have not master the pytest. To be honest this is the first time I tried a pytest