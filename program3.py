"""
#feriechallenge #program3
No to trzeci dzień wyzwania! 🤩 Dzisiaj zapewne większość ma wolne (a zresztą i tak nie ma gdzie wyjść...),
więc proponujemy coś nieco bardziej skomplikowanego i chyba najbardziej #praktycznego - sami niedawno potrzebowaliśmy 
takiej funkcjonalności w naszej firmie do upraszczania życia 💌 Przenieśmy się do świata początkującego korpo 
lub nowoczesnego "zdigitalizowanego" urzędu 🏤, w którym systemy nie są skonfigurowane, 
o bazach danych nikt nie słyszał, więc są przechowywane w tabelkach w Excelu... 📝
#MAIL #SENDER
Stwórz prosty program, który będzie wysyłał spersonalizowany mailing do wybranych osób. 
“Bazą danych” jest plik Excela (aby było “ciekawiej” 😉 ) lub CSV, zawierający dwie kolumny
z nagłówkami: “E-mail” oraz “Imię i nazwisko” (zakładamy, że zawsze w takiej kolejności, a imię i nazwisko są oddzielone spacją). 
Do użytkowników należy wysłać maila z tematem “Your image” oraz spersonalizowaną prostą treścią 
np. “Hi {Imię}! it’s file generated for you”. Dodatkowo w załączniku maila znajduje się plik graficzny o nazwie “{Imię}_{Nazwisko}_image.png”
 (pliki są w zadanej lokalizacji). Odpowiednio zabezpiecz program (np. brakujący plik Excela, brakujące dane w Excelu, brak pliku png) 
 oraz zabezpiecz przed spamowaniem (np. jeden mail wysyłany co 1 sekundę). Mogą przydać się moduły: smtplib, email, ssl, xlrd, re, os. 
 
 
Propozycje rozszerzenia: dodaj opcję wysyłania maili z treścią w HTML oraz walidator poprawności maila
 (np. używając wyrażeń regularnych - moduł re).
"""

import pandas as pd 
import smtplib
from time import sleep 

your_email = "email@gmail.com"
your_password = "PASSWORD"
  
server = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
server.ehlo() 
server.login(your_email, your_password) 
  

email_list = pd.read_excel('email.xlsx') 
  

names = email_list['NAME']
 
emails = email_list['EMAIL'] 

for i in range(len(emails)):
   
    name = names[i] 
    email = emails[i]
    sp = name.split()
    imie=(sp [0])
    nazwisko=(sp[1])
    msg = "Hi " + imie+"! it's file generated for you "
    subject = "Your image"
    body = "Subject: {}\n\n{}".format(subject,msg)

    server.sendmail(your_email, [email], body) 
    sleep(1)

server.close() 



