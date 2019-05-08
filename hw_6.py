import urllib.request
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
token = '7763de25972f52e2445caffbe4d29fda5e9c0723d619c4fa302e40f3f10d8e1dc6be940d980cf18cbcac9'
owner_id = 69511861
owner_unstripped = ':69511861,'
schetchik = 0
counter = 0
def comments_words(whichpost):
    print(whichpost)
    req = urllib.request.Request('https://api.vk.com/method/wall.getComments?owner_id={}&post_id={}&offset={}&v=5.92&access_token={}'.format(owner_id, whichpost, counter, token)) 
    response = urllib.request.urlopen(req) 
    result = response.read().decode('utf-8')

    comments = []
    m = result.split('"')
    for x in range (len (m)):
        if m[x] == 'text':
            comments.append(m[x+2])

        if m[x] == 'response' and m[x+2] == "count" and m[x+3] == ':0,':
            print('no comments to post')
    wordsnum = 0
    numbers = []
    amounts = 0
    for comment in comments:
        wordsnum = len(comment.split())
        for x in range (1, len(comment)-1):
            if comment[x] == '\\' and comment[x+1] == 'n':
                wordsnum = wordsnum+1
        numbers.append(wordsnum)
    if len(numbers)!= 0:
        amounts = sum(numbers)/len(numbers)
        print(len(numbers))
    
    return (amounts)

def post_words():
    counter = 0
    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id={}&offset={}&count=5&v=5.92&access_token={}'.format(owner_id, schetchik, token)) 
    response = urllib.request.urlopen(req) 
    result = response.read().decode('utf-8')
    m = result.split('"')
    postids = []
    for y in range (len(m)):
        if m[y] == 'id' and m[y+2] == 'from_id':
            whichpost = int(m[y+1].split(",")[0].split(":")[1])
            postids.append(whichpost)
    posts = []
    for x in range (len (m)):
        if m[x] == 'post' and m[x+2] == 'text' and m[x+4] != '' and m[x-7] == owner_unstripped:
             posts.append(m[x+4])
    wordsnum = 0
    whichpost = ""
    z = 0
    for post in posts:
        wordsnum = len(post.split())
        for x in range (1, len(post)-1):
            if post[x] == '\\' and post[x+1] == 'n':
                wordsnum = wordsnum+1
        amounts = comments_words(postids[z])
        z = z+1
        
        if amounts != 0:
            ratio = wordsnum/amounts
            print(wordsnum, 'words with average length of comments:', amounts, ', ratio:', ratio)

        else:
            print(wordsnum, 'words with no comments')
        scatter1 = plt.scatter(wordsnum, amounts)
    return (ratio)

def extra_infos():
    request = 'https://api.vk.com/method/users.get?user_ids={}&fields=sex,city,home_town,bdate&v=5.92&access_token={}'.format(owner_id, token)
    req = urllib.request.Request(request)
    response = urllib.request.urlopen(req) 
    result = response.read().decode('utf-8')
    m = result.split('"')
    print(m)
    return m
    
post_words()
schetchik=schetchik+100
ratio = post_words()
m = extra_infos()

plt.show()
