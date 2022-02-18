# by Kami Bigdely
# Extract class

class Person:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def send_hiring_email(self):
        print("email sent to: ", self.email)

    def get_full_name(self):
        print(self.first_name + " " + self.last_name)

    def get_movies_played(self):
        print('Movies Played: ', end='')
        for m in self.movies:
            print(m, end=', ')
        print()


first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']
    
for i, value in enumerate(emails):
    person = Person(first_names[i], last_names[i], birth_year[i], movies[i], value)
    if person.birth_year > 1985:
        person.get_full_name()
        person.get_movies_played()
        person.send_hiring_email()
