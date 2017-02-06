__author__ = 'isaac'

"""

Written By: Gil Rael

My dropbox sandbox environment for learning the the dropbox SDK

p1B5gzbofYMAAAAAAAAFSatK1PSjUQFKQwAUYPmlBjxVpMIYxmBPwZx91Keu5HMa




"""

import dropbox



dbx = dropbox.Dropbox('p1B5gzbofYMAAAAAAAAFSatK1PSjUQFKQwAUYPmlBjxVpMIYxmBPwZx91Keu5HMa')


dbx.users_get_current_account()


for entry in dbx.files_list_folder('').entries:
    print(entry.name)

dbx.files_upload("story.txt",'/cavs_vs_warriors/game5/story.txt')