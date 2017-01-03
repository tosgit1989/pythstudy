#!/usr/bin/env python

import random
print("Content-Type: text/html; charset=utf-8")

no = random.randint(1, 6)
print("""
  <html>
  <head><title>Dice</title></head>
  <body>
    <h1>{num}</h1>
  </body>
  </html>
""".format(num=no))

