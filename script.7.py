


def main():
    personal_information = {
        'name':'Jimmy' ,
        'student_id':'10265232',
        'pizza_toppings': [
            'cheese' ,
            'Mushrooms',
            'pepperoni'
        ],
        'movies' : [
            {'title':'Harry Potter',
             'genre':'fantasy'
            },
            { 'title':'John Wick',
              'genre':'action'
            }
        ]
    }

    movie_more = {'title':'Free Guy','genre':'comedy'}
    personal_information['movies'].append(movie_more)

    pizza_topping =  'sausage' ,'green pepper',
    personal_information['pizza_toppings'].append(pizza_topping)

    print_1(personal_information)
    print_2(personal_information)
    print_3(personal_information)
    print_4(personal_information)

def print_1(personal_information):
    
    sentence1  = 'Hi Joe, my name is '
    sentence1 += personal_information['name']
    sentence1 += ' and my student ID is '
    sentence1 += personal_information['student_id']
    sentence1 += '.'
    
    print(sentence1)

def print_2(personal_information):
    
    sentence2 = 'My ideal pizza has '

    for i,p in enumerate(personal_information['pizza_toppings']):
        sentence2 += str(p)
        if i < len (personal_information['pizza_toppings'])-1:
            sentence2 += ','
    sentence2 += '.'
    print(sentence2)

def print_3(personal_information):
    sentence3 = 'I like to watch '

    for i,p in enumerate(personal_information['movies']):
        sentence3 += p['genre']
        if i < len (personal_information['movies'])-1:
            sentence3 += ','
    
    sentence3 += ' movies.'
    
    print(sentence3)

def print_4(personal_information):

    sentence4 = 'Some of my favourites are '
    for i,p in enumerate(personal_information['movies']):
        sentence4 += p['title']
        if i < len (personal_information['movies'])-1:
            sentence4 += ','
    
    sentence4 += '!'

    print(sentence4)


main()
