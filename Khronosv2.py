import requests

## TODO: tor integration

api_endpoint = "https://api.github.com/users/"
api_repo = "https://api.github.com/repos/"

def main():
    username = input("Target username: ")
    webhook = input("Webhook URL (optional): ")

    if username:
        user_info = get_user_info(username)
        email_info = get_email_info(username)
        
        user_data = f"""
-------------------------------
[+] USER INFO
-------------------------------
            
Username: {user_info.get('login')}
Name: {user_info.get('name')}
URL: {user_info.get('html_url')}
Type: {user_info.get('type')}
User View Type: {user_info.get('user_view_type')}
Site Admin: {user_info.get('site_admin')}
Company: {user_info.get('company')}
Blog: {user_info.get('blog')}
Location: {user_info.get('location')}
Email: {user_info.get('email')}
Hireable: {user_info.get('hireable')}
Bio: {user_info.get('bio')}
Twitter Username: {user_info.get('twitter_username')}
Public Repos: {user_info.get('public_repos')}
Public Gists: {user_info.get('public_gists')}
Followers: {user_info.get('followers')}
Following: {user_info.get('following')}
Created At: {user_info.get('created_at')}
"""

        email_data = f"""
------------------------------- 
[+] EMAIL INFO
-------------------------------\n
"""

        for author in email_info:
            email_data += "+++++++++++++++++++++++++++++++\n"
            email_data += f"Author: {author}\n"
            for email in email_info[author]:
                email_data += f"Email: {email}\n"
            email_data += "+++++++++++++++++++++++++++++++\n\n"
        
        print(user_data)
        print(email_data)

        if webhook:
            send_webhook(webhook, user_data, email_data)

def send_webhook(webhook, user_info, email_info):
    ##  TODO: webhook message too long
    print("Sending user info...")
    data = { "content": f"```{user_info}```", "username":"Khronos" }
    requests.post(webhook, json=data)
    print("Sending email info...")
    data = { "content": f"```{email_info}```", "username":"Khronos" }
    requests.post(webhook, json=data)

def get_user_info(username):
    try:
        response = requests.get(f"{api_endpoint}{username}")
        response.raise_for_status()
        user_info = response.json()
        return user_info
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user info: {e}")

def get_email_info(username):
    user_and_emails = {}
    try:
        response = requests.get(f"{api_endpoint}{username}/repos")
        repos = response.json()
        for repo in repos:
            print(f"Repository: {str(repo['name'])}")
            repo_data = requests.get(f"{api_repo}{username}/{repo['name']}/commits")
            for commit in repo_data.json():
                author = str(commit["commit"]["author"]["name"])
                email = str(commit["commit"]["author"]["email"])

                if author and email != "":
                    if author not in user_and_emails:
                        user_and_emails[str(author)] = [str(email)]
                    else: 
                        if email not in user_and_emails[str(author)]:
                            user_and_emails[str(author)].append(str(email))
        return user_and_emails

    except requests.exceptions.RequestException as e:
        print(f"Error fetching email info: {e}")

if __name__ == "__main__":
    main()
