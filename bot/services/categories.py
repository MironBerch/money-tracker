import json

from .session import get_csrf_token, get_user_session_key, session


def get_user_categories(url, user_id):
    session_key = get_user_session_key(user_id=user_id)
    session.cookies.set('sessionid', session_key)
    response = session.get(
        url='http://server:8000' + url,
    )
    response = response.json()
    return response


def create_category(user_id, name):
    session_key = get_user_session_key(user_id=user_id)
    session.cookies.set('sessionid', session_key)
    session.cookies.set('csrftoken', get_csrf_token(session))
    response = session.post(
        url='http://server:8000/api/categories-create/',
        data=json.dumps(
            {
                'name': str(name),
            },
        ),
        headers={
            'Content-Type': 'application/json',
        },
    )
    return response
