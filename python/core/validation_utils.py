def validate_id(value, field_name="id"):
    """
    Validate that the given value is a positive integer.
    Returns None if valid, else returns an error dict.
    """
    if not isinstance(value, int):
        return {
            "error": f"{field_name} must be an integer",
            "status": "failed"
        }

    if value <= 0:
        return {
            "error": f"{field_name} must be greater than 0",
            "status": "failed"
        }

    return None


def validate_required_fields(data: dict, required_fields: list):
    """
    Validate that required fields exist in a dictionary.
    """
    missing = [field for field in required_fields if field not in data]

    if missing:
        return {
            "error": f"Missing required fields: {', '.join(missing)}",
            "status": "failed"
        }

    return None