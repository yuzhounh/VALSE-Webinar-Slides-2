# Download slides from: http://valser.org/webinar/slide/. 
# 2020-7-15 22:13:13

import re
import os
import string
import urllib.request
from urllib.parse import quote

# open the url and read
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
def getHtml(url):
    url_new=quote(url,safe=string.printable)
    req=urllib.request.Request(url=url_new, headers=headers)
    page=urllib.request.urlopen(req)
    html = page.read().decode('UTF-8')
    page.close()
    return html

# example: /webinar/slide/index.php/Home/Index/index/dir/20200710.html
# compile the regular expressions and find the stuff we need
def getDate(html):
    reg = r'/webinar/slide/index.php/Home/Index/index/dir/(\d{8}).html'
    tmp = re.compile(reg).findall(html)
    return tmp

# example:  <a target="_blank"  href="http://valser.org/webinar/slide/slides/20200710/howtoproperlyreviewaipapers-200710022751.pdf">howtoproperlyreviewaipapers-200710022751.pdf</a>
def getName(html):
    reg = r'<a target="_blank"  href="http://valser.org/webinar/slide/slides/(.*)/(.*)">(.*)</a>'
    tmp = re.compile(reg, re.IGNORECASE).findall(html)
    return tmp

# download a file
def getFile(url, file):
    f = open(file, 'wb')
    url_new = quote(url, safe = string.printable)
    u = urllib.request.urlopen(url_new)
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()

# make a directory to store the slides
slides_dir = 'slides'
if not os.path.exists(slides_dir):
    os.mkdir(slides_dir)

# store information of the slides
slides_info = 'slides_info'
FileHandle = open(slides_info, 'w', encoding='UTF-8')
FileHandle.close()

# main page: http://valser.org/webinar/slide/
url = 'http://valser.org/webinar/slide/'
html = getHtml(url)
date_list = getDate(html)

# example: http://valser.org/webinar/slide/index.php/Home/Index/index/dir/20200710.html
for date in date_list:
    url="http://valser.org/webinar/slide/index.php/Home/Index/index/dir/{}.html".format(date)
    try:
        html=getHtml(url)
    except:
        # output the error
        print("{} error".format(date))
        FileHandle = open(slides_info, 'a', encoding='UTF-8')
        FileHandle.write("{} error\n".format(date))
        FileHandle.close()
        continue

    file_list=getName(html)

    # example: http://valser.org/webinar/slide/slides/20200710/howtoproperlyreviewaipapers-200710022751.pdf
    for file in file_list:
        file=file[1]
        url="http://valser.org/webinar/slide/slides/{}/{}".format(date, file.replace(' ','%20')) # replace blank spaces
        file="{} {}".format(date, file)

        # output the file information
        print(file)
        FileHandle = open(slides_info, 'a', encoding='UTF-8')
        FileHandle.write("{}\n".format(file))
        FileHandle.close()

        # download the file
        getFile(url, "{}/{}".format(slides_dir, file))