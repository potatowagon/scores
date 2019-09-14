import os
import re
from datetime import datetime

class Music():

    def __init__(self, pdf: str):
        '''
        Create a Music instance to hold music data

        Args:
            pdf (str): relative path to pdf, with where this file is at being the root reference
        '''
        self.root = "https://potatowagon.github.io/scores/"
        self.title = os.path.basename(pdf).split('.')[0]
        self.audio_src = None
        self.pdf = (self.root + pdf).replace('\\', '/')
    
    def set_audio_src(self, src: str):
        '''
        Set the audio source to the source path when it is hosted online
        Args:
            src (str): relative path to pdf, with where this file is at being the root reference
        '''
        # .wav files take priority
        if src.endswith(".wav"):
            self.audio_src = (self.root + src).replace('\\', '/')
        if self.audio_src is None and src.endswith(".mp3"):
            self.audio_src = (self.root + src).replace('\\', '/')

class MusicContentCreator():

    def __init__(self, dir_path, spotlight=[]):
        self.spotlight = spotlight
        self.music_list = self._collect_music(dir_path)
        self.music_content_list = []

    def _music_content(self, music: Music):
        header = '### ' + music.title.replace('_', ' ')
        pdf_link = '[%s.pdf](%s)' % (music.title, music.pdf)
        return '\n\n'.join([header, MarkdownUtils.embedded_audio(music.audio_src), pdf_link, MarkdownUtils.embedded_pdf(music.pdf)])

    def _collect_music(self, dir_path):
        music_list = []
        dir_items = os.listdir(dir_path)
        for item in dir_items:
            if item.endswith('.pdf'):
                music_list.append(Music(os.path.join(os.path.basename(dir_path), item)))

        for item in dir_items:
            if item.endswith('.mp3') or item.endswith('.wav'):
                title = item.split('.')[0]
                for music in music_list:
                    if title == music.title:
                        music.set_audio_src(os.path.join(os.path.basename(dir_path), item))
        return music_list

    def _get_music(self, title):
        for music in self.music_list:
            if title == music.title:
                return music
        raise FileNotFoundError("canot find %s in music_list" % (title))
                
    def make_music_content_section(self):
        for title in self.spotlight:
            music = None
            try:
                music = self._get_music(title)
            except FileNotFoundError as e:
                print("Cannot find spotlight title %s" % title)
            if music:    
                self.music_content_list.append(self._music_content(music))
                self.music_list.remove(music)

        for music in self.music_list:
            self.music_content_list.append(self._music_content(music))

        return '\n\n'.join(self.music_content_list) 

class MarkdownUtils():
    
    @classmethod
    def embedded_pdf(cls, pdf):
        return '<object data=\"%s\" type=\"application/pdf\" width=\"1000px\" height=\"500px\"><embed src="%s"></embed></object>' % (pdf, pdf)

    @classmethod
    def embedded_audio(cls, audio_src):
        return '<figure><audio controls src=\"%s\">Your browser does not support the<code>audio</code> element.</audio></figure>' % (audio_src)

    @classmethod
    def last_update(cls):
        return "Last update %s" % str(datetime.now())
    
    @classmethod
    def write_readme(cls, txt):
        with open("README.md", "w+") as md:
            md.write(txt)

def main():

    items = []

    done_spotlight = ["the_eggs"]
    wip_spotlight = ["Secret_Diary"]

    header1 = "# Scores"
    musescore_link = "[musecore, no pro `:(`](https://musescore.com/user/28262500)"
    soundcloud_link = "[Soundcloud](https://soundcloud.com/sherry-wong-59815924)"
    docs_link = "[This page is generated with a python script!](https://potatowagon.github.io/scores/docs.md)"

    items.append(header1)
    items.append(musescore_link)
    items.append(soundcloud_link)
    items.append(docs_link)
    
    done_music_content_creator = MusicContentCreator(os.path.join(os.getcwd(), "done"), done_spotlight)
    done_music_section = done_music_content_creator.make_music_content_section()
    items.append(done_music_section)

    wip_header = "## WIP"
    items.append(wip_header)

    wip_music_content_creator = MusicContentCreator(os.path.join(os.getcwd(), "wip"), wip_spotlight)
    wip_music_section = wip_music_content_creator.make_music_content_section()
    items.append(wip_music_section)
    items.append(MarkdownUtils.last_update())

    md = '\n\n'.join(items)
    MarkdownUtils.write_readme(md)

main()
