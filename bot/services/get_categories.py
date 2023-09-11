from services import get_user_session_key, session


def get_user_categories(url, user_id):
    session_key = get_user_session_key(user_id=user_id)
    session.cookies.set('sessionid', session_key)
    response = session.get(
        url='http://server:8000' + url,
    )
    response = response.json()
    return response
