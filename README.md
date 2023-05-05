# fueler2JSON
**NOTE:No Riten Debnath or Fueler Employees were Harmed in making this REPO**
This repo is meant to scrape Fueler Profiles and Projects/Blogs into JSON/Python dict Format, afterall whynot?

Just use it as a Library. You are welcome

# Sample Usage
```
(Fueler2JSON) ➜  fueler2json git:(master) ✗ python3 app.py -h
usage: app.py [-h] [-u USERNAME] [-o OUTPUT] [-v]

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        The Username of the Fueler User
  -o OUTPUT, --output OUTPUT
                        Output JSON file name
  -v, --verbose         increase output verbosity
```

```python
extract_profile(username) # Username Required
extract_project(username, slugname) # Username and Slug name of Project Required
```
