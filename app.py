from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

names = {}

# Define mandatory args
RouteTwo_put_args = reqparse.RequestParser()
RouteTwo_put_args.add_argument(
    "name", type=str, help="Name of person required", required=True)
RouteTwo_put_args.add_argument(
    "age", type=str, help="Age of person required", required=True)
RouteTwo_put_args.add_argument(
    "fav_food", type=str, help="Fav food of person required", required=True)


def abort_if_name_does_not_exist(name):
    if name not in names:
        abort(404, message="Names not in names dictionary")

def abort_if_name_exists(name):
    if name in names:
        abort(409, message="Name already in names dictionary")


class RouteOne(Resource):
    def get(self):
        return {"data": "RouteOne: GET"}

    def post(self):
        return {"data": "RouteOne: POST"}


class RouteTwo(Resource):
    def get(self, name):
        abort_if_name_does_not_exist(name)
        return names[name]

    def put(self, name):
        args = RouteTwo_put_args.parse_args()
        names[name] = args
        return names[name]
    
    def delete(self, name):
        abort_if_name_does_not_exist(name)
        del names[name]
        return f"{name} was deleted!"



# API Routing
api.add_resource(RouteOne, '/')
api.add_resource(RouteTwo, '/routetwo/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)
