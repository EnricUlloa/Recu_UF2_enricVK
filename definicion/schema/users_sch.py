def user_schema(user) -> dict:
    return {
        "id": user[0],
        "nombre": user[1],
        "apellido": user[2],
        "email": user[3],
        "curso": user[4],
        "anio": user[5],
        "direccion": user[6]
    }

def users_schema(users) -> list[dict]:
    return [user_schema(user) for user in users]
