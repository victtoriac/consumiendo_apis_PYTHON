import requests

client_id='' 
client_secret=''
code=''
access_token=''

if __name__=='main':
    url='https://api.github.com/user/repos' #endpoint al que realizo peticion para obtener repositorios
    payload={'name': 'git_api_cf_comunidad'}
    headers={'Accept': 'application/json', 'Authorization':'token' + access_token} 

    response=requests.post(url,headers=headers,json=payload)

    if response.status_code==200:
        print(response.json())
    else:
        print(response.content) #asi visualizo el error
        