from flask_pymongo import PyMongo

mongo = PyMongo()


def init_mongodb(app):
    mongo.init_app(app=app, uri=app.config['MONGO_URI'])
