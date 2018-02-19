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
    print('Looking for ' + search_string + ' in ' + filename + '\n')
    with open(filename, "rb") as f:
        for char_offset in range(-256,256):
            buf = f.read(len(search_string))
            if not buf: break
            if guess(buf, char_offset, search_string):
                print('We found the offset!')
                break

if __name__ == '__main__': hunt(sys.argv[1], ' '.join(sys.argv[2:]))
