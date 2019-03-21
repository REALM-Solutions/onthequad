import pyrebase

class DataBaseSetUp:

    def config():
        config ={
            'apiKey': "AIzaSyBEaQNRbDl0qmfTBORJ-4gbMdiBaSm3Q_o",
            'authDomain': "on-the-quad.firebaseapp.com",
            'databaseURL': "https://on-the-quad.firebaseio.com",
            'projectId': "on-the-quad",
            'storageBucket': "on-the-quad.appspot.com",
            'messagingSenderId': "535666577502"
        }
        firebase = pyrebase.initialize_app(config)
        return firebase   

    def setup(): 

        firebase = DataBaseSetUp.config()
        database = firebase.database()
        return database

    def authentication():

        firebase = DataBaseSetUp.config()
        authen = firebase.auth()
        return authen

    def noquote(s):
        return s
    pyrebase.pyrebase.quote = noquote
    
        