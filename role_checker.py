def can_access_dashboard(user_role):
    """
    Checks if the user has access to the dashboard.

    Access is granted to 'admin' and 'moderator' roles.

    Args:
        user_role (str): The role of the user.

    Returns:
        bool: True if access is allowed, False otherwise.
    """
    if user_role == "admin" or "moderator":
        return True
    return False