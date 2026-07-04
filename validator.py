def validate(data):

    if data["employee_id"] == "":
        return False

    if data["full_name"] == "":
        return False

    if data["email"] == "":
        return False

    if data["phone"] == "":
        return False

    return True
