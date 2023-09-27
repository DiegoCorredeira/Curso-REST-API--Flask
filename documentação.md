# Documentação REST API Arctic Monkeys Songs


Este documento explica com exemplos como utilizar recursos disponiveis no REST API de Músicas do Arctic Monkeys. Assim como , as formas de se realizar uma requisição e suas possiveis respostas.


# 1. Consultar Músicas / Albuns

#### Requisição

Requisição para listar todos as músicas do sistema, podendo opcionalmente receber filtros personalizados via path, de forma que se o cliente não definir nenhum parâmetro de consulta (nenhum filtro), os parâmetros receberão os valores padrão.

⦁	Possíveis parâmetros de consulta. Padrão: Null.
⦁	title ⇒ Filtra músicas pelo nome. Padrão: Null.
⦁	artist ⇒ Filtra músicas pelo nome dos artistas envolvidos. Padrão: Null.
⦁	album ⇒ Filtra músicas pelo album. Padrão: Null.
⦁	released_date ⇒ Filtra músicas pela data de lançamento. Padrão: Null.
⦁	time ⇒ Filtra músicas pelo tempo de duração. Padrão: Null.

| Method        | URL                          |
| ------------- | ---------------------------- |
| **GET** | /all?release_date=2009-08-19 |

#### Resposta

Como resposta, obtemos uma lista com as músicas que se enquadram nos filtros de requisição acima.

| Status  |
| ------- |
| 200, OK |

#### Response Body: 

```
"humbug_songs": {
        "All Humbug Songs": {
            "Humbug Songs": [
                {
                    "id": 1,
                    "title": "My Propeller",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "3:27"
                },
                {
                    "id": 2,
                    "title": "Crying Lightning",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "3:43"
                },
                {
                    "id": 3,
                    "title": "Dangerouss Animals",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "3:30"
                },
                {
                    "id": 4,
                    "title": "Secret Door",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "3:43"
                },
                {
                    "id": 5,
                    "title": "Potion Approaching",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "3:32"
                },
                {
                    "id": 6,
                    "title": "Fire and the Thud",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "3:57"
                },
                {
                    "id": 7,
                    "title": "Cornerstone",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "3:17"
                },
                {
                    "id": 8,
                    "title": "Dance Little Liar",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "4:43"
                },
                {
                    "id": 9,
                    "title": "Pretty Visitors",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "3:40"
                },
                {
                    "id": 10,
                    "title": "The Jeweller's Hands",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "5:43"
                }
            ]
        }
    },
```



### Requisição

Requisição para visualizar os dados de um album especifico (GET)

/all

/suckitandsee

/WPSIATWIN

/FWN

/humbug


### Resposta

Resposta: 200, OK

### Response Body

```
"Suck It And See Songs": [
        {
            "id": 1,
            "title": "She's Thunderstorms",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "3:55"
        },
        {
            "id": 2,
            "title": "Black Treacle",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "3:35"
        },
        {
            "id": 3,
            "title": "Brick by Brick",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "2:59"
        },
        {
            "id": 4,
            "title": "The Hellcat Spangled Shalalala",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "3:00"
        },
        {
            "id": 5,
            "title": "Don't Sit Down 'Cause I've Moved Your Chair",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "3:04"
        },
        {
            "id": 6,
            "title": "Library Pictures",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "2:22"
        },
        {
            "id": 7,
            "title": "All My Own Stunts",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "3:52"
        },
        {
            "id": 8,
            "title": "Reckless Serenade",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "2:43"
        },
        {
            "id": 9,
            "title": "Piledriver Waltz",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "3:24"
        },
        {
            "id": 10,
            "title": "Love Is a Laserquest",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "3:12"
        },
        {
            "id": 11,
            "title": "Suck It and See",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "3:46"
        },
        {
            "id": 12,
            "title": "That's Where You're Wrong",
            "artist": "Arctic Monkeys",
            "album": "Suck It And See",
            "release_date": "2011-06-07",
            "time": "4:17"
        }
    ]
}
```


### Requisição

| Method | URL                          |
| ------ | ---------------------------- |
| GET    | /suckitandsee/id_inexistente |

### Resposta

| Status         | Response Body                          |
| -------------- | -------------------------------------- |
| 404, not found | {<br />   "message": "null" <br />} |
