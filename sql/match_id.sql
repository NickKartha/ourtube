CREATE OR REPLACE FUNCTION public.match_id(vid character varying)
 RETURNS TABLE(video_id character varying, uploader character varying, uploader_id character varying, title character varying, description character varying, upload_date integer, filepath character varying, playlists character varying[])
 LANGUAGE sql
AS $function$
SELECT * FROM metadata WHERE video_id = $1;
$function$

