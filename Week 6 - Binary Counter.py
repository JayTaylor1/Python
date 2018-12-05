for count in range(0, 128):
    if count < 10:
        print(str(count) + "    " + '{0:08b}'.format(count))
    elif count < 100:
        print(str(count) + "   " + '{0:08b}'.format(count))
    else:
        print(str(count) + "  " + '{0:08b}'.format(count))
pass
