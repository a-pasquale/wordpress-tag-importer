import json
from subprocess import call

ids = []
with open('post_ids.json') as f:
  for line in f:
    ids.append(json.loads(line))
 
with open('items.jl') as f:
  for line in f:
    post = (json.loads(line))
    for item in ids[0]:
       # Replace unicode non-breaking spaces with ascii chars.
       if item["post_title"] == post["title"][0].replace(u"\u00a0", " "):
         call(["/usr/bin/php", "/home/ec2-user/wp-cli.phar", "--path=/var/www/northstar/wordpress", "post", "update", str(item["ID"]), "--tags_input=" + post["tags"]])
