import pakcrack

print('\n\x1b[1;37m Checking Update...');time.sleep(0.5)

os.system('git pull')

try:

    import gtts

except IOError:

    os.system('pip install gtts')

def Update():

    exit('\033[1;31m(×) Commands On Update Please Wait For Update ❤ ')




pakcrack.pak()
