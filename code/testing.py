from pyglet import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pyglet
from mutagen.mp3 import MP3

def playVideos(FinalResults, checker, time ,OneVid,Video):
    if OneVid == False:
        for key in FinalResults:
            vidPath = 'Mp4Files/' + key
            config = pyglet.gl.Config(sample_buffers=2, samples=4)
            window = pyglet.window.Window(config=config)
            player = pyglet.media.Player()
            source = pyglet.media.StreamingSource()
            MediaLoad = pyglet.media.load(vidPath)
            player.queue(MediaLoad)
            if checker == True:
                time = int(time)
                fn=key.split(".")[0]
                path = "Mp3Files/" +fn + ".mp3"
                audio = MP3(path)
                duration = audio.info.length
                if(duration>time):
                    player.seek(time)
                else:
                    from dialogueBox import Ui_MainWindow
                    global msgWindow
                    msgWindow = QtWidgets.QMainWindow()
                    lui = Ui_MainWindow("Entered time is more than video duration")
                    lui.setupUi(msgWindow)
                    msgWindow.show()
            player.play()

            @window.event
            def on_draw():
                window.clear()

                if player.source and player.source.video_format:
                    player.get_texture().blit(20, 20)

            @window.event
            def on_key_press(symbol, modifiers):
                window.clear()
                window.close()
                player.delete()
                pyglet.app.exit()

            @window.event
            def on_close():
                print("closing Video")
                window.clear()
                window.close()
                player.delete()
                pyglet.app.exit()

            pyglet.app.run()
    else:
        print("Print else test")
        playOne(Video)


def playOne(filename):


    vidPath = 'Mp4Files/' + filename
    config = pyglet.gl.Config(sample_buffers=2, samples=4)
    print("Playing Video")
    window = pyglet.window.Window(config=config)
    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()
    MediaLoad = pyglet.media.load(vidPath)
    player.queue(MediaLoad)

    player.play()

    @window.event
    def on_draw():
        window.clear()

        if player.source and player.source.video_format:
            player.get_texture().blit(20, 20)

    @window.event
    def on_key_press(symbol, modifiers):
        window.clear()
        window.close()
        player.delete()
        pyglet.app.exit()

    @window.event
    def on_close():
        print("closing Video")
        window.clear()
        window.close()
        player.delete()
        pyglet.app.exit()

    pyglet.app.run()

# if __name__ == "__main__":
    # playVideos([1], True, "1", "facebook")
    # playVideos([1], True, "1", "facebook")
