import json


def load_medical_knowledge(path):

    with open(path,"r",encoding="utf-8") as f:
        data=json.load(f)

    texts=[]

    for item in data:

        text=f"""
Condition: {item['condition']}

Symptoms: {', '.join(item['symptoms'])}

First Aid Steps:
{' '.join(item['first_aid'])}

Source: {item['source']}
"""

        texts.append(text)

    return texts
