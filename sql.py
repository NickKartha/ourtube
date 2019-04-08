import psycopg2
import psycopg2.extras

def OpenConnection(auth):
    return psycopg2.connect(host=auth[0], user=auth[1], password=auth[2])
def AddMetadata(_metadata, auth, _filepath):
    conn = OpenConnection(auth)
    with conn:
        with conn.cursor() as cursor:
            if(_metadata['playlist']):
                cursor.callproc('add_metadata', (_metadata['id'], _metadata['uploader'], _metadata['uploader_id'], _metadata['title'], _metadata['description'], int(_metadata['upload_date']), _filepath, _metadata['playlist_id'], _metadata['playlist_index'], _metadata['playlist']))
            else:
                cursor.callproc('add_metadata', (_metadata['id'], _metadata['uploader'], _metadata['uploader_id'], _metadata['title'], _metadata['description'], int(_metadata['upload_date']), _filepath, None, None, None))
    conn.close()
def GetFirst(_num, auth):
    conn = OpenConnection(auth)
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.callproc('get_first', (_num,));
            _returnValue = cursor.fetchall()
    conn.close()
    return _returnValue
def MatchID(_id, auth):
    conn = OpenConnection(auth)
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.callproc('match_id', (_id,));
            _returnValue = cursor.fetchall()
    conn.close()
    return _returnValue
def MatchTitle(_title, auth):
    conn = OpenConnection(auth)
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.callproc('match_title', (_title,))
            _returnValue = cursor.fetchall()
    conn.close()
    return _returnValue
def LikeTitle(_title, auth):
    conn = OpenConnection(auth)
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.callproc('like_title', (_title,))
            _returnValue = cursor.fetchall()
    conn.close()
    return _returnValue
