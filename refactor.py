import requests

url = "https://countries.trevorblades.com"

json = {'query': '''
{
  country(code: "UZ") {
    name
    native
    emoji
    currency
    languages {
      code
      name
    }
    phone
    awsRegion
  }
}
'''}

r = requests.post(url, json=json)
print(r.json())