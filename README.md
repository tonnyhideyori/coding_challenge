# coding_challenge

This is a simple backend server that uses Flask.

## Prerequisites

Make sure you have docker if you want to run in a container and python3 if you want to run locally.

### Run locally

1. Create a virtual env: `virtualenv venv`
2. Activate it: `source venv/bin/activate`
3. Install dependencies: `pip3 install -r requirements.txt`
4. Running the app:`python3 server.py`

### Run with Docker

1. Build an image with docker-compose : `docker-compose build`.
2. Run the app on fly:`docker-compose up`

### Further explanations

- This application has three files : `server.py`, `database.py` and `key.json`
- `server.py` is the server handling all traffic from the browser to the database.
- `database.py` handles database queries.
- `key.json` store symmetric key for encryption and decryption.

### Security risks/assumptions

- `symmetric key`: we store the symmetric in the project because the app lacks infrastructure for keeping the key secret.
- `suggestion`: key should be keep in secret secure places like AWS-secret-manager.
- The application checks the input and performs `input sanitization` to prevent `XSS Attack`.
- Encryption is considered for all messages and URLs stored in the in-memory database because in case an attacker hacks into the database, he/she can not see the data in plaintext.
- Data stored in the database automatically delete themselves after seven days, we compare the day of today and going back seven days if any data matches the date it is deleted. it is achieved by a cron in `server.py`.
- For the `randomization URL` application, use `uuid`, which has a low chance of collision and is infeasible to guess.

### Database

1. App uses an in-memory database. However, sometimes you have to make several requests for the database to save the data so you can access the data through a URL.
2. Once the database saves the data, onwards the application runs smoothly hence no need of multiple requests to save the data

### Routes
1. `server.py`:
    - `@app.route("/",methods=['POST'])` : post message to the server
    - `@app.route("/message/<url>",methods=["GET"])` : with right url it bring the message stored in the database.
    - `@app.route('/delete',methods=['POST'])` : delete all messages which have expired.

### Database functions

- `connect` : create the in-memory database and create a table, furthermore inserting data to the table
- `access_db` : Retrieve data from database when quired
- `delete_data` :  Delete all the data which matches the query.

### Pytest

- I managed to run 3 tests with a score of 100%
- I could not test some other function since I have not mastered the pytest. To be honest, this is the first time I have tried a pytest