# Python
repo for projects while learning python.

Coding Challenge:

The goal here is to replicate this top-50 webpage: https://www.spaceweatherlive.com/en/auroral-activity/top-50-geomagnetic-storms (just the main table, no need to replicate the HTML around it). The raw data for this is available at Kp Index Archive at Helmhotz Centre: http://www.gfz-potsdam.de/en/section/earths-magnetic-field/data-products-services/kp-index/archive/, specifically at: ftp://ftp.gfz-potsdam.de/pub/home/obs/kp-ap/tab/. The entire directory has been copied to avoid hitting the domain again and again, and is available under: gfz-data. 
Write a Python program to read the files and create the table.
One of the things to figure out is the format of the files in here (the `.tab` files), and how to parse them. This may require a little bit of background reading, but you don't need to know a lot to understand the mapping between the data in those files and the rows in the top-50 list above -- the mapping is pretty straightforward.
