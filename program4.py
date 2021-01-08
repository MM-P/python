"""
Dzisiaj kolejny piątek, a przed nami kolejny weekend w tym tygodniu 😂 
Wczoraj spalaliśmy kalorie 🏃‍♀️ (taaa, siedząć przed kompem i klepiąc kod 😎),
 dzisiaj przestajemy się oszukiwać i siadamy na kanapie przed Netflixem, HBO 
 czy zwykłą telewizją 📺 Propozycja na dzisiaj dość luźna, ale całkiem "życiowa",
 bo będziemy odtwarzać backend Filmweba czy podobnych stron 🎥 
 A jeśli ktoś nie lubi filmów, to zawsze można poszukać odpowiedniego 
 API i zrobić wyszukiwarkę gier 🎮 i na przykład zamiast aktorów pobrać
 platformy, na które gra wyszła 🧐
PS: W weekend nie publikujemy nowych zadań, trzeba odpocząć 😴
PPS: Ale można zapraszać na wydarzenie znajomych, którzy ciężko 
pracują cały tydzień, a w weekend znajdą czas, żeby nadrobić poprzednie zadanka 🤯
PPPS: Wiecie, że w 2020 miała wyjść/wyszła bollywódzka wersja #RAMBO? 😱
#MOVIE #FINDER
Przy wykorzystaniu API (np. IMDB) wyszukaj wszystkie części 
filmu zadanego w wyszukiwaniu (np. Rambo, Scary Movie, Shrek). 
Można przyjąć założenie, że wszystkie filmy “z serii” muszą zawierać szukany ciąg 
- czasem zdarzają się błędne wyniki wyszukiwania z baz, można je spróbować odfiltrować.
 Wyświetl dla każdego podstawowe informacje np. rok, długość, ocena, spis aktorów (pierwszych 5 z listy).
Przykładowe API do wykorzystania: 
https://rapidapi.com/apidojo/api/imdb8/endpoints - do wyszukania filmów z daną nazwą 
(do odfiltrowania można użyć warunku, że dany rekord posiada nazwę i rok wydania)
https://rapidapi.com/.../imdb-internet-movie-database... - pobranie szczegółów o danym filmie

"""






import imdb

moviesDB = imdb.IMDb()

film=input('Podaj Nazwe Filmu: ')

movies = moviesDB.search_movie(film)

x=0
print(f'Szukam filmu o nazwie: {film}:')

for i in movies:
    x=x+1
    title = i['title']
    year = i['year']
    print(f'{title} - {year}')  
    if x==5:
        break

for i in range(5):
    id = movies[i].getID()
    movie = moviesDB.get_movie(id)
    
    title = movie['title']
    year = movie['year']
    rating = movie['rating']
    directors = movie['directors']
    casting = movie['cast']
    
    print('\nInformacja o filmie:')
    print(f'{title} - {year}')
    print(f'Ranking: {rating}')
    print("")
    direcStr = ' '.join(map(str,directors))
    print(f'Dyrektor: {direcStr}')
    print("")
    actors = ', '.join(map(str, casting))
    print(f'Aktorzy: {actors}')
    print("")
