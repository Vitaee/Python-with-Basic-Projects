import urllib.request


url1 ="Enter URL of image"
url2 ="Enter URL of image"
url3 ="Enter URL of image"

urllst = [url1,url2,url3]

say =1

for url in urllst:
    urllib.request.urlretrieve(url,"İmage" + str(say) + ".jpg")
    say +=1
