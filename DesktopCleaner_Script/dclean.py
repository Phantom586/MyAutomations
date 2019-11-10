import os
import shutil
import platform

BASE_DIR = "C:\\Users\\"
# username
usr = "Phantom"
# working Directory
wdir = "Desktop"

# Some Common Categories of Extensions
# if your device have some other extensions as well then you can add in their respective category list.\

music = [".mp3", ".ac3", ".wma", ".aac", ".wav", ".flac"]
video = [".mp4", ".mov", ".wmv", ".flv", ".avi", ".mkv", ".3gp", ".m4v", ".h264", ".mpeg"]
files = [".txt", ".doc", ".docx", ".pdf", ".rtf", ".tex", ".wks", ".wps", ".wpd", ".odt", ".pps", ".ppt", ".pptx"]
programming = [".c", ".cpp", ".py", ".class", ".cs", ".h", ".java", ".sh", ".swift"]
web_dev = [".asp", ".aspx", ".cer", ".cfm", ".cgi", ".pl", ".css", ".htm", ".html", ".js", ".jsp", ".part", ".php", ".rss", ".xhtml"]
image = [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff"]
database = [".csv", ".dat", ".db", ".dbf", ".log", ".sql"]
compressed = [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip"]


print("")
print(" :: Welcome to the Desktop Cleaner Script :: ")
print("")
print("    -> This script Manages your files at your desktop and moves them into their dedicated folders...")
print("    -> So No Hazzle for you...just provide "'few things'" and sit back and relax.....")
print("    -> while the Script is doing all the repetitive and annoying task for you.....")
print("")
print(" :: Written By : -- Ph@ntomBoy -- ::")

print("")
print("Enter your username :")
print("    can be found at :- ")
# Identifying the OS on ehich the Script is running On.
OS = platform.system()
if OS == "Windows":
    print("    [Windows] - 'C:\\Users\\right_here\\Desktop'")
elif OS == "Mac":
    print("    [Mac] - '/Users/right_here/home'")


# usr = input()
# Creating an absolute path to Desktop
path = os.path.join(BASE_DIR, usr, wdir)
print(path)

# Changing the current directory to Desktop
os.chdir(path)

# for f in os.listdir():
#     print(f)

# Iterating through the list of the files present in Desktop.
for f in os.listdir():
    # splitting the files into file_names and their extensions
    f_name, f_ext = os.path.splitext(f)
    # checking the extensions of the files and proceeding accordingly

    # Destination Folder
    dest_folder = ""

    if f_ext in music:

        dest_folder = "Music"
    
    elif f_ext in video:

        dest_folder = "Video"

    elif f_ext in files:

        dest_folder = "Files"

    elif f_ext in programming:

        dest_folder = "Programming"

    elif f_ext in web_dev:

        dest_folder = "Web_Development"

    elif f_ext in image:

        dest_folder = "Images"

    elif f_ext in database:

        dest_folder = "Database"

    elif f_ext in compressed:

        dest_folder = "Compressed"

    if dest_folder is not "":

        if os.path.exists(dest_folder):
                exists = os.path.isdir(dest_folder)
                if not exists:
                    print("Created Folder : ", dest_folder)
                    os.mkdir(dest_folder)
        else:
            print("Created Folder : ", dest_folder)
            os.mkdir(dest_folder)

    
        print("Moving From : ", os.path.join(path, f_name+f_ext), "To : ", os.path.join(path, dest_folder))
        shutil.move(os.path.join(path, f_name+f_ext), os.path.join(path, dest_folder))


# shutil.move(path+"\\Clever Programmer(Webinar) 9 November.txt", path+"\\Files\\")