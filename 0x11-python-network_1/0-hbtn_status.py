#!/usr/bin/python3

"""
A Phython script that
  - fetches https://alx-intranet.hbtn.io/status.
  - must uses urlib package
  - must use a with statement
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
