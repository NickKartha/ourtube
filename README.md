# Ourtube

A local copy of YouTube where you can search, view videos & playlists, et cetera.

Expects a postgres server on a Docker domain at "ourtube-net" by default, modify this if you will choose a different name or manually configure postgres.

## Implementation Details

This runs using magical unicorns and tiny house elves. <strike> not really </strike>

## Dependencies

 - psycopg2
 - Flask
 - psycopg2-binary

These can be found in the `requirements.txt` which you can use to call `pip` on.
