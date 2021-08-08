import os
import dropbox.files 


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:

                local_path = os.path.join(root, filename)


                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode =('overWrite'))



def main():
    access_token = 'sl.A10XTYR3zfWs149wOw7WDfWCts4E8xPagzXASbroXos7161u4EvW3W6GC15r29XrlKYiAwqNUIYbrFcrc_MJMkkR355Vz1c_dFDfo2bSSA93K8ynvPrBCyrv31mMjMYas6bVBaE'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input ("Enter the path to upload to dropbox: ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been transferred")
if __name__ == '__main__':
    main()