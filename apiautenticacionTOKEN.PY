import requests

#desp de q me registro pag git me redirijiria aca y me daria ambos codigos
#code me lo da en la url http... code=.....
client_id='' #me lo dio github cuando me registre app
client_secret=''
code=''
#asi obtendre mi access token
if __name__=='main':

    url='https://github.com/login/oauth/access_token'
    payload={'client_id': client_id, 'client_secret': client_secret, 'code': code}
    headers={'Accept': 'application/json'}

    response=requests.post(url,json=payload,headers=headers)

    if response.status_code==200:
        response_json=response.json
        access_token=response_json['access_token'] #obtengo mi access token para luego usarlo
        print(access_token)
