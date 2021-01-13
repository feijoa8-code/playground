import pandas as pd
import matplotlib.pyplot as plt


def createPie(data: dict):
    saliences = [x*100 for x in data['salience']]
    wedges = plt.pie(
        saliences, labels=data['types'], shadow=True, autopct='%1.1f%%', startangle=90)
    plt.show()


def createTable(data: list):
    types = []
    salience = []
    entities = []
    count = []
    for x in data:
        types.append(x['type'])
        salience.append(x['salience'])
        entities.append(x['entities'])
        count.append(len(x['entities']))
    stemdf = pd.DataFrame({'type': types, 'salience': salience,
                           'entitiesCount': count, 'entities': entities})
    print(stemdf)
    return {"salience": salience, "types": types}
