def right_justify(term):
    pad_char = ' '
    line_size = 80
    term_size = len(term)
    pad_size = line_size - term_size
    padding = pad_char * pad_size
    print padding + str(term)

right_justify('Will')
