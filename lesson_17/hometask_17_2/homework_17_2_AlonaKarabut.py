import requests
import urllib.request

print('\nGET:')
with open('TEST.jpg', 'rb') as file:
    files = {'image': file}
    response = requests.post('http://127.0.0.1:8080/upload', files=files)

print(response.status_code, '\n', response.text)

print('GET:')
response = requests.get(
    'http://127.0.0.1:8080/image/TEST.jpg',
    headers={'Content-Type': 'image'}
)


with open('downloaded_TEST.jpg', 'wb') as f:
    f.write(response.content)
print(response.status_code, '\n', 'Зображення завантажено як downloaded_TEST.jpg')


print('\nDELETE:')
response = requests.delete('http://127.0.0.1:8080/delete/TEST.jpg')
print(response.status_code, '\n', response.text)