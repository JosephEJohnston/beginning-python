# 从类似于 http://www.something.com 的 URL 中提取域名

url = input('Please enter the URL: ')
domain = url[11:-4]

print("Domain name: " + domain)
