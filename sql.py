import psycopg2
import psycopg2.extras

def OpenConnection(auth):
    return psycopg2.connect(host=auth[0], user=auth[1], password=auth[2])
def does_playlist_exist(_id, cursor):
    cursor.callproc('get_playlist', (_id,))
    return cursor.fetchall()
def add_metadata(_metadata, auth, _filepath):
    conn = OpenConnection(auth)
    with conn:
        with conn.cursor() as cursor:
            if(_metadata['playlist']):
                if does_playlist_exist(_metadata['playlist_id'], cursor):
                    cursor.callproc('add_to_playlist', (_metadata['playlist_id'], _metadata['id']))
                else:
                    cursor.callproc('new_playlist', (_metadata['playlist_id'], _metadata['id'], _metadata['playlist']))
                cursor.callproc('add_metadata', (_metadata['id'], _metadata['uploader'], _metadata['uploader_id'], _metadata['title'], _metadata['description'], int(_metadata['upload_date']), _filepath, _metadata['playlist_id']))
            else:
                cursor.callproc('add_metadata', (_metadata['id'], _metadata['uploader'], _metadata['uploader_id'], _metadata['title'], _metadata['description'], int(_metadata['upload_date']), _filepath, None))
    conn.close()
def get_first(_num, auth):
    conn = OpenConnection(auth)
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.callproc('get_first', (_num,));
            retval = cursor.fetchall()
    conn.close()
    return retval
def match_playlist_id(_id, auth):
    conn = OpenConnection(auth)
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.callproc('match_playlist_id', (_id,));
            retval = cursor.fetchall()
    conn.close()
    return retval
def match_id(_id, auth):
    conn = OpenConnection(auth)
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.callproc('match_id', (_id,));
            retval = cursor.fetchall()
    conn.close()
    return retval
def match_title(_title, auth):
    conn = OpenConnection(auth)
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.callproc('match_title', (_title,))
            retval = cursor.fetchall()
    conn.close()
    return retval
def like_title(_title, auth):
    conn = OpenConnection(auth)
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.callproc('like_title', (_title,))
            retval = cursor.fetchall()
    conn.close()
    return retval
