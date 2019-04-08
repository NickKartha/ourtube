CREATE OR REPLACE FUNCTION public.new_playlist(pid character varying, vid character varying, title character varying)
 RETURNS void
 LANGUAGE sql
AS $function$
INSERT INTO playlist VALUES ($1, ARRAY[$2], $3);
$function$

