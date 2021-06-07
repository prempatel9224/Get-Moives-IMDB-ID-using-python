import imdb
#Enter The Movie Name Here
name = ''

ia = imdb.IMDb()
search = ia.search_movie(name)
s = search
open('info.txt', 'w').write(str(search))
text = open('info.txt', 'r')
idn = text.read()
id = idn[11:18]
print(id)
