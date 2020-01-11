import os
import urllib.request

data_dir = r'C:\Users\Blu\projects\udemy'
pages = [

    {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
    {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},

]

for page in pages:

    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)

        print("Transform {}  => {} ", format(page["url"], file_name))
        urllib.request.urlretrieve(page["url"], path)

    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break

else:
    print('All pages downloaded successfully!!!')
