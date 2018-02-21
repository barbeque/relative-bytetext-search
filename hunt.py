import sys

def safe_print(maybe_illegal, char_offset):
    sys.stdout.write('%d: ' % char_offset)

    for i in range(len(maybe_illegal)):
        val = ord(maybe_illegal[i]) + char_offset
        if val >= 65 and val <= 127:
            # seems ok
            sys.stdout.write(chr(val))
        else:
            sys.stdout.write('?')
    print '' # newline

def get_pattern(search_string):
    result = [0] * len(search_string)
    for i in range(len(search_string)):
        result[i] = ord(search_string[i]) - ord(search_string[0])
    return result

def string_matches_pattern(chunk, pattern):
    if len(chunk) != len(pattern):
        return False

    for i in range(len(chunk)):
        our_diff = ord(chunk[i]) - ord(chunk[0])
        if our_diff <> pattern[i]:
            return False

    return True

def hunt(filename, search_string):
    attempts = 0

    print('Looking for "%s" in %s' % (search_string, filename))
    pattern = get_pattern(search_string)

    with open(filename, "rb") as f:
        while True:
            buf = f.read(len(search_string))
            if not buf or len(buf) < len(search_string):
                break

            if string_matches_pattern(buf, pattern):
                DEBUG_PREVIEW_SIZE = 35
                offset = ord(search_string[0]) - ord(buf[0])
                f.seek(-len(search_string), 1)
                temp_buf = f.read(DEBUG_PREVIEW_SIZE)
                safe_print(temp_buf, offset)
                f.seek(-DEBUG_PREVIEW_SIZE + len(search_string), 1)

            attempts += 1

            # seek backward so we don't have to count on it being aligned
            seek = len(search_string) - 1
            f.seek(-seek, 1)

    print('Total attempts: %d' % attempts)

assert get_pattern('foobar')[0] == 0
assert get_pattern('abcdef') == [0, 1, 2, 3, 4, 5]
assert string_matches_pattern('light', get_pattern('light'))
assert string_matches_pattern('light', get_pattern('LIGHT'))
assert string_matches_pattern('mjhiu', get_pattern('light'))

if __name__ == '__main__': hunt(sys.argv[1], ' '.join(sys.argv[2:]))
