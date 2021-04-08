import time
import os


def modify():
    i = 1
    for filename in os.listdir(folder_to_track):
        print(filename)

        # documents
        if filename.lower().endswith(('.doc', '.pdf', '.csv','.xlsx','.docx','.xls','.pptx','.txt')):
            src = folder_to_track + '/' + filename
            newDestination = folder_to_dest_doc + '/' + filename
            if not filename in os.listdir(folder_to_dest_zip):
                os.rename(src, newDestination)

        # Images
        elif filename.lower().endswith(('.png', '.jpg', '.jpeg', '.jfif')):
            src = folder_to_track + '/' + filename
            newDestination = folder_to_dest_img + '/'  + filename
            if not filename in os.listdir(folder_to_dest_zip):
                os.rename(src, newDestination)
        # softwares
        elif filename.lower().endswith(('.exe', '.msi')):
            src = folder_to_track + '/' + filename
            newDestination = folder_to_dest_exe + '/'  + filename
            if not filename in os.listdir(folder_to_dest_zip):
                os.rename(src, newDestination)
        # zip
        elif filename.lower().endswith(('.rar', '.rar4', '.zip')):
            src = folder_to_track + '/' + filename
            newDestination = folder_to_dest_zip + '/'  + filename
            if not filename in os.listdir(folder_to_dest_zip):
                os.rename(src, newDestination)
        # mislaneous
        else:
            src = folder_to_track + '/' + filename
            newDestination = folder_to_dest_mis + '/' + filename
            if not filename in os.listdir(folder_to_dest_zip):
                os.rename(src, newDestination)


folder_to_track = 'D:/Downloads'

folder_to_dest_img = 'D:/Testing/Image'
folder_to_dest_doc = 'D:/Testing/Documents'
folder_to_dest_exe = 'D:/Testing/Exe'
folder_to_dest_mis = 'D:/Testing/Mislaneous'
folder_to_dest_zip = 'D:/Testing/Zip'
modify()