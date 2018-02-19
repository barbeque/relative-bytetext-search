import sys

def guess(buf, char_offset, search_string):
    if len(buf) != len(search_string):
        print('Guess and actual have different lengths, bailing early')
        return False

    for i in range(0, len(search_string)):
        juiced = chr((ord(buf[i]) + char_offset) % 256)
        if(juiced != search_string[i]):
            return False

    print('Offset is probably', char_offset)
    return True

def hunt(filename, search_string):
    attempts = 0
    print('Looking for ' + search_string + ' in ' + filename + '\n')
    with open(filename, "rb") as f:
        for char_offset in range(-256,256):
            while True:
                buf = f.read(len(search_string))
                if not buf:
                    print 'Done with char_offset = %d' % char_offset
                    break
                attempts += 1
                if guess(buf, char_offset, search_string):
                    print('We found the offset!')
                    break
                    # reset the file pointer for another read
            f.seek(0)
    print('Total attempts: %d' % attempts)

# FIXME: do this in a 'signal' approach (relative offset from c[i+1] to c[1])
# so it's faster

if __name__ == '__main__': hunt(sys.argv[1], ' '.join(sys.argv[2:]))
