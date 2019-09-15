# Doc

## The inspiration 
I wanted a place where I could display and store music works online, both the score and the audio file, in one page. Soundcloud shares audio files nicely but doesn't support display of score sheets. Musescore has what I need; it allows score and playback sharing, and has a community, but unfortunately it iss not free if I wanted to host more than 5 scores. Therefore I decided to make my own free score with playback hosting page!

## How it works
Github is used to host the files, and github-pages is used to deploy a static page to display the files nicely. The homepage is a README.md file which github-pages renders to html using jekyll. Editing the readme for each music piece I wanted to add would be a tedious, repetitive and error prone task if I were to do it manually. Therefore I wrote a [python script](generate_readme.py) to generate README.md

How I would add a music piece would be like this:

1) Copy the pdf score sheet and audio file to the local repo, to the done folder if its done and to the wip folder if its incomplete.

2) run 

```
py generate_readme.py
```
to generate README.md

3) push to github

I think it is a simple and convenient process :) 

## New things I learned

1) github pages links doesnt render the markdown file `.md` to html if the markdown file is named `docs.md`. This is likely because the name `docs` clashes with the folder name `docs` which is a standard point of entry for github pages to know where to load pages from.

2) Github pages does not redeploy README.md if there are no changes to README.md. I wanted Githubpages to redeploy README.md each time I pushed. Adding a last updated timestamp to README.md did the trick.
