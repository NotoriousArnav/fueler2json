from selectorlib import Extractor
from email_decode import *
import requests

def extract_profile(fueler_username):
    e = Extractor.from_yaml_file('profile.yml')
    r = requests.get(f'https://fueler.io/{fueler_username}')
    projects = requests.get(f'https://fueler.io/api/{fueler_username}/get-user-work')
    data = e.extract(r.text)
    links = data.get('links')
    email = [f"mailto:{cfDecodeEmail(x.split('#')[1]).split('?')[0]}" for x in links if '/cdn-cgi/' in x]
    not_email = [x for x in links if '/cdn-cgi/' not in x]
    links = []
    links.extend(email)
    links.extend(not_email)
    data['links'] = links
    data['projects'] = projects.json()
    return data

def extract_project(username, project_slugname):
    e = Extractor.from_yaml_file('project.yml')
    r = requests.get(f'https://fueler.io/{username}/{project_slugname}')
    data = e.extract(r.text)
    return data
