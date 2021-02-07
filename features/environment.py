import requests

def after_scenario(context, scenario):
    if "library" in scenario.tags:

        delete_user = requests.delete("https://reqres.in/api/users", json={'id': context.user_id},
                        headers={"Content-Type": "application/json"}, )
        print(delete_user.status_code)
        assert delete_user.status_code == 204