import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = '/home/makuss/inny dysk/projects/udemy'
tmpfile = 'downlad.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        print("usuwanie")
        os.remove(tmpfile_path)

    print("zapisywanie")
    save_url_to_file(url, tmpfile_path)

    print("kopiowanie")
    shutil.copy(tmpfile_path, file_path)

except requests.exceptions.ConnectionError:
    print("nie działa połczenie z {}".format(url))

except PermissionError:
    print("'nie działa zapisywanie do pliku {}".format(tmpfile_path))

except FileNotFoundError:
    print("nie ma pliku {}".format(file_path))

except Exception as e:
    print("nie działa {}".format(e))

else:
    print("zadzialalo")

finally:
    if os.path.exists(tmpfile_path):
        print('jeszcze raz plik zostal usuniety {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    print('DONE!')
