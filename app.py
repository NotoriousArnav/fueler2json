from scraper import *
import argparse
import datetime
import json

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', type=str, help='The Username of the Fueler User', default='arnav2004')
parser.add_argument('-o', '--output', type=str, help='Output JSON file name', default=str(datetime.datetime.now())+'fuler.io.json')
parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')

args = parser.parse_args()

print(args)

p = extract_profile(args.username)
profile = {'profile':p, 'projects':[]}
for x in p['projects']['project']:
    profile['projects'].append(extract_project(args.username, x['slug']))

with open(args.output, 'wt') as out:
    json.dump(profile, out)
