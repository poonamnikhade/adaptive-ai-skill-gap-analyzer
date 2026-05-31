import requests
import json

base = 'http://127.0.0.1:5000'
session = requests.Session()

def print_res(name, r):
    print(f'--- {name} ---')
    print('Status:', r.status_code)
    try:
        print('JSON:', r.json())
    except Exception:
        txt = r.text.strip().replace('\n', ' ')[:200]
        print('Text:', txt)

# 1. Index page
r = session.get(base + '/')
print_res('Index', r)

# 2. Auth page
r = session.get(base + '/auth')
print_res('Auth', r)

# 3. Login POST
payload = {'email': 'test@example.com', 'name': 'Test User'}
r = session.post(base + '/login', data=payload, allow_redirects=False)
print_res('Login POST', r)
# Follow redirect if any
if r.status_code in (301, 302) and 'Location' in r.headers:
    r = session.get(base + r.headers['Location'])
    print_res('Redirected Dashboard', r)

# 4. Analysis GET (form)
r = session.get(base + '/analysis')
print_res('Analysis GET', r)

# 5. Analysis POST
payload = {'target_role': 'Data Scientist', 'current_skills': 'Python, SQL, Statistics'}
r = session.post(base + '/analysis', data=payload)
print_res('Analysis POST', r)

# 6. Quiz GET
r = session.get(base + '/quiz')
print_res('Quiz GET', r)

# 7. Submit quiz (dummy answers)
# Retrieve questions to know ids; for simplicity send empty or default answers
quiz_payload = {'answers': {}}
r = session.post(base + '/submit_quiz', json=quiz_payload)
print_res('Submit Quiz', r)

# 8. Roadmap GET
r = session.get(base + '/roadmap')
print_res('Roadmap GET', r)

# 9. History GET
r = session.get(base + '/history')
print_res('History GET', r)
