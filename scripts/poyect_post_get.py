import requests

url = "http://192.168.0.25:35000/"
url_projects = url + "projects"
res = requests.post(url_projects, json={
    "name": "Modulo de Proyectos - PSA",
    "client": "PSA",
    "start_date": "2023-01-01",
    "end_date": "2023-09-01",
    "project_leader": "Aguanti",
    "development_team": ["Tribu A"],
    "tasks": [{
        "id": "1",
        "state": "Ongoing",
        "name": "MVP",
        "start_date": "2023-01-02",
        "end_date_est": "2023-09-02",
        "hours_est": "900",
    }]
})
print(res.status_code)
print(res.content)
