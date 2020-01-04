src = open('a.txt', 'rb')
des = open('a_copy.txt', 'wb')
des.write(src.read())

des.close()
src.close()


