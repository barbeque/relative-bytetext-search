# Relative bytetext searcher

## When would you want to use this?
Imagine you have a binary file (like a Super Nintendo ROM) where you want to decipher the text. Often, text in ROMs doesn't use straight ASCII, and is usually just indices into a text table that is used to look up characters and special control code.

With this tool, you can try to find patterns in the file that 'look like' your target text, and then see what the text around it would look like with that offset.

## How to use
> hunt.py (file) (search phrases...)

Here is an example of it in use:
```
$ python hunt.py Phantasy\ Star\ IV\ \(4\)\ \[\!\].bin meseta
Looking for "meseta" in Phantasy Star IV (4) [!].bin
40: mesetaZ????????????is?????Z????????
40: mesetaZ??CC?meseta?procuredZ??R???R
40: meseta?procuredZ??R???R???R?V?R?r?R
70: meseta{?]ouldFyouFcareFtoFstay??FZh
70: meseta{?]illFyouFwantFtoFstay??Zhan
70: meseta{?NowFaboutFthat??FZhankFyouF
70: meseta{?allFright??Zhanks??]illFyou
70: meseta}Fright??ZhanksFaFlot??Yometh
Total attempts: 3145723
```
As you can see, there are two different offsets in use, which probably indicates there are two different text tables (maybe two different fonts?).

Some other things we've discovered, at least in the second set (+70):
 * `F` is probably supposed to be a space character.
 * Uppercase characters have a different offset than lowercase (with `T` being shown as `Z`). An offset of 6 indicates `A`-`F` are special characters, maybe punctuation.

## Limitations
Obviously, this only works on uncompressed/unencrypted text patterns that are stored in alphabetical order.
