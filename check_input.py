def check_num(text: str) -> bool:

    result = True
    try:
        num = int(text)
    except ValueError:
        result = False

    return result