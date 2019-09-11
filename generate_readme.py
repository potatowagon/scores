import os
import re

def write_readme(txt):
    with open("README1.md", "w+") as md:
        print("hi")
        md.write(txt)

def embedded_pdf(pdf):
    return '<object data=\"%s\" type=\"application/pdf\" width=\"1000px\" height=\"500px\"><embed src="%s"></embed></object>' % (pdf, pdf)

def embedded_audio(audio_src):
    return '<figure><audio controls src="%s">Your browser does not support the<code>audio</code> element.</audio></figure>' % (audio_src)

def music_content(title):
    pass

def main():

    items = []

    done_spotlight = []
    wip_spotlight = []

    header1 = "## Scores"
    header1_content = "[musecore, no pro `:(`](https://musescore.com/user/28262500)\n\n[Soundcloud](https://soundcloud.com/sherry-wong-59815924)"

    items.append(header1)
    items.append(header1_content)
    items.append(embedded_pdf("https://potatowagon.github.io/scores/done/the_eggs.pdf"))
    items.append(embedded_audio("https://potatowagon.github.io/scores/done/the_eggs.mp3"))
    md = '\n\n'.join(items)
    write_readme(md)

main()
