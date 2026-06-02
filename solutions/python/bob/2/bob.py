def response(hey_bob):
    reply = 'Whatever.'
    statement = hey_bob.strip()
    is_upper = hey_bob.isupper()
    if not statement:
        reply = 'Fine. Be that way!'
    if statement.endswith('?'):
        reply = 'Sure.'
    if is_upper:
        reply = 'Whoa, chill out!'
    if statement.endswith('?') and is_upper:
        reply = "Calm down, I know what I'm doing!"

    return reply
