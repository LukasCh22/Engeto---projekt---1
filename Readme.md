# Engeto projekt č.1 (Textový analyzátor)

První projekt na Python Akademii od Engeta. 

## Popis projektu
Program nejdříve ověří, jestli je uživatel zaregistrovaný, pokud ano, pozdraví jej a umožní mu analyzovat texty.
Pokud uživatel registrovaný není, upozorní jej na to a program se ukončí.

Dále program nechá vybrat uživatele mezi třemi texty k analýze a spočítá násladující statistiky:

1. počet slov,
2. počet slov začínajících velkým písmenem
3. počet slov psaných velkými písmeny
4. počet slov psaných malými písmeny,
5. počet čísel (ne cifer),
6. sumu všech čísel (ne cifer) v textu.

Nakonec program tato data zobrazí v jednoduchém sloupcovém grafu.

### Ukázka programu
```
username: bob
password: 123
----------------------------------------
Welcome to the app Bob!
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 2
----------------------------------------
There are 62 words in the selected text.
There are 10 titlecase words.
There are 0 uppercase words.
There are 51 lowercase words.
There are 1 numeric strings.
The sum of all the numbers 300
----------------------------------------
LEN|    OCCURENCES    |NR.
----------------------------------------
 2 |*******           |  7
 3 |***************** | 17
 4 |*********         |  9
 5 |**********        | 10
 6 |*******           |  7
 7 |***               |  3
 8 |**                |  2
 9 |*****             |  5
10 |*                 |  1
13 |*                 |  1
```