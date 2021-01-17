import requests

url = 'https://fertilizerprediction.herokuapp.com/api'

r = requests.post(url,json={'V1':27, 'V2':55, 'V3':54, 'V4':1, 'V5':6, 'V6':12, 'V7':4, 'V8':4,})

print(r.json())
ctdict = {1:'Barley', 2:'Cotton', 3:'Groundnuts', 4:'Maize', 5:'Millets', 6:'Oil Seeds', 7:'Paddy', 8:'Pulses', 9:'Sugarcane', 10:'Tobacco', 11:'Wheat'}
stdict = {1:'Black', 2:'Clayey', 3:'Loamy', 4:'Red', 5:'Sandy'}
ferdict = {1:'DAP', 2:'14-35-14', 3:'17-17-17', 4:'10-26-26', 5:'28-28', 6:'20-20', 7:'Urea'}
#print('Fertilizer Required : ',ferdict[int(r.json())])
