
from bs4 import BeautifulSoup
from PIL import Image
import requests
from pathlib import Path
import re

platform_id_dict = {
    "all":0,
    "pc":1,
    "3ds":4912,
    "n64": 3,
    "ds": 8,
    "nes": 7,
    "game boy": 4,
    "game boy color":41,
    "game boy advance": 5,
    "game cube": 2,
    "switch": 4971,
    "wii": 9,
    "wii u":38,
    "playstation":10,
    "playstation 2": 11,
    "playstation 3": 12,
    "playstation 4": 4919,
    "playstation 5": 4980,
    "snes": 6,
    "xbox": 14,
    "xbox 360": 15,
    "xbox one": 4920,
    "xbox series x": 4981,
    
    }


path = Path(__file__).parent.parent
cover_art_dir = path / "data" / "cover_art"

platform = "xbox series x"
game_name = "pentiment"

platform_id = platform_id_dict[platform]
platform_url_part = f"platform_id%5B%5D={platform_id}"
name_url_part = f"name={game_name}"
search_url = f"https://thegamesdb.net/search.php?{platform_url_part}&{name_url_part}"

search_result_page = requests.get(search_url)

parsed_html = BeautifulSoup(search_result_page.content, "html.parser")

parsing_array = parsed_html.find_all('img', src=re.compile(r'https://cdn.thegamesdb.net/images/thumb/boxart/'))
art_url = parsing_array[0]['src']

r = requests.get(art_url) # create HTTP response object 

cover_art_file_name = f"{game_name}.jpg"
cover_art_path = cover_art_dir / cover_art_file_name

# Open the image file and write the request data to it.
with open(cover_art_path,'wb') as f: 
    f.write(r.content)
    f.close()

img = Image.open(cover_art_path)
img.save(cover_art_path, "jpeg", optimize=True)



"""
if __name__ == "__main__":
    
    def main():
        
        
    main
"""