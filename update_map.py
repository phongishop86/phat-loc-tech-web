import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the iframe src with the new query-based one
old_src = 'src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.066465365518!2d106.63665791480112!3d10.806222892301142!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752b1e3271221b%3A0x7d0231d6833130d!2zNDkxLzEgVHLGsOG7nW5nIENoaW5oLCBQaMaw4budbmcgMTQsIFTDom4gQsOsbmgsIEjhu5MgQ2jDrSBNaW5oLCBWaWV0bmFt!5e0!3m2!1sen!2s!4v1700000000000!5m2!1sen!2s"'
new_src = 'src="https://maps.google.com/maps?q=491/1%20Tr%C6%B0%E1%BB%9Dng%20Chinh,%20Ph%C6%B0%E1%BB%9Dng%2014,%20T%C3%A2n%20B%C3%ACnh,%20H%E1%BB%93%20Ch%C3%AD%20Minh,%20Vi%E1%BB%87t%20Nam&t=&z=17&ie=UTF8&iwloc=&output=embed"'

if old_src in content:
    content = content.replace(old_src, new_src)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Successfully updated map iframe')
else:
    print('Failed to find old src')
