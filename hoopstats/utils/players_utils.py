# Basic Suffix Formula: <first_letter_of_last_name>/<first_five_letters_of_last_name><first_two_letters_of_first_name><unique_id>
def create_player_suffix(first_name: str, last_name: str, unique_id: str) -> str:
    """
    Utilizes the Suffix Formula above to construct the Basketball Reference Player Suffix

    Args:
        first_name (str): First Name of a Player
        last_name (str): Last Name of a Player
        unique_id (str): Unique ID for a Player (Used in the case of if two players have the same suffix)

    Returns:
        str: Basketball Reference Suffix
    """
    # Process last name
    last_name_part = last_name[:5].lower()
    if len(last_name) > 1:
        last_name_prefix = last_name[0].lower()
    else:
        last_name_prefix = ''

    # Process first name
    first_name_part = first_name[:2].lower()

    # Construct suffix
    suffix = f"{last_name_prefix}/{last_name_part}{first_name_part}{unique_id}"

    return suffix
