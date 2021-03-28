import json
import requests

file_path = 'SGAD-Prodasdf'
root_url = 'https://ggg43721.sprint.dynatracelabs.com/'
token = ''

header = {
    "Authorization": "Api-token " + token,
    "Content-Type": "application/json"
}


def parse_dashboard(path):
    # parses dashboard from file to json
    path = path.replace('\n', '')
    dashboard_file = open(path, 'r')
    dashboard_json = json.load(dashboard_file)
    #print(dashboard_json)

    dashboard_json.pop('metadata', None)
    dashboard_json.pop('id', None)
    dashboard_json['dashboardMetadata']['owner'] = 'mark.bley@dynatrace.com'
    return dashboard_json


def validate_dashboard(dasboard):
    url = root_url + 'api/config/v1/dashboards/validator'
    payload = json.dumps(dasboard)
    res = requests.post(url, data=payload, headers=header)

    if res.status_code > 204:
        print(res.text)
        exit(-1)
    #print('valid dashboard')

# psuhes dashboard to tentant
def push_dashboard(dashboard):
    dashboard = parse_dashboard(dashboard)
    #rint(json.dumps(dashboard))
    #exit(-1)
    validate_dashboard(dashboard)
    url = root_url + 'api/config/v1/dashboards'
    payload = json.dumps(dashboard)
    res = requests.post(url, data=payload, headers=header)

    #print(res.status_code)
    if res.status_code > 204:
        print(res.text)
        exit(-1)

    res_json = json.loads(res.text)
    print('https://ggg43721.sprint.dynatracelabs.com/#dashboard;gtf=-2h;gf=all;id=' + res_json['id'])

def get_dashboards():
    url = root_url + 'api/config/v1/dashboards'
    res = requests.get(url, headers=header)

    if res.status_code > 201:
        print(res.text)
        exit(-1)

    print(res.text)


def delete_dashboard(id):
    url = root_url + 'api/config/v1/dashboards/' + id
    res = requests.delete(url, headers=header)

    if res.status_code != 204:
        print(res.text)
        print('cloud not delete: ' + id)
        exit(-1)


def main():
    #dashboard_list = open('dashboard-list.txt', 'r')
    dashboard_list = ['./Memory Utilization.json']
    for d in dashboard_list:
        #dj = parse_dashboard(d)
        push_dashboard(d)
        #break

    #get_dashboards()


    print('Done')


def multi_delete():
    delete = ['ee4eceb6-7d72-4b01-b997-cbed722b4e06']
    for d in delete:
        delete_dashboard(d)


#multi_delete()
main()
