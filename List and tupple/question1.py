# WAP to ask the uset to enter names of their # favorite movies and store them in a list. Then print out the movies in the list in reverse order.

allmovies = []

for i in range(5):
    movie = input("Enter the name of your favorite movie: ")
    allmovies.append(movie)

print(allmovies[::-1])

allmovies.sort(reverse= True)

print(allmovies)