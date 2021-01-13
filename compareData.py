import requests
import visual
import json
import preProcessData

data = ["The vet was very good", " My cat did not like the vet, but my dog did", " I do not like vets, they are too expensive", "I love my vet", " I love my dog", " I like brown cats best", " I like brown dogs", " The cat jump through a window and injured itself", "I enjoyed the experience", " I would recommend my vet", " The vet was good, but I had to wait too long and my cat", " I have farm animals and the vet does not support them", " I like horses", " My cat is my best friend and I give him the best", "I valued the transaction", " I thought the service was over priced", " I do not think the vet likes cats", " My cat does not like vets", " I had to wait to long", " It was very expensive", " I was not told how much it would cost", "I have three cats and a rabbit and take them all to the same vet",
        " My cat was very sick and the vet was fantastic", "I wish the vet was quicker", " I had to wait to long and would not recommend this vet", "I wanted to by insurance for my pet, but they would not", " My dog misbehaved at the vet", " I adopted my dog from this vet", " I need a microchip scanned", " The vet was very sensitive to my needs at a challenging time", " The vet lost my cat and I was devastated", " I had a budgie, but it escaped at the vet", " The medicine was very expensive", " I need to take the cat back to the vet many times", " I liked the vet", " I miss my original vet", " I wish my doctor was as good as my vet", " Why is the vet more expensive than my doctor? I am happy with the treatment given by my vet", " My cat caught fleas at the vet", " She needed a vaccination"]

url = 'https://text-classification-engine-rest-dot-feijoa8-dev.ts.r.appspot.com/api/v1/text/classify/entity-sentiments'
header = {'Content-Type': 'application/json',
          'industryVertical': 'testing', 'Accept': 'application/json'}


requestBody = {"data": data}
response = requests.post(url, json=requestBody, headers=header)
response_dict = json.loads(response.text)

preProcesseddata = preProcessData.preprocessData(data)
requestBodyPreprocess = {"data": preProcesseddata}
responsePrepProcess = requests.post(
    url, headers=header, json=requestBodyPreprocess)
response_dict_preprocess = json.loads(responsePrepProcess.text)

print('Without data preprocessing')
value = visual.createTable(response_dict)
visual.createPie(value)

print('With data preprocessing')
preProcessedValue = visual.createTable(response_dict_preprocess)
visual.createPie(preProcessedValue)
