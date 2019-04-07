import sql
import pycurl
import youtube_dl
import os
from pathlib import PurePath
#dl_list = ['wj6C-wdoXz8', 'pNBI8wUifdE', 'l3C6CAdXh44', 's04fn1wtKg0', 'bOfYvze1ueo']
#dl_list = ['https://www.youtube.com/playlist?list=PL_MvsrI4mukQiIPf_zP07yk2nKd8W4UpB']
dl_list = ['PTgchyWrgH8']
dl_dir = "web/static"
auth = ['localhost', 'postgres', 'docker']
def GetMetadata(url):
    with youtube_dl.YoutubeDL({}) as ydl:
        return ydl.extract_info(url, False)
def GetFormat(_metadata):
    # go from best, to worst.
    formats = []
    for x in _metadata.get('formats', [_metadata]):
        formats.append(x['format_id'])
    # VP9 1080p60FPS + Opus 160Kbps (303+251)
    if "303" in formats:
        print("VP9 1080p60")
        return [".webm", "303+251"]
    # VP9 1080p30FPS + Opus 160Kbps (248+251) 
    elif "248" in formats:
        print("VP9 1080p30.")
        return [".webm", "248+251"]
    # H264 1080p60FPS + AAC (298)
    elif "298" in formats:
        print("H264 1080p60")
        return [".mp4", "298+140"]
    # H264 720p30FPS + AAC (22)
    elif "22" in formats:
        print("H264 720p30")
        return [".mp4", "22"]
    else:
        print("Unable to find a suitable format.")
        return False
def GetThumbnail(_metadata):
    with open(f'{dl_dir}/thumbnail/{_metadata["id"]}.jpg', 'wb') as thumbnail:
        curl = pycurl.Curl()
        curl.setopt(curl.URL, _metadata['thumbnail'])
        curl.setopt(curl.WRITEDATA, thumbnail)
        curl.perform()
        curl.close()
        return True
def GetName(_metadata, opts, _type):
    return PurePath(youtube_dl.YoutubeDL(opts).prepare_filename(_metadata)).stem + _type[0]
def AddToDatabase(_metadata, _name, _replace = False):
    if sql.MatchID(_metadata["id"], auth):
        if _replace:
            print("ID found in database, replacing.")
        else:
            print("ID found in database, skipping.")
    else:
        print(f"Adding {_name} to database.")
        sql.AddMetadata(_metadata, auth, _name)
def DownloadVideo(url, _opts):
    with youtube_dl.YoutubeDL(_opts) as ydl:
        ydl.download([url])
for x in dl_list:
    metadata = GetMetadata(x)
    formats = GetFormat(metadata)
    name = GetName(metadata, {}, formats)
    DownloadVideo(x, {'format': formats[1], 'outtmpl': f'{dl_dir}/video/%(uploader_id)s/{name}'})
    GetThumbnail(metadata)
    AddToDatabase(metadata, name)
#GetFormats(metadata)

