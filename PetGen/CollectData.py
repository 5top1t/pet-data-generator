import urllib.request
import json
import requests
import math
import time
import random
from Pet import Pet


def download_image():
    resp = requests.get(url="https://dog.ceo/api/breeds/image/random").json()
    if resp['status'] == "success":
        url = resp['message']
        file_name = "images/" + url.split("/")[4] + ".jpg"
        print(url + "\t" + file_name)
        urllib.request.urlretrieve(url, file_name)
        return url.split("/")[4] + ".jpg"
    else:
        return "failure"


def name_generator(param):
    firstname = [line.rstrip('\n') for line in open('firstnames.txt')]
    lastname = [line.rstrip('\n') for line in open('lastnames.txt')]
    if param == "pet":
        return firstname[random.randint(0, 199)]
    elif param == "owner":
        return firstname[random.randint(0, 199)] + " " + lastname[random.randint(0, 199)]
    else:
        return ""


def date_generator(param):
    start = "1/1/2010 1:30 PM"
    end = "12/30/2017 4:50 AM"
    scheme = "%m/%d/%Y %I:%M %p"
    stime = time.mktime(time.strptime(start, scheme))

    etime = time.mktime(time.strptime(end, scheme))
    ptime = stime + random.random() * (etime - stime)
    age = math.ceil((ptime - stime) / (60 * 60 * 24 * 365))
    return age


def main():
    count = int(input("Enter the count of data desires: "))
    # How to delete file content
    f = open("petdb.txt", "a+")
    f.seek(0)
    f.truncate()
    for n in range(0, count, 1):
        name = name_generator("pet")
        owner = name_generator("owner")
        age = date_generator(0)
        image = download_image()
        breed = image.split(".")[0]

        new_pet = Pet(n, image, name, breed, age, owner)
        f.write(str(new_pet) + "\n")


if __name__ == '__main__':
    main()
