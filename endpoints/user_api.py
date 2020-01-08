
from run import app, api, Resource, request, fields, Namespace
from datetime import datetime

from database.dbcontext import db_session
from database.models.dbUser import User


ns = api.namespace('user', 
                   description='User endpoints')

from endpoints.models.user_api_response import user_api_response, user_list_api_response
from endpoints.models.add_user_api_request import add_user_api_request

@ns.route('/<name>')
@ns.doc(params={'name': 'The user name'})
class UserApi_Get(Resource):
    @ns.marshal_with(user_api_response, mask=False, code=200)
    def get(self, name):       
        user = User.query.filter(User.name == name).first() 
        return user

@ns.route('/')
class UserApi_Gets(Resource):
    @ns.marshal_with(user_list_api_response, mask=False, code=200)
    def get(self):       
        users = User.query.all()
        return {'items': users}

@ns.route('')
class UserApi_Post(Resource):
    @ns.expect(add_user_api_request)
    @ns.marshal_with(user_api_response, mask=False, code=200)
    def post(self):       
        now = datetime.now()
        formatted_now = now.strftime("%A, %d %B, %Y at %X")        
        r = request.json      
        u = User(r.get('name'), r.get('email'))
        db_session.add(u)
        db_session.commit()
        return u