# Doc

## The inspiration

## How it works

## New things I learned

1) github pages links dont render the markdown file `.md` to html if the markdown file is named `docs.md`. This is likely because the name `docs` clashes with the folder name `docs` which is a standard point of entry for github pages to know where to load pages from.

2) Github pages does not redeploy README.md if there are no changes to README.md. I wanted Githubpages to redeploy README.md each time I pushed. Adding a last updated timestamp to README.md did the trick.
