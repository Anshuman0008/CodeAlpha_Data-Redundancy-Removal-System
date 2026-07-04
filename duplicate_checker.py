from database import get_connection

def is_duplicate(employee_id, email, phone):

    db = get_connection()

    cursor = db.cursor()

    query = """
    SELECT *
    FROM employee
    WHERE employee_id=%s
    OR email=%s
    OR phone=%s
    """

    cursor.execute(query, (employee_id, email, phone))

    result = cursor.fetchone()

    db.close()

    return result is not None
