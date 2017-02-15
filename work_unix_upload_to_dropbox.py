"""

Written By: Gil Rael

The following script tars files located /home/isaac/documents   recursively
and uploads the archive.tar file to /unix_systems/ubuntu_desktop/home/isaac/documents/archive.tar


p1B5gzbofYMAAAAAAAAFSatK1PSjUQFKQwAUYPmlBjxVpMIYxmBPwZx91Keu5HMa


"""

import dropbox
import os

def obtain_user_information():
    print os.name
    user_name = raw_input("Enter your username.")
    print(user_name)
    pw = raw_input("Enter your password.")
    print(pw)
    protocol = raw_input("Enter protocol either http or https.")
    print(protocol)
    command = "export " + '"' + (protocol) + "_proxy=" + (protocol) + "://" + (user_name) + ":" + (pw) + "@proxyout.lanl.gov:8080" + '"'
    print(command)
    os.popen(command, 'w')
obtain_user_information()



def unix_upload_to_dropbox():
    path = "/home/isaac/code"
    dropbox_path = '/unix_systems/work_alki/home/isaac/code/work_alki_archive.tar'
    command ="tar -cf work_alki_archive.tar *"
    mode = 'w'
    # Authenticate to Dropbox
    dbx = dropbox.Dropbox('p1B5gzbofYMAAAAAAAAFSatK1PSjUQFKQwAUYPmlBjxVpMIYxmBPwZx91Keu5HMa', max_retries_on_error=10)
    dbx.users_get_current_account()
    # print account holder information
    account = dbx.users_get_current_account()
    print(account)
    # Change to the directory that you want to tar the files and dirs recursively
    os.chdir(path)
    os.popen(command,mode)
    print(os.listdir(path))
    # The code below will open and read the archive.tar file and upload that file to Dropbox
    f = open('work_alki_archive.tar', 'rb')
    data = f.read()
    mode = (dropbox.files.WriteMode.overwrite)
    dbx.files_upload(data, dropbox_path, mode)
    print(dbx.files_get_metadata(dropbox_path).server_modified)
unix_upload_to_dropbox()




