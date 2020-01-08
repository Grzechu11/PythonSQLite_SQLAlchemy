from run import api, fields

user_api_response = api.model('user_api_response', {
    'name': fields.String(description='The user name', required=True),
    'email': fields.String(description='The user email', required=True)
})

user_list_api_response = api.model('user_list_api_response', {
    'items': fields.List(fields.Nested(user_api_response))
})