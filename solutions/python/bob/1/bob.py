def response(hey_bob):
    response = 'Whatever.'
    statement = hey_bob.strip()
    is_upper = hey_bob.isupper()
    if not statement:
        response = 'Fine. Be that way!'
    if statement.endswith('?'):
        response = 'Sure.'
    if is_upper:
        response = 'Whoa, chill out!'
    if statement.endswith('?') and is_upper:
        response = "Calm down, I know what I'm doing!"

    return response
