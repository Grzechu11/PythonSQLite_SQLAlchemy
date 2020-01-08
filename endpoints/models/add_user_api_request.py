from run import api, fields

add_user_api_request = api.model('add_user_api_request', {
    'name': fields.String(description='The user name', required=True),
    'email': fields.String(description='The user email', required=True)
})