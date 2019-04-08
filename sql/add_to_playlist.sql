CREATE OR REPLACE FUNCTION public.add_to_playlist(pid character varying, vid character varying)
 RETURNS void
 LANGUAGE sql
AS $function$
UPDATE playlist SET video_id = array_append(video_id, $2) WHERE playlist_id = $1;
UPDATE metadata SET playlists = array_append(playlists, $1) WHERE video_id = $2;
$function$

