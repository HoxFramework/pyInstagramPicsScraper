import json
import requests
import random
import string
def profiler(link):
    #takes in a link,  gets .json data and downloads HD posts.
    json_key = requests.get(link)
    json_key = json_key.text
    json_loaded = json.loads(json_key)
    
    data = json_loaded['graphql']['user']['edge_owner_to_timeline_media']['edges']

    #edge owner to timeline media
    for k in range(0,len(data)):
        randomname = random.choice(string.ascii_uppercase + string.digits)
        randomname = randomname + str(random.choice(string.ascii_uppercase + string.digits))
        randomname = randomname + str(random.choice(string.ascii_uppercase + string.digits))
        #print(randomname)
        #print(k)
        myhdpic = data[k]['node']['display_url']
        #print(myhdpic)
        #print("____________")
        #print(myhdpic)
        if "p1080x1080" in myhdpic:
            picrequest = requests.get(myhdpic)
            picrequest = picrequest.content
            
            with open('./images/hd/{}.jpg'.format(randomname), 'wb') as hdpic:
                hdpic.write(picrequest)
            print("[+] Pic saved :",myhdpic)
        elif "s1080x1080" in myhdpic:
            picrequest = requests.get(myhdpic)
            picrequest = picrequest.content
            with open('./images/hd/{}.jpg'.format(randomname), 'wb') as hdpic:
                hdpic.write(picrequest)
            print("[+] Pic saved :",myhdpic)

                
                
        else:
            try:
                picrequest = requests.get(myhdpic)
                picrequest = picrequest.content
                with open('./images/hd/{}.jpg'.format(randomname),'wb') as hdpic:
                    hdpic.write(picrequest)
                print("[+] Pic saved :",myhdpic)
            except:
                #
                print("[-] Could not get : ",myhdpic)
            #print("NOT DOWNLOADING")
            #pass
