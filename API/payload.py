from API.utilities.configurations import getQuery


def addpayload(user):
    user = {
        "name": user,
        "job": "leader"
    }
    return user

def buildpayload(query):
    add= {}
    tp = getQuery(query)
    add['name'] = tp[0]
    add['job'] = tp[1]
    return add