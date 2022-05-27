SELECT 
a.first_name || "" || a.last_name AS full_name,
a.id AS id,
g.*
FROM Auth_user a
JOIN levelupapi_gamer gr 
    ON gr.user_id = a.id
JOIN levelupapi_game g
    ON g.gamer_id = gr.id
SELECT 
a.id AS gamer_id,
a.first_name || "" || a.last_name AS full_name,
e.id AS id,
e.date AS date,
e.time AS time,
g.title AS game_name
FROM Auth_user a
JOIN levelupapi_gamer gr 
    ON gr.user_id = a.id
JOIN levelupapi_eventgamer eg 
    ON eg.gamer_id = gr.id
JOIN levelupapi_event e 
    ON eg.event_id = e.id
JOIN levelupapi_game g
    ON g.id = e.game_id
-- 
-- [
--     {
--         "gamer_id": 1,
--         "full_name": "Molly Ringwald",
--         "events": [
--         {
--             "id": 5,
--             "date": "2020-12-23",
--             "time": "19:00",
--             "game_name": "Fortress America"
--         }
--         ]
--     }
-- ]