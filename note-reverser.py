import subprocess
from datetime import date

def read_from_clipboard():
    return subprocess.check_output(
        'pbpaste', env={'LANG': 'en_US.UTF-8'})

text = read_from_clipboard()

split = text.split('\n\n')
split.reverse()

now = date.today()
today = now.isoformat()
filename = '/Users/xwh/Dropbox/Applications/Bitcron/xwh.bitcron.com/2018/' + today + '.md'

file_object = open(filename, 'a')

for line in split:
    file_object.write(line)
    file_object.write('\n\n')
file_object.close()
