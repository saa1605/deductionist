import praw,requests,re


r = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    password="PASSWORD",
    user_agent="USERAGENT",
    username="USERNAME",
)
subreddit = r.get_subreddit('EarthPorn')
posts = subreddit.get_top_from_day(limit=1)
for post in posts:
    url = (post.url)
    file_name = url.split("/")
    if len(file_name) == 0:
        file_name = re.findall("/(.*?)", url)
    file_name = file_name[-1]
    if "." not in file_name:
        file_name += ".jpg"
    print(file_name)
r = requests.get(url)
with open(file_name,"wb") as f:
    f.write(r.content)