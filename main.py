# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json
import os
import yaml
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
   # url = "https://pub-sub-consumer.eu-gb.mybluemix.net/api/consumer"
   # response = requests.get(url)
   # json_data = response.json()

    #print(json_data)
    #with open('data.json', 'w') as f:
    #    json.dump(json_data, f)
    with open('kubernetes.json') as f:
        root = json.load(f)
    for r in root['resources']:
        servicelistroot=json.loads(json.dumps(r))
        print(servicelistroot)
        for s in servicelistroot['serviceList']:
            print(s['name'])
#            with open(r'test.yaml') as file:
#                documents = yaml.full_load(file)
#                for item, doc in documents.items():
#                    print(item, ":", doc)
            dict_file = {'version': '1.0.0',
                         'title': 'What happens if we terminate a Pod?',
                         'description': 'If a Pod is terminated, a new one should be created in its places',
                         'tags': ['k8s', 'pod'],
                         'method': [{'type': 'action', 'name': 'terminate-pod',
                                     'provider': {'type': 'python', 'module': 'chaosk8s.pod.actions',
                                                  'func': 'terminate_pods',
                                                  'arguments': {'label_selector': 'app='+s['name'], 'rand': True,
                                                                'ns': 'default'}}}]

                         #print(data['resources'])
                     }
            with open(r'probe-for-' + s['name'] + '.yaml', 'w') as file:
                documents = yaml.dump(dict_file, file)
            #uncomment this in production
            #os.system('chaos run '+'probe-for-' + s['name'] + '.yaml')
    os.system('chaos run probe-for-payment.yaml')
    os.system('chaos run probe-for-productpage.yaml')
    os.system('chaos run probe-for-ratings.yaml')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
