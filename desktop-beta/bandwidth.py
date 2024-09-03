url = "https://fast.com//"
page = requests.get(url)
time.sleep(2)
soup = BeautifulSoup(page.content, "lxml")
speed = soup.find(id="speed-value").text
print("Your speed is", speed, ".")
if (speed <= 40):
    print("Your speed is too slow by ", speed - 40, ".")
else:
  print ("Your speed is good.")
return speed