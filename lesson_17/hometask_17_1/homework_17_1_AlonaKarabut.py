import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)
data = response.json()

photos = data.get('photos', [])

for i, photo in enumerate(photos[:2], start=1):
    image_url = photo['img_src']
    image_data = requests.get(image_url).content
    with open(f'mars_photo{i}.jpg', 'wb') as file:
        file.write(image_data)
    print(f'Фото {i} збережено як mars_photo{i}.jpg')