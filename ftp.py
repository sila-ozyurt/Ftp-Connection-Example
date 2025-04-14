import ftplib
import os

class FtpClient:

    def __init__(self):
        self.ftp = None

    # a function to establish an FTP connection with the given host, port, username, and password
    def setConnection(self, host, port, username, psw):
        try:
            self.ftp = ftplib.FTP()
            self.ftp.connect(host, port)
            self.ftp.login(username, psw)
            self.ftp.set_pasv(True)
            print("FTP connection established.")
        except Exception as e:
            print(f"Error establishing FTP connection: {e}")

    # a function to list the contents of the remote FTP directory
    def listRemoteDir(self):
        try:
            print("Remote Directory Listing:")
            self.ftp.retrlines('LIST')
        except Exception as e:
            print(f"Error listing remote directory: {e}")

    # a function to list the contents of the local directory
    def listLocalDir(self, path="."):
        try:
            print("Local Directory Listing:")
            for file in os.listdir(path):
                print(file)
        except Exception as e:
            print(f"Error listing local directory: {e}")

    # a function to create a new directory on the FTP server
    def createDir(self, dirname):
        try:
            self.ftp.mkd(dirname)
            print(f"Directory '{dirname}' created on FTP server.")
        except Exception as e:
            print(f"Error creating directory '{dirname}': {e}")

    # a function to delete a directory from the FTP server
    def deleteDir(self, dirname):
        try:
            self.ftp.rmd(dirname)
            print(f"Directory '{dirname}' deleted from FTP server.")
        except Exception as e:
            print(f"Error deleting directory '{dirname}': {e}")

    # a function to upload a local file to the FTP server
    def uploadFile(self, local_file, remote_file):
        try:
            with open(local_file, 'rb') as file:
                return_code = self.ftp.storbinary(f'STOR {remote_file}', file)

            if return_code.startswith("226"):
                print("Upload successful.")
            else:
                print("Upload failed.")
        except Exception as e:
            print(f"Error uploading file '{local_file}': {e}")

    # a function to download a file from the FTP server to the local system
    def downloadFile(self, remote_file, local_file):
        try:
            with open(local_file, 'wb') as file:
                return_code = self.ftp.retrbinary(f'RETR {remote_file}', file.write)

            if return_code.startswith("226"):
                print("Download successful.")
            else:
                print("Download failed.")
        except Exception as e:
            print(f"Error downloading file '{remote_file}': {e}")

    # a function to rename a file on the FTP server
    def renameFile(self, old_name, new_name):
        try:
            self.ftp.rename(old_name, new_name)
            print(f"File renamed from '{old_name}' to '{new_name}'.")
        except Exception as e:
            print(f"Error renaming file from '{old_name}' to '{new_name}': {e}")

    # a function to close the FTP connection
    def closeConnection(self):
        try:
            self.ftp.quit()
            print("FTP connection closed.")
        except Exception as e:
            print(f"Error closing FTP connection: {e}")

#connection infos
host = "localhost"
port = 21
#username and password is set as below
username = "ftpuser"
password = "sifren123"

ftp_client = FtpClient()


ftp_client.setConnection(host, port, username, password)

ftp_client.listRemoteDir()

ftp_client.listLocalDir()

ftp_client.createDir("new_folder")

ftp_client.uploadFile("test.txt", "new_folder/test.txt")

ftp_client.downloadFile("new_folder/test.txt", "downloaded_test.txt")

ftp_client.renameFile("new_folder/test.txt", "new_folder/renamed_test.txt")

ftp_client.deleteDir("new_folder")

ftp_client.closeConnection()
