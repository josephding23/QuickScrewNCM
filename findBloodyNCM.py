import os
import json

def get_default_dir():
    f = open('./settings.json', encoding='utf-8')
    setting = json.load(f)
    default = setting["default_directory"]
    return default


def fuck_that_ncm():
    dir = get_default_dir()
    print(dir)
    performerList = os.listdir(dir)
    ncmDirs = list()
    for performer in performerList:
        performerDir = dir + '/' + performer + '/'
        try:
            albumList = os.listdir(performerDir)
            for album in albumList:
                albumDir = performerDir + album + '/'
                songsList = os.listdir(albumDir)
                for song in songsList:
                    if os.path.splitext(song)[-1] == '.ncm':
                        ncmpath = dir + '/' + performer + '/' + album + '/' + song
                        ping = os.popen('main.exe "' + ncmpath + '"').read().strip()
                        mp3path = dir + '/' + performer + '/' + album + '/' + os.path.splitext(song)[-2] + '.mp3'
                        #print(mp3path)
                        if os.path.exists(mp3path):
                            os.remove(ncmpath)
                        else:
                            print(mp3path)
        except:
            pass

if __name__ == '__main__':
    fuck_that_ncm()
    input("The process is over, ENTER to quit.")