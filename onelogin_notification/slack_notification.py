import requests
import os

headers = {"Authorization": f"Bearer {os.environ['SLACK_TOKEN']}"}


def get_user_id(email):
    """Get Slack user ID.

    :param email: Passed in during function call.
    :return: (dict)
    """
    url = "https://slack.com/api/users.lookupByEmail"
    querystring = {"email": email}
    response = requests.get(url, headers=headers, params=querystring)

    return response.json()["user"]["id"]


def send_user_msg(email, days_left):
    """Send user Slack direct message.

    :param email: Passed in during function call (needed to get Slack user ID)
    :param days_left: Onelogin password days left passed in during call
    """
    id = get_user_id(email)
    url = "https://slack.com/api/chat.postMessage"
    querystring = {
        "channel": id,
        "text": f"Your Onelogin password will be expiring in {days_left} days, please "
        "visit this link for more information: *link_here*",
    }

    requests.post(url, headers=headers, params=querystring)


def main():
    pass


if __name__ == "__main__":
    main()
