#Movies
# Ethan Liberty
# Feb 15 2022

#MovieName = input('Input Movie Name: ')
#MovieLength = input('Input Movie Length: ')
#MovieYear = input('Input Year Of Movie')
#MovieDirector = input('Input Director Of The Movie: ')
#MovieCompanies = input('Input Production Companies')
#MovieDescription = input('Input Movie Description')

movie = {
    "Name": "",
    "Length": 0,
    "Year": 0,
    "Director": "",
    "Production Companies": "",
    "Description": "",
    "Where To Watch": "",
    "Cast": "",
    "Rating": "",
}

movie["Name"] = input('Input Movie Name: ')
movie["Length"] = input('Input Movie Length: ')
movie["Year"] = input('Input Movie Year: ')
movie["Director"] = input('Input Movie Director: ')
movie["Production Companies"] = input('Input Movie Production Companies: ')
movie["Description"] = input('Input Movie Description: ')
movie["Where To Watch"] = input('Input Where to Watch Movie: ')
movie["Cast"] = input('Input Movie Cast: ')
movie["Rating"] = input('Input Movie Rating: ')

print(movie)
