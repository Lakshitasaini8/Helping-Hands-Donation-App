from flask_restplus import Api

from .user import user_ns as ns1
from .application import app_ns as ns2

api = Api(
    title='Helping Hands',
    version='0.1.0',
    description='Adopt',
)

api.add_namespace(ns1)
api.add_namespace(ns2)
