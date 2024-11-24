from enum import Enum

class GovernmentType(Enum):
    #types of government
    DEMOCRACY = 'Democracy'
    REPUBLIC = 'Republic'
    AUTOCRACY = 'Autocracy'
    MONARCHY = 'Monarchy'

class Country:
    def __init__(self, name: str, capital: str, code: str, population: int, area: float, gdp: int, government: GovernmentType):
        #just starting init method
        self.name = name
        self.capital = capital
        self.code = code
        self.population = population
        self.area = area
        self.gdp = gdp
        self.government = government

    def population_density(self) -> float:
        #calculating population density
        return self.population / self.area

    def __repr__(self):
        #method of showing the information
        return (f"Country(name={self.name}, capital={self.capital}, code={self.code}, "
                f"population={self.population}, area={self.area}, gdp={self.gdp}, "
                f"government={self.government.name})")

class Land:
    def __init__(self, name: str):
        #another init method
        self.name = name
        self.countries = []

    def add_country(self, country: Country):
        #adding country on continent
        self.countries.append(country)

    def sort_countries_by_gdp(self):
        #sorting by gdp without using sort(
        for i in range(len(self.countries)):
            for j in range(i + 1, len(self.countries)):
                if self.countries[i].gdp < self.countries[j].gdp:
                    self.countries[i], self.countries[j] = self.countries[j], self.countries[i]

    def choose_country_by_government(self, gov_type: GovernmentType):
        #finding countries with our gov type
        selected_countries = []
        for country in self.countries:
            if country.government == gov_type:
                selected_countries.append(country)
        return selected_countries

    def top_countries_by_gdp(self, top_n: int):
        #best countries by gdp 
        self.sort_countries_by_gdp()
        return self.countries[:top_n]

    def choose_country_by_population_and_government(self, min_population: int, max_population: int, gov_type: GovernmentType):
        #chosing our countries on gap including our gov_type
        selected_countries = []
        for country in self.countries:
            if min_population <= country.population <= max_population and country.government == gov_type:
                selected_countries.append(country)
        return selected_countries

    def calculate_population_density(self) -> float:
        #calculating avarage densic=ty on Land
        total_population = 0
        total_area = 0
        for country in self.countries:
            total_population += country.population
            total_area += country.area
        if total_area > 0:
            return total_population / total_area
        return 0
    
class Movies:
    def __init__(self):
        self.movies_list = []

    def add_movie(self, title, release_date, countries):
        self.movies_list.append((title, release_date, countries))

    def sort_movies_by_release_date(self):
        n = len(self.movies_list)
        for i in range(n):
            for j in range(1 + i, n):
                if self.movies_list[i][1] > self.movies_list[j][1]:
                    self.movies_list[i],self.movies_list[j] = self.movies_list[j], self.movies_list[i]

    def get_movies_by_country(self, country):
        return [movie for movie in self.movies_list if country in movie[2]]


    def __repr__(self):
            return "\n".join(f"{title} ({release_date[0]}-{release_date[1]:02d}-{release_date[2]:02d}), countries: {', '.join(countries)}"
                         for title, release_date, countries in self.movies_list)
    
usa = Country("USA", "Washington, D.C.", "US", 331000000, 9833517, 21433225, GovernmentType.REPUBLIC)
canada = Country("Canada", "Ottawa", "CA", 37590000, 9984670, 18003000, GovernmentType.REPUBLIC)
china = Country("China", "Beijing", "CN", 1393409038, 9596961, 22700000, GovernmentType.AUTOCRACY)
india = Country("India", "New Delhi", "IN", 1380004385, 3287263, 3200000, GovernmentType.DEMOCRACY)

north_america = Land("North America")
north_america.add_country(usa)
north_america.add_country(canada)

asia = Land("Asia")
asia.add_country(china)
asia.add_country(india)

print("Average population density in Asia:", asia.calculate_population_density())

north_america.sort_countries_by_gdp()
print("Countries in North America sorted by GDP:", north_america.countries)

top_asian_countries = asia.top_countries_by_gdp(3)
print("Top 3 countries by GDP in Asia:", top_asian_countries)

democracies = asia.choose_country_by_population_and_government(min_population=1000000000, max_population=1500000000, gov_type=GovernmentType.DEMOCRACY)
print("Democracies with population between 1B and 1.5B:", democracies)

movies = Movies()
movies.add_movie("Inception", (2010, 7, 16), ["usa", "canada"])
movies.add_movie("The Matrix", (1999, 9, 31), ["china", "usa"])
movies.add_movie("Avatar", (2009, 12, 18), ["india"])

print("all sorted movies")
movies.sort_movies_by_release_date()
print(movies)

print("\n""movies from usa")
usa_movies = movies.get_movies_by_country("usa")
for movie in usa_movies:
    print(f"{movie[0]},({movie[1][0]},{movie[1][1]},{movie[1][2]}),")
