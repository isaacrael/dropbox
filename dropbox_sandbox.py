__author__ = 'isaac'

"""

Written By: Gil Rael

My dropbox sandbox environment for learning the the dropbox SDK

p1B5gzbofYMAAAAAAAAFSatK1PSjUQFKQwAUYPmlBjxVpMIYxmBPwZx91Keu5HMa




"""

import dropbox
import os
import subprocess
path = "/home/isaac/Documents"




dbx = dropbox.Dropbox('p1B5gzbofYMAAAAAAAAFSatK1PSjUQFKQwAUYPmlBjxVpMIYxmBPwZx91Keu5HMa')


dbx.users_get_current_account()

# print account holder information
account = dbx.users_get_current_account()
print(account)

#dir = os.chdir(path)
print(os.listdir(path))

# list files and folders in the root directory
for entry in dbx.files_list_folder('').entries:
    print(entry.name)

# The code below will read a text file and upload file to Dropbox
f = open('story.txt', 'r')
line = f.read()
print(line)
data = str.encode(line)
f.close()

mode = (dropbox.files.WriteMode.overwrite)
dbx.files_upload(data,'/cavs_vs_warriors/game_5/story.txt', mode)
print(dbx.files_get_metadata('/cavs_vs_warriors/game_5/story.txt').server_modified)



# The code below will read a binary file and upload that file to Dropbox
f = open('sushiplate.jpg', 'rb')
data = f.read()
mode = (dropbox.files.WriteMode.overwrite)
dbx.files_upload(data,'/cavs_vs_warriors/game_5/sushiplate.jpg', mode)
print(dbx.files_get_metadata('/cavs_vs_warriors/game_5/sushiplate.jpg').server_modified)