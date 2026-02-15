def withdraw(balance, amount):
    """
    Processes a withdrawal from a bank account.

    Args:
        balance (float): The current account balance.
        amount (float): The amount to withdraw.

    Returns:
        float: The new balance after withdrawal.

    Raises:
        ValueError: If amount exceeds balance.
    """
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount