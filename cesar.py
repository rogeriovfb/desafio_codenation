
import requests, json, hashlib
url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=17597f8135080613ca38102063f6b1e6a3b418a1'

data = requests.get(url)
json_data = json.loads(data.text)
decif = ''

for i in json_data['cifrado']:
# No nosso caso os números e pontos serão mantidos, ou seja:
    if i == " " or i == "." or i=="-" or i==',':
        decif = decif+i
        continue

    valor = ord(i)-int(json_data['numero_casas'])

    if valor < 97:
        valor += 26
    decif = decif + chr(valor)


json_data['decifrado'] = decif
json_data['resumo_criptografico'] = hashlib.sha1(decif.encode('utf-8')).hexdigest()

with open('answer.json', 'w') as outfile:
    json.dump(json_data, outfile)

r = requests.post(
    'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=17597f8135080613ca38102063f6b1e6a3b418a1',
    files={'answer': open('answer.json', 'rb')}
)
print(r.content)
