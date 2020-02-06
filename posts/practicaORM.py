from datetime import date

users = [
    {
        'email': '2fredy@platzi.com',
        'first_name': 'Fredy',
        'last_name': 'Vega',
        'password': '982784495',
    },
    {
        'email': '2yesica@platzi.com',
        'first_name': 'Yésica',
        'last_name': 'Cortés',
        'password': 'qwerty',
        'birthdate': date(1990, 12, 19)
    },
    {
        'email': '2arturo@platzi.com',
        'first_name': 'Arturo',
        'last_name': 'Martinez',
        'password': 'msicomputa',
        'is_admin': True,
        'birthdate': date(1982, 11, 6),
        'bio':'Lo interesante de la vida es un misterio, pues siempre buscamos lo que ya tenemos...',
    },
    {
        'email': '2yuri@gmail.com',
        'first_name': 'Yuri',
        'last_name': 'X',
        'password': '124153',
    }    
]

from post.models import User

for user in users:
    obj = User.objects.create(**user)
    print(obj.pk, ':', obj.email, ':',obj.first_name)