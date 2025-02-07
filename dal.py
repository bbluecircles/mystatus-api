from django.db import connection

def get_actions_by_username(username):
    with connection.cursor() as cursor:
        cursor.callproc('get_actions_with_weights', [username])
        columns = [col[0] for col in cursor.description] if cursor.description else []
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return results