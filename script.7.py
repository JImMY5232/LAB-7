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

    movie_1 = {'title':'Harry Potter','genre':'fantasy'}
    movie_2 = {'title':'John Wick','genre':'action'}
    personal_information['movie'].append(movie_1,movie_2)

    toppings ={ 'cheese' ,'Mushrooms','pepperoni'}
    pizza_toppings(personal_information , toppings)

def print_1(personal_information):
    sentence ='hi joe, my name is ', personal_information['name'] , 'and my student ID is' ,personal_information['student_id'],'.'
    print(sentence)