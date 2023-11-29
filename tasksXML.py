'''To list all the child tags of the <movie> element using the iter() function and
print out the movie descriptions using the itertext() function, 
as well as finding the number of favorite and non-favorite movies'''

import xml.etree.ElementTree as ET

tree = ET.parse('movie.xml')
root = tree.getroot()

favorites_count = 0
non_favorites_count = 0

for movie in root.iter('movie'):
    # List all the child tags of the movie element
    print(f"Child tags of {movie.get('title')}:")
    for child in movie:
        print(child.tag)

    # Print out the movie descriptions using itertext()
    print(f"Movie Description for {movie.get('title')}:")
    description_text = ''.join(movie.find('description').itertext()).strip()
    print(description_text)

    favorite = movie.get('favorite')
    
    if favorite.lower() == "true":
        favorites_count += 1
    else:
        non_favorites_count += 1

print(f"Favorite movies = {favorites_count}, Non-favorite movies = {non_favorites_count}")

