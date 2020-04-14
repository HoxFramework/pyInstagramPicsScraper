
import json
import requests
import random
import string
import UpgradedLoader

profile_picked = str(input("Enter the profile URL:"))
if "/?hl=en" in profile_picked:
    profile_picked = profile_picked.replace("/?hl=en","")
    
profile_picked = profile_picked + "/?__a=1"
profile_picked = profile_picked.replace("//?","/?")

randoms = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'a','b','c','d','e','f','g','h','i','j','k']

key = requests.get(profile_picked)
json_key = json.loads(key.text)
data = json_key['graphql']['user']['edge_owner_to_timeline_media']['edges']
counter = 0

##

path = json_key['graphql']['user']
username = path['username']
bio = path['biography']
profile_pic_link = path['profile_pic_url_hd']
#print("[+] User :",username)
#print("[+] Bio :",bio)
#print("[+] Profile pic :",profile_pic_link)
print("\nSaving the profile...")
pic = requests.get(profile_pic_link)
pic = pic.content
with open('./images/profilepic.jpg','wb') as picture:
    picture.write(pic)

with open('./images/main.html','w',encoding="utf-8") as html_file:
    code = r"<h1 style='text-align:center;'>User data gathered.</h1><br /><img src='profilepic.jpg' style='margin-left:5%;'><br /> <h3 style='margin-left:2%;'>Username: {0}</h3><h3 style='margin-left:2%;'>Bio: {1}</h3><br /><h2 style='text-align:center;'>Images</h2><br />".format(username,bio)
    html_file.write(code)


##
        
for k in data:
    enviroment = data[counter]['node']['thumbnail_resources']
    counter += 1
    for r in enviroment:
        random_one = str(random.choice(randoms))
        random_two = str(random.choice(randoms))
        
        #print(r['src'])
        if "s150x150" in r['src']:
            pass
        elif "s240x240" in r['src']:
            pass
        elif "s320x320" in r['src']:
            pass
        #
        elif "s480x480" in r['src']:
            pass
        #so we are basically ignoring every low resolution and
        #downloading the rest. Honestly I hope 320x320 IS NOT the biggest
        #resolution, because noone uploads THAT low pic quality.
        #we have smartphones now.

        else:
            print("[+] Getting image:\n",r['src'])
            image_get = requests.get(r['src'])
            image_get = image_get.content
            image_final = './images/image-{0}{1}.jpg'.format(random_one,random_two)
            with open(image_final,'wb') as image_got:
                image_got.write(image_get)

            image_final_replaced = image_final.replace("./images/","")
            with open('./images/main.html','a',encoding="utf-8") as html_file_two:
                code_two = r"<br /><img src='{0}'><br />".format(image_final_replaced)
                html_file_two.write(code_two)
        

UpgradedLoader.profiler(profile_picked)
