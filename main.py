from worker.driver import 


def check_aggrement(aggrements: list):
    for aggrement in aggrements:
        pass


def lambda_handler(event, context):
    user_id       = event["id"]
    user_password = event["password"]
    aggrements    = event["aggrement"]


