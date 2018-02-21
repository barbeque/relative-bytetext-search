import sys

def guess(buf, char_offset, search_string):
    if len(buf) != len(search_string):
        print('Guess and actual have different lengths, bailing early')
        return False

    for i in range(0, len(search_string)):
        juiced = chr((ord(buf[i]) + char_offset) % 256)
        if(juiced != search_string[i]):
            return False

    print('Offset could be %d:' % char_offset)

    return True

def safe_print(maybe_illegal, char_offset):
    for i in range(len(maybe_illegal)):
        val = ord(maybe_illegal[i]) + char_offset
        if val >= 65 and val <= 127:
            # seems ok
            sys.stdout.write(chr(val))
        else:
            sys.stdout.write('?')
    print '' # newline

def hunt(filename, search_string):
    attempts = 0

    print('Looking for %s in %s' % (search_string, filename))

    with open(filename, "rb") as f:
        for char_offset in range(-256,256):

            while True:
                buf = f.read(len(search_string))
                if not buf:
                    # eof
                    break
                attempts += 1
                if guess(buf, char_offset, search_string):
                    # let's print out the buf + some more
                    some_more = f.read(20)
                    safe_print(buf + some_more, char_offset)

                    break
                    # reset the file pointer for another read
            f.seek(0)
    print('Total attempts: %d' % attempts)

# FIXME: do this in a 'signal' approach (relative offset from c[i+1] to c[1])
# so it's faster

if __name__ == '__main__': hunt(sys.argv[1], ' '.join(sys.argv[2:]))
