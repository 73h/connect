# Test hosting a Python-Flask-Application on Google Cloud Run and Google Firebase for static files

## This project is based on this page

https://medium.com/firebase-developers/hosting-flask-servers-on-firebase-from-scratch-c97cfb204579

### Development

Use ```dev.py``` for local run.

### Setup

#### Cloud Run

```
cd server
gcloud init
```

#### Firebase

```
npm init -y # creates a package.json
npm install -D firebase-tools
```

```
./node_modules/.bin/firebase login
./node_modules/.bin/firebase init hosting
```

### Deployment

#### Cloud Run

```
cd server
gcloud builds submit --tag gcr.io/connect-b9fa2/connect
gcloud beta run deploy --image gcr.io/connect-b9fa2/connect

```

#### Firebase

```
./node_modules/.bin/firebase deploy
```

Test configuration local

```
./node_modules/.bin/firebase serve
```
