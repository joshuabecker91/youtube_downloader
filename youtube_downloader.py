from pytube import YouTube
# https://pypi.org/project/pytube/
# You may need to make cmder run as administrator and then upgrade pip python.exe -m pip install --upgrade pip
# You can install pytube by running: python -m pip install git+https://github.com/pytube/pytube
# or python -m pip install pytube

# ------------------------------------------------------------------------------------------------------------

def download(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print("error: downloading youtube video has failed")
    print("youtube video download completed!")

link = input("Youtube Link: ")
download(link)


# Example Test Links:-----------------------------------------------------------------------------------------

# How to Use Python with AWS S3 | Python Boto3 Tutorial
# download("https://www.youtube.com/watch?v=7r2z3Qn3Qz8")

# Kubernetes Vs Docker | Docker Vs Kubernetes Difference |Kubernetes And Docker Explained |Simplilearn
# download("https://www.youtube.com/watch?v=tuyq3H4EXL0")