import pyshorteners

link = input("Put down the link: ")
shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)


