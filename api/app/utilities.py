def success_response(message):
    return json_response(200, 'OK', message)

def error_response(args_list):
    msg_list = []
    message = ''
    for arg in args_list:
        message = f'Missing parameter {arg}'
        msg_list.append(message)
    return json_response(400, 'Bad request', msg_list)


def json_response(code, status, message):
    return {
        'Status': code,
        'StatusText': status,
        'Message': message,
    }
