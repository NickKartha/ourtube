CREATE OR REPLACE FUNCTION public.add_metadata(_video_id character varying, _uploader character varying, _uploader_id character varying, _title character varying, _description character varying, _upload_date integer, _filepath character varying, _playlists character varying)
 RETURNS void
 LANGUAGE sql
AS $function$
INSERT INTO metadata (video_id, uploader, uploader_id, title, description, upload_date, filepath, playlists) VALUES (_video_id, _uploader, _uploader_id, _title, _description, _upload_date, _filepath, ARRAY[_playlists])
$function$

